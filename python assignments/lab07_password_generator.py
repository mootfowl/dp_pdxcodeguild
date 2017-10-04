'''
This program prompts the user to pick a number, enter their name, and then generates a password the length of the
chosen number from letters in their name.
'''

import random

print("Let's make a random password together!")
user_selected_number = input("Pick any two digit number. This will determine how many characters are in your new password. > ")
# This converts the input string into an integer.
number = int(user_selected_number)
user_generated_content = input(f"Type your first and last name to generate a random {number} character password. > ")


password = ""
i = 0
# A random.choice character is selected from the users name and added to the end of the password until such time that the characters equals the number chosen.
while i < number:
    password += random.choice(user_generated_content)
    i += 1

print("Here is your password:", password)
