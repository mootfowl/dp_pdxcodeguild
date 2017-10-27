'''

Turn-based Action Point COMBAT system
v1

'''

import random


class Entity:
    def __init__(self, name=f'Enemy', target=None):
        self.name = name
        self.health = 30
        self.action_points = 2
        self.damage = 7
        self.accuracy = 80
        self.heal = 4
        self.target = target
        self.combo = 0

    def quick_attack(self):
        print(f"The {self.name} attempts to JAB {self.target.name}!")
        quick_modifier = 10
        dmg = self.damage - 3
        x = random.randint(1, 100)
        self.action_points -= 1
        if x < self.accuracy + quick_modifier:
            print(f"The JAB hurts {self.target.name} for {dmg}!")
            self.target.health -= dmg
            self.action_points += 2
            self.combo += 1
        else:
            print(f"{self.target.name} evades the JAB!")

    def strong_attack(self):
        print(f"The {self.name} attempts to SMACK {self.target.name}!")
        strong_modifier = -10
        dmg = self.damage - 2
        x = random.randint(1, 100)
        self.action_points -= 3
        if x < self.accuracy + strong_modifier:
            print(f"The SMACK hurts {self.target.name} for {dmg}!")
            self.target.health -= dmg
            self.action_points += 4
            self.combo += 1
        else:
            print(f"{self.target.name} evades the SMACK!")

    def vicious_attack(self):
        print(f"The {self.name} attempts to CLOBBER {self.target.name}!")
        vicious_modifier = -20
        dmg = self.damage
        x = random.randint(1, 100)
        self.action_points -= 4
        if x < self.accuracy + vicious_modifier:
            print(f"The CLOBBER hurts {self.target.name} for {dmg}!")
            self.target.health -= dmg
            # self.action_points += 1
            self.combo += 1
        else:
            print(f"{self.target.name} evades the CLOBBER!")

    def repair(self):
        print(f"The {self.name} repairs itself for {self.heal}!")
        self.health += self.heal
        self.action_points -= 2

    def combat_turn(self):
        while self.action_points > 0 and self.target.health > 0:
            print(f'action: {self.action_points} combo: {self.combo}')
            if self.action_points >= 4 and self.health >= 12 and self.combo >= 2:
                self.vicious_attack()
            elif self.action_points >= 3 and self.health < 12:
                self.repair()
            elif self.action_points >= 3 and self.combo >= 1:
                self.strong_attack()
            elif self.action_points >= 1:
                self.quick_attack()
            else:
                pass
        print(f'action: {self.action_points} combo: {self.combo}')
        self.action_points += 3
        if self.combo >= 1:
            self.combo -= 1


x = Entity('Drone')

y = Entity('Player', x)

def combat_round(enemy):
    x.target = enemy
    i = 0
    while x.health > 0 and y.health > 0:
        i += 1
        print(f">>> ROUND {i}")
        x.combat_turn()
        print(f"{x.name} health: {x.health}, {y.name} health: {y.health}")
        print()
        y.combat_turn()
        print(f"{x.name} health: {x.health}, {y.name} health: {y.health}")
        print()


combat_round(y)