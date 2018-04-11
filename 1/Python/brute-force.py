class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, p in enumerate(nums):
            for j, q in enumerate(nums[i + 1:], i + 1):
                if p + q == target:
                    return [i, j]
        return []


if __name__ == '__main__':
    s = Solution().twoSum([2, 7, 11, 15], 9)
    print(s)
