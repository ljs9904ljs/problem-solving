"""

문제 푸는 데 걸린 시간: 5분 50초

"""


import sys

input = sys.stdin.readline


T = int(input())
tc = [int(input()) for _ in range(T)]


for n in tc:

    """

    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4  # 1+1+1, 1+2, 2+1, 3 -->> 순서 바뀌면 다른 경우임.
    """
    dp = [0] * 15
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    

    print(dp[n])
