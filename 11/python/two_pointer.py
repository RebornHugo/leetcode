class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxWater = 0
        i, j = 0, len(height) - 1
        while i != j:
            maxWater = max(maxWater, min(height[i], height[j]) * (j - i))
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return maxWater


if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([1, 1]))
