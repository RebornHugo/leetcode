def quick_sort_in_place(nums):
    nums = nums[:]
    n = len(nums)

    def partition(nums, start, end):
        i = start - 1
        pivotIndex = end
        pivot = nums[end]
        for j in range(start, end):
            if nums[j] < pivot:
                i = i + 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[pivotIndex] = \
            nums[pivotIndex], nums[i + 1]
        return i + 1

    def sort(nums, start, end):
        if start >= end:
            return
        p = partition(nums, start, end)
        sort(nums, start, p - 1)
        sort(nums, p + 1, end)

    sort(nums, 0, n - 1)
    return nums


def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    less = []
    greater = []
    pivot = nums.pop()
    for item in nums:
        if item < pivot:
            less.append(item)
        else:
            greater.append(item)
    nums.append(pivot)
    return quick_sort(less) + [pivot] + quick_sort(greater)


print(quick_sort([3, 2, 5, 6, 1]))
