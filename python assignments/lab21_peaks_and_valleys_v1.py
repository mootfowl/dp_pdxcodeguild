'''
LAB21: Peaks and Valleys

Define the following functions:

peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.
valleys - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.
peaks_and_valleys - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.
'''


def peaks(nums):
    peaks_list = []
    for i in range(1, len(nums) - 1): # The - 1 prevents an index error
        if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            peaks_list.append(i)
    return peaks_list

def valleys(nums):
    valleys_list = []
    for i in range(1, len(nums) - 1):
        if nums[i] < nums[i - 1] and nums[i] < nums[i + 1]:
            valleys_list.append(i)
    return valleys_list

def peaks_and_valleys(nums):
    peaks_and_valleys_list = []
    for i in range(1, len(nums) - 1):
        if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            peaks_and_valleys_list.append(i)
        elif nums[i] < nums[i - 1] and nums[i] < nums[i + 1]:
            peaks_and_valleys_list.append(i)
    return peaks_and_valleys_list

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
print(peaks(data))
print(valleys(data))
print(peaks_and_valleys(data))