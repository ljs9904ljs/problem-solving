"""

문제 푸는 데 걸린 시간: 8분 53초

"""




import sys
from functools import cache



input = sys.stdin.readline


N = int(input())
dp = [0] * 1000005

dp[1] = 0
dp[2] = 1
dp[3] = 1

for i in range(4, N + 1):
    mn = dp[i - 1] + 1
    if i % 3 == 0:
        mn = min(mn, dp[i // 3] + 1)
    if i % 2 == 0:
        mn = min(mn, dp[i // 2] + 1)
    
    dp[i] = mn


print(dp[N])



