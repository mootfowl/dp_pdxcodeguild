'''
LAB23: Blackjack Advice

Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards.

First, ask the user for three playing cards. Save the user's inputs as a string: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K.

Then, figure out the point value of each card individually. Number cards are worth their number, all face cards are worth 10.
At this point, assume aces are worth 1.

Now, in Blackjack, aces can be worth 11 if they won't put the total point value of both cards over 21.

Lastly, figure out what the playing advice will be. Use the following rules:

Less than 17, advise to "Hit"
Over or equal to 17, advise to "Stay"
Exactly 21, advise "Blackjack!"
Over 21, advise "Already Busted"
Then print out the current total point value and the advice.
'''

def pick_a_card(): # A reusable function to select 3 "cards" and return their value.
    selection = input("Pick a card: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K > ")
    if selection == 'J' or selection == 'Q' or selection == 'K':
        return 10
    elif selection == 'A':
        return 1
    else:
        return int(selection)

def blackjack():
    three_cards = [] # The list of 3 selected cards.
    for i in range(3):
        three_cards.append(pick_a_card())
    total = sum(three_cards)
    if total <= 11 and 1 in three_cards: # This line effectively increases an Ace from 1 to 11 if it won't cause a bust
        total += 10
    if total == 21:
        print(f"{total} Blackjack!")
    elif total < 17:
        print(f"{total} HIT!")
    elif total >= 18 and total < 21: # Had to add second condition (and < 21) after a few test runs suggested that someone with 30 should 'Stay'...
        print(f"{total} Stay.")
    elif total > 21:
        print(f"{total} Busted. :(")

blackjack()




