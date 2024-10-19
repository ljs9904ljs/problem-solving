"""
출처: https://youtu.be/5Lu34WIx2Us?si=KtEDFxBTDp2Ik9RX

유형: DP
제목: 효율적인 화폐 구성


<문제>
- N가지 종류의 화폐가 있습니다. 이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 하려고 합니다.
    이 때 각 종류의 화폐는 몇 개라도 사용할 수 있습니다.
- 예를 들어 2원, 3원 단위의 화폐가 있을 때는 15원을 만들기 위해 3원을 5개 사용하는 것이 가장 최소한의 화폐 개수입니다.
- M원을 만들기 위한 최소한의 화폐 개수를 출력하는 프로그램을 작성하세요.

- 입력;
첫째 줄에 N, M이 주어진다. (1<= N <= 100, 1 <= M <= 10,000)
이후 N 개의 줄에는 각 화폐의 가치가 주어진다. 화폐의 가치는 10,000보다 작거나 같은 자연수이다.

- 출력;
첫째 줄에 최소 화폐 개수를 출력한다. 불가능할 때는 -1을 출력한다.

- 입력 예시1;
2 15
2
3

- 입력 예시2;
3 4
3
5
7

- 출력 예시1;
5

- 출력 예시2;
-1


<나의 답안 해석>

화폐 가치를 a0, a1, a2, a3, ... 라 하자

dp[n] = min( dp[n], dp[n - a0] + 1, dp[n - a1] + 1, dp[n - a2] + 1, ... )


"""

N, M = map(int, input().split())
vals = []
for i in range(N):
    vals.append(int(input()))

INF = 2_000_000_000
def dp(vals: list[int], m: int) -> int:
    cnt = INF
    
    if m == 0: return 0

    for val in vals:
        if (m - val) >= 0:
            result = dp(vals, m - val)
            if result is None: 
                continue
            else: 
                cnt = min(cnt, result + 1)
    
    if cnt == INF:  # 내가 들고 있는 화폐들 중에서 어떤 것도 사용할 수 없는 경우이다.
        return None
    else:  # 하나 이상의 화폐가 사용 가능한 경우
        return cnt


result = dp(vals, M)  
print(-1 if result is None else result)




### 동영상 속에서 주어진 답 ##

n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))
    
d = [10001] * (m + 1)  # 10001은 INF의 역할을 한다.

d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
