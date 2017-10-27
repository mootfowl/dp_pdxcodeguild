'''

LAB30v3 - Adventure!!

'''

import random
import time

height = 20  # the height of the board
width = 40  # the width of the board

# create a board with the given width and height
# we'll use a list of list to represent the board
board = []  # start with an empty list
for i in range(height):  # loop over the rows
    board.append([])  # append an empty row
    for j in range(width):  # loop over the columns
        board[i].append(' ')  # append an empty space to the board


### ENEMIES ###

possible_enemies = [{'type': 'Skeleton', 'icon': '\u2620', 'loc': [], 'aggro': 4, 'health': 4, 'dmg': 3,
                     'atk': 'removes a rib and throws it at you!', 'skill': 7, 'exp': 1},
                    {'type': 'Zombie', 'icon': '\u2686', 'loc': [], 'aggro': 4, 'health': 3, 'dmg': 3,
                     'atk': 'gnashes its teeth viciously!', 'skill': 7, 'exp': 1},
                    {'type': 'Goblin', 'icon': '\u263f', 'loc': [], 'aggro': 6, 'health': 5, 'dmg': 4,
                     'atk': 'aims his spear at your chest!', 'skill': 7, 'exp': 2},
                    {'type': 'Cyclops', 'icon': '\u2609', 'loc': [], 'aggro': 6, 'health': 8, 'dmg': 7,
                     'atk': 'swings his massive hammer at your head!', 'skill': 6, 'exp': 3},
                    {'type': 'Bandit', 'icon': '\u26b2', 'loc': [], 'aggro': 6, 'health': 5, 'dmg': 3,
                     'atk': 'draws a dagger and attempts to stab you!', 'skill': 9, 'exp': 2},
                    {'type': 'Dragon', 'icon': '\u262c', 'loc': [], 'aggro': 3, 'health': 30, 'dmg': 10,
                     'atk': 'breathes a massive cone of fire towards you!', 'skill': 8, 'exp': 8}
                    ]

enemy_icons = []
for enemy in possible_enemies:  # Populates enemy_icons list with all icons which are later checked for collision with player
    enemy_icons.append(enemy['icon'])

active_enemies = []

### TREASURE ###

# Possible treasure dropped from slain enemies
treasure = {0: {'item': 'pocket full of lint', 'slot': None, 'power': 0, 'health': 0, 'armor': 0, 'skill': 0,
                'abilities': None},
            1: {'item': 'Potion of Healing', 'slot': None, 'power': 0, 'health': 3, 'armor': 0, 'skill': 0,
                'abilities': None},
            2: {'item': 'Healing Herb', 'slot': None, 'power': 0, 'health': 1, 'armor': 0, 'skill': 0,
                'abilities': None},
            3: {'item': 'Rusty Axe', 'slot': 'melee', 'power': 1, 'health': 0, 'armor': 0, 'skill': 0,
                'abilities': None},
            4: {'item': 'Steel Warhammer', 'slot': 'melee', 'power': 2, 'health': 0, 'armor': 0, 'skill': 5,
                'abilities': None},
            5: {'item': 'Flaming Longsword', 'slot': 'melee', 'power': 3, 'health': 0, 'armor': 0, 'skill': 5,
                'abilities': None},
            6: {'item': 'sack full of rocks', 'slot': None, 'power': 0, 'health': 0, 'armor': 0, 'skill': 0,
                'abilities': None},
            7: {'item': 'lump of stinky cheese', 'slot': None, 'power': 0, 'health': 1, 'armor': 0, 'skill': 0,
                'abilities': None},
            8: {'item': 'Horned Helmet', 'slot': 'helmet', 'power': 1, 'health': 0, 'armor': 1, 'skill': 0,
                'abilities': None},
            9: {'item': 'Tower Shield', 'slot': 'shield', 'power': 0, 'health': 0, 'armor': 1, 'skill': 0,
                'abilities': 'BASH (2 dmg - 100%)'},
            10: {'item': 'Balanced Shortbow', 'slot': 'ranged', 'power': 0, 'health': 0, 'armor': 0, 'skill': 0,
                 'abilities': 'SHOOT (3 dmg - 70%)'},

            51: {'item': 'Sharpened Stick', 'slot': 'melee', 'power': 0, 'health': 0, 'armor': 0, 'skill': 0,
                 'abilities': None}
            }

### PLAYER ###

# define the player attributes
player_i = 10
player_j = 20
player_icon = '\u2658'
player_health = 10
player_power = 3
player_armor = 0
player_skill = 65
player_abilities = [f"attack[Q] (1-{player_power} dmg - {player_skill}% success)", "h[E]al (2 pts)"]
player_inventory = {'keys': 0, 'melee': treasure[51], 'ranged': None, 'shield': None, 'helmet': None}
player_ammunition = 0


def spawn_enemy(num):
    for i in range(num):
        enemy = eval(repr(random.choice(possible_enemies)))
        # eval(repr()) makes an actual copy (rather than just a a duplicate variable pointing at the same object)
        enemy_i = random.randint(3, height - 1)
        enemy_j = random.randint(3, width - 1)
        active_enemies.insert(0, enemy)
        active_enemies[0]['loc'].append(enemy_i)
        active_enemies[0]['loc'].append(enemy_j)
        board[enemy_i][enemy_j] = enemy['icon']
        print(f"A {enemy['type']} enters the area.")
    time.sleep(2)
    # print(active_enemies)

def enemy_movement():
    for enemy in active_enemies:
        board[enemy['loc'][0]][enemy['loc'][1]] = ' ' # I *think* this will delete their original position...
        if abs(player_i - enemy['loc'][0]) < enemy['aggro'] and abs(player_j - enemy['loc'][1]) < enemy['aggro']: # checks range
            if player_i > enemy['loc'][0]:
                if abs(player_i - enemy['loc'][0]) >= 3: # Pursues in steps of 2 until 1 tile away
                    enemy['loc'][0] += 2
                else:
                    enemy['loc'][0] += 1
            elif player_j > enemy['loc'][1]:
                if abs(player_j - enemy['loc'][1]) >= 3:
                    enemy['loc'][1] += 2
                else:
                    enemy['loc'][1] += 1
            elif player_i < enemy['loc'][0]:
                if abs(player_i - enemy['loc'][0]) >= 3:
                    enemy['loc'][0] -= 2
                else:
                    enemy['loc'][0] -= 1
            elif player_j < enemy['loc'][1]:
                if abs(player_j - enemy['loc'][1]) >= 3:
                    enemy['loc'][1] -= 2
                else:
                    enemy['loc'][1] -= 1
        else:
            if enemy['loc'][0] > 2 and enemy['loc'][0] < height - 1 and enemy['loc'][1] > 2 and enemy['loc'][1] < width - 1:
                enemy['loc'][0] += random.randint(0, 1)
                enemy['loc'][0] -= random.randint(0, 1)
                enemy['loc'][1] += random.randint(0, 1)
                enemy['loc'][1] -= random.randint(0, 1)
        board[enemy['loc'][0]][enemy['loc'][1]] = enemy['icon'] # ...and this draws their new position
    return

def enemy_attack(monster):
    global player_health
    print(f"The {monster['type']}", monster['atk'])
    time.sleep(0.5)
    monster_attempt = random.randint(0, 10)
    if monster_attempt >= monster['skill']:
        print(f"The {monster['type']}'s attack MISSES!")
    elif monster_attempt < monster['skill']:
        print(f"The {monster['type']}'s attack hits you squarely!")
        monster_dmg = (random.randint(1, monster['dmg'])) - player_armor
        if monster_dmg > 0:
            print(f"You take {monster_dmg} points of damage!")
            player_health -= monster_dmg
        else:
            print("Your ARMOR absorbs the full damage of the attack!")
    return

def enemy_death(monster):
    global player_skill
    print(f"The {monster['type']} has been defeated!")
    print(f"You earn {monster['exp']} experience points!")
    if player_skill < 90:
        player_skill += monster['exp']
    find_treasure(monster)
    return


def inventory():
    print("INVENTORY >>")
    print(f"KEYS: {player_inventory['keys']} | AMMUNITION: {player_ammunition}")
    if player_inventory['melee'] != None:
        print(f"MELEE: {player_inventory['melee']['item']}", end=' ')
    if player_inventory['ranged'] != None:
        print(f"| RANGED: {player_inventory['ranged']['item']}")
    if player_inventory['shield'] != None:
        print(f"SHIELD: {player_inventory['shield']['item']}", end=' ')
    if player_inventory['helmet'] != None:
        print(f"| HELMET: {player_inventory['helmet']['item']}")
    print()
    x = input("RETURN to game...")
    return


def find_treasure(source):
    global player_health
    global player_power
    global player_armor
    global player_abilities
    global player_skill
    global player_ammunition
    print(f"You search the {source['type']} for treasure...")
    time.sleep(1)
    print()
    x = random.randint(0, 10)
    if x in [1, 3, 5]:
        player_inventory['keys'] += 1
        print("You've found a key!")
    if x % 2 == 0:
        y = random.randint(0, 3)
        player_ammunition += y
        if y > 0:
            print(f"You've found {y} ammunition!")
    loot = treasure[x]['item']
    print(f"You find a {loot}!")
    if treasure[x]['health'] > 0:
        player_health += treasure[x]['health']
        print(f"Your HEALTH has increased by {treasure[x]['health']}.")
    if treasure[x]['slot'] != None:
        compare_slot = treasure[x]['slot'] # This compares found treasure with what is currently equipped, and only equips improvements
        if player_inventory[compare_slot] == None or player_inventory[compare_slot]['power'] < treasure[x]['power']\
                or player_inventory[compare_slot]['armor'] < treasure[x]['armor']:
            print(f"You equip the {treasure[x]['item']}.")
            if treasure[x]['power'] > 0:
                player_power += treasure[x]['power']
                if player_inventory[compare_slot] != None:
                    player_power -= player_inventory[compare_slot]['power']
                print(f"Your POWER has increased by {treasure[x]['power']}.")
            if treasure[x]['armor'] > 0:
                player_armor += treasure[x]['armor']
                if player_inventory[compare_slot] != None:
                    player_armor -= player_inventory[compare_slot]['armor']
                print(f"Your ARMOR has increased by {treasure[x]['armor']}.")
            if treasure[x]['skill'] > 0:
                player_skill += treasure[x]['skill']
                print(f"Your SKILL has increased by {treasure[x]['skill']}.")
            if treasure[x]['abilities'] != None:
                if treasure[x]['abilities'] not in player_abilities:
                    player_abilities.append(treasure[x]['abilities'])
                    print(f"You gain the {treasure[x]['abilities']} ability!")
            player_inventory[compare_slot] = treasure[x]
    time.sleep(3.5)
    return


def random_event():
    global player_health
    x = random.randint(0, 30)
    if x in [0, 1, 2]:
        print("What's that sound...?!")
        time.sleep(2)
        print(f"You've wandered into a hidden {possible_enemies[x]['type']}!")
        time.sleep(1)
        enemy_attack(possible_enemies[x])
        enemy_encounter(possible_enemies[x])
    elif x == 3:
        print("You happen upon some edible berries on the side of the road!")
        print("Your health is increased by 1!")
        time.sleep(2)
        player_health += 1
    elif x == 4:
        print("An angry squirrel bites you on the ankle!")
        print("Your health is decreased by 1!")
        player_health -= 1
        time.sleep(2)
    else:
        return

def enemy_encounter(monster):
    global player_health
    global player_ammunition
    print()
    print(f"The {monster['type']} eyes you menacingly! ", monster['icon'])
    enemy_health = monster['health']
    while enemy_health > 0 and player_health > 0:
        print()
        print(f"{monster['type']}: {enemy_health}")
        action = input(f"HEALTH: {player_health} | ABILITIES >> {player_abilities} >> ")
        if action.lower() == 'q':
            print("You attempt an attack...")
            swing_attempt = random.randint(0, 100)

            if swing_attempt > player_skill:
                print("You swing and MISS!")
                time.sleep(1)
                enemy_attack(monster)

            if swing_attempt <= player_skill:
                print(f"Your attack hits the {monster['type']}!")
                dmg = random.randint(1, player_power)
                enemy_health -= dmg
                print(f"Your attack does {dmg} points of damage.")
                time.sleep(1)
                if enemy_health > 0:
                    enemy_attack(monster)

        elif action.lower() == 'e':
            print("You heal yourself for 2 points.")
            player_health += 2
            enemy_attack(monster)

        elif action == 'bash' and 'BASH (2 dmg - 100%)' in player_abilities:
            print(f"You bash the {monster['type']} with your shield for 2 points.")
            enemy_health -= 2
            enemy_attack(monster)

        elif action == 'shoot' and 'SHOOT (3 dmg - 70%)' in player_abilities:
            if player_ammunition > 0:
                swing_attempt = random.randint(0, 100)
                if swing_attempt > 60:
                    print("Your shot MISSES!")
                    time.sleep(0.5)
                    enemy_attack(monster)
                    player_ammunition -= 1

                if swing_attempt <= 70:
                    print(f"Your shot hits the {monster['type']}, causing 3 damage!")
                    enemy_health -= 3
                    player_ammunition -= 1
                    if enemy_health > 0:
                        enemy_attack(monster)
            else:
                print("You are out of ammunition!")

    if enemy_health <= 0:
        enemy_death(monster)
        board[player_i][player_j] = ' '  # remove the enemy from the board
        for enemy in active_enemies:
            if enemy['loc'][0] == player_i and enemy['loc'][1] == player_j:
                active_enemies.remove(enemy)
                x = random.randint(0, 10)
                if x > 5:
                    spawn_enemy(random.randint(0, 3))
        return

    if player_health <= 0:
        print(f"You have been slain by a {monster['type']}!")
        print("GAME OVER")
        exit()


### GAMEPLAY START ###

print("Your ADVENTURE begins...")
time.sleep(1)
print()
spawn_enemy(9)

# loop until the user says 'done' or dies
while True:
    print()
    print(player_icon, f"HEALTH - {player_health} | POWER - {player_power} | ARMOR - {player_armor} | SKILL - {player_skill}%")
    command = input("EXPLORE >> up[W], down[S], left[A], right[D] >> [I]nventory >> ")  # get the command from the user

    if command.lower() == 'done':
        break  # exit the game
    elif command.lower() == 'a':
        player_j -= 1  # move left
        random_event()
        enemy_movement()
    elif command.lower() == 'd':
        player_j += 1  # move right
        random_event()
        enemy_movement()
    elif command.lower() == 'w':
        player_i -= 1  # move up
        random_event()
        enemy_movement()
    elif command.lower() == 's':
        player_i += 1  # move down
        random_event()
        enemy_movement()
    elif command.lower() == 'i':
        inventory()

    # check if the player is on the same space as an enemy
    if board[player_i][player_j] in enemy_icons:
        for enemy in active_enemies:
            if enemy['icon'] == board[player_i][player_j]: # and enemy['loc'][0] == [player_i] and enemy['loc'][1] == [player_j]:
                current_enemy = enemy
                enemy_encounter(current_enemy)



    # print out the board
    for i in range(height):
        for j in range(width):
            # if we're at the player location, print the player icon
            if i == player_i and j == player_j:
                print(player_icon, end=' ')
            else:
                print(board[i][j], end=' ')  # otherwise print the board square
        print()