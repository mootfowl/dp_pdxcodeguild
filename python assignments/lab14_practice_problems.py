'''

Lab 14: Practice Problems

'''
import random

print("Problem 1: Return the number of letter occurences in a string.\n")


def count_letter(char_to_find, word):
    x = 0
    for char in word.lower():
        if char == char_to_find:
            x += 1
    print(f"There are {x} {char_to_find}'s in the word {word}.")


count_letter('i', 'Antidisestablishmentterianism')
count_letter('p', 'Pneumonoultramicroscopicsilicovolcanoconiosis')

print("\nProblem 2: Convert input strings to lowercase without any surrounding whitespace.\n")


def lower_case(clean_up):
    lowered = clean_up.lower()
    stripped = lowered.strip('     ')
    print(stripped)


lower_case("SUPER!")
lower_case("        NANNANANANA BATMAN        ")


print("\nProblem 3: Write a function that tells whether a number is even or odd - hint, compare a/2 and a//2, or use a%2\n")


def is_even(a):
    if a / 2 != a // 2:
        print(False)
    else:
        print(True)


is_even(5)
is_even(6)
is_even(102)
is_even(24)
is_even(1033)


print("\nProblem 4: Write a function using random.randint and subscription to get a random element of a list and return it.\n")


def random_element(a):
    x = random.randint(0,len(a)-1)
    print(a[x])


fruits = ['apples', 'bananas', 'pears']
random_element(fruits)

print("\nProblem 5: Write a function that returns the maximum of 3 parameters.\n")


def maximum_of_three(a, b, c):
    if a > b and a > c:
        print(f"{a} is greater than {b} and {c}.")
    elif b > a and b > c:
        print(f"{b} is greater than {a} and {c}.")
    elif c > a and c > b:
        print(f"{c} is greater than {a} and {b}.")


maximum_of_three(5, 6, 2)
maximum_of_three(-4, 3, 10)

print("\nProblem 6: Print out the powers of 2 from 2^0 to 2^20.\n")

for i in range(0, 21):
    print(2 ** i)

print("\nProblem 7: Write functions to find the minimum, maximum, mean, and mode of a list of numbers.\n")

def minimum(nums):
    nums.sort()
    return(nums[0])


def maximum(nums):
    nums.sort()
    return(nums[-1])

def mean(nums):
    x = 0
    for num in nums:
        x += num
    return int(x / len(nums))

# def mode(nums): OPTIONAL


number_list = [13, 14, 35, 2, 539, 32, 65, 123]
minimum(number_list)
print(minimum(number_list))
maximum(number_list)
print(maximum(number_list))
mean(number_list)
print(mean(number_list))

print("\nProblem 8: Write a function that returns the reverse of a list.\n")


def reverse(nums):
    x = []
    for numbers in nums:
        x.insert(0, numbers)
    print(x)

# ...or use reverse() :P


a_mess_of_numbers = [1, 3, 5, 7, 11, 13, 17]
reverse(a_mess_of_numbers)

print("\nProblem 9: Write a function to find all common elements between two lists.\n")

commonalities = []

def common_elements(nums1, nums2):
    for num in nums1:
        if num in nums2:
            commonalities.append(num)

list1 = [1, 3, 5, 7, 9, 2, 14, 10]
list2 = [4, 7, 8, 5, 10, 24, 345, 72, 0]

common_elements(list1, list2)

print(commonalities)

print("\nProblem 10: Write a function to move all the elements of a list with value less than 10 to a new list and return it.\n")

list_under_ten = []


def extract_less_than_ten(nums):
    for num in nums:
        if num < 10:
            list_under_ten.append(num)


range_of_numbers = [123, 1, 5, 9870, 4, 6, 35, 62, 9]
extract_less_than_ten(range_of_numbers)

print(list_under_ten)

print("\nProblem 11: Write a function to combine two lists of equal length into one, alternating elements.\n")

combined_list = []

def combine(list1, list2):
    for nums in list1:
        combined_list.append(nums)

    i = 0

    for nums2 in list2:
        combined_list.insert(i, nums2)
        i += 2

    print(combined_list)


combine(['a','b','c'],[1,2,3])