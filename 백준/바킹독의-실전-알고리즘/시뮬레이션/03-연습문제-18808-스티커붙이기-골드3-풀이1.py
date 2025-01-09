"""
푸는데 58분 20초 걸렸음.

< 실수한 부분 정리 >

1. 스티커 제대로 입력받았는 지 출력할 때 게임판 배열을 출력해서 혼동함.
2. 스티커를 붙이는 "attach" 함수에서 nc 값을 계산할 때 c + j를 해야하는데, c + i를 하는 오타를 쳐서 버그가 발생함.
3. 스티커를 붙일 수 있는 지 검사하고 붙이는 부분에서, 
    붙였으면 회전을 안 시켜야하는데 붙여도 회전시킨 뒤 검사하는 부분이 있어서 버그가 발생함. 
    break로 탈출해서 해결함.

"""






import sys
from typing import Union


input = sys.stdin.readline

n, m, k = map(int, input().split())

board = [[0] * m for _ in range(n)]
stickers = []

for _ in range(k):
    r, c = map(int, input().split())
    mat = list()
    for _ in range(r):
        mat.append(list(map(int, input().split())))
    
    stickers.append(mat)


def rotate_sticker(sticker: list[list[int]]) -> list[list[int]]:
    # CW로 90도 회전
    return [list(reversed(it)) for it in zip(*sticker)]
    

def is_attachable(sticker: list[list[int]]) -> Union[tuple[int, int], None]:
    def check_r_c(r: int, c: int) -> bool:
        if 0 <= r < n and 0 <= c < m:
            sticker_r_len = len(sticker)
            sticker_c_len = len(sticker[0])
            for i in range(sticker_r_len):
                for j in range(sticker_c_len):
                    nr = r + i
                    nc = c + j
                    if 0 <= nr < n and 0 <= nc < m:
                        if sticker[i][j] == 1 and board[nr][nc] != 0:  # 신규 스티커를 붙여야 하는데, 이미 스티커가 차지하고 있는 칸
                            return False
                    else:  # 보드판 이탈
                        return False
            return True
        else:  # 보드판 이탈
            return False

    for r in range(n):
        for c in range(m):
            if check_r_c(r, c):
                return (r, c)  # 여러 곳에 붙일 수 있다면? 되도록 위쪽, 그 다음으로는 되도록 왼쪽
            
    return None


def attach(r: int, c: int, sticker: list[list[int]]):
    sticker_r_len = len(sticker)
    sticker_c_len = len(sticker[0])
    for i in range(sticker_r_len):
        for j in range(sticker_c_len):
            nr = r + i
            nc = c + j
            if sticker[i][j] == 1:
                board[nr][nc] = sticker[i][j]
           
           
def count_attached() -> int:
    count = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                count += 1
    return count


def print_arr(arr: list[list[int]]):
    print()
    print("="*20)
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j], end=' ')
        print()
    print("="*20)


for sticker in stickers:
    temp = sticker
    
    
    for trial in range(4):
        coord = is_attachable(temp)
        if coord is not None:
            r, c = coord
            attach(r, c, temp)
            break
        else:
            if trial == 3:
                continue
            else: 
                temp = rotate_sticker(temp)
                

print(count_attached())