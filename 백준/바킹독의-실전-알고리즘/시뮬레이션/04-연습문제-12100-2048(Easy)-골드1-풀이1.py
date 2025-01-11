"""
푸는데 2시간 9분 걸렸다.

경우의 수마다 분기하기 전에 board를 원본으로 새롭게 deep copy해주는 것을 잊으면 안 된다.


<다른 풀이 공부한 후 메모>
- 문제에서 제시한 줄 글을 그대로 적용해서 풀기보다는, 풀기 쉬운 방식으로 수정해보는 시도가 필요하다.

- 이동을 한 방향으로만 할 수 있고, 게임판을 90도 씩 회전시키면서 검사하는 방식의 풀이가 있다.
- DFS를 이용한 백트래킹 방식의 풀이가 있다.

- 나는 실제로 게임판 원소를 살펴보며 새로운 게임판에 합쳐서 넣는 방식을 썼다.
    - 합쳐질 수 있다 or not 에 대한 bool을 두는 방식이 있네?

- '바킹독' 강의에서는 왼쪽으로 기울여서 합체시킨다는 발상을 제시했는데, 이게 문제를 이해하기 더 쉬웠다.

    


"""



import sys
from typing import Union

input = sys.stdin.readline

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

# 입력한 키보드 자판이
# [상, 하, 좌, 우] 인 경우
    # '상'을 입력하면 위에서부터 아래로 탐색을 하며 합체해야 한다.
dr = [1, -1 , 0, 0]
dc = [0, 0, 1, -1]

EMPTY_BLOCK = 0

def next(b: list[list[int]], r: int, c: int, d: int) -> Union[tuple[int, int], None]:
    nr = r
    nc = c
    while (0 <= nr < N and 0 <= nc < N) and b[nr][nc] == EMPTY_BLOCK:
        nr += dr[d]
        nc += dc[d]
        
    if not (0 <= nr < N and 0 <= nc < N):
        return None
    else:
        if b[nr][nc] == EMPTY_BLOCK:
            raise Exception("unreachable@@@@@@@@@@@@@")  # TODO: 체크하고 제거해야 할 라인이다.
        return (nr, nc)
    

def erase(b: list[list[int]], r: int, c: int):
    if (0 <= r < N) and (0 <= c < N):
        b[r][c] = 0
    

def play(b: list[list[int]], d: int) -> list[list[int]]:
    if d not in [0, 1, 2, 3]:
        raise Exception("unreachable!!!!!!!!!")
    
    new_board = [[0] * N for _ in range(N)]
    
    for i in range(N):
        if d == 0:
            # 상
            cur_r = 0
            cur_c = i
            
        elif d == 1:
            # 하
            cur_r = N - 1
            cur_c = i
            
        elif d == 2:
            # 좌
            cur_r = i
            cur_c = 0
            
        else:
            # 우
            cur_r = i
            cur_c = N - 1
                
        for j in range(N):
            if d == 0:
                # 상
                ni = j
                nj = i
                
            elif d == 1:
                # 하
                ni = N - 1 - j
                nj = i
                
            elif d == 2:
                # 좌
                ni = i
                nj = j
                
            else:
                # 우
                ni = i
                nj = N - 1 - j
            
            nxt = next(b, cur_r, cur_c, d)
            if nxt is not None:
                new_board[ni][nj] = b[nxt[0]][nxt[1]]
                erase(b, nxt[0], nxt[1])
                
                cur_r += dr[d]
                cur_c += dc[d]
                nxt2 = next(b, cur_r, cur_c, d)
                if nxt2 is not None:
                    if new_board[ni][nj] == b[nxt2[0]][nxt2[1]]:
                        new_board[ni][nj] *= 2
                        erase(b, nxt2[0], nxt2[1])
                        
                        cur_r += dr[d]
                        cur_c += dc[d]
                    else:
                        continue
                else:
                    break
            else:
                break
            
    return new_board


def find_max_block(b: list[list[int]]) -> int:
    return max([max(row) for row in b])


def copy_board(b: list[list[int]]) -> list[list[int]]:
    new_board = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_board[i][j] = b[i][j]
            
    return new_board



max_block = 0
for case in range(4 ** 5):
    """
    NOTE: 이 곳처럼 매 번 새롭게 진행되는 게임에 대해, 새롭게 보드판을 초기화해주는 것을 잊으면 안 된다.
            경우의 수를 나눠서 A 케이스 점수는? B 케이스 점수는? C 케이스 점수는? 하고 비교하는 것이기 때문에
            매 경우마다 새로운 판에서 게임하는 것이라고 보아야 한다.
            
            또한 배열을 복사할 때 그냥 play_board = board 라고 해버리면 shallow copy가 발생해서 의도한 방식대로 동작하지 않음.
            배열 원소 하나 하나를 정성껏 복사해줘야 한다.
    """
    play_board = copy_board(board)  
    for _ in range(5):
        direction = case % 4
        case = case // 4
        
        play_board = play(play_board, direction)
                
    max_block = max(max_block, find_max_block(play_board))
    
print(max_block)
        
        
