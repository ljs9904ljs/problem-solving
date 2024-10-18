"""
출처: https://youtu.be/5Lu34WIx2Us?si=KtEDFxBTDp2Ik9RX

유형: DP
제목: 1로 만들기


<문제>
 정수 X가 주어졌을 때, 정수 X에 사용할 수 있는 연산은 다음과 같이 4가지입니다.
  1. X가 5로 나누어 떨어지면, 5로 나눕니다.
  2. X가 3으로 나누어 떨어지면, 3으로 나눕니다.
  3. X가 2로 나누어 떨어지면, 2로 나눕니다.
  4. X에서 1을 뺍니다.
 정수 X가 주어졌을 때, 연산 4가지를 적절히 사용해서 값을 1로 만들고자 합니다.
 연산을 사용하는 횟수의 최소값을 출력하세요. 
 예를 들어, 정수가 26이면 다음과 같이 계산해서 3번의 연산이 최소값입니다.
  - 26 -> 25 -> 5 -> 1


- 입력;
첫 째 줄에 정수 X가 주어집니다. (1<=X<30,000)

- 출력;
첫 째 줄에 연산을 하는 횟수의 최소값을 출력합니다.

- 입력 예시;

- 출력 예시;


<나의 답안 해석>

dp[n] := n을 1로 만들기 위해 필요한 최소한의 연산 횟수

dp[n] = 1 + min(dp[n // 2],
                dp[n // 3],
                dp[n // 5],
                dp[n - 1] )

"""


X = int(input())

memo = [None] * (X + 5)
memo[1] = 0
def dp(x: int) -> int:
    if memo[x] is not None: return memo[x]
    
    print(f"number : ({x})")
    if x == 1: return 0
    
    min_num_of_op = dp(x - 1)
    if x % 5 == 0:
        min_num_of_op = min(
            min_num_of_op, 
            dp(x // 5)
        )
    if x % 3 == 0:
        min_num_of_op = min(
            min_num_of_op, 
            dp(x // 3)
        )
    if x % 2 == 0:
        min_num_of_op = min(
            min_num_of_op, 
            dp(x // 2)
        )
    
    memo[x] = min_num_of_op + 1
    return min_num_of_op + 1
    

print(dp(X))


### 동영상 속에서 주어진 답 ##


# x = int(input())
# d = [0] * 30001

# for i in range(2, x + 1):
#     d[i] = d[i - 1] + 1
#     if i % 2 == 0:
#         d[i] = min(d[i], d[i // 2] + 1)
#     if i % 3 == 0:
#         d[i] = min(d[i], d[i // 3] + 1)
#     if i % 5 == 0:
#         d[i] = min(d[i], d[i // 5] + 1)

# print(d[x])