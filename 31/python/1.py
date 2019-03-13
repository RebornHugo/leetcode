from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        reference: https://www.cnblogs.com/grandyang/p/4428207.html
        """

        if not nums or len(nums) in (0, 1): return
        length = len(nums)
        left = length - 2
        while left >= 0 and nums[left] >= nums[left + 1]:
            left -= 1
        if left < 0:
            nums.sort()
            return
        right = length - 1
        while right > left and nums[right] <= nums[left]:
            right -= 1
        nums[left], nums[right] = nums[right], nums[left]
        # nums[left + 1:] = sorted(nums[left + 1:])
        nums[left + 1:] = reversed(nums[left + 1:])


s = Solution()
s.nextPermutation([1, 3, 2])
