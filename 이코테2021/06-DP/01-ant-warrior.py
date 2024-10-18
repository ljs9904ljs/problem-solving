"""
출처: https://youtu.be/5Lu34WIx2Us?si=KtEDFxBTDp2Ik9RX

유형: DP
제목: 개미 전사


<문제>
 개미 전사는 부족한 식량을 충당하고자 메뚜기 마을의 식량 창고를 몰래 공격하려고 합니다.
메뚜기 마을에는 여러 개의 식량 창고가 있는데 식량 창고는 일직선으로 이어져 있습니다.
 각 식량 창고에는 정해진 수의 식량을 저장하고 있으며 개미 전사는 식량 창고를 선택적으로 약탈하여 식량을 빼앗을 예정입니다.
이 때 메뚜기 정찰병들은 일직선 상에 존재하는 식량 창고 중에서 서로 인접한 식량 창고가 공격받으면 알 수 있습니다.
 따라서 개미 전사가 정찰병에게 들키지 않고 식량 창고를 약탈하기 위해서는 최소한 한 칸 이상 떨어진 식량 창고를 약탈해야 합니다.


- 입력;
    - 첫째 줄에 식량 창고의 개수 N이 주어집니다. (3<=N<=100)
    - 둘째 줄에 공백을 기준으로 각 식량 창고에 저장된 식량의 개수 K가 주어집니다. (0<=K<=1,000)

- 출력;
    - 첫째 줄에 개미 전사가 얻을 수 있는 식량의 최대값을 출력하세요.

- 입력 예시;
4
1 3 1 5

- 출력 예시;
8


<나의 답안 해석>
일직선으로 이동하니까 일종의 DAG으로 간주할 수 있다. 
이 문제를 풀기 위해서 DAG의 longest path problem 아이디어를 차용했다.

식량 창고의 번호를 n(0, 1, 2, ...) 라고 했을 때
a[n] := 0번 창고부터 n번 창고까지 계산했을 때, 최대 식량 개수
food[n] := n번 창고의 식량 개수

a[n] = MAX{ (case1, n번 창고의 식량이 포함되지 않을 때) a[n-1] ,
            (case2, n번 창고의 식량이 포함될 때) a[n-2] + food[n] }
    

"""


N = int(input())
foods = list(map(int, input().split()))

def dp(n: int) -> int:
    if n == 0:
        return foods[0]
    if n == 1:
        return max(foods[0], foods[1])
    
    return max(dp(n - 1), dp(n - 2) + foods[n])


memo = [None] * 105  # 3 <= N <= 100 이므로 105칸.
def dp_with_memoization(n: int) -> int:
    if memo[n] is not None:
        return memo[n]
    
    if n == 0:
        memo[0] = foods[0]
        return memo[0]
    if n == 1:
        memo[1] = max(foods[0], foods[1])
        return memo[1]
    
    memo[n] = max(dp(n - 1), dp(n - 2) + foods[n])
    return memo[n]




print(dp_with_memoization(N - 1))



### 동영상 속에서 주어진 답 ##


# n = int(input())
# array = list(map(int, input().split()))

# d = [0] * 100

# d[0] = array[0]
# d[1] = max(array[0] array[1])
# for i in range(2, n):
#     d[i] = max(d[i - 1], d[i - 2] + array[i])
    
# print(d[n - 1])





