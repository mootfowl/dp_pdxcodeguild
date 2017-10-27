'''
EVENTS

Character creation, overarching story, puzzle rooms, areas of interest

'''

import random
import time
import Entities
import Items

# >> CHARACTER CREATION <<

timer = 2


def the_story_begins():
    print("\nYou awaken from a dream...")

    time.sleep(timer)
    
    print("""\nLooking around the cold, empty room, you spot a simple, closed door. Your eye wanders to find a 
    a small, ornately carved box sitting on the floor at the room's center. As you inspect the box more closely, you 
    notice two things: The hinged lid of the box is sturdily locked. And there is a small inscription of two initials
    on the top of the lid that you can vaguely make out. The letters seem vaguely familiar to you.""")

    time.sleep(timer * 2)

    inscription = input("\nWhat are the letters inscribed on the box? >> ")

    print(f"""\nWhat could "{inscription}" mean? And why is it so familiar? Returning your attention to the box, you 
    search the room for a key. Although a key is nowhere to be found, you discover a rusty, broken knife, and a hollow, 
    metal rod. Perhaps you can force the box open in some way...?""")

    time.sleep(timer)

    print("\nHow will you open the box...?")

    time.sleep(timer)
    
    print("""\n\tUse the dull knife to pry[P] open the lid?
    \n\tOr smash[S] the box apart with the heavy stick?""")

    method = input("\nACTION >> ")

    if method.lower() == 'p':
        print("\n\tThe lock breaks easily as you slide the knife under the lid and pry it open.")
    elif method.lower() == 's':
        print("\n\tThe walls of the box smash apart as you swing the metal rod down forcefully.")
    # elif method.lower() != 'p' or 's':

    print("\tThe box contains a simple, coarse stone the size of your fist with a large hole running through its center.")

    time.sleep(timer)

    print("\tAn idea emerges...")

    time.sleep(timer)

    if method.lower() == 'p':
        print("\nYou use the coarse surface of the stone to sharpen the knife.")
        time.sleep(1)
        print("\tYou EQUIP the BROKEN KNIFE.")
        print("\tYou gain the STAB ability.")
    elif method.lower() == 's':
        print("\nThe hole of the stone fits snugly over the end of the metal rod, forming a makeshift hammer.")
        time.sleep(timer)
        print("\tYou EQUIP the MAKESHIFT HAMMER.")
        print("\tYou gain the SMASH ability.")
    # elif method.lower() != 'p' or 's':


    time.sleep(timer)

    print("""\tYou feel emboldened by your new found weapon and ability.
    
    You open the door, and your ADVENTURE begins...""")
    user_input = input("\n>> ")
    print()

    time.sleep(timer)

    return inscription, method





