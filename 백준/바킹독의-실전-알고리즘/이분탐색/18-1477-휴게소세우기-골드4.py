"""

혼자 힘으로 풀지 못해서 풀이를 봤다.

특정 최대값을 만들 수 있는지를 체크하려고 시도했었는데, 그 check 함수를 구현하지 못했다. 

나는 m개의 신규 휴게소를 기존의 구간들에 어떻게 배치할 지를 위주로 고민했었는데,
풀이를 보니 구간마다 최대값을 충족할 수 있게 하려면 몇 개의 휴게소를 배치하는 지를 count하더라.


"""



import sys


input = sys.stdin.readline


n, m, l = map(int, input().split())
if n == 0:
    arr = []
else:
    arr = list(map(int, input().split()))
    

# 다리의 시작점과 끝점을 넣어서 계산을 편하게 한다.
arr.append(0)
arr.append(l)
arr.sort()


def check(x: int) -> bool:
    
    needed_cnt = 0
    for i in range(len(arr) - 1):
        dist = arr[i + 1] - arr[i]
        
        if dist % x == 0:
            needed_cnt += max(0, dist // x - 1)
        else:
            needed_cnt += (dist // x) 
    
    return needed_cnt > m


left = 0
right = l

while left < right:
    mid = (left + right) // 2
    
    if check(mid):
        left = mid + 1
    else:
        right = mid

print(left)
