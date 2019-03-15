from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # lowest: lowest price up to the i-th day
        # profit: max profit at the i-th day
        if not prices: return 0
        lowest = prices[0]
        profit = 0
        for price in prices:
            lowest = min(lowest, price)
            profit = max(profit, price - lowest)
        return profit

    def maxProfit2(self, prices: List[int]) -> int:
        # 使用gain的方法来做 参考leetcode 53.
        if not prices or len(prices) <= 1: return 0
        gains = [0]
        for i, price in enumerate(prices[1:]):
            gains.append(price - prices[i])

        f = [0]  # max sub list sum up to the i-th element
        for gain in gains:
            cur = f[-1] + gain if f[-1] > 0 else gain
            f.append(cur)
        return max(f)


s = Solution()
print(s.maxProfit2([7, 1, 5, 3, 6, 4]))
