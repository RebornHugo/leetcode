class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i, p in enumerate(nums[:-2]):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            low, high, target = i + 1, len(nums) - 1, -p
            while low < high:
                if nums[low] + nums[high] == target:
                    res.append([p, nums[low], nums[high]])
                    while low < high and nums[low] == nums[low + 1]: low += 1
                    while low < high and nums[high] == nums[high - 1]: high -= 1
                    low += 1
                    high -= 1
                elif nums[low] + nums[high] < target:
                    low += 1
                elif nums[low] + nums[high] > target:
                    high -= 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([1, 2, 0, 0, 0, 1, -1]))
