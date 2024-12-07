import random
import copy

def lomuto_partition(nums, left, right):
    pivot_idx = (left + right) // 2
    pivot = nums[pivot_idx]
    nums[left], nums[pivot_idx] = nums[pivot_idx], nums[left]

    i, j = right, right
    while j > left:
        if nums[j] > pivot:
            nums[j], nums[i] = nums[i], nums[j]
            i -= 1
        j -= 1
    nums[left], nums[i] = nums[i], nums[left]
    return i

def hoare_partition(nums, left, right):
    pivot_idx = (left + right) // 2
    pivot = nums[pivot_idx]
    nums[left], nums[pivot_idx] = nums[pivot_idx], nums[left]

    i, j = left + 1, right
    # descending order
    while True:
        # move i until find a lower or equal
        while i < j and nums[i] < pivot:
            i += 1
        
        # move j until find a greater or equal

        while i < j and nums[j] > pivot:
            j -= 1
        
        # when i and j are not acrossed, swap
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        else:
            break
        
        # two possible edge cases of i - j after swapping
        # 1. i = j + 1, in this case j is already on the number that is greater or equal than pivot
        # 2  i = j, in this case the number at j may not be greater or equal than pivot, so need to move j one more time
    while nums[j] > pivot:
        j -= 1

    nums[left], nums[j] = nums[j], nums[left]
    return j
    

def quicksort(nums, left, right):
    # print(left, right)
    if left >= right:
        return
    
    # idx = hoare_partition(nums, left, right)
    idx = lomuto_partition(nums, left, right)

    quicksort(nums, idx + 1, right)
    quicksort(nums, left, idx - 1)


for i in range(100):
    test_l = [random.randrange(20) for j in range(10)]
    quicksort(test_l, 0, len(test_l) - 1)
    a = copy.deepcopy(test_l)
    test_l.sort(reverse=False)
    assert a == test_l
    print(f'{i}--------------------------------------')