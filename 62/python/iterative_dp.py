class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m < 0 or n < 0: return 0
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        dp[1][1] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if not (i == 1 and j == 1):
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m][n]


if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(3, 7))
