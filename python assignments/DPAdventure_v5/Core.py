'''

DPAdventure_v5 - CORE

The Core file contains the primary gameplay

** BUG LIST **

* Colliding with an Area of Interest returns all matching AoI
* Approaching the map border can cause a crash >> ADD boundary collision

>> FEATURE ROADMAP

4. ADD COMBAT skills feature
    > Flee, Throw, Shoot
    > ADD COMBAT conditions associated with weapon types - Blind, Disorient, Burn, Stun, Bleed
6. ADD Talent Tree
7. ADD combat targeting system (ie, Head, Body, Arm, Leg) with skill attempt modifiers
8. ADD Story scripting mechanism to random_event that incrementally tells an overarching story
9. MORE random_events
12. ADD multiple maps and transition among them
13. ADD onboarding gameplay tooltips
14. ADD more random items that can be spawned, used, and dropped by enemies

'''

import random
import time
import Entities
import Story
import Enemies
import Items
import Maps
import Areas
import simpleaudio as sa


# >> AUDIO TEST <<

def swan_song():
    wave_obj = sa.WaveObject.from_wave_file("wilhelm_scream.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()

# >> WORLD MAP << TBD...Move to Maps.py

height = 20  # the height of the board
width = 50  # the width of the board

# create a board with the given width and height
# we'll use a list of list to represent the board
board = []  # start with an empty list
for i in range(height):  # loop over the rows
    board.append([])  # append an empty row
    for j in range(width):  # loop over the columns
        board[i].append(' ')  # append an empty space to the board


# >> ACTIVE ELEMENTS <<

active_enemies = []
active_areas_of_interest = []


def spawn_enemy(num): # NEEDS to be expanded to create multiple types
    for i in range(num):
        x = random.randint(3, height - 1)
        y = random.randint(3, width - 1)
        enemy = Entities.BasicEnemy(i=x, j=y)
        if random.randint(0, 1) < 1 == True:
            weapon = Items.Weapon(*Items.basic_primary_weapons[random.randint(0, len(Items.basic_primary_weapons) - 1)])
            enemy.equip_primary_weapon(weapon)
        print(f"A {enemy.name} enters the area.")
        active_enemies.append(enemy)
    print()
    time.sleep(1) # increase later


def enemy_movement():
    for enemy in active_enemies:
        if abs(player.loc_i - enemy.loc_i) < enemy.detection and abs(player.loc_j - enemy.loc_j) < enemy.detection:
            if player.loc_i > enemy.loc_i:
                if abs(player.loc_i - enemy.loc_i) >= 3:  # Pursues in steps of 2 until 1 tile away
                    enemy.loc_i += 2
                else:
                    enemy.loc_i += 1
            elif player.loc_j > enemy.loc_j:
                if abs(player.loc_j - enemy.loc_j) >= 3:
                    enemy.loc_j += 2
                else:
                    enemy.loc_j += 1
            elif player.loc_i < enemy.loc_i:
                if abs(player.loc_i - enemy.loc_i) >= 3:
                    enemy.loc_i -= 2
                else:
                    enemy.loc_i -= 1
            elif player.loc_j < enemy.loc_j:
                if abs(player.loc_j - enemy.loc_j) >= 3:
                    enemy.loc_j -= 2
                else:
                    enemy.loc_j -= 1
        else:
            if enemy.loc_i > 2 and enemy.loc_i < height - 1 and enemy.loc_j > 2 and enemy.loc_j < width - 1:
                enemy.loc_i += random.randint(0, 2)
                enemy.loc_i -= random.randint(0, 2)
                enemy.loc_j += random.randint(0, 2)
                enemy.loc_j -= random.randint(0, 2)
    return


def enemy_encounter(player, enemy):
    player.target = enemy
    enemy.target = player
    print()
    print(f">> You've encountered a {enemy.name.upper()}!")
    print(f'{enemy.name} | {enemy.icon} | LVL{enemy.level} | HEALTH - {enemy.health}')
    while player.health > 0 and enemy.health > 0:
        if player.health > 0:
            player.player_combat_turn()
        if enemy.health > 0:
            enemy.combat_turn()
        if player.health <= 0:
            swan_song()
            print(f"You have been killed by a {enemy.name}!")
            print("GAME OVER")
            exit()
        if enemy.health <= 0:
            enemy_death(enemy)
            x = random.randint(0, 10)
            if x >= 8:
                spawn_enemy(random.randint(0, 3))
    return


def enemy_death(enemy):
    swan_song()
    print(f"\nThe {enemy.name} has been defeated!")
    if enemy.primary_weapon != None:
        print(f"\tIts {enemy.primary_weapon.quality} {enemy.primary_weapon.name} falls to the ground.")
        print(f"\tThe equipment has been added to your inventory.")
        player.inventory.append(enemy.primary_weapon)
    print(f"\tYou earn {enemy.experience_reward} experience points!")
    print()
    player.experience_points += enemy.experience_reward
    active_enemies.remove(enemy)
    player.level_up(player.level)
    Items.search_for_loot(enemy, player)
    return


def spawn_area_of_interest(num):
    for i in range(num):
        i = random.randint(0, height - 1)
        j = random.randint(0, width - 1)
        aoi = Areas.Container(name='Locked Chest', loc_i=i, loc_j=j)
        active_areas_of_interest.append(aoi)


def discover_area(area, player):
    print(f"You approach a {area.name}!")
    if area.locked == True:
        print(f"The {area.name} requires a key to open...")
        time.sleep(1)
        if player.keys > 0:
            print("\tYou remove a key from your inventory and open the lock.")
            print(f"\tInside of the {area.name} you discover a {area.contents}.")
            print(f"\tThe equipment has been added to your inventory.")
            player.inventory.append(area.contents)
            player.experience_points += area.experience_reward
            player.level_up(player.level)
            player.keys -= 1
            active_areas_of_interest.remove(area)
            user_input = input("\n>> ")
            return
        elif player.keys == 0:
            print("\tPerhaps the denizens of the area carry keys...?")
            user_input = input("\n>> ")
            return


def random_event():
    x = random.randint(0, 50)
    if x in [0, 1]:
        print("\nThe grinding sound of metal gears unexpectedly catches your attention...")
        enemy = Entities.BasicEnemy(name='Drone', target=player)
        if random.randint(0, 1) < 1 == True:
            weapon = Items.Weapon(*Items.basic_primary_weapons[random.randint(0, len(Items.basic_primary_weapons) - 1)])
            enemy.equip_primary_weapon(weapon)
        active_enemies.append(enemy)
        time.sleep(2)
        print(f"You've wandered into a hidden {enemy.name}!")
        time.sleep(1)
        enemy.combat_turn()
        enemy_encounter(player, enemy)
    # elif x == 3:
    #     print()
    #     print("You happen upon some edible berries on the side of the road!")
    #     print("\tYour health is increased by 1!")
    #     time.sleep(2)
    #     player_health += 1
    # elif x == 4:
    #     print()
    #     print("An angry squirrel bites you on the ankle!")
    #     print("\tYour health is decreased by 1!")
    #     player_health -= 1
    #     time.sleep(2)
    else:
        return

# if __name__ == '__main__':


# >> GAMEPLAY START <<

name, method = Story.the_story_begins() # << This TOTALLY works!
player = Entities.PlayerCharacter(name)
time.sleep(0) # Increase this later...
if method == 'p':
    starting_weapon = Items.Weapon(*Items.starting_weapons[0])
    player.equip_primary_weapon(starting_weapon)
elif method == 's':
    starting_weapon = Items.Weapon(*Items.starting_weapons[1])
    player.equip_primary_weapon(starting_weapon)


spawn_enemy(7)
spawn_area_of_interest(5)

# >> MOVEMENT <<

while True:
    player.exploration_interface()
    command = input("EXPLORE >> up[W], down[S], left[A], right[D] >> character[C] >> ")  # get the command from the user

    if command.lower() == 'a':
        player.loc_j -= 1  # move left
        random_event()
        enemy_movement()
    elif command.lower() == 'd':
        player.loc_j += 1  # move right
        random_event()
        enemy_movement()
    elif command.lower() == 'w':
        player.loc_i -= 1  # move up
        random_event()
        enemy_movement()
    elif command.lower() == 's':
        player.loc_i += 1  # move down
        random_event()
        enemy_movement()
    elif command.lower() == 'c':
        player.character_screen()

    elif command.lower() == 'p':
        print(active_enemies)

    # >> COLLISION <<

    # check if the player is on the same space as an enemy
    for enemy in active_enemies:
        if enemy.loc_i == player.loc_i and enemy.loc_j == player.loc_j:
            enemy_encounter(player, enemy)

    # check if the player is on the same space as an Area of Interest
    for area in active_areas_of_interest:
        if area.loc_i == player.loc_i and area.loc_j == player.loc_j:
            discover_area(area, player)


    # print out the board
    for i in range(height):
        for j in range(width):
            # if we're at the player location, print the player icon
            if i == player.loc_i and j == player.loc_j:
                print(player.icon, end=' ')
            for enemy in active_enemies:
                if enemy.loc_i == i and enemy.loc_j == j:
                    print(enemy.icon, end=' ')
            for aoi in active_areas_of_interest:
                if aoi.loc_i == i and aoi.loc_j == j:
                    print(aoi.icon, end=' ')
            else:
                print(board[i][j], end=' ')  # otherwise print the board square
        print()