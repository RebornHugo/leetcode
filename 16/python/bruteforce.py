from typing import List


class Solution:
    def threeSumClosest(self, nums: 'List[int]', target: 'int') -> 'int':
        length = len(nums)
        difference = 1e10
        for i in range(length - 2):
            for j in range(i + 1, length - 1):
                for m in range(j + 1, length):
                    temp = target - nums[i] - nums[j] - nums[m]
                    difference = temp if abs(temp) < abs(difference) else difference
        return target - difference


if __name__ == '__main__':
    s = Solution()
    print(s.threeSumClosest([-1, 2, 1, -4], 1))
