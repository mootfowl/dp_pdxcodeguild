'''

DPAdventure_v5 - ENTITIES

Roadmap >>

* Add an "Aimed Attack[A]"
    > Head[H], Torso[T], etc.
    > Increased difficulty, but higher damage and/or special effect (reduce enemy AP)

* Add "Disarm[D]"
    > Useable only on armed enemies
    > Unequips their primary weapon

* Refine Block[B] mechanism
    > Add diminishing returns on subsequent blocks

* Add "Throw[T]"
* Add "Shoot[S]"

* For each weapon type, add other unique combat modifiers
    > increased/decrease AP point cost
    > Temporary conditions - Stun, Disorient, Blind, etc.

'''

import random
import time


class Entity:
    def __init__(self, name='Creature', target=None, i=0, j=0):
        self.name = name
        self.target = target
        self.loc_i = i
        self.loc_j = j
        self.level = 0
        self.health_cap = 20 + self.level * 2
        self.health = self.health_cap
        self.action_points = 2
        self.ap_cap = 5
        self.power = 1
        self.damage = int(10 + (self.power / 2))
        self.toughness = 1
        self.armor = int(0 + (self.toughness / 2))
        self.accuracy = 60 + self.level * 3
        self.repair_cap = 5 + self.level
        self.combo_points = 0
        self.cp_cap = 3
        self.quick_name = 'JAB'
        self.strong_name = 'HOOK'
        self.vicious_name = 'SLAM'
        self.block_status = False
        self.block_amount = 2
        self.primary_weapon = None
        self.ranged_weapon = None
        self.shield = None
        self.head_armor = None

    def ap_combo_check(self, req_ap=0, req_combo=0):
        if req_ap > self.action_points:
            print("\tYou don't have enough action points for that ability!")
            return False
        if req_combo > self.combo_points:
            print(f"\tThat ability requires {req_combo} combo points to execute!")
            return False
        else:
            return True

    def quick_attack(self):
        ap_cost = 1
        combo_cost = 0
        if self.ap_combo_check(ap_cost, combo_cost) == True:
            print(f"{self.name} attempts to {self.quick_name} {self.target.name}!")
            time.sleep(.5)
            quick_modifier = 10
            dmg = int(self.damage / 3)
            x = random.randint(1, 100)
            self.action_points -= ap_cost
            if x < self.accuracy + quick_modifier:
                if self.target.block_status == False:
                    print(f"\tThe {self.quick_name} damages {self.target.name} for {dmg}!")
                    self.target.health -= dmg
                else:
                    print(f"\t{self.target.name} BLOCKS the {self.quick_name}, reducing the damage by {self.target.block_amount}.")
                    modified_dmg = dmg - self.target.block_amount
                    if modified_dmg < 0:
                        modified_dmg = 0
                    if modified_dmg > 0:
                        print(f"\tThe {self.quick_name} damages {self.target.name} for {modified_dmg}!")
                        self.target.health -= modified_dmg
                self.action_points += 2
                if self.action_points > self.ap_cap:
                    self.action_points = self.ap_cap
                self.combo_points += 1
                if self.combo_points > self.cp_cap:
                    self.combo_points = self.cp_cap
            else:
                print(f"\t{self.target.name} evades the {self.quick_name}!")
                self.combo_points = 0
        else:
            return

    def strong_attack(self):
        ap_cost = 3
        combo_cost = 1
        if self.ap_combo_check(ap_cost, combo_cost) == True:
            print(f"{self.name} attempts to {self.strong_name} {self.target.name}!")
            time.sleep(.5)
            strong_modifier = -10
            dmg = int(self.damage / 2)
            x = random.randint(1, 100)
            self.action_points -= ap_cost
            if x < self.accuracy + strong_modifier:
                if self.target.block_status == True:
                    print(f"\tThe force of the {self.strong_name} DISABLES {self.target.name}'s BLOCK.")
                    self.target.block_status = False
                print(f"\tThe {self.strong_name} damages {self.target.name} for {dmg}!")
                self.target.health -= dmg
                self.action_points += 4
                if self.action_points > self.ap_cap:
                    self.action_points = self.ap_cap
                self.combo_points += 1
                if self.combo_points > self.cp_cap:
                    self.combo_points = self.cp_cap
            else:
                print(f"\t{self.target.name} evades the {self.strong_name}!")
                self.combo_points = 0
                self.action_points = 0
        else:
            return

    def vicious_attack(self):
        ap_cost = 5
        combo_cost = 3
        if self.ap_combo_check(ap_cost, combo_cost) == True:
            print(f"{self.name} attempts to {self.vicious_name} {self.target.name}!")
            time.sleep(.5)
            vicious_modifier = -20
            dmg = self.damage
            x = random.randint(1, 100)
            self.action_points -= ap_cost
            if x < self.accuracy + vicious_modifier:
                print(f"\tThe {self.vicious_name} damages {self.target.name} for {dmg}!")
                self.target.health -= dmg
                # self.combo_points += 1
                # if self.combo_points > self.cp_cap:
                #     self.combo_points = self.cp_cap
            else:
                print(f"\t{self.target.name} evades the {self.vicious_name}!")
                self.combo_points = 0
                self.action_points = 0
        else:
            return

    def repair(self):
        ap_cost = 2
        if self.ap_combo_check(ap_cost) == True:
            repair_amount = random.randint(int(self.repair_cap / 2), self.repair_cap)
            self.health += repair_amount
            print(f"\t{self.name} repairs itself for {repair_amount}!")
            if self.health > self.health_cap:
                self.health = self.health_cap
            self.action_points -= ap_cost
        else:
            return

    def block(self):
        ap_cost = 1
        if self.ap_combo_check(ap_cost) == True:
            print(f"{self.name} prepares to BLOCK!")
            print(f"\tBlocking will reduce incoming damage by {self.block_amount}.")
            self.block_status = True
            self.action_points -= ap_cost
            time.sleep(1)

    def equip_primary_weapon(self, weapon):
        self.quick_name = weapon.quick_name
        self.strong_name = weapon.strong_name
        self.vicious_name = weapon.vicious_name
        self.power += weapon.power
        self.accuracy += weapon.accuracy
        self.primary_weapon = weapon

    def drop_primary_weapon(self, weapon):
        self.quick_name = 'JAB'
        self.strong_name = 'HOOK'
        self.vicious_name = 'SLAM'
        self.power -= weapon.power
        self.accuracy -= weapon.accuracy
        self.primary_weapon = None
        print(f"{self.name} is disarmed, dropping its {self.primary_weapon} to the ground.")
        # ADD some mechanism for self or other to pick it up

    def reset_combat_turn(self):
        self.combo_points = 0
        self.action_points = 2
        self.target.block_status = False
        print()


class BasicEnemy(Entity):
    def __init__(self, name='Malfunctioning Automaton', target=None, i=0, j=0, icon='\u2687'):
        super().__init__(name, target, i, j)
        self.icon = icon
        self.experience_reward = 1 + self.level
        self.detection = 10

    def __str__(self):
        return f'{self.name} | {self.icon} | LVL{self.level} | HEALTH - {self.health}'

    def combat_turn(self):
        print(self)
        if self.primary_weapon != None:
            print(f"The {self.name} steadies its {self.primary_weapon.quality} {self.primary_weapon.name} as it "
                  f"prepares its next action...")
        else:
            print(f"The {self.name} calculates its course of action...")
        time.sleep(1.5)
        print()
        while self.action_points > 0 and self.target.health > 0:
            time.sleep(1)
            if self.action_points >= 5 and self.health >= 12 and self.combo_points >= 3:
                self.vicious_attack()
            elif self.action_points >= 2 and self.health < self.health_cap / 2:
                self.repair()
            elif self.action_points >= 3 and self.combo_points >= 1:
                self.strong_attack()
            elif self.action_points > 1:
                self.quick_attack()
            elif self.action_points == 1:
                self.block()
            else:
                pass
        self.reset_combat_turn()


class PlayerCharacter(Entity):
    def __init__(self, name, target=None, i=2, j=2, icon='\u26b2'):
        super().__init__(name, target, i, j)
        self.icon = icon
        self.experience_points = 0
        self.keys = 0
        self.ammunition = 0
        self.inventory = []

    def unequip_primary_weapon(self, weapon):
        self.quick_name = 'JAB'
        self.strong_name = 'HOOK'
        self.vicious_name = 'SLAM'
        self.power -= weapon.power
        self.accuracy -= weapon.accuracy
        self.primary_weapon = None
        self.inventory.append(weapon)

    def exploration_interface(self):
        print(f'{self.name} {self.icon} | LVL{self.level} '
              f'| HEALTH {self.health} / {self.health_cap} | EXP {self.experience_points}')

    def character_screen(self):
        print()
        self.exploration_interface()
        print("\nATTRIBUTES >>")
        print(f"\tPower - {self.power} | Damage - {self.damage} | Accuracy - {self.accuracy}"
              f"\n\tToughness - {self.toughness} | Armor - {self.armor}")
        if self.primary_weapon != None:
            print("\nGEAR >>")
            print(f"\tPRIMARY: {self.primary_weapon}")
        if self.ranged_weapon != None:
            print(f"\tRANGED: {self.ranged_weapon}")
        if self.shield != None:
            print(f"\tSHIELD: {self.shield}")
        if self.head_armor != None:
            print(f"\tHEAD: {self.head_armor}")
        print("\nINVENTORY >>")
        print(f"\tKeys - {self.keys} | Ammunition - {self.ammunition}")
        for i in range(0, len(self.inventory)):
            print(f"\t{i + 1}. {self.inventory[i]}")
        x = input("\nRETURN to game or equip[E] item from inventory. >> ")
        if x.lower() == 'e':
            y = int(input(f"Equip which item? 1 - {len(self.inventory)} >> "))
            if self.primary_weapon != None:
                self.unequip_primary_weapon(self.primary_weapon)
                self.equip_primary_weapon(self.inventory[y-1])
                del self.inventory[y-1]
                print(f"You equip the {self.primary_weapon.name}.")
                time.sleep(2)
            else:
                self.equip_primary_weapon(self.inventory[y - 1])
                del self.inventory[y - 1]
        return

    def combat_interface(self):
        print()
        print(f'HEALTH {self.health} | ENEMY {self.target.health}')
        print('AP', '\u2771' * self.action_points, '| CP', '\u29C1' * self.combo_points)

    def player_combat_turn(self):
        while self.action_points > 0 and self.target.health > 0:
            self.combat_interface()
            print('\t> Quick Atk[Q]', end='')
            if self.combo_points >= 1:
                print(' | >>> Strong Atk[S]', end='')
            if self.combo_points >= 2:
                print(' | >>>>> Vicious Atk[V]', end='')
            if self.action_points >= 2:
                print(' | Repair[R]', end='')
            if self.action_points >= 1:
                print(' | Block[B] ', end='')
            action = input('>> ')
            if action == 'q':
                self.quick_attack()
            elif action == 's':
                self.strong_attack()
            elif action == 'v':
                self.vicious_attack()
            elif action == 'r':
                self.repair()
            elif action == 'b':
                self.block()
        self.reset_combat_turn()

    def level_up(self, current_level):
        if self.experience_points >= current_level * 5:
            self.accuracy += 2
            self.power += 1
            self.toughness += 1
            self.level += 1
            print()
            print("Your focus sharpens from the trials of experience.")
            print("\tYour skill in combat has increased.")
            print(f"\tAccuracy - {self.accuracy} | Power - {self.power} | Toughness - {self.toughness}")
            user_input = input("\n>> ")
            print()
            if self.health < self.health_cap:
                self.health = self.health_cap
            time.sleep(1)
            return
        else:
            return


# Code below only runs if module is executed as main for the purposes of debugging.

# if __name__ == '__main__':



    # player_one = PlayerCharacter('Player')
    #
    # enemy001 = BasicEnemy('Drone')
    #
    # player_one.equip_weapon('spear')
    # enemy001.equip_weapon('club')
    #
    #
    # def combat_round(hero, enemy):
    #     hero.target = enemy
    #     enemy.target = hero
    #     while player_one.health > 0 and enemy001.health > 0:
    #         if hero.health > 0:
    #             player_one.player_combat_turn()
    #         if enemy.health > 0:
    #             enemy.combat_turn()
    #         if hero.health <= 0:
    #             print(f"{hero} has been slain by {enemy}!")
    #         if enemy.health <= 0:
    #             print(f"{enemy} has been slain by {hero}!")
    #         print()
    #
    #
    # combat_round(player_one, enemy001)

