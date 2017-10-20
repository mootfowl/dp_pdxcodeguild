'''
LAB16v2: Another approach to the Pick 6 problem that utilizes a function that calls another function.
Also, instead of comparing if each of the ticket numbers is in the list of winning numbers, regardless of position,
this new version requires ticket and winning numbers match the same index. This mirrors the actual way in which the
lottery works.

'''

import random

def pick_six():
    six_random = []
    for i in range(6):
        six_random.append(random.randint(0, 99))
    return(six_random)

def are_you_feeling_lucky(attempts):
    matching_numbers = []
    expenses = 0
    winnings = 0

    for tickets in range(attempts):

        ticket_numbers = pick_six()
        print(f"NEXT TICKET {ticket_numbers}.")

        # Compares the ticket numbers at each index (0-5) with the corresponding winning numbers.
        # If they match, they are added to the matching numbers list.
        # if ticket_numbers[0] == winning_numbers[0]:
        #     matching_numbers.append(ticket_numbers[0])
        #
        # if ticket_numbers[1] == winning_numbers[1]:
        #     matching_numbers.append(ticket_numbers[1])
        #
        # if ticket_numbers[2] == winning_numbers[2]:
        #     matching_numbers.append(ticket_numbers[2])
        #
        # if ticket_numbers[3] == winning_numbers[3]:
        #     matching_numbers.append(ticket_numbers[3])
        #
        # if ticket_numbers[4] == winning_numbers[4]:
        #     matching_numbers.append(ticket_numbers[4])
        #
        # if ticket_numbers[5] == winning_numbers[5]:
        #     matching_numbers.append(ticket_numbers[5])
        for i in range(6):
            if ticket_numbers[i] == winning_numbers[i]:
                matching_numbers.append(ticket_numbers[i])

        print(f"You matched {matching_numbers}.")

        # Determines the amount won for this ticket, if anything.
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


i_am_feeling_lucky = int(input("Are you feeling lucky!? \nHow many tickets would you like to buy? "))
number_of_attempts = i_am_feeling_lucky

winning_numbers = pick_six()
print(f"The winning numbers are {winning_numbers}.")
are_you_feeling_lucky(number_of_attempts)
