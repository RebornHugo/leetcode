# import itertools
# one line solution : return list(itertools.combinations(range(1, n + 1), k))

from collections import deque


class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        l = list(range(1, n + 1))
        res = []

        def dfs(cur, depth):
            if depth == k:
                res.append(list(cur))
                return
            try:
                start = cur[-1]
            except IndexError:
                start = 0
            for i in l[start:]:
                # if cur and i <= cur[-1]:
                #     continue
                cur.append(i)
                dfs(cur, depth + 1)
                cur.pop()

        dfs(deque(), 0)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.combine(4, 2))
