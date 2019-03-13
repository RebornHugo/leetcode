class Solution:
    def divide(self, dividend: 'int', divisor: 'int') -> 'int':
        if dividend == 0: return 0
        sign_dividend = 1 if dividend > 0 else -1
        sign_divisor = 1 if divisor > 0 else -1
        res = 0
        dividend = dividend * sign_dividend
        divisor = divisor * sign_divisor
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                res += i
                dividend -= temp
                i <<= 1
                temp <<= 1

        res = sign_divisor * sign_dividend * res
        return min(max(-2 ** 31, res), 2 ** 31 - 1)


s = Solution()
print(s.divide(-2147483648, -1))
