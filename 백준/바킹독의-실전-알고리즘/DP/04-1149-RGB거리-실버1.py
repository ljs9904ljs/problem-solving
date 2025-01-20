"""

문제 푸는 데 걸린 시간: 49분 19초

dp[i][0] = dp[i-1][1] or dp[i-1][2]
dp[i][1] = dp[i-1][0] or dp[i-1][2]
dp[i][2] = dp[i-1][0] or dp[i-1][1]

"""

import sys


input = sys.stdin.readline


n = int(input())
arr = []
arr.append([0, 0, 0])

for _ in range(n):
    arr.append(list(map(int, input().split())))

dp = [[0] * 3 for _ in range(n + 5)]

dp[1][0] = arr[1][0]
dp[1][1] = arr[1][1]
dp[1][2] = arr[1][2]

for i in range(2, n + 1):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + arr[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + arr[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + arr[i][2]


print(min(dp[n][0], dp[n][1], dp[n][2]))