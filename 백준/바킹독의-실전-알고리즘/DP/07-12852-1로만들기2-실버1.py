"""

문제 푸는 데 걸린 시간: 44분 13초 정도

dp[1] = 0
dp[2] = 1
dp[3] = 1

dp[i] = min{ dp[i - 1], dp[i // 3],  dp[i // 2] } + 1


참고)
이거 

'if dp[i // 3] <= mn:'랑
'if dp[i // 2] <= mn:'에서,

등호를 둘 다 빼놓고 작성했을 때 백준 저지 94%쯤에서 실패했다.
그런데 등호를 둘 다 추가하니까 테스트를 전부 통과했다.


"""

import sys

input = sys.stdin.readline

N = int(input())

MAX = int(1e7)
dp = [MAX] * (N + 55)

dp[1] = 0
dp[2] = 1
dp[3] = 1

s = set()
d = dict()
d[3] = 1
d[2] = 1
d[1] = None



for i in range(4, N + 1):
    mn = dp[i - 1]
    mn_num = i - 1

    if i % 3 == 0:
        if dp[i // 3] <= mn:
            mn_num = i // 3
            mn = dp[i // 3]
    
    if i % 2 == 0:
        if dp[i // 2] <= mn:
            mn_num = i // 2
            mn = dp[i // 2]
    
    dp[i] = mn + 1
    d[i] = mn_num


print(dp[N])

l = list()
l.append(N)
cur = d[N]
while cur is not None:
    l.append(cur)
    cur = d[cur]

print(" ".join(map(str, l)))