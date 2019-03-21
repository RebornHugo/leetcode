def heap_sort(nums):
    def sift_down(start, end):
        root = start
        while True:
            child = 2 * root + 1
            if child > end:
                break
            if child + 1 <= end and nums[child] < nums[child + 1]:
                child += 1
            if nums[child] > nums[root]:
                nums[root], nums[child] = nums[child], nums[root]
                root = child
            else:
                break

    # create maximum heap
    for start in range((len(nums) - 2) // 2, -1, -1):
        sift_down(start, len(nums) - 1)

    # heap sort
    for end in range(len(nums) - 1, 0, -1):
        nums[0], nums[end] = nums[end], nums[0]
        sift_down(0, end - 1)


def main():
    l = [9, 2, 1, 7, 6, 8, 5, 3, 4]
    heap_sort(l)
    print(l)


if __name__ == "__main__":
    main()
