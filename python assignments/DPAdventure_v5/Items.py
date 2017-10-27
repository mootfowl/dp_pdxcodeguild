'''
ITEMS - Loot (weapons, armor, etc.) and interactive objects (locked boxes, ????)

Quality scaling concepts:

Slashing (knife, sword, spear) - Dull, Sharpened
Crushing (hammer, cudgel, club, staff) - Makeshift, Balanced
Piercing (spear, ???)

Useful unicode weapon icons:

Pickaxe \u26cf
Crossed Swords \u2694
Crossed Hammer and Pickaxe \u2692
Arrow \u27b4

'''

import time
import random


class Item:
    def __init__(self, name, level=0):
        self.name = name
        self.level = level
        self.health = 0
        self.power = level * 3
        self.toughness = level * 3


class Weapon(Item):
    def __init__(self, name, level, quality, icon, quick_name, strong_name, vicious_name):
        super().__init__(name, level)
        self.quality = quality
        self.icon = icon
        self.accuracy = self.level * 3
        self.quick_name = quick_name.upper()
        self.strong_name = strong_name.upper()
        self.vicious_name = vicious_name.upper()

    def __str__(self):
        return f'{self.quality} {self.name} | {self.icon} | LVL{self.level} | Power - {self.power} | Accuracy - {self.accuracy}'


class Armor(Item):
    def __init__(self, name, quality, type, slot):
        super().__init__(name)
        self.quality = quality
        self.type = type
        self.slot = slot

# >> LOOT TABLES <<

starting_weapons = [
    ('Knife', 1, 'Broken', '\u2903', 'Stab', 'Slash', 'Puncture'),
    ('Hammer', 1, 'Makeshift', '\u2692', 'Smash', 'Whack', 'Demolish')
    ]


basic_primary_weapons = [
    ('Knife', 2, 'Rusty', '\u2694', 'Stab', 'Slash', 'Puncture'),
    ('Hammer', 2, 'Worn', '\u2692', 'Smash', 'Whack', 'Demolish'),
    ('Spear', 2, 'Unbalanced', '\u279a', 'Stab', 'Slash', 'Skewer')
    ]

# x = Weapon(*items[0])
# print(x)


def search_for_loot(source, player):
    print(f"You search the remains of the {source.name} for salvageable parts...")
    time.sleep(1)
    x = random.randint(0, 20)
    if x in [1, 3]:
        player.keys += 1
        print("\tYou've found a KEY!")
    if x in [1, 7]:
        y = random.randint(1, 4)
        player.ammunition += y
        print(f"\tYou've found {y} ammunition!")
    else:
        print(f"The {source.name} was too badly damaged to find anything useful.")
    user_input = input("\n>> ")
#
#     loot = treasure[x]['item']
#     print(f"\tYou find a {loot}!")
#     if treasure[x]['health'] > 0:
#         player_health += treasure[x]['health']
#         print(f"\tYour HEALTH has increased by {treasure[x]['health']}.")
#     if treasure[x]['slot'] != None:
#         compare_slot = treasure[x]['slot'] # This compares found treasure with what is currently equipped, and only equips improvements
#         if player_inventory[compare_slot] == None or player_inventory[compare_slot]['power'] < treasure[x]['power']\
#                 or player_inventory[compare_slot]['armor'] < treasure[x]['armor']:
#             print(f"You equip the {treasure[x]['item']}.")
#             if treasure[x]['power'] > 0:
#                 player_power += treasure[x]['power']
#                 if player_inventory[compare_slot] != None:
#                     player_power -= player_inventory[compare_slot]['power']
#                 print(f"\tYour POWER has increased by {treasure[x]['power']}.")
#             if treasure[x]['armor'] > 0:
#                 player_armor += treasure[x]['armor']
#                 if player_inventory[compare_slot] != None:
#                     player_armor -= player_inventory[compare_slot]['armor']
#                 print(f"\tYour ARMOR has increased by {treasure[x]['armor']}.")
#             if treasure[x]['skill'] > 0:
#                 player_skill += treasure[x]['skill']
#                 print(f"\tYour SKILL has increased by {treasure[x]['skill']}.")
#             if treasure[x]['abilities'] != None:
#                 if treasure[x]['abilities'] not in player_abilities:
#                     player_abilities.append(treasure[x]['abilities'])
#                     print(f"\tYou gain the {treasure[x]['abilities']} ability!")
#             player_inventory[compare_slot] = treasure[x]
#     time.sleep(3.5)
#     return
