from collections import deque

map_dict = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "": return []
        cur = deque()
        res = []
        self.dfs(digits, cur, 0, res)
        return res

    def dfs(self, digits, cur, l, res):
        if l == len(digits):
            res.append(''.join(cur))
            return
        for i in map_dict[digits[l]]:
            cur.append(i)
            self.dfs(digits, cur, l + 1, res)
            cur.pop()


if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations('23'))
