import sys
# 参考leetcode 135. candy  https://leetcode.com/problems/candy

_N = int(sys.stdin.readline().strip())
for i in range(_N):
    if i == _N: break
    N = int(sys.stdin.readline().strip())
    nums = list(map(int, sys.stdin.readline().split()))
    res_dict = {}
    leastIndex = nums.index(min(nums))
    res_dict[leastIndex] = 1
    cur = leastIndex
    while len(res_dict) < N:
        last = cur
        cur = last + 1 // N
        if nums[cur] > res_dict[last]:
            res_dict[cur] = res_dict[last] + 1

    print(sum(res_dict.values()))
    # print(N)
    # print(nums)
