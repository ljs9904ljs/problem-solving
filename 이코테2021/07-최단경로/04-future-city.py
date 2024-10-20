"""
출처: https://youtu.be/acqm9mM1P6o?si=2Jl-Bmclheg_FlnP

유형: 최단경로
제목: 미래 도시


<문제>
    미래 도시에는 1번부터 N번까지의 회사가 있는데 특정 회사끼리는 서로 도로를 통해 연결되어 있다. 방문 판매
    원 A는 현재 1번 회사에 위치해 있으며, X번 회사에 방문해 물건을 판매하고자 한다.
    미래 도시에서 특정 회사에 도착하기 위한 방법은 회사끼리 연결되어 있는 도로를 이용하는 방법이 유일하다. 
    
    또한 연결된 2개의 회사는 양방향으로 이동할 수 있다. 
    
    공중 미래 도시에서 특정 회사와 다른 회사가 도로로 연결되어 있다면, 정확히 1만큼의 시간으로 이동할 수 있다.
    
    또한 오늘 방문 판매원 A는 기대하던 소개팅에도 참석하고자 한다. 소개팅의 상대는 K번 회사에 존재한다. 방문
    판매원 A는 X번 회사에 가서 물건을 판매하기 전에 먼저 소개팅 상대의 회사에 찾아가서 함께 커피를 마실 예정
    이다. 
    
    따라서 "방문 판매원 A는 1번 회사에서 출발하여 K번 회사를 방문한 뒤에 X번 회사로 가는 것"이 목표다.
    
    이때 방문 판매원 A는 가능한 한 빠르게 이동하고자 한다.
    방문 판매원이 회사 사이를 이동하게 되는 최소 시간을 계산하는 프로그램을 작성하시오.


- 입력;
    • 첫째 줄에 전체 회사의 개수 N과 경로의 개수 M이 공백으로 구분되어 차례대로 주어진다.
    (1 ≤ N, M ≤ 100)

    • 둘째 줄부터 M + 1번째 줄에는 연결된 두 회사의 번호가 공백으로 구분되어 주어진다.
    • M +2번째 줄에는 X와 K가 공백으로 구분되어 차례대로 주어진다. (1 ≤ K ≤ 100)

- 출력;
    • 첫째 줄에 방문 판매원 A가 K번 회사를 거쳐 X번 회사로 가는 최소 이동 시간을 출력한다.
    • 만약 X번 회사에 도달할 수 없다면 -1을 출력한다.


- 입력 예시;
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5

- 출력 예시;
3


<나의 답안 해석>
undirected graph이다.
edge weight가 전부 1이다. BFS로 최단 거리를 계산할 수 있다.
BFS를 이용하여 node 1부터 node K까지의 최단 거리를 구하고 node K부터 node X까지의 최단 거리를 구해서 둘을 합하면 된다.

<메모>


"""

from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for i in range(M):
    src, dst = map(int, input().split())
    graph[src].append( (dst, 1) )
    graph[dst].append( (src, 1) )

X, K = map(int, input().split())


def bfs(start: int) -> list[int]:
    dist = [0] * (N + 1)
    visited = [False] * (N + 1)
    
    q = deque()
    q.append(start)
    visited[start] = True
    
    while q:
        i = q.popleft()
        
        for j, _ in graph[i]:
            if not visited[j]:
                dist[j] = dist[i] + 1
                
                q.append(j)
                visited[j] = True
    
    return dist


if all(map(lambda e: e[0] != X, graph[1])):
    print(-1)
else:
    dist1 = bfs(1)
    dist2 = bfs(K)

    print(dist1[K] + dist2[X])


### 동영상 속에서 주어진 답 ##

# Floyd-Warshall Algorithm을 사용하였다. 그런데 edge weight가 전부 1인데 굳이 이렇게 해야 하나싶다.

# INF = int(1e9)

# n, m = map(int, input().split())
# graph = [[INF] * (n + 1) for _ in range(n + 1)]

# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i == j:
#             graph[i][j] = 0

# for _ in range(m):
#     src, dst = map(int, input().split())
#     graph[src][dst] = 1
#     graph[dst][src] = 1
    
# x, k = map(int, input().split())
    
# for k in range(1, n + 1):
#     for i in range(1, n + 1):
#         for j in range(1, n + 1):
#             graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
            
# result = graph[1][k] + graph[k][x]

# if result >= INF:
#     print(-1)
# else:
#     print(result)