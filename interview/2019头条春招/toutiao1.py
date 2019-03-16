import sys

N = int(sys.stdin.readline().strip())
remain = 1024 - N
res = []
# for i in range(remain + 1):
#     print(i)
#     for j in range(remain + 1):
#         for n in range(remain + 1):
#             if i + 4 * j + 16 * n == remain:
#                 res.append(i + j + n)
# print(min(res))

count = 0
for cash in [16, 4, 1]:
    count += remain // cash
    remain = remain % cash
print(count)