"""
문제 및 강의 출처: https://youtu.be/2zjoKjt97vQ?si=PpaK6DISWRoLL4Id

유형: 구현
제목: 상하좌우


<문제>
- 첫 째 줄에 공간의 크기를 나타내는 1 <= N <= 100 이 주어집니다.
- 둘 째 줄에 여행가 A가 이동할 계획서 내용이 주어집니다. (1 <= 이동횟수 <= 100)
- R, L, U, D로 이동한다. 오른쪽/왼쪽/위쪽/아래쪽 1칸 이동
- 지도를 벗어난 움직임은 무시한다.


<나의 답안 해석>
문제에서 주어진 조건을 있는 그대로 구현하였다.


"""

N = int(input())
directions = list(input().split())  # e.g. ["R", "R", "U", "D"]

# R L U D
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

d = {'R': (1, 0), 'L': (-1, 0), 'U': (0, -1), 'D': (0, 1)}

x_coord = 1
y_coord = 1

for direction in directions:

    dx, dy = d[direction]
    nx = x_coord + dx
    ny = y_coord + dy
    if 1 <= nx <= N and 1 <= ny <= N:
        x_coord = nx
        y_coord = ny

print(
    y_coord, x_coord
)  # 문제에서 column number를 y좌표로 간주하고, row number를 x좌표로 간주하고 있기 때문에 실제 좌표평면 상의 x좌표 혹은 y좌표와 반대로 생각해야 함.

### 동영상 속에서 주어진 답 ###

# n = int(input())
# x, y = 1, 1
# plans = input().split()

# # L R U D
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# move_types = ['L', 'R', 'U', 'D']

# for plan in plans:
#     for i in range(len(move_types)):
#         if plan == move_types[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]

#     # 지도를 벗어나는 경우는 무시한다.
#     if nx < 1 or ny < 1 or nx > n or ny > n:
#         continue

#     x, y = nx, ny  # 이동 수행

# print(x, y)
