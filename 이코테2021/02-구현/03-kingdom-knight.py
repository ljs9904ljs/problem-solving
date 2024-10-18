"""
문제 및 강의 출처: https://youtu.be/2zjoKjt97vQ?si=PpaK6DISWRoLL4Id

유형: 구현
제목: 왕실의 나이트


<문제>
- 8x8 체스판에서 나이트가 움직인다.
- 입력; 첫 째 줄에 8 x 8 좌표 평면 상에서 현재 나이트가 위치한 곳의 좌표를 나타내는 두 문자로 구성된 문자열이 입력된다. 입력 문자는 a1처럼 열과 행으로 이뤄진다.
- 출력; 첫 째 줄에 나이트가 이동할 수 있는 경우의 수를 출력하시오.

- 입력 예시; a1
- 출력 예시; 2

<나의 답안 해석>
- 주어진 조건을 그대로 구현하였다. 모든 조건을 고려하더라도 시간 제한을 초과할 일이 없으므로 그대로 구현한 것이다.

"""

alpha_to_num = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}

s = input()
x = alpha_to_num[s[0]]
y = int(s[1])

movements = [(-1, 2), (1, 2), (-1, -2), (1, -2), (-2, 1), (-2, -1), (2, 1),
             (2, -1)]

count = 0

for movement in movements:
    dx, dy = movement
    nx = x + dx
    ny = y + dy
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        count += 1

print(count)

### 동영상 속에서 주어진 답 ###

# 내 풀이랑 거의 같음. 다만, alphabet을 integer로 변경하는 부분을 참고할 수 있겠다.
# int(ord(input_data[0])) - int(ord('a')) + 1

