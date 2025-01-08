import sys
from itertools import product

input = sys.stdin.readline

n, m = map(int, input().split())

office = [[0] * m for _ in range(n)]

for i in range(n):
    office[i] = list(map(int, input().split()))



directions = [0, 1, 2, 3]  # 90도 씩 회전할 수 있으므로 4가지 경우가 존재한다.


def printOffice(o: list[list[int]]):
    for i in range(n):
        for j in range(m):
            print(o[i][j], end=' ')
        print()


def copy_office() -> list[list[int]]:
    new_office = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            new_office[i][j] = office[i][j]
    
    return new_office


def find_cctvs() -> list[tuple[int, int, int]]:
    # list of (row, col, CCTV type)
    result = []
    for i in range(n):
        for j in range(m):
            if 1 <= office[i][j] <= 5:
                result.append( (i, j, office[i][j]) )
    return result


def is_wall(r: int, c: int) -> bool:
    return office[r][c] == 6


def process_right(o: list[list[int]], start_row: int, start_col: int):
    # 3시
    c = start_col
    while (0 <= c < m and not is_wall(start_row, c)):
        o[start_row][c] = "#"
        c += 1
    
    
def process_left(o: list[list[int]], start_row: int, start_col: int):
    # 9시
    c = start_col
    while (0 <= c < m and not is_wall(start_row, c)):
        o[start_row][c] = "#"
        c -= 1


def process_up(o: list[list[int]], start_row: int, start_col: int):
    # 12시
    r = start_row
    while (0 <= r < n and not is_wall(r, start_col)):
        o[r][start_col] = "#"
        r -= 1


def process_down(o: list[list[int]], start_row: int, start_col: int):
    # 6시
    r = start_row
    while (0 <= r < n and not is_wall(r, start_col)):
        o[r][start_col] = "#"
        r += 1


def count_type_1(o: list[list[int]], cctv: tuple[int, int, int], d: int):
    # type 1인 CCTV의 r, c 좌표를 입력받아서 d 방향으로 시뮬레이션 된 new_office를 리턴한다.
    
    if d not in [0, 1, 2, 3]:
        raise Exception("unreachable @@@@@@@@@@@@@@@@@@@@@@@@")
    
    row, col, type = cctv
    
    if d == 0:
        process_right(o, row, col)
    elif d == 1:
        process_down(o, row, col)
    elif d == 2:
        process_left(o, row, col)
    else:
        process_up(o, row, col)
    


def count_type_2(o: list[list[int]], cctv: tuple[int, int, int], d: int):
    if d not in [0, 1]:
        raise Exception("unreachable @@@@@@@@@@@@@@@@@@@@@@@@")
    
    row, col, type = cctv
    
    if d == 0:
        # 좌우
        process_left(o, row, col)
        process_right(o, row, col)
    else:
        # 상하
        process_up(o, row, col)
        process_down(o, row, col)


def count_type_3(o: list[list[int]], cctv: tuple[int, int, int], d: int):
    if d not in [0, 1, 2, 3]:
        raise Exception("unreachable @@@@@@@@@@@@@@@@@@@@@@@@")
    
    row, col, type = cctv
    
    if d == 0:
        # 12시, 3시
        process_up(o, row, col)
        process_right(o, row, col)
    elif d == 1:
        # 3시, 6시
        process_right(o, row, col)
        process_down(o, row, col)
    elif d == 2:
        # 6시, 9시
        process_down(o, row, col)
        process_left(o, row, col)
    else:
        # 9시, 12시
        process_left(o, row, col)
        process_up(o, row, col)


def count_type_4(o: list[list[int]], cctv: tuple[int, int, int], d: int):
    if d not in [0, 1, 2, 3]:
        raise Exception("unreachable @@@@@@@@@@@@@@@@@@@@@@@@")
    
    row, col, type = cctv
    
    if d == 0:
        process_up(o, row, col)
        process_left(o, row, col)
        process_right(o, row, col)
    elif d == 1:
        process_up(o, row, col)
        process_right(o, row, col)
        process_down(o, row, col)
    elif d == 2:
        process_left(o, row, col)
        process_right(o, row, col)
        process_down(o, row, col)
    else:
        process_up(o, row, col)
        process_left(o, row, col)
        process_down(o, row, col)


def count_type_5(o: list[list[int]], cctv: tuple[int, int, int], d: int):
    if d not in [0]:
        raise Exception("unreachable @@@@@@@@@@@@@@@@@@@@@@@@")
    
    row, col, type = cctv
    
    process_up(o, row, col)
    process_left(o, row, col)
    process_right(o, row, col)
    process_down(o, row, col)


def count_no_cctv_zones(o: list[list[int]]) -> int:
    count = 0
    for i in range(n):
        for j in range(m):
            if o[i][j] != 6 and o[i][j] != "#":
                count += 1
    return count


def process() -> int:
    cctvs = find_cctvs()
    
    types = [cctv[2] for cctv in cctvs]
    selections = []
    
    for t in types:
        if t == 1:
            selections.append([0,1,2,3])
        elif t == 2:
            selections.append([0,1])
        elif t == 3:
            selections.append([0,1,2,3])
        elif t == 4:
            selections.append([0,1,2,3])
        else:
            selections.append([0])
    
    min_no_cctv_zones = n * m
    
    for directions in product(*selections):
        
        new_office = copy_office()
        for d, cctv in zip(directions, cctvs):
            if cctv[2] == 1:
                count_type_1(new_office, cctv, d)
            elif cctv[2] == 2:
                count_type_2(new_office, cctv, d)
            elif cctv[2] == 3:
                count_type_3(new_office, cctv, d)
            elif cctv[2] == 4:
                count_type_4(new_office, cctv, d)
            else:
                count_type_5(new_office, cctv, d)
                
        min_no_cctv_zones = min(min_no_cctv_zones, count_no_cctv_zones(new_office))
    
    return min_no_cctv_zones


print(process())

"""
다 푸는데 2시간 4분 정도 걸렸다.


"""