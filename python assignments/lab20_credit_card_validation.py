'''
LAB20: Credit Card Validation
Let's write a function which returns whether a string containing a credit card number is valid as a boolean.
The steps are as follows:

Convert the input string into a list of ints
Slice off the last digit. That is the check digit.
Reverse the digits.
Double every other element in the reversed list.
Subtract nine from numbers over nine.
Sum all values.
Take the second digit of that sum.
If that matches the check digit, the whole card number is valid.
For example, the worked out steps would be:

4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
4 5 5 6 7 3 7 5 8 6 8 9 9 8 5
5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
85
5
Valid!
'''

def validation(credit_card_number):
    number_list = list(credit_card_number.replace(' ', '')) # Deletes the spaces and makes a list
    integers = []
    for num in number_list:
        integers.append(int(num)) # Converts string numbers into integers
    check_digit = integers.pop(-1) # Removes last int from list and saves as a variable
    integers.reverse() # Reverses the list of integers
    print(integers)

    x = 0
    while x < len(integers):
        integers[x] *= 2 # Multiplies by 2
        x += 2 # Increases index by 2
    print(integers)

    y = 0
    while y < len(integers):
        if integers[y] > 9:
            integers[y] -= 9 # Subtracts 9 from numbers in the list greater than 9
        y += 1

    # y = 0
    # while y < len(integers):
    #     for i in integers:
    #         if i > 9: # Subtracts 9 from numbers in the list greater than 9
    #             i = i - 9
    #             integers[y] = i
    #         y += 1
    print(integers)

    total = (sum(integers)) % 10 # Adds all numbers in the list, divides by 10, and stores the remainder (mod) as a variable
    return total == check_digit # Compares the check to the final mod

number = '4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5'
print(validation(number))