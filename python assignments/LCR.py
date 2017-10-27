import random

player_names = ['David', 'Chloe', 'Allen', 'Brandon', 'Terri', 'Ziya', 'Cameron', 'Kyle', 'Marcel', 'Matthew']

num_players = int(input("How many players? "))

def pick_players():
    players = []
    for player in range(num_players):
        players.append({player_names[random.randint(0, len(player_names)]: 3})
    return players

print(pick_players())

