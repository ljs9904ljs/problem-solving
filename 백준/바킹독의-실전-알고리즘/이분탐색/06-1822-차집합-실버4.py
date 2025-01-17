"""

푸는 데 걸린 시간: 8분 43초

"""


import sys

input = sys.stdin.readline


a, b = map(int, input().split())

aset = set(map(int, input().split()))
bset = set(map(int, input().split()))

result = []
for aelem in aset:
    if aelem in bset:
        continue
    else:
        result.append(aelem)

if len(result) == 0:
    print(0)
else:
    result.sort()
    print(len(result))
    print(" ".join(map(str, result)))