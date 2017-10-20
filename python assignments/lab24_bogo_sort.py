'''
LAB24: Bogo Sort

Bogo sort is one of the least efficient sorting algorithms imaginable!
It works by generating random arrangements of a list, checking if the list is sorted, and if it is, return it.
For a list of 200 numbers, there are 200! = 7.88*10^374 possible combinations, only one of them is the sorted list.

random_list(n) generates and returns a list of length n, with random values between 0 and 100

shuffle(nums) randomly re-arranges a list

> iterate through the indices of the list
> for each index, generate a random index
> swap the elements at the two indices

is_sorted(nums) checks if a list is sorted

> iterate through the indices of the list
> if the element at the current index is greater than the element at the next index, the list isn't sorted, and you can return False
> if you get through the entire list and each element is less than or equal to the next element,
the list is sorted, and you can return True

bogosort(nums) continues to generate random arrangements until the list is sorted

'''

import random

def random_list(n):
    list = []
    for i in range(n):
        list.append(random.randint(0, 100))
    return list

def shuffle(nums):
    # print(nums)
    for i in range(len(nums)):
        j = random.randint(0, len(nums) - 1)
        p = nums[j] # Placeholder variable to store value of second (random) index
        nums[j] = nums[i] # Redefines i, but now both i and j are the same
        nums[i] = p # Reassigns i to what j originally was
    return nums

        # nums[i], nums[j] = nums[j], nums[i] # Example of tuple packing and unpacking, enabling a simultaneous swap

def is_sorted(nums):
    print(nums)
    for i in range(len(nums)):
        if i < len(nums) - 1:
            if nums[i] > nums[i + 1]:
                return False

            elif nums[i] <= nums[i + 1]:
                continue

        elif i == len(nums) - 1:
            if nums[i] >= nums[i - 1]:
                return True

            else:
                return False

def bogosort(nums):
    set = random_list(nums) # Calls the random function to generate a list of length nums
    counter = 0
    while is_sorted(shuffle(set)) != True: # Loops through the shuffle and is_sorted functions until True is returned
        is_sorted(shuffle(set))
        counter += 1
    return counter

print(bogosort(5))

# print(is_sorted(shuffle(random_list(5))))
