'''

LAB30v2 - Adventure!!

'''

import random
import time

height = 15  # the height of the board
width = 40  # the width of the board

# create a board with the given width and height
# we'll use a list of list to represent the board
board = []  # start with an empty list
for i in range(height):  # loop over the rows
    board.append([])  # append an empty row
    for j in range(width):  # loop over the columns
        board[i].append(' ')  # append an empty space to the board

# define the player attributes
player_i = 10
player_j = 4
player_icon = u"\U0001F680"

possible_enemies = [{'type': 'Saucer', 'icon': u"\U0001F6F0", 'loc': [], 'aggro': 5},
                    {'type': 'Frigate', 'icon': u"\U0001F681", 'loc': [], 'aggro': 10}]

enemy_icons = []
for enemy in possible_enemies: # Populates enemy_icons list with all icons which are later checked for collision with player
    enemy_icons.append(enemy['icon'])

active_enemies = []

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


spawn_enemy(5)

# loop until the user says 'done' or dies
while True:
    print(player_icon, end=' ')
    command = input("EXPLORE >> W, S, A, D >> ")  # get the command from the user

    if command.lower() == 'done':
        break  # exit the game
    elif command.lower() == 'a':
        player_j -= 1  # move left
        enemy_movement()
    elif command.lower() == 'd':
        player_j += 1  # move right
        enemy_movement()
    elif command.lower() == 'w':
        player_i -= 1  # move up
        enemy_movement()
    elif command.lower() == 's':
        player_i += 1  # move down
        enemy_movement()

    # check if the player is on the same space as an enemy
    if board[player_i][player_j] in enemy_icons:
        FIGHT = input("IT WORKED!")
        board[player_i][player_j] = ' '  # remove the enemy from the board
        for enemy in active_enemies:
            if enemy['loc'][0] == player_i and enemy['loc'][1] == player_j:
                active_enemies.remove(enemy)
                x = random.randint(0, 10)
                if x > 5:
                    spawn_enemy(2)

    # print out the board
    for i in range(height):
        for j in range(width):
            # if we're at the player location, print the player icon
            if i == player_i and j == player_j:
                print(player_icon, end=' ')
            else:
                print(board[i][j], end=' ')  # otherwise print the board square
        print()