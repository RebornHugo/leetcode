class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        def dp(i, j):
            if i == j: return 1
            # if j - i == 1:
            #     if s[i] == s[j]:
            #         return 1
            #     else:
            #         return 2
            if s[i] in s[i + 1:j + 1]: return dp(i + 1, j)
            if s[j] in s[i:j]: return dp(i, j - 1)
            if s[i] not in s[i + 1:j + 1] and s[j] not in s[i:j]:
                return 1 + max(dp(i, j - 1), dp(i + 1, j))

        return dp(0, len(s) - 1)


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("pwwkew"))
