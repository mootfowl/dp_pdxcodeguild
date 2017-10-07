#
# print("Hello, world.")

def swap(nums, i, j):
    t = nums[i]
    nums[i] = nums[j]
    nums[j] = t


def reverse(nums):
    half_length = len(nums) // 2
    for i in range(half_length):
        swap(nums, i, len(nums)-i-1)


nums = [1, 2, 3, 4, 5, 6, 7, 8]
reverse(nums)
print(nums)