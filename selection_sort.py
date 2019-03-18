# Selection sort

def selection_sort(nums):
    n = len(nums)
    for i in range(n - 1):
        index = i
        for j in range(i + 1, n):
            if nums[j] < nums[index]:
                index = j
        nums[i], nums[index] = nums[index], nums[i]