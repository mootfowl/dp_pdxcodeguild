'''
LAB29: Road Trip v1

We've mapped what cities are directly connected by roads and stored them in a dictionary:

Traveling from one city to an adjacent one is called a hop.
Let the user enter a city. Print out all the cities connected to that city.
Then print out all cities that could be reached through two hops.
'''

city_to_accessible_cities = {
  'Boston': {'New York', 'Albany', 'Portland'},
  'New York': {'Boston', 'Albany', 'Philadelphia'},
  'Albany': {'Boston', 'New York', 'Portland'},
  'Portland': {'Boston', 'Albany'},
  'Philadelphia': {'New York'}
}


def starting_point():
    city = input("Where are you? (enter one) >> Boston | New York | Albany | Portland | Philadelphia | EXIT >> ")
    if city == 'EXIT' or city == 'Exit' or city == 'exit':
        print("Yeah, travel is overrated.")
        exit()
    else:
        return city


def one_hop(city):
    return city_to_accessible_cities[city]


def two_hops(cities, start):
    more_destinations = []
    two = []
    for city in cities:
        more_destinations += (list(city_to_accessible_cities[city])) # Combines all locations into a single list
    for i in range(len(more_destinations)):
        if more_destinations[i] not in cities and more_destinations[i] != start and more_destinations[i] not in two:
            two.append(more_destinations[i]) # Filters out duplicates
    return two


start = starting_point()
destinations = one_hop(start)
print(f"Here are the cities you can reach from {start} in a single hop: ", (list(destinations)))
print(f"And here are the cities you can reach from {start} in two hops: ", two_hops(destinations, start))
# two_hops(destinations_one)