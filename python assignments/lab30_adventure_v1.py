import random
import time

width = 100  # the width of the board
height = 20  # the height of the board

# create a board with the given width and height
# we'll use a list of list to represent the board
board = []  # start with an empty list
for i in range(height):  # loop over the rows
    board.append([])  # append an empty row
    for j in range(width):  # loop over the columns
        board[i].append(' ')  # append an empty space to the board

# define the player attributes
player_i = 4
player_j = 4
player_icon = '\u2658'
player_health = 10
player_power = 3
player_armor = 0
player_skill = 65
player_abilities = [f"ATTACK (1-{player_power} dmg - {player_skill}% success)", "HEAL (2 pts)"]

# Roster of enemies
enemies = {'Skeleton': {'icon': '\u2620', 'health': 4, 'dmg': 4, 'atk': 'removes a rib and throws it at you!', 'skill': 6, 'experience': 1},
           'Cyclops': {'icon': '\u2686', 'health': 8, 'dmg': 7, 'atk': 'swings his massive hammer!', 'skill': 5, 'experience': 3},
           'Hidden Bandit': {'icon': '\u2694', 'health': 5, 'dmg': 3, 'atk': 'attempts to stab you with his dagger!', 'skill': 8, 'experience': 2},
           'Dragon': {'icon': '\u262c', 'health': 30, 'dmg': 10, 'atk': 'breathes a massive cone of fire!', 'skill': 7, 'experience': 5}
           }

# Possible treasure dropped from slain enemies
treasure = {0: {'item': 'pocket full of lint', 'power': 0, 'health': 0, 'armor': 0, 'skill': 0, 'abilities': None},
            1: {'item': 'Potion of Healing', 'power': 0, 'health': 3, 'armor': 0, 'skill': 0, 'abilities': None},
            2: {'item': 'Healing Herb', 'power': 0, 'health': 1, 'armor': 0, 'skill': 0, 'abilities': None},
            3: {'item': 'Rusty Axe', 'power': 1, 'health': 0, 'armor': 0, 'skill': 0, 'abilities': None},
            4: {'item': 'Steel Warhammer', 'power': 2, 'health': 0, 'armor': 0, 'skill': 5, 'abilities': None},
            5: {'item': 'Flaming Longsword', 'power': 3, 'health': 0, 'armor': 0, 'skill': 5, 'abilities': None},
            6: {'item': 'sack full of rocks', 'power': 0, 'health': 0, 'armor': 0, 'skill': 0, 'abilities': None},
            7: {'item': 'lump of stinky cheese', 'power': 0, 'health': 1, 'armor': 0, 'skill': 0, 'abilities': None},
            8: {'item': 'Horned Helmet', 'power': 1, 'health': 0, 'armor': 1, 'skill': 0, 'abilities': None},
            9: {'item': 'Tower Shield', 'power': 0, 'health': 0, 'armor': 1, 'skill': 0, 'abilities': 'BASH (2 dmg - 100%)'},
            10: {'item': 'Balanced Shortbow', 'power': 3, 'health': 0, 'armor': 3, 'skill': 0, 'abilities': 'SHOOT (5 dmg - 60%)'}

            }


# add 4 Skeletons in random locations
for i in range(4):
    enemy_i = random.randint(0, height - 1)
    enemy_j = random.randint(0, width - 1)
    board[enemy_i][enemy_j] = enemies['Skeleton']['icon']

# Add 3 Cyclops in random locations
for i in range(3):
    enemy_i = random.randint(0, height - 1)
    enemy_j = random.randint(0, width - 1)
    board[enemy_i][enemy_j] = enemies['Cyclops']['icon']

# Add 1 Dragon
for i in range(1):
    enemy_i = random.randint(0, height - 1)
    enemy_j = random.randint(0, width - 1)
    board[enemy_i][enemy_j] = enemies['Dragon']['icon']

def enemy_attack(monster):
    global player_health
    print(f"The {monster}", enemies[monster]['atk'])
    time.sleep(0.5)
    monster_attempt = random.randint(0, 10)
    if monster_attempt >= enemies[monster]['skill']:
        print(f"The {monster}'s attack MISSES!")
    elif monster_attempt < enemies[monster]['skill']:
        print(f"The {monster}'s attack hits you squarely!")
        monster_dmg = (random.randint(1, enemies[monster]['dmg'])) - player_armor
        if monster_dmg > 0:
            print(f"You take {monster_dmg} points of damage!")
            player_health -= monster_dmg
        else:
            print("Your ARMOR absorbs the full damage of the attack!")

def enemy_death(monster):
    global player_health
    global player_power
    global player_armor
    global player_skill
    global player_abilities
    print(f"The {monster} has been defeated!")
    print(f"You earn {enemies[monster]['experience']} experience points!")
    if player_skill < 90:
        player_skill += enemies[monster]['experience']
    print(f"You search the {monster}'s corpse for treasure...")
    time.sleep(1)
    x = random.randint(0, 10)
    loot = treasure[x]['item']
    print(f"You find a {loot}!")
    if treasure[x]['health'] > 0:
        player_health += treasure[x]['health']
        print(f"Your HEALTH has increased by {treasure[x]['health']}.")
    if treasure[x]['power'] > 0:
        player_power += treasure[x]['power']
        print(f"Your POWER has increased by {treasure[x]['power']}.")
    if treasure[x]['armor'] > 0:
        player_armor += treasure[x]['armor']
        print(f"Your ARMOR has increased by {treasure[x]['armor']}.")
    if treasure[x]['skill'] > 0:
        player_skill += treasure[x]['skill']
        print(f"Your SKILL has increased by {treasure[x]['skill']}.")
    if treasure[x]['abilities'] != None:
        if treasure[x]['abilities'] not in player_abilities:
            player_abilities.append(treasure[x]['abilities'])
            print(f"You gain the {treasure[x]['abilities']} ability!")

def random_event():
    global player_health
    x = random.randint(1, 20)
    if x in [1, 2]:
        enemy_encounter('Hidden Bandit')
    elif x == 3:
        print("You happen upon some edible berries on the side of the road!")
        print("Your health is increased by 1!")
        player_health += 1
    elif x == 4:
        print("An angry squirrel bites you on the ankle!")
        print("Your health is decreased by 1!")
    else:
        return

def enemy_encounter(monster):
    global player_health
    print(f"You've encountered a {monster}! ", enemies[monster]['icon'])
    enemy_health = enemies[monster]['health']
    while enemy_health > 0 and player_health > 0:
        print(f"{monster}: {enemy_health}")
        action = input(f"HEALTH: {player_health} | ABILITIES >> {player_abilities} >> ")
        if action == 'attack':
            print("You attempt an attack...")
            swing_attempt = random.randint(0, 100)

            if swing_attempt > player_skill:
                print("You swing and MISS!")
                time.sleep(0.5)
                enemy_attack(monster)

            if swing_attempt <= player_skill:
                print(f"Your attack hits the {monster}!")
                dmg = random.randint(1, player_power)
                enemy_health -= dmg
                print(f"Your attack does {dmg} points of damage.")
                if enemy_health > 0:
                    enemy_attack(monster)

        elif action == 'heal':
            print("You heal yourself for 2 points.")
            player_health += 2
            enemy_attack(monster)

        elif action == 'bash' and 'BASH (2 dmg - 100%)' in player_abilities:
            print(f"You bash the {monster} with your shield for 2 points.")
            enemy_health -= 2
            enemy_attack(monster)

        elif action == 'shoot' and 'SHOOT (5 dmg - 60%)' in player_abilities:
            swing_attempt = random.randint(0, 100)
            if swing_attempt > 60:
                print("Your arrow MISSES!")
                time.sleep(0.5)
                enemy_attack(monster)

            if swing_attempt <= 60:
                print(f"Your arrow hits the {monster}, causing 5 damage!")
                enemy_health -= 5
                if enemy_health > 0:
                    enemy_attack(monster)

    if enemy_health <= 0:
        enemy_death(monster)
        board[player_i][player_j] = ' '  # remove the enemy from the board

    if player_health <= 0:
        print(f"You have been slain by a {monster}!")
        print("GAME OVER")
        exit()

# loop until the user says 'done' or dies
while True:
    print(f"\u2658 HEALTH - {player_health} | POWER - {player_power} | ARMOR - {player_armor} | SKILL - {player_skill}%")
    command = input("EXPLORE >> - L, R, U, D >> ")  # get the command from the user

    if command.lower() == 'done':
        break  # exit the game
    elif command.lower() == 'l':
        player_j -= 1  # move left
        random_event()
    elif command.lower() == 'r':
        player_j += 1  # move right
        random_event()
    elif command.lower() == 'u':
        player_i -= 1  # move up
        random_event()
    elif command.lower() == 'd':
        player_i += 1  # move down
        random_event()

    # check if the player is on the same space as an enemy
    if board[player_i][player_j] == enemies['Cyclops']['icon']:
        enemy_encounter('Cyclops')
    elif board[player_i][player_j] == enemies['Skeleton']['icon']:
        enemy_encounter('Skeleton')
    elif board[player_i][player_j] == enemies['Dragon']['icon']:
        enemy_encounter('Dragon')

    # print out the board
    for i in range(height):
        for j in range(width):
            # if we're at the player location, print the player icon
            if i == player_i and j == player_j:
                print(player_icon, end=' ')
            else:
                print(board[i][j], end=' ')  # otherwise print the board square
        print()