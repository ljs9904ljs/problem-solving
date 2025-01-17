"""

1시간 넘게 못 풀어서 풀이를 보았다.

"""

# 입력 값 리스트는 오름차순으로 정렬되어 있다.

import sys
from bisect import bisect_left


input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))


### 투 포인터를 이용한 풀이이다. 다른 풀이를 보고 알게 되었다.

# i = 0
# j = n - 1

# ans = int(2e9)
# ans_pair = None
# while i < j:
#     score = arr[i] + arr[j]
    
#     if ans > abs(score):
#         ans = abs(score)
#         ans_pair = (i, j)
    
#     if score > 0:
#         j -= 1
#     elif score < 0:
#         i += 1
#     else:
#         break

# i, j = ans_pair
# print(arr[i], arr[j])
        

ans = int(2e9)
ans_pair = None

for i in range(n):
    """
    결국 arr[i]의 바로 반대되는 값인 -arr[i]가 존재하면 0을 만들 수 있으니 그게 0이랑 제일 가까운 값이다.
    -arr[i]가 존재하지 않는다면 -arr[i]와 제일 가까운 거리에 있는 것들을 검사해보면 된다.
    그 제일 가까운 거리에 있는 것들이 바로 idx - 1과 idx + 1일 것이다.
    arr[idx]의 왼쪽에 있는 값은 arr[idx]보다 작을 것이고 오른쪽에 있는 값은 arr[idx]보다 클 것이다.
    딱 그 둘을 검사해보면 된다.
    
    """
    
    idx = bisect_left(arr, -arr[i])
        
    if idx != i and (0 <= idx < n) and abs(arr[i] + arr[idx]) < ans:
        ans = abs(arr[i] + arr[idx])
        ans_pair = (arr[i], arr[idx])
    
    if idx - 1 != i and (0 <= idx - 1 < n) and abs(arr[i] + arr[idx - 1]) < ans:
        ans = abs(arr[i] + arr[idx - 1])
        ans_pair = (arr[i], arr[idx - 1])
        
    if idx + 1 != i and (0 <= idx + 1 < n) and abs(arr[i] + arr[idx + 1]) < ans:
        ans = abs(arr[i] + arr[idx + 1])
        ans_pair = (arr[i], arr[idx + 1])
    
ans_pair = sorted(ans_pair)
print(ans_pair[0], ans_pair[1])
            