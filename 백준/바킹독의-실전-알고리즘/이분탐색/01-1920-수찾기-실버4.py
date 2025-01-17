

import sys

input = sys.stdin.readline


n = int(input())
nums = set(map(int, input().split()))
m = int(input())
checks = list(map(int, input().split()))


for check in checks:
    if check in nums:
        print("1")
    else:
        print("0")
