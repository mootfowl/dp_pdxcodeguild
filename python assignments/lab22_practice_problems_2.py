'''

LAB22: Practice Problems 2

'''

# Problem 1 : Write a REPL which asks users for a list of numbers, which they enter, until they say 'done'. Then print out the list.


# numbers_list = []
#
# while True:
#     prompt = input("Enter a number or 'done' > ")
#     if prompt == "done":
#         print(numbers_list)
#         exit()
#
#     else:
#         numbers_list.append(int(prompt))

# Problem 2: Print out every other element of a list, first using a while loop, then using a for loop.

# def print_every_other(nums):
#     x = 0
#     while x < len(nums):
#         print(nums[x])
#         x += 2

# def print_every_other(nums):
#     for i in nums:
#         if i % 2 == 0:
#             print(i)
#
# nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]
#
# print_every_other(nums)

# Problem 3: Given a list of numbers, and a target number, find a pair of numbers from the list that sum to a target number


def find_pair(nums, target):
    for i in range(len(nums) - 1):
        if target - nums[i] > 0:
            p = target - nums[i]
            if p in nums:
                return nums[i], p

nums = [5, 6, 2, 3, 43, 49, 123, 32, 14, 1, 6, 19, 8]
target = 125
print(find_pair(nums, target))

# Problem 4: Get a string from the user, print out another string, doubling every letter.

response = input("Type anything > ")
double = ''
for i in response:
    double += i + i
print(double)

# Problem 5: Write a function that merges two lists into a single list,
# where each element of the outlist list is another list containing two elements.
# merge([5,2,1], [6,8,2]) -> [[5,6],[2,8],[1,2]]

listA = [5, 2, 1, 37, 45, 123]
listB = [6, 8, 2, 4, 6, 15, 37, 54]

def merge(A, B):
    listC = []
    for i in range(len(A)):
        temp_list = []
        temp_list.append(A[i])
        temp_list.append(B[i])
        listC.append(temp_list)
    return listC

print(merge(listA, listB))

# Problem 6: Write a function that takes two ints, a and b, and returns True if one is positive and the other is negative.


# Problem 7: Write a function that returns True if a number within 10 of 100.

def near_100(num):
    if num > 90 and num < 100:
        return True
    else:
        return False

near_100_num = int(input("Enter a number >"))
print(near_100(near_100_num))

# Problem 8: Write a function that takes a string, and returns a list of strings, each missing a different character.

import random

def missing_char(word):
    missing_list = []
    word_list = word.split()
    for i in range (0, len(word_list)):
        missing_list.append(word_list.pop[i])
    return missing_list

print(missing_char('kitten'))