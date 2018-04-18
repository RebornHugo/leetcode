class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ""
        i = 0
        flag = False
        while True:
            cur = ''
            for s in strs:
                if i == len(s):
                    flag = True
                    break
                if not cur:
                    cur = s[i]
                elif cur != s[i]:
                    flag = True
                    break
            if flag:
                break
            i += 1
        return strs[0][:i]


if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["flower", "flow", "flight"]))
