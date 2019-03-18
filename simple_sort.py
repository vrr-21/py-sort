# This will take an input and sort it by just finding the minimum everytime.

def simple_sort(nums):
    x = []
    while len(nums) > 0:
        min_elem = min(nums)
        x.append(min_elem)
        nums.remove(min_elem)
    while len(x) > 0:
        nums.append(x.pop(0))