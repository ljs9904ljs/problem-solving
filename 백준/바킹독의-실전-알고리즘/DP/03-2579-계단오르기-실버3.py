"""
문제 푸는 데 25분 2초 걸림.

dp[i][1 or 2] = max { dp[i - 1][1] , dp[i - 2][1 or 2] } + val[i]

dp[1][1] = val[1]
dp[1][2] = 0

dp[2][1] = val[2]
dp[2][2] = val[1] + val[2]  # dp[2 - 1][1] + val[2]

dp[3][1] = dp[3 - 2][1 or 2] + val[3]
dp[3][2] = dp[3 - 1][1] + val[3]

"""



import sys

input = sys.stdin.readline


n = int(input())
val = []
val.append(0)
val.extend([int(input()) for _ in range(n)])



if n == 1:
    print(val[1])
elif n == 2:
    print(val[1] + val[2])
else:

    dp = [[0] * 3 for _ in range(n + 5)]

    dp[1][1] = val[1]
    dp[2][1] = val[2]
    dp[2][2] = val[1] + val[2]

    for i in range(3, n + 1):
        dp[i][1] = max(dp[i - 2][1], dp[i - 2][2]) + val[i]
        dp[i][2] = dp[i - 1][1] + val[i]


    print(max(dp[n][1], dp[n][2]))

