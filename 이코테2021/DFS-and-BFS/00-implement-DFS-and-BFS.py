"""
문제 및 강의 출처: https://youtu.be/7C9RgOcvkvo?si=3MYI12alOB_AJNKJ

DFS랑 BFS를 구현해보자.

bfs2_wrong은 이렇게 해도 되는지 내가 한 번 고민하고 구현해본 것이었는데, 문제가 될 수 있는 부분을 발견했고 왜 bfs1처럼 구현하는지 이해하는데 도움이 되었다.
visited는 실제로 방문했다는 의미보다 queue에 중복되게 삽입되는 것을 막는 역할이라고 이해하는 게 더 낫다.


"""


def dfs(graph, v, visited):

    ### Do the jobs that you want to process
    visited[v] = True
    print(f"vertex num : {v}")
    ### until this line.
    for vertex in graph[v]:
        if not visited[vertex]:
            dfs(graph, vertex, visited)


from collections import deque


def bfs1(graph, v, visited):

    q = deque()

    q.append(v)
    visited[v] = True

    while q:
        w = q.popleft()
        print(w, end=' ')
        # something to do

        for vertex in graph[w]:
            if not visited[vertex]:
                q.append(vertex)
                visited[vertex] = True


def bfs2_wrong(graph, start, visited):
    q = deque()
    q.append(start)

    while q:
        v = q.popleft()
        visited[v] = True
        print(v, end=' ')

        for w in graph[v]:
            # 이렇게 처리하면, queue에 한 번 집어넣었는데 아직 popleft되기 전에 중복되 서 다시 한 번 집어넣어질 수 있다. 따라서 집어넣으면서 visited를 True로 표시해야 중복 삽입을 막을 수 있다.
            if not visited[w]:
                q.append(w)


def bfs_right(graph, start, visited):
    q = deque()

    q.append(start)
    visited[start] = True

    while q:
        v = q.popleft()
        print(v, end=' ')
        # something to do with v

        for w in graph[v]:
            if not visited[w]:
                q.append(w)
                visited[w] = True


graph = [
    [],  # 0번은 사용하지 않음.
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9  # 1번 vertex ~ 8번 vertex, 0번은 사용하지 않음.

dfs(graph, 1, visited)
print("=======111=================")
visited = [False] * 9  # 1번 vertex ~ 8번 vertex, 0번은 사용하지 않음.
bfs_right(graph, 1, visited)
print("\n")
print("========================")
visited = [False] * 9  # 1번 vertex ~ 8번 vertex, 0번은 사용하지 않음.
bfs2_wrong(graph, 1, visited)
print("\n")
### 동영상 속에서 주어진 답 ###
