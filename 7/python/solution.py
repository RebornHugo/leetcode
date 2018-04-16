class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        if x < 0: return -self.reverse(-x)
        while x:
            res = res * 10 + x % 10
            x = x // 10
        return res if res < 2 ** 31 else 0


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(-123))
