from typing import List


# class Solution:
#     def findMedianSortedArrays(self, nums1: 'List[int]', nums2: 'List[int]') -> 'float':




class Solution2():
    def findMedianSortedArrays(self, nums1: 'List[int]', nums2: 'List[int]') -> 'float':
        nums = nums1 + nums2
        nums.sort()
        length = len(nums)
        if length % 2 == 1:
            res = nums[int((length - 1) / 2)]
        else:
            res = (nums[int(length / 2)] + nums[int(length / 2 - 1)]) / 2
        return res


s = Solution2()
print(s.findMedianSortedArrays([1, 3], [2]))
