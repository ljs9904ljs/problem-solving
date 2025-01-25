"""

문제 푸는 데 걸린 시간: 20분 36초

Connected Component의 개수를 세는 문제였다.
타겟(배추)의 좌표 리스트를 들고 있었기에 편하게 풀 수 있었다.
다음에 비슷한 문제가 배열의 형태로 input을 주면 타겟(배추 등)의 좌표만 따로 추려서 BFS를 반복시키는 것도 좋은 방법일 것 같다.

"""


import sys


input = sys.stdin.readline


t = int(input())



    
    


for _ in range(t):
    m, n, k = map(int, input().split())
    positions = [list(map(int, input().split())) for _ in range(k)]
    positions = [(n - 1 - pos[1], pos[0]) for pos in positions]
    arr = [[0] * m for _ in range(n)]
    for r, c in positions:
        arr[r][c] = 1
    
    visited = [[False] * m for _ in range(n)]
    
    
    def bfs(board: list[list[int]], src_r: int, src_c: int):
        
        q = list()
        q.append((src_r, src_c))
        visited[src_r][src_c] = True
        
        # 상 하 좌 우
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        
        
        while len(q) > 0:
            r, c = q.pop(0)
            
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                
                if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and board[nr][nc] == 1:
                    visited[nr][nc] = True
                    q.append((nr, nc))
                    
    cnt = 0
    for r, c in positions:
        if not visited[r][c]:
            bfs(arr, r, c)
            cnt += 1
        
    print(cnt)
    
    


