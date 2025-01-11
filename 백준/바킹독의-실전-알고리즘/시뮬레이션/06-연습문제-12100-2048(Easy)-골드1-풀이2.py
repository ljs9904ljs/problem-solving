"""
바킹독이 제시한 풀이대로 새롭게 풀어본다.

"""

import sys

input = sys.stdin.readline

N = int(input())
board1 = []
for _ in range(N):
    board1.append(list(map(int, input().split())))

board2 = [[0] * N for _ in range(N)]
    
    
def init_board2():
    for i in range(N):
        for j in range(N):
            board2[i][j] = board1[i][j]
    
    
def rotate():
    global board2
    board2 = [list(reversed(col)) for col in zip(*board2)]


def tilt(d: int):
    # 내가 필요한 값은 최종적으로 알게 될 max block의 값이기 때문에 돌려놓고 원복하지 않아도 된다.
    for _ in range(d):
        rotate()
        
    for r in range(N):
        tilted = [0] * N
        idx = 0  # 내가 지금 살펴보는 tilted 리스트의 칸 인덱스. 이 칸이 비어있나? 차있다면 -> 게임판 값이랑 같나 다르나?
        for i in range(N):
            
            """
            NOTE: 이 부분이 필요하다. 왜냐하면 나는 지금 idx가 가리키는 부분을 보드의 값과 충돌시키고 있는데,
            이 코드 라인이 없다면 보드 상에서 값이 없는 부분을 tilted의 블록과 충돌시키는 것이 되기 때문이다.
            이렇게 되면 사실 보드의 다음 블록이랑 충돌해서 합쳐질 수도 있는 건데 무조건 안 합친다로 가버리는 것과
            마찬가지이기 때문에 실행 결과가 달라질 수 있다.
            
            즉, 보드판 상에서 다음 값이 있는 블록을 찾아 바로 점프하기 위해 존재하는 코드 라인이라고 생각할 수도 있다.
            """
            if board2[r][i] == 0: continue
                
                
                
            if tilted[idx] == 0:
                # 해당 칸이 비어있는 경우
                tilted[idx] = board2[r][i]
            elif tilted[idx] == board2[r][i]:
                # 현재 칸 2배 해주기
                tilted[idx] *= 2
                idx += 1
            else:
                # 바로 다음 칸에 값 집어 넣기
                idx += 1
                tilted[idx] = board2[r][i]
    
        board2[r][:] = tilted


max_block = 0
for case in range(4 ** 5):
    init_board2()
    for _ in range(5):
        d = case % 4
        case //= 4
        tilt(d)
        
    max_block = max(max_block, max([max(r) for r in board2]))
    
print(max_block)
    