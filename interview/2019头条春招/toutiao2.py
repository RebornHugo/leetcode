import sys

N = int(sys.stdin.readline().strip())
strs = []
for i, line in enumerate(sys.stdin):
    if i == N: break
    strs.append(line.split())


def f(s):
    s = s[0]
    if len(s) <= 2: return s
    i = 2
    while i < len(s):
        if s[i - 2] == s[i - 1] and s[i - 1] == s[i]:
            s = s[:i - 1] + s[i:]
        else:
            i += 1

    if len(s) <= 3: return s
    i = 3
    while i < len(s):
        if s[i - 3] == s[i - 2] and s[i - 1] == s[i]:
            s = s[:i - 1] + s[i:]
        else:
            i += 1

    return s


strs = list(map(f, strs))
for s in strs:
    print(s)

#
# nums = []
# for i, line in enumerate(sys.stdin):
#     if i == N: break
#     nums.append(list(map(int, line.split())))
