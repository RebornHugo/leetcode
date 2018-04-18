class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        dict_buffer = {}
        for i, n in enumerate(nums):
            dict_buffer[n] = i
        for i, n in enumerate(nums):
            target = -n
