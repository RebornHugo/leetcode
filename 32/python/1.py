class Solution:
    def longestValidParentheses(self, s: str) -> int:
        i = 0
        res = 0
        while i < len(s):
            j = i + 1
            while j <= len(s):
                if self.isValid(s[i:j]):
                    res = max(j - i, res)
                j += 1
            i += 1
        return res

    def isValid(self, s: str):
        if not s: return False
        stack = []
        for cur in s:
            if cur == '(':
                stack.append(cur)
            elif cur == ')':
                if not stack or stack.pop() != '(':
                    return False
        if not stack:
            return True


s = Solution()
print(s.longestValidParentheses(")()())"))
