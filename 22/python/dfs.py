from typing import List


class Solution:
    """
    带剪枝的dfs
    """

    def generateParenthesis(self, n: 'int') -> 'List[str]':
        self.n = n
        stack = []
        res = []
        cur = ''
        self.dfs(cur, stack, res)
        return res

    def dfs(self, cur: 'str', stack: 'List', res: 'List'):
        if len(cur) == self.n * 2:
            res.append(cur)
            return

        if stack and stack[-1] == '(':
            # cur += ')'
            stack.pop()
            self.dfs(cur + ')', stack, res)
            stack.append('(')
            # cur = cur[:-1]

        if cur.count('(') < self.n:
            stack.append('(')
            self.dfs(cur + '(', stack, res)
            stack.pop()
            # 最后这里一定要注意退栈！！！！！


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))
