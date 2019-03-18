def merge_sort(nums):
    if len(nums) > 1:
        mid_pt = len(nums) // 2
        L = nums[:mid_pt]
        R = nums[mid_pt:]

        merge_sort(L)
        merge_sort(R)

        i, j = 0, 0
        num_ind = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                nums[num_ind] = L[i]
                i += 1
            else:
                nums[num_ind] = R[j]
                j += 1
            num_ind += 1
        
        while i < len(L):
            nums[num_ind] = L[i]
            i += 1
            num_ind += 1
        while j < len(R):
            nums[num_ind] = R[j]
            j += 1
            num_ind += 1