"""

푸는 데 걸린 시간: 8분 33초.

"""


import sys

input = sys.stdin.readline


k, n = map(int, input().split())
lens = [int(input()) for _ in range(k)]


def check(hope: int) -> bool:
    count = 0
    
    for len in lens:
        while len >= hope:
            count += 1
            len -= hope
    
    return count >= n
    

l = 0
r = int(2 << 31 - 1)

ans = None
while l <= r:
    mid = (l + r) // 2
    
    if check(mid):
        ans = mid
        l = mid + 1
    else:
        r = mid - 1


print(ans)