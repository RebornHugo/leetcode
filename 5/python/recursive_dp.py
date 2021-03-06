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

        def recursive(s, start, end):
            if dp[start][end] != 0: return dp[start][end]
            if s[start] == s[end]:
                dp[start][end] = recursive(s, start + 1, end - 1)
                return dp[start][end]
            dp[start][end] = -1
            return -1

        for i in range(len(s)):
            for j in range(i, len(s)):
                recursive(s, i, j)
        start = end = maxLen = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dp[i][j] == 1 and j - i + 1 > maxLen:
                    maxLen = j - i + 1
                    start, end = i, j
        return s[start:end + 1]


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome('babad'))
