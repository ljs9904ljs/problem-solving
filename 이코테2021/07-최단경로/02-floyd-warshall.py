
import pandas as pd

INF = int(1e9)
N = 5

def floyd_warshall(graph):
    table = [[INF] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                table[i][j] = 0
                
    for i in range(len(graph)):
        for j, weight in graph[i]:
            table[i][j] = weight
        
    
    # 쉽게 생각하면, dp[i][j] = min (dp[i][j], dp[i][k] + dp[k][j])
        # 그런데 이렇게만 보면 k가 왜 제일 바깥에 있어야 하는지 이해하기 어렵다.
    # 보다 정확하게는, dist[i][j][k] = min { dist[i][j][k-1], dist[i][k][k-1] + dist[k][j][k-1]}
        # 이렇게 보면 k를 채우기 위해 k-1에 관한 i,j들이 미리 계산되어 있어야 한다는 것을 알 수 있다.
            # node를 1,2,3,...,K번이라고 번호를 매겨 놓고 하나씩 고려 대상에 추가하며 최단 거리를 다시 계산하는 것이다.
        # 이 때 k는 S_k := permissible intermediate nodes를 나타내며 1,2,3,...k번 node까지 고려한 것을 나타낸다.
        # 하지만 코드는 0,1,2,3, ... N-1번 node가 존재하는 것으로 간주하고 작성되었다.
    for k in range(N):  # K loop가 항상 가장 바깥에 있어야 함.
        for i in range(N):
            for j in range(N):
                table[i][j] = min(table[i][j], table[i][k] + table[k][j])
    
    return table
        
        
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
    
    
    table = floyd_warshall(graph)
    print(table)
    print(pd.DataFrame(table))
    
main()