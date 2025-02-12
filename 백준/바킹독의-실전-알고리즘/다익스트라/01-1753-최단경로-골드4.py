"""

문제 푸는 데 걸린 시간: 27분 3초

"""

import sys
import heapq


input = sys.stdin.readline

MAX = int(1e9)

v, e = map(int, input().split())
start = int(input())

g =  [list() for _ in range(v + 5)]
parents = [None] * (v + 5)
dist = [MAX] * (v + 5)

for _ in range(e):
    u1, v1, w = map(int, input().split())
    
    g[u1].append((v1, w))


def dijkstra(src):
    
    q = []
    heapq.heappush(q, (0, src))
    parents[src] = None
    dist[src] = 0
    
    while q:
        w, uu = heapq.heappop(q)
        
        for vv, weight in g[uu]:
            
            if dist[uu] + weight < dist[vv]:
                dist[vv] = dist[uu] + weight
                parents[vv] = uu
                heapq.heappush(q, (dist[vv], vv))
    
    

dijkstra(start)

for i in range(1, v + 1):
    if dist[i] == MAX:
        print("INF")
    else:
        print(dist[i])

