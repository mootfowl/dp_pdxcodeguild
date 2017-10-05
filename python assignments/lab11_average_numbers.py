'''
Lab11: Average Numbers

We're going to average a list of numbers.
Start with the following list, iterate through it, keeping a 'running sum', then divide that sum by the number of elements in that list.
Remember len will give you the length of a list.

The code below hows how to loop through an array, and prints the elements one at a time.

nums = [5, 0, 8, 3, 4, 1, 6]

# loop over the elements
for num in nums:
    print(num)

# loop over the indices
for i in range(len(nums)):
    print(nums[i])

'''

# v1
# nums = [5, 0, 8, 3, 4, 1, 6]
# total = 0
#
# for num in nums:
#     total += num
#
# print(total / len(nums))

# v2

# Creates a list called nums2, and a variable total2 with no value
nums2 = []
total2 = 0

# Loops prompts asking for a number; if 'done' is entered, the loop breaks. Otherwise the entered numbers are added to the nums2 list.
while True:
    var = input("enter a number > ")
    if var == 'done':
        break
    else:
        nums2.append(var)

print(nums2)

sum = 0
# Adds all the numbers together
for numbers in nums2:
    sum += int(numbers)

# Divides the average by the quantity of numbers in the list.
print("The average of the numbers you entered is ", sum / len(numbers))