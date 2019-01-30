class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        mapping = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'

                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        # if len(stack) == 0: return True
        return not stack


if __name__ == '__main__':
    s = Solution()
    print(s.isValid("()"))
