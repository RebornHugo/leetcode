class Solution:
    """
    递归的做法会导致时间溢出
    """
    dp = dict(dict())

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m <= 0 or n <= 0: return 0
        if m == 1 and n == 1: return 1
        if Solution.dp.get(m) and Solution.dp.get(m).get(n): return Solution.dp.get(m).get(n)
        left_path = self.uniquePaths(m - 1, n)
        right_path = self.uniquePaths(m, n - 1)
        Solution.dp[m] = {n: left_path + right_path}
        return Solution.dp[m][n]


if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(3, 7))
