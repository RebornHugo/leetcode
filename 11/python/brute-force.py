class Solution:
    def maxArea(self, height):
        """
        TLE 233333333
        :type height: List[int]
        :rtype: int
        """
        res = [[0 for _ in range(len(height))] for _ in range(len(height))]
        for i, p in enumerate(height):
            for j, q in enumerate(height[i + 1:], start=i + 1):
                res[i][j] = min(p, q) * (j - i)
        # i = 0
        # while i < len(height):
        #     j = i + 1
        #     while j < len(height):
        #         res[i][j] = min(height[i], height[j]) * (j - i)
        #         j += 1
        #     i += 1

        # maxRes = 0
        # for res_ in res:
        #     maxRes = max(maxRes, max(res_))

        maxRes = max(map(max, res))
        return maxRes


if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([1, 1]))
