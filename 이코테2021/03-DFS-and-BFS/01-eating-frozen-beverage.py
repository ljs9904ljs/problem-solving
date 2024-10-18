"""
문제 및 강의 출처: https://youtu.be/7C9RgOcvkvo?si=3MYI12alOB_AJNKJ

유형: DFS & BFS
제목: 음료수 얼려 먹기


<문제>
- N x M 크기의 얼음 틀이 있다. 구멍이 뚫린 부분은 0, 칸막이가 있는 부분은 1로 표시된다. 구멍 뚫려 있는 부분이 상|하|좌|우로 붙어 있다면 서로 연결되어 있는 것으로 간주한다. 이렇게 얼음 틀의 모양이 주어질 때 생성되는 총 아이스크림의 개수를 구해라.

- 입력; 첫 번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어진다. (1 <= N, M <= 1000). 두 번째 줄부터 N + 1 번째 줄까지 얼음 틀의 형태가 주어진다. 구멍 뚫려 있는 부분은 0이고 아닌 부분은 1이다.

- 출력; 한 번에 만들 수 있는 아이스크림의 개수를 출력한다.

<나의 답안 해석>
- connected component의 개수를 구하는 문제이다. BFS나 DFS는 모두 connected component를 체크하는 데 사용할 수 있다.

"""

# 좌 우 상 하
# dc = [-1, 1, 0, 0]
# dr = [0, 0, -1, 1]

# def dfs(graph, start, visited):

#     i, j = start
#     if graph[i][j] == 1 or visited[i][j]:
#         return

#     visited[i][j] = True
#     # nothing to do. just check every visiting
#     print(i, j)

#     for k in range(4):
#         nr = i + dr[k]
#         nc = j + dc[k]
#         if 0 <= nc <= M-1 and \
#             0 <= nr <= N-1 and \
#             (not visited[nr][nc]) and \
#             (graph[nr][nc] == 0):
#             dfs(graph, (nr, nc), visited)

# N, M = map(int, input().split())
# arr = [[0] * M for _ in range(N)]
# visited = [[False] * M for _ in range(N)]

# for i in range(N):
#     input_data = input()
#     for j in range(M):
#         arr[i][j] = int(input_data[j])

# print(arr)

# cc = 0  # the number of connected components
# for i in range(N):
#     for j in range(M):
#         if (arr[i][j] == 0) and (not visited[i][j]):
#             cc += 1
#             dfs(arr, (i, j), visited)

# print(cc)
# print("END!!!!")

### 동영상 속에서 주어진 답 ###

# dfs

# input 입력받기
n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))  # 한 줄에 공백이 없는 숫자들이 나열되어 있으므로.


def sol_dfs(x, y):

    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        sol_dfs(x - 1, y)
        sol_dfs(x + 1, y)
        sol_dfs(x, y - 1)
        sol_dfs(x, y + 1)
        return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        if sol_dfs(i, j):
            result += 1

print(result)
