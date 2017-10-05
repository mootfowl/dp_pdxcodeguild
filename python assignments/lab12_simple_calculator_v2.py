'''
Lab12 v2: Simple Calculator

Allow the user to keep performing operations until they say 'done'. Use while True and break. Below is some sample input/output.

> what is the operation you'd like to perform? +
> what is the first number? 5
> what is the second number? 12
> 5 + 12 = 17
> what is the operation you'd like to perform? done
> goodbye!


'''

while True:
    operation = input("What is the operation you'd like to perform? (Options: +, -, *, /) > ")
    if operation == "done":
        break
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