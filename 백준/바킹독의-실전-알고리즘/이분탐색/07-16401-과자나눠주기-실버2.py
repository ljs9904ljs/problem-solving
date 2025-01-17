"""

푸는 데 걸린 시간: 11분 21초

과자 1개를 희망하는 길이로 한 개 씩 끊어내서 몇 개를 만들 수 있는지 
체크하는 게 아니라, 만들 수 있는 개수를 한 번에 계산할 수 있다.

"""


import sys

input = sys.stdin.readline


m, n = map(int, input().split())
lens = list(map(int, input().split()))


def check(hope: int) -> bool:
    if hope == 0:
        return True
    
    count = 0
    for len in lens:
        count += len // hope    
            
    return count >= m



l = 0
r = int(1e9)

while l <= r:
    mid = (l + r) // 2
    
    if check(mid):
        ans = mid
        l = mid + 1
    else:
        r = mid - 1

# 모든 아이에게 똑같은 크기로 나눠주는 게 불가능하다면 0을 출력한다.
    # 해당 경우에는 mid == 0으로 호출된 결과물이 담길 것이다.
print(ans)