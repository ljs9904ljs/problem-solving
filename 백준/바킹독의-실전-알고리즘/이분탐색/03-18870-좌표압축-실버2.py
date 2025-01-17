"""

푸는데 걸린 시간: 14분 12초

"""


import sys

input = sys.stdin.readline


n = int(input())
nums = list(map(int, input().split()))


nums_set = sorted(set(nums))

cache = dict()


result = []

for i, num in enumerate(nums_set):
    if num not in cache:
        cache[num] = i

for num in nums:
    if num in cache:
        result.append(cache[num])
    else:
        raise Exception("unreachable!")

print(" ".join(map(str, result)))
        
