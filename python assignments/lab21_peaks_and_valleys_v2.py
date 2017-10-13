'''
LAB21v2: Peaks and Valleys v2

Using the data list, draw the image of X's.
'''


def X_or_NO(numbers, cap):
    t = cap
    line = '' # Building an ever-growing string of either spaces or Xs
    for i in range(len(numbers)):
        if numbers[i] < t:
            line += '  '

        elif numbers[i] >= t:
            line += 'X '
    print(line)


def draw_peaks_and_valleys(nums):
    x = 9 # This can also be x = max(nums) per Matthew's input
    while x > 0: # Loop ends at 0
        X_or_NO(nums, x)
        x -= 1 # Reduces x until it reaches 0


data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
draw_peaks_and_valleys(data)
