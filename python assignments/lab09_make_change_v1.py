'''
Let's convert a dollar amount into a number of coins.
The input will be the total amount, the output will be the number of quarters, dimes, nickles, and pennies.
Always break the total into the highest coin value first, resulting in the fewest amount of coins.
For this, you'll have to use floor division //, which throws away the remainder. 10/3 is 3.333333, 10//3 is 3.

VERSION 1: Have the user enter the total number in pennies, e.g. for $1.36, the user will enter 136.

'''

# Prompts the user to enter a number, and re-prompts if the argument they enter cannot be converted to an integer.
while True:
    try:
        pocket_change = int(input("How much money do you have in your pocket? Enter the total amount in pennies. "))
        break
    except ValueError:
        print("Can I get that in an actual number, por favor?")

print(f"Okay, so you have the equivalent of {pocket_change} pennies in your pocket. Let's do some math!")

pocket_change_quarters = pocket_change // 25
print(f"You have {pocket_change_quarters} quarters.")
pocket_change_dimes = int((pocket_change % 25) / 10)
print(f"You have {pocket_change_dimes} dimes.")
pocket_change_nickels = int((pocket_change - (25 * pocket_change_quarters) - (10 * pocket_change_dimes)) / 5)
print(f"You have {pocket_change_nickels} nickels.")
pocket_change_pennies = int((pocket_change - (25 * pocket_change_quarters) - (10 * pocket_change_dimes) - (5 * pocket_change_nickels)))
print(f"And you have {pocket_change_pennies} pennies.")
