'''
LAB16: Makes my head explode! But let's do this! -dp

Have the computer play pick6 many times and determine net balance.
Initially the program will pick 6 random numbers as the 'winner'.
Then try playing powerball 100,000 times, with the ticket cost and payoff below.

A ticket contains 6 numbers, 1 to 99, and the number of matches between the ticket and the winning numbers determines the payoff.
Calculate your net winnings (the sum of all expenses and earnings).

the price of a ticket is $2
if 1 number matches, you win $4
if 2 numbers match, you win $7
if 3 numbers match, you win $100
if 4 numbers match, you win $50,000
if 5 numbers match, you win #1,000,000
if 6 numbers match, you win #25,000,000

Version 2

The ROI (return on investment) is defined as (earnings - expenses)/expenses. Calculate your ROI, print it out along with your earnings and expenses.
'''

import random

winning_numbers = []

# This randomly generates the six winning numbers.
for i in range(6):
    winning_numbers.append(random.randint(0, 99))

def are_you_feeling_lucky(attempts):
    ticket_numbers = []
    matching_numbers = []
    expenses = 0
    winnings = 0
    for tickets in range(attempts):

        for i in range(6):
            ticket_numbers.append(random.randint(0, 99)) # Generates the 6 numbers for each ticket
        print(f"NEXT TICKET {ticket_numbers}.")

        for numbers in ticket_numbers:
            if numbers in winning_numbers: # Compares ticket numbers to winning numbers
                matching_numbers.append(numbers) # Adds matching numbers to a temporary list (matching_numbers)
        print(f"You matched {matching_numbers}.")

        # Determines the amount won for this ticket, if anything
        if len(matching_numbers) == 1:
            winnings += 4
        elif len(matching_numbers) == 2:
            winnings += 7
        elif len(matching_numbers) == 3:
            winnings += 100
        elif len(matching_numbers) == 4:
            winnings += 50000
        elif len(matching_numbers) == 5:
            winnings += 1000000
        elif len(matching_numbers) == 6:
            winnings += 25000000

        expenses += 2 # Adds 2 dollars to the expenses total per ticket
        print(f"You've spent ${expenses} on tickets.")
        print(f"Your earnings so far are ${winnings}.")
        print(f"Your return on investment (ROI) is", (winnings - expenses) / expenses)

        matching_numbers = [] # Empties the list for the next ticket
        ticket_numbers = [] # Also empties the list for the next ticket

i_am_feeling_lucky = int(input("Are you feeling lucky!? \nHow many tickets would you like to buy? "))
print(f"The winning numbers are {winning_numbers}.")
number_of_attempts = i_am_feeling_lucky
are_you_feeling_lucky(number_of_attempts)