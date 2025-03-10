"""

문제 푸는 데 걸린 시간: 28분 8초



"""



import sys
from collections import deque


input = sys.stdin.readline

# 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


m, n = map(int, input().split())

arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))
    

startings = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            startings.append((i, j) )


def bfs():
    q = deque()
    visited = [[False] * m for _ in range(n)]
    
    for r, c in startings:
        visited[r][c] = True
        q.append((r, c, 0) )
    
    last_days = 0
    
    while q:
        
        r, c, days = q.popleft()
        last_days = days
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and arr[nr][nc] == 0:
                arr[nr][nc] = 1
                visited[nr][nc] = True
                q.append((nr, nc, days + 1) )
                
        
    
    return last_days



def main():
    result = bfs()
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                print(-1)
                return
    
    print(result)


main()