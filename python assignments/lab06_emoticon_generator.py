'''
This program randomly generates 5 emoticons from a predetermined list of eyes, noses, and mouths.
'''

import random

# These are the various facial features.
eyes = [':', ';', '!']
noses = ['>', '+', '<', '*']
mouths = [']', ')', 'P', 'Q', 'D']

# This emoticons variable is used as the starting point for the loop that generates the emoticons below.
emoticons = 0

# This loop actually constructs the emoticons. Once 5 are created, the conditional becomes false and the program ends.
while emoticons < 5:
    random_eyes = random.choice(eyes)
    random_noses = random.choice(noses)
    random_mouths = random.choice(mouths)
    print(random_eyes + random_noses + random_mouths)
    emoticons += 1 # Each time an emoticon is created, the emoticons variable is increased by 1.