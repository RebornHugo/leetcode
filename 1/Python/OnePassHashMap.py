class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        buffer_dict = {}
        for i, p in enumerate(nums):
            if target - p in buffer_dict:
                return buffer_dict[target - p], i
            else:
                buffer_dict[p] = i


if __name__ == '__main__':
    s = Solution().twoSum([2, 7, 11, 15], 22)
    print(s)
