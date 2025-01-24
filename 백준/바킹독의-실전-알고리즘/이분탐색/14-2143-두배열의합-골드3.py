"""

문제 푸는 데 걸린 시간: 13분 58초

"""



import sys
from collections import defaultdict



input = sys.stdin.readline


t = int(input())
n = int(input())
arra = list(map(int, input().split()))
m = int(input())
arrb = list(map(int, input().split()))


# O(N) or O(M)
def make_prefix_sum(arr: list[int]) -> list[int]:
    prefixsums = []
    
    prev = 0
    for num in arr:
        prefixsums.append(num + prev)
        prev += num
    
    return prefixsums

# O(1)
def subsum(prefixsums: list[int], i: int, j: int) -> int:
    if i == 0:
        return prefixsums[j]
    
    return prefixsums[j] - prefixsums[i - 1]


asums = make_prefix_sum(arra)
bsums = make_prefix_sum(arrb)

asubsums = defaultdict(int)
bsubsums = defaultdict(int)

# O(N^2)
for i in range(n):
    for j in range(i, n):
        asubsums[subsum(asums, i, j)] += 1
        
# O(M^2)
for i in range(m):
    for j in range(i, m):
        bsubsums[subsum(bsums, i, j)] += 1

cnt = 0

# O(N * 1) = O(N)
for asubsum in asubsums:  # O(N)
    if t - asubsum in bsubsums:  # O(1)
        cnt += asubsums[asubsum] * bsubsums[t - asubsum]

print(cnt)