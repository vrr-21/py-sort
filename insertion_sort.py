# Insertion Sort:

def insertion_sort(nums):
    n = len(nums)
    for i in range(n):
        j = i - 1
        while j > 0 and nums[j] < nums[j - 1]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            j -= 1
    