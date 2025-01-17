"""

문제 푸는데 걸린 시간: 4분 7초

"""



import sys
from collections import defaultdict
input = sys.stdin.readline


n = int(input())
nums = list(map(int, input().split()))
m = int(input())
checks = list(map(int, input().split()))

d = defaultdict(int)
for num in nums:
    d[num] += 1


for check in checks:
    if check in d:
        print(d[check], end=' ')
    else:
        print(0, end=' ')

print()