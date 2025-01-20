"""

문제 푸는 데 걸린 시간: 9분 39초

prefix sum 문제인 듯?


"""

import sys


input = sys.stdin.readline


n, m = map(int, input().split())
nums = list(map(int, input().split()))
intervals = []
for _ in range(m):
    s, e = map(int, input().split())
    intervals.append((s, e))

prefix_sums = [0] * n

for i, num in enumerate(nums):
    if i - 1 >= 0:
        prefix_sums[i] = num + prefix_sums[i - 1]
    else:
        prefix_sums[i] = num

result = []
for i, j in intervals:
    to = prefix_sums[j - 1]
    frm = prefix_sums[i - 2] if i - 2 >= 0 else 0
    result.append(to - frm)

for sm in result:
    print(sm)

