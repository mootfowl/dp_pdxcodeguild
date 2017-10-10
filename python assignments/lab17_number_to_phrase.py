'''
LAB17: Number to Phrase

Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.

Hint: you can use modulus to extract the ones and tens digit.

x = 67
tens_digit = x//10
ones_digit = x%10
Hint2: use the digit as an index to look up a string in a list.
'''

ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['zero', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['zero', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']


def number_to_phrase(number):
    hundreds_index = number // 100
    tens_index = (number % 100) // 10
    ones_index = number % 10
    if ones_index > 0 and tens_index < 2 and hundreds_index < 1:
        print(teens[ones_index])
    elif hundreds_index > 0:
        print(ones[hundreds_index], "hundred", tens[tens_index], ones[ones_index])
    else:
        print(tens[tens_index], ones[ones_index])


num = int(input("Pick a number between 0 and 999 > "))
number_to_phrase(num)