class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
            if i < len(s) - 1 and s[i] == s[i + 1]: dp[i][i + 1] = 1
        for step_size in range(2, len(s)):
            for start in range(len(s) - step_size):
                if s[start] == s[start + step_size]:
                    dp[start][start + step_size] = dp[start + 1][start + step_size - 1]
                else:
                    dp[start][start + step_size] = 0
        start = end = maxLen = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dp[i][j] == 1 and j - i + 1 > maxLen:
                    maxLen = j - i + 1
                    start, end = i, j
        return s[start:end + 1]

    def exec(self):
        print(s.longestPalindrome("ccc"))


if __name__ == '__main__':
    s = Solution()
    s.exec()
