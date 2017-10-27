'''
AREAS

Areas and objects of interest

'''

import random
import time
import Entities
import Items


class AreaOfInterest:
    def __init__(self, name, loc_i=0, loc_j=0, locked=True, guard=False, experience_reward=1):
        self.name = name
        self.loc_i = loc_i
        self.loc_j = loc_j
        self.locked = locked
        self.guard = guard
        self.experience_reward = experience_reward


class Container(AreaOfInterest):
    def __init__(self, name, loc_i, loc_j, locked=True, guard=False, experience_reward=1, icon='\u2690'):
        super().__init__(name, loc_i, loc_j, locked, guard, experience_reward)
        self.icon = icon
        self.contents = Items.Weapon(*Items.basic_primary_weapons[random.randint(0, len(Items.basic_primary_weapons) - 1)])









