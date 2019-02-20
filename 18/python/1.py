"""
18. 4sum
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Method 1: using the same method in 3sum with a more for loop !
"""
from typing import List


class Solution:
    def fourSum(self, nums: 'List[int]', target: 'int') -> 'List[List[int]]':
        nums.sort()
        res = set()
        length = len(nums)
        for i in range(0, length - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, length - 2):
                if j > 1 and nums[j] == nums[j - 1] and nums[i] != nums[j]:
                    continue
                low, high, remain = j + 1, length - 1, target - nums[i] - nums[j]
                while low < high:
                    if nums[low] + nums[high] < remain:
                        low += 1
                    elif nums[low] + nums[high] > remain:
                        high -= 1
                    else:
                        res.add((nums[i], nums[j], nums[low], nums[high]))
                        low += 1
                        high -= 1
        # remove duplicates
        # import itertools
        # res.sort()
        # res = list(k for k, _ in itertools.groupby(res))

        return [list(_) for _ in res]


s = Solution()
print(s.fourSum([-1, 0, -5, -2, -2, -4, 0, 1, -2], -9))
