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

class Solution3:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        p = 1
        length = len(nums)
        output = []
        for i in range(0, length):
            output.append(p)
            p = p * nums[i]
        p = 1
        for i in range(length - 1, -1, -1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output


s = Solution()
print(s.productExceptSelf([1, 2, 3, 4, 0]))
