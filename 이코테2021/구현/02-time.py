"""
출처: https://youtu.be/2zjoKjt97vQ?si=PpaK6DISWRoLL4Id

유형: 구현
제목: 시각


<문제>
- 입력; 첫 째 줄에 정수 N이 입력됩니다. (0 <= N <= 23)
- 출력; 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 출력한다.

- 입력 예시; 5
- 출력 예시; 11475

<나의 답안 해석>
- N == 23일 때, 0.035초 소요됨.
- 문제에서 주어진 조건을 보고 연산 횟수를 계산했을 때 단순히 3중 for문을 수행하더라도 시간 제한에 걸리지 않겠다는 것을 추측할 수 있었음. 그래서 단순히 주어진 조건 그대로 구현함.
- Brute force

"""

N = int(input())

hour = 0
min = 0
sec = 0

count = 0

for h in range(N + 1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) or '3' in str(m) or '3' in str(s):
                count += 1

print(count)

### 동영상 속에서 주어진 답 ###

# 내 풀이랑 거의 같음. 다만,
# if '3' in str(i) + str(j) + str(k) 같은 방식으로 문자열을 concatenation해서 체크함.
