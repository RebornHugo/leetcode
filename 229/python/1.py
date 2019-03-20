from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums: return []
        res = set()
        if len(nums) <= 2: return list(set(nums))

        nums.sort()
        for i in range(len(nums)):
            if nums[i] == nums[i - len(nums) // 3]:
                res.add(nums[i])
        return list(res)


class Solution2:
    def majorityElement(self, nums: List[int]) -> List[int]:
        lenth = len(nums)
        ret = []
        import collections
        counter = collections.Counter(nums)
        for i, v in counter.items():
            if v > (lenth / 3):
                ret.append(i)
        return ret


class Solution3:
    def majorityElement(self, nums: 'List[int]') -> 'List[int]':
        if not nums:
            return []
        cand1, cand2, count1, count2 = 0, 1, 0, 0
        for n in nums:
            if n == cand1:
                count1 += 1
            elif n == cand2:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = n, 1
            elif count2 == 0:
                cand2, count2 = n, 1
            else:
                count1 -= 1
                count2 -= 1
        return [n for n in [cand1, cand2] if nums.count(n) > len(nums) // 3]
