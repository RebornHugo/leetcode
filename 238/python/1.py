class Solution:
    def productExceptSelf(self, nums: 'List[int]') -> 'List[int]':
        def get_product(ns):
            _m = 1
            for _ in ns:
                _m *= _
            return _m

        m = get_product(nums)

        def func_product(n):
            if n:
                return int(m / n)
            else:
                temp = nums.copy()
                temp.remove(n)
                return get_product(temp)

        return list(map(func_product, nums))


s = Solution()
print(s.productExceptSelf([1, 2, 3, 4, 0]))
