# https://www.bilibili.com/video/av16071242?from=search&seid=6919871183808047155
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings:
            return 0
        if len(ratings) == 1:
            return 1

        res = [1 for _ in range(len(ratings))]

        # left2right
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                res[i] = res[i - 1] + 1

        # right2left
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                res[i] = max(res[i], res[i + 1] + 1)

        return sum(res)


s = Solution()
print(s.candy([1, 2, 2]))
