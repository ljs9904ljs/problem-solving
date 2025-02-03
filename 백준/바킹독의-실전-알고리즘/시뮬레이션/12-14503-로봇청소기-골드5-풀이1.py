"""

문제 푸는 데 걸린 시간: 1시간 11분 33초



note)

문제에서 "반시계" 방향으로 회전한다고 제시해줬는데 나는 "시계" 방향으로 회전시켰었다...

( 현재 방향 값 + i ) % 4 로 회전시켰었는데, i를 1,2,3,4로 주면 시계 방향 90도 회전이었다.
    그러고 수정한 게 i + 2 하는 거였는데 이렇게 하면 여전히 시계 방향인 것인데 착각했다.
    그래서 최종적으로 수정한 게 i를 3,2,1,0 으로 주는 것이었다. 이렇게 하면 "반시계" 방향 90도 회전으로 검사하는 게 된다.


"""




import sys
from collections import deque


input = sys.stdin.readline


n, m = map(int, input().split())

# d에 대해
# 북 동 남 서
# 0  1  2  3
r, c, d = map(int, input().split())

# 0은 청소해야될 곳, 1은 벽, 2는 청소를 완료한 곳
room = [list(map(int, input().split())) for _ in range(n)]



# 북 동 남 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

clean_cnt = 0

def bfs(src_r: int, src_c: int, direction: int):
    global clean_cnt

    q = deque()

    q.append((src_r, src_c, direction))

    while len(q) > 0:
        r, c, dd = q.popleft()

        if room[r][c] == 0:
            room[r][c] = 2
            clean_cnt += 1
        
        no_dirty = True
        for i in range(1,5):
            nd = (dd + i) % 4
            nr = r + dr[nd]
            nc = c + dc[nd]
            
            if 0 <= nr < n and 0 <= nc < m and room[nr][nc] == 0:
                no_dirty = False
                break
        
        if no_dirty:
            nr = r - dr[dd]
            nc = c - dc[dd]
            if 0 <= nr < n and 0 <= nc < m and room[nr][nc] != 1:
                q.append((nr, nc, dd))
                continue
            else:
                break
        else:
            for i in range(3, -1, -1):
                nd = (dd + i) % 4
                nr = r + dr[nd]
                nc = c + dc[nd]

                if 0 <= nr < n and 0 <= nc < m and room[nr][nc] == 0:
                    
                    # 한 번에 한 방향으로만 쭉 청소해나가게끔 하기 위해서 하나 추가하면 바로 break했다.
                    q.append((nr, nc, nd))
                    break
        
                

bfs(r, c, d)

print(clean_cnt)

    




