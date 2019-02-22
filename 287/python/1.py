from typing import List


class Solution1:
    """
    排序
    """
    def findDuplicate(self, nums: 'List[int]') -> 'int':
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == nums[i + 1]:
                return nums[i]


class Solution2:
    """
    直接算出来
    """
    def findDuplicate(self, nums: 'List[int]') -> 'int':
        su = sum(nums) - sum(set(nums))
        length = len(nums) - len(set(nums))
        return int(su / length)


class Solution:
    """
    集合
    """
    def findDuplicate(self, nums: 'List[int]') -> 'int':
        empty = set()
        for item in nums:
            if item in empty:
                return item
            else:
                empty.add(item)


class Solution:
    def findDuplicate(self, nums):
        # Find the intersection point of the two runners.
        tortoise = nums[0]
        hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        # Find the "entrance" to the cycle.
        ptr1 = nums[0]
        ptr2 = tortoise
        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]

        return ptr1

s = Solution()
print(s.findDuplicate([3, 1, 3, 4, 2]))
