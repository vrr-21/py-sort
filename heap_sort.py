def __heapify(nums, n, root_ind):
    # This is for max-heap
    largest_val = root_ind
    left_val = 2*root_ind + 1
    right_val = 2*root_ind + 2

    if left_val < n and nums[largest_val] < nums[left_val]:
        largest_val = left_val
    
    if right_val < n and nums[largest_val] < nums[right_val]:
        largest_val = right_val

    # Swap the nodes if needed.
    if largest_val != root_ind:
        nums[largest_val], nums[root_ind] = nums[root_ind], nums[largest_val]
        # Recurse!
        __heapify(nums, n, largest_val)
    
def heap_sort(nums):
    n = len(nums)

    for index in range(n, -1, -1):
        __heapify(nums, n, index)
    
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        __heapify(nums, i, 0)