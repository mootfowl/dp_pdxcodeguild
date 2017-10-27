'''

LAB32: Rain Data

'''

import random
import math
import datetime


# date = datetime.datetime.strptime('25-MAR-2016', '%d-%b-%Y')
# print(date)
# print(date.day)
# list_of_dates = []
# list_of_dates.append(date)
# print(list_of_dates)


# nums = []
# for i in range(10):
#     nums.append(random.randint(0, 100))
#
# print(nums)

def total(list):
    total = 0
    for i in list:
        total += i
    return total

def average(nums):
    total = 0
    for num in nums:
        total += num
    return total/len(nums)

def variance(nums, average):
    total = 0
    for num in nums:
        diff = num - average
        total += diff*diff
    return total/len(nums)

with open('airport_way.rain') as f:
    data = f.readlines()
    del data[0:12]

# print(data[0]) # <<<

edited_data = []
for i in data:
    day = {}
    j = i.replace('\n', '').replace('    ', ' ').replace('   ', ' ').replace('  ', ' ').split(' ') # removes extra spaces
    date = datetime.datetime.strptime(j[0], '%d-%b-%Y')
    # print(j)
    day['day'] = date
    day['total'] = int(j[1])
    # print(day)
    del j[0], j[0]
    # print(j)
    hours = []
    for hour in j:
        hours.append(int(hour))
    day['hours'] = hours
    edited_data.append(day)

print(edited_data[0]) # <<<
print(total(edited_data[0]['hours']))
# for i in edited_data:
#     print(i)

# for data_row in edited_data: ## "pretty printing"
#     for datum in data_row:
#         print(datum, end=' ')
#     print()



#
#
# av = average(nums)
# var = variance(nums, av)
# std = math.sqrt(var)
#
# print(f'average: {av}')
# print(f'variance: {var}')
# print(f'standard deviation: {std}')
