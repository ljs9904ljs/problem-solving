import heapq

INF = int(1e9)
N = 5



def dijkstra(graph, start):
    dist = [INF] * N
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    
    while q:
        _, i = heapq.heappop(q)
        print(f"방문한 노드 번호 : ({i})")
        
        if dist[i] < _:
            continue
        
        for j, weight in graph[i]:
            if dist[j] > dist[i] + weight:
                dist[j] = dist[i] + weight
                heapq.heappush(q, (dist[i], j))
    
    return dist
                

def main():
    
    graph = [[] for _ in range(5)]
    
    
    graph[0].append((1, 7))  # 0번 노드에서 1번 노드까지 weight가 7이다.
    graph[1].append((0, 7))
    
    graph[0].append((4, 1))
    graph[4].append((0, 1))
    
    graph[1].append((4, 8))
    graph[4].append((1, 8))
    
    graph[1].append((2, 3))
    graph[2].append((1, 3))
    
    graph[2].append((3, 6))
    graph[3].append((2, 6))
    
    graph[2].append((4, 2))
    graph[4].append((2, 2))
    
    graph[3].append((4, 7))
    graph[4].append((3, 7))
    
    
    dist = dijkstra(graph, 0)
    print(dist)
    
main()