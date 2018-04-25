from collections import deque


class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # return list(map(list, list(set(map(tuple, list(itertools.permutations(nums)))))))
        res = []
        used = [False] * len(nums)
        nums.sort()

        def dfs(cur, l):
            if l == len(nums):
                res.append(list(cur))
                return
            for i, content in enumerate(nums):
                if used[i] or (i > 0 and content == nums[i - 1] and used[i - 1]):
                    continue
                used[i] = True
                cur.append(content)
                dfs(cur, l + 1)
                cur.pop()
                used[i] = False

        dfs(deque(), 0)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.permuteUnique([1, 1, 2]))
