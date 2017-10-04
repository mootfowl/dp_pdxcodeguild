'''
This program mimics the Magic 8 Ball toy. It prompts the user to ask a question and randomly returns a prediction for
the outcome of the question.
'''

import random
from sys import exit

# These are the various predictions, separated into multiple lists...
predictions1 = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes definitely', 'You may rely on it', 'As I see it, yes', 'Most likely']
predictions2 = ['Outlook good', 'Yes', 'Signs point to yes', 'Reply hazy, try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now']
predictions3 = ['Concentrate and ask again', 'Don\'t count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']

# ...that are combined into a single list here.
all_predictions = predictions1 + predictions2 + predictions3

# This is the welcome message at the start of the program.
print("Welcome to Madame Wanda's fortune booth!")

# The string that is input is assigned to the "question" variable.
print("Ask me any question to learn what the future holds!")
question = input("> ")

# This loop returns a prediction to the question. It then asks the user if they'd like to ask another question or exit by typing "done".
while input != "done":
    print(random.choice(all_predictions))
    repeat = input("Ask another question, or type done to obscure your sight from the future! > ")
    if repeat == "done":
        exit()