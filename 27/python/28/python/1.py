class Solution2:
    def strStr(self, haystack: 'str', needle: 'str') -> 'int':
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1

class Solution:
    def strStr(self, haystack: 'str', needle: 'str') -> 'int':
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1


s = Solution()
print(s.strStr(haystack='aaaaa', needle='bba'))
