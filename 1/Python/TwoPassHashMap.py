class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        buffer_dict = {}
        for i, p in enumerate(nums):
            buffer_dict[p] = i
        for j, q in enumerate(nums):
            left = target - q
            if left in buffer_dict and not buffer_dict[left] == j:
                return [j, buffer_dict[left]]
        return []


if __name__ == '__main__':
    s = Solution().twoSum([2, 7, 11, 15], 9)
    print(s)
