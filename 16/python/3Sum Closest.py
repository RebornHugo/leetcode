class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        for i, a in enumerate(nums[:-2]):
            low, high = i + 1, len(nums) - 1
            while low < high:
                if a + nums[low] + nums[high] == target:
                    return a, nums[low], nums[high]
                elif a + nums[low] + nums[high] < target:
                    low += 1
                else:
                    high -= 1


if __name__ == '__main__':
    s = Solution()
    print(s.threeSumClosest([-1, 2, 1, -4], 1))
