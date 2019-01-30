# 20. Valid Parentheses
mapping_dict = {
    '{': '}',
    '[': ']',
    '(': ')'
}


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True

        def isPartValid(x):
            if len(x) == 0:
                return True
            if len(x) == 1:
                return False
            for idx, i in enumerate(x[:-1]):
                if i in mapping_dict and mapping_dict[i] == x[idx+1]:
                    if len(x) - 2 > idx:
                        return isPartValid(x[:idx] + x[idx+2:])
                    else:
                        return isPartValid(x[:idx])
            return False

        return isPartValid(s)


if __name__ == '__main__':
    s = Solution()
    print(s.isValid("()"))
