"""
출처: https://youtu.be/5Lu34WIx2Us?si=KtEDFxBTDp2Ik9RX

유형: DP
제목: 금광


<문제>
n * m 크기의 금광이 있습니다. 금광은 1 * 1 크기의 칸으로 나누어져 있으며, 각 칸은 특정한 크기의 금이 들어 있습니다.
채굴자는 첫 번째 열부터 출발하여 금을 캐기 시작합니다. 맨 처음에는 첫 번째 열의 어느 행에서든 출발할 수 있습니다.
이후에 m - 1번에 걸쳐서 매 번 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동해야 합니다.
결과적으로 채굴자가 얻을 수 있는 금의 최대 크기를 출력하는 프로그램을 작성하세요.


- 입력;
첫째 줄에 테스트 케이스 T가 입력된다. (1<=T<=1,000)
매 테스트 케이스 첫 째 줄에 n과 m이 공백으로 구분되어 입력된다. (1 <= n, m <= 20)
둘 째 줄에 n * m개의 위치에 매장된 금의 개수가 공백으로 구분되어 입력됩니다.( 1 <= 각 위치에 매장된 금의 개수 <= 100 )

- 출력;
테스트 케이스마다 채굴자가 얻을 수 있는 금의 최대 크기를 출력합니다. 각 테스트 케이스는 줄 바꿈을 이용해 구분합니다.

- 입력 예시; [행1] [행2] [행3] ... 같은 순서로 써있는 거임
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2


- 출력 예시;
19
16


<나의 답안 해석>

dp[*][0] = gold[*][0]
dp[i][j] = max( dp[i+1][j-1], dp[i][j-1], dp[i-1][j-1] ) + gold[i][j]

<메모>
이 문제에서 파이썬 인풋을 받는 부분을 참고할 만 함.

"""

T = int(input())

for t in range(T):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    arr = [ [0] * m for _ in range(n) ]
    for i in range(n):
        for j in range(m):
            arr[i][j] = data.pop(0)


    memo = [ [None] * m for _ in range(n) ]
    def dp(gold_arr, x: int, y: int) -> int:
        if memo[x][y] is not None:
            return memo[x][y]
        
        if y == 0:
            memo[x][y] = gold_arr[x][0]
            return gold_arr[x][0]
        
        gold = dp(gold_arr, x, y - 1)
        if x + 1 <= n - 1:
            gold = max(gold, dp(gold_arr, x + 1, y - 1))
        if x - 1 >= 0:
            gold = max(gold, dp(gold_arr, x - 1, y - 1))
        gold += gold_arr[x][y]
        
        memo[x][y] = gold
        return gold


    result = max( [dp(arr, i, m - 1) for i in range(n)] )
    print(result)






### 동영상 속에서 주어진 답 ##

# for tc in range(int(input())):
#     n, m = map(int, input().split())
#     array = list(map(int, input().split()))
    
#     dp = []
#     index = 0
#     for i in range(n):
#         dp.append(array[index:index + m])
#         index += m
    
#     for j in range(1, m):
#         for i in range(n):
#             if i == 0: left_up = 0
#             else: left_up = dp[i - 1][j - 1]
            
#             if i == n - 1: left_down = 0
#             else: left_down = dp[i + 1][j - 1]
            
#             left = dp[i][j - 1]
#             dp[i][j] = dp[i][j] + max(left_up, left_down, left)
#     result = 0
#     for i in range(n):
#         result = max(result, dp[i][m - 1])
    
#     print(result)