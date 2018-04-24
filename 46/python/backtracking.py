import itertools
from collections import deque


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # return list(itertools.permutations(nums))
        res = []

        def dfs(cur, l):
            if l == len(nums):
                res.append(list(cur))
            for i in nums:
                if i in cur: continue
                cur.append(i)
                dfs(cur, l + 1)
                cur.pop()

        dfs(deque(), 0)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.permute([1, 2, 3]))
