def __partition(nums, l, h):
    # i will be for tracking the nums lesser than the pivot element.
    i = l - 1
    pivot = nums[h]
    for j in range(l, h):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    partition_pt = i + 1
    nums[partition_pt], nums[h] = nums[h], nums[partition_pt]
    return partition_pt

def quick_sort(nums, low, high):
    if low < high:
        partition_pt = __partition(nums, low, high)
        quick_sort(nums, low, partition_pt - 1)
        quick_sort(nums, partition_pt + 1, high)