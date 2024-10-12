"""
출처: https://youtu.be/2zjoKjt97vQ?si=PpaK6DISWRoLL4Id

유형: 그리디
제목: 1이 될 때까지

<문제>
어떤 수 N이 1이 될 때까지 두 과정 중 하나를 반복적으로 선택 및 수행한다.
두 번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있다.

1. N에서 1을 뺀다.
2. N을 K로 나눈다.

정수 N과 정수 K가 주어질 때 N이 1이 될 때까지 1번 혹은 2번 과정을 수행해야 하는 최소 횟수를 구해라.

<나의 답안 해석>
매 라운드마다 1번 연산이나 2번 연산 중에서 하나를 선택해야만 한다. 그 때 1만큼씩 빼는 것보다는 나누기(K가 2이상이라면)가 수를 훨씬 더 빠르게 감소시킬 수 있다. 그래서 최대한 2번 연산을 선택하려고 해야 한다. 하지만 2번 연산을 선택할 수 없는 경우가 있으므로 그 때만 부득이하게 1번 연산을 선택한다. 그렇게 1까지 계산했을 때 최소 횟수를 획득할 수 있다.

별개로, N이 1이상의 정수라면 주어진 수 N을 1로 만드는 것은 항상 가능하다. 1번 연산을 N-1번 수행하면 반드시 가능하기 때문이다. 
"""

N, K = map(int, input().split())


def op1():
  global N
  N -= 1


def op2():
  global N
  if N % K == 0:
    N = N // K


def is_op2_possible():
  global N, K
  return N % K == 0


cnt = 0
while N != 1:
  if is_op2_possible():
    op2()
    cnt += 1
  else:
    op1()
    cnt += 1

print(cnt)

### 동영상 속에서 주어진 답 ###
"""
n, k = map(int, input().split())

# 1번 연산 수행 횟수 + 2번 연산 수행 횟수
result = 0

while True:
  # 제일 가까운 k의 배수 찾기
  # 이렇게하면, 2번 연산 직전까지 필요한 1번 연산 횟수를 한 번에 계산할 수 있다.
  target = (n // k) * k

  # 1번 연산 수행한 횟수를 한 번에 더해주기.
  result += n - target
  n = target

  # 2번 연산 수행이 불가능함.
  if n < k:
    break

  n //= k
  result += 1

# 마지막으로 1번 연산을 최대한 수행한다.
result += (n - 1)
print(result)
"""
