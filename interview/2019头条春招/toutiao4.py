# 二分
import sys

n, m = list(map(int, sys.stdin.readline().split()))
nums = list(map(int, sys.stdin.readline().split()))
nums.sort(reverse=True)


def f(temp):
    count = 0
    for num in nums:
        count += int(num / temp)
    if count >= m:
        return True
    else:
        return False


left = 0
right = sum(nums) / m
while abs(right - left) > 1e-5:
    mid = (left + right) / 2
    if f(mid):
        left = mid
    else:
        right = mid
print('%.2f' % left)
