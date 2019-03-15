from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # if len(nums) == 1: return nums[0]

        # f: the maxSubArray up to the i-th element (must use the i-th element)
        res = f = nums[0]
        for num in nums[1:]:
            cur = f if f > 0 else 0
            f = cur + num
            res = max(res, f)
        return res


s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
