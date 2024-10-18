"""
문제 및 강의 출처: https://youtu.be/7C9RgOcvkvo?si=3MYI12alOB_AJNKJ

유형: DFS & BFS
제목: 미로 탈출


<문제>
- 동빈이는 N x M 크기의 직사각형 형태의 미로에 갇혔습니다. 미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야 합니다.
- 동빈이의 위치는 (1, 1)이며 미로의 출구는 (N, M)의 위치에 존재하며 한 번에 한 칸 씩 이동할 수 있습니다. 이 때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있습니다. 미로는 반드시 탈출할 수 있는 형태로 제시됩니다.
- 이 때 동빈이가 탈출하기 위해 움직여햐 하는 최소 칸의 개수를 구하세요. 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산합니다.

- 입력; 첫 째 줄에 두 정수 N, M (4 <= N, M <= 200)이 주어집니다. 다음 N개의 줄에는 각각 M개의 정수 (0 혹은 1)로 미로의 정보가 주어집니다. 각각의 수들은 공백없이 붙어서 입력으로 제시됩니다. 또한 시작 칸과 마지막 칸은 항상 1입니다.

- 출력; 첫 째 줄에 최소 이동 칸의 개수를 출력합니다.


<나의 답안 해석>
BFS를 활용하여 출발지점 <-> 도착지점 사이의 거리를 계산한다. BFS에서, 한 노드부터 다른 노드까지 진행할 때 거리 값은 1만큼씩 증가한다. 그 점을 활용하여 dist값을 1씩 증가시키며 최종 목적지까지의 거리를 계산한다.


"""
from collections import deque

INF = 100_000

N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

dist = [[INF] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def my_bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    dist[x][y] = 1

    while q:
        i, j = q.popleft()

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            if 0 <= ni <= N-1 and \
                0 <= nj <= M-1 and \
                (not visited[ni][nj]) and \
                (graph[ni][nj] == 1):

                q.append((ni, nj))
                visited[ni][nj] = True
                dist[ni][nj] = dist[i][j] + 1


my_bfs(0, 0)

print(dist[N - 1][M - 1])

### 동영상 속에서 주어진 답 ###

# from collections import deque

# n, m = map(int, input().split())
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def sol_bfs(x, y):
#     queue = deque()
#     queue.append((x, y))

#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if nx < 0 or nx >= n or ny < 0 or ny >= m:
#                 continue
#             if graph[nx][ny] == 0:
#                 continue

#             # 해당 노드를 처음 방문하는 경우에만 최단 거리를 기록한다.
#             if graph[nx][ny] == 1:
#                 graph[nx][ny] = graph[x][y] + 1
#                 queue.append((nx, ny))

#     return graph[n - 1][m - 1]

# print(sol_bfs(0, 0))
