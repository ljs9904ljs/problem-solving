"""

문제 푸는 데 걸린 시간: 6분 31초

dp[1] = 1
dp[2] = 2
dp[i] = dp[i - 1] + dp[i - 2]

"""


import sys


input = sys.stdin.readline


n = int(input())

dp = [0] * (n + 5)


dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 10007


print(dp[n] % 10007)