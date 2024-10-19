"""
출처: https://youtu.be/5Lu34WIx2Us?si=KtEDFxBTDp2Ik9RX

유형: DP
제목: 병사 배치하기


<문제>
N명의 병사가 무작위로 나열되어 있습니다. 각 병사는 특정한 값의 전투력을 보유하고 있습니다.
병사를 배치할 때는 전투력이 높은 병사가 앞 쪽에 오도록 내림차순으로 배치를 하고자 합니다.
다시 말해 앞 쪽에 있는 병사의 전투력이 항상 뒤 쪽에 있는 병사보다 높아야 합니다.
또한 배치 과정에서는 특정한 위치에 있는 병사를 열외시키는 방법을 이용합니다.
그러면서도 남아 있는 병사의 수가 최대가 되도록 하고 싶습니다.

- 입력;
첫째 줄에 N이 주어집니다. (1 <= N <= 2,000)
둘째 줄에 각 병사의 전투력이 공백으로 구분되어 차례대로 주어집니다.
각 병사의 전투력은 10,000,000보다 작거나 같은 자연수입니다.

- 출력;
첫째 줄에 남아 있는 병사의 수가 최대가 되도록 하기 위해서 열외시켜야 하는 병사의 수를 출력합니다.


- 입력 예시;
7
15 11 4 8 5 2 4

- 출력 예시;
2


<나의 답안 해석>
Longest Increaseing Subsequence 문제와 비슷하다.

n := element order (n = {0, 1, 2, ...})
dp[n] := Considering items from '0'th to 'n'th element, the length of the longest increasing subsequence
val[n] := the value(here '전투력') of 'n'th element

dp[n] = 1 + {max(dp[i]) | i < n AND val[i] >= val[n] }

solution := len(input array) - dp[n - 1]

<메모>


"""

N = int(input())
arr = list(map(int, input().split()))

def dp(arr: list[int], n: int) -> int:
    if n == 0: return 1
    
    return 1 + max([dp(arr, i) for i in range(len(arr)) if i < n and arr[i] >= arr[n]], 
                    default=0)

print(len(arr) - dp(arr, N - 1))






### 동영상 속에서 주어진 답 ##

# n = int(input())
# array = list(map(int, input().split()))

# # 순서를 뒤집어 Longest Increasing Subsequence 문제로 변환
# array.reverse()

# dp = [1] * n

# for i in range(1, n):
#     for j in range(0, i):
#         if array[j] < array[i]:
#             dp[i] = max(dp[i], dp[j] + 1)

# print(n - max(dp))