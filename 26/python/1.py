from typing import List


class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> 'int':
        # if not nums:
        #     return 0
        j = 0
        for i in range(len(nums)):
            if j == 0 or nums[i] != nums[j - 1]:
                nums[j] = nums[i]
                j += 1
        return j


s = Solution()
print(s.removeDuplicates([1, 2, 3]))
