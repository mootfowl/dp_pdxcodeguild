'''
Lab12: Simple Calculator

Write a program that asks the user for an operator and each operand.
Don't forget that input returns a string, which you can convert to a float using float(user_input) where user_input
is the string you got from input.
Below is some sample input/output.

'''

# First three lines prompt the user inputs: two numbers and an operation
operation = input("What is the operation you'd like to perform? (Options: +, -, *, /) > ")
first_number = int(input("What is the first number? > "))
second_number = int(input("What is the second number? > "))

if operation == '+':
    print(f"{first_number} + {second_number} = ", first_number + second_number)

elif operation == '-':
    print(f"{first_number} - {second_number} = ", first_number - second_number)

elif operation == '*':
    print(f"{first_number} * {second_number} = ", first_number * second_number)

elif operation == '/':
    print(f"{first_number} / {second_number} = ", first_number / second_number)

else:
    print("I am but a lowly, simply calculator. The operation you chose is beyond my rudimentary capabilities.")