from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: 'List[int]', nums2: 'List[int]') -> 'float':
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)
        k = (n1 + n2 + 1) // 2
        l, r = 0, n1

        while l < r:
            m1




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
