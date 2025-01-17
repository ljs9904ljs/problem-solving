"""

푸는 데 걸린 시간: 6분 31초.


절단기로 자르고 남은 나무의 높이가 음수가 될 수 없음을 유념하자.

"""



import sys

input = sys.stdin.readline

n, m = map(int, input().split())
heights = list(map(int, input().split()))



def check(cutter: int) -> bool:
    return sum([max(h - cutter, 0) for h in heights]) >= m


l = 0
r = max(heights)

ans = None
while l <= r:
    mid = (l + r) // 2
    
    if check(mid):
        ans = mid
        l = mid + 1
    else:
        r = mid - 1
        

print(ans)