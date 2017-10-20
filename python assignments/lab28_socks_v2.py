'''

LAB28: Socks v2

Now you have a mix of types and colors.
Represent socks using tuples containing one color and one type ('black', 'crew'). R
andomly generate these, and then group them into pairs.

'''

import random

sock_types = ['ankle', 'crew' ,'calf', 'thigh']
sock_colors = ['black', 'white', 'blue']
all_my_socks = {}

for i in range(100):
    j = random.randint(0, len(sock_types) - 1)
    k = random.randint(0, len(sock_colors) -1)
    sock = (sock_types[j], sock_colors[k])
    if sock in all_my_socks:
        all_my_socks[sock] += 1
    else:
        all_my_socks[sock] = 1

print(all_my_socks)

for socks in all_my_socks:
    print(f'{socks}:', all_my_socks[socks] // 2, 'pairs', all_my_socks[socks] % 2, 'straggler')