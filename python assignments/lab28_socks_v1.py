'''

LAB28: Socks

You've just finished laundry and your expansive sock collection is in complete disorder.
Sort your socks into pairs and pull out any loners.

Generate a list of 100 random socks, randomly chosen from a set of types: sock_types = ['ankle', 'crew', 'calf', 'thigh']

Find the number of duplicates and loners for each sock type. Hint: dictionaries are helpful here.
'''

import random

sock_types = ['ankle', 'crew' ,'calf', 'thigh']
all_my_socks = {}

for i in range(100):
    j = random.randint(0, len(sock_types) - 1)
    sock = (sock_types[j])
    if sock in all_my_socks:
        all_my_socks[sock] += 1
    else:
        all_my_socks[sock] = 1

print(all_my_socks)

for socks in all_my_socks:
    print(f'{socks}:', all_my_socks[socks] // 2, 'pairs', all_my_socks[socks] % 2, 'straggler')