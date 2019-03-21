def quick_sort_in_place(lst):
    lst = lst[:]
    n = len(lst)

    def partition(lst, start, end):
        i = start - 1
        pivotIndex = end
        pivot = lst[end]
        for j in range(start, end):
            if lst[j] < pivot:
                i = i + 1
                lst[i], lst[j] = lst[j], lst[i]
        lst[i + 1], lst[pivotIndex] = lst[pivotIndex], lst[i + 1]
        return i + 1

    def sort(lst, start, end):
        if start >= end:
            return
        p = partition(lst, start, end)
        sort(lst, start, p - 1)
        sort(lst, p + 1, end)

    sort(lst, 0, n - 1)
    return lst


def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    less = []
    greater = []
    pivot = lst.pop()
    for item in lst:
        if item < pivot:
            less.append(item)
        else:
            greater.append(item)
    lst.append(pivot)
    return quick_sort(less) + [pivot] + quick_sort(greater)


print(quick_sort([3, 2, 5, 6, 1]))
