'''
LAB21v3: Peaks and Valleys v2

Using the data list, draw the image of X's.
'''

water = 0

def X_or_NO(numbers, cap):
    t = cap
    line = ''
    counter = 0
    global water
    for i in range(len(numbers)):
        if numbers[i] <= t:
            if numbers[i] < t:
                line += '  '
            elif numbers[i] == t:
                line += 'X '
                break
        counter += 1 # Matthew's addition which enables the next loop (j) to resume where i left off at the break

    for j in range(counter + 1, len(numbers)):
        if numbers[j] < t:
            line += '0 '
            water += 1 # Tallies the total amount of water drawn with each '0 '
        elif numbers[j] >= t:
            line += 'X '


    print(line)


def draw_peaks_and_valleys(nums):
    x = max(nums)
    while x > 0:
        X_or_NO(nums, x)
        x -= 1


data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
# data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]
draw_peaks_and_valleys(data)
print(f"\nThe total amount of water is {water} units.")

