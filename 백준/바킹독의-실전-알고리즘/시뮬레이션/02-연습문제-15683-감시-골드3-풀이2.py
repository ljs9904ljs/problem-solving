"""
똑같은 백준-감시-골드3 문제를 유튜브에서 확인한 다른 사람의 풀이 방식대로 다시 풀어본다.

원래 나의 풀이에서는 각 CCTV 별 방향의 경우의 수를 고려할 때 
itertools.product (cartesian product를 생성해줌)을 사용했는데,
이 풀이에서는 K진법으로 표현해서 경우의 수를 따지는 방식을 사용했다.

- CCTV 각각이 4가지 방향이 될 수 있고, CCTV가 3개라면
    - 세 자리 4진법 수로 방향에 대한 모든 경우의 수를 나타낼 수 있다.
    - 10진수 수의 범위: [0, 4^3 - 1] 에 대해서 4진법으로 변환한다고 생각하면 된다.

또한 감시 가능한 영역을 한 방향(상 || 하 || 좌 || 우)으로 쭉 따라서 표시하는 기능을 4개 각각으로 작성하는 게 아니라,
하나의 함수로 할 수 있게 한다.

다시 푸는 데 37분 정도 걸렸다!
"""


import sys


input = sys.stdin.readline

n, m = map(int, input().split())
office = [[0] * m for _ in range(n)]

for i in range(n):
    office[i] = list(map(int, input().split()))

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
d_len = 4

def copy_office() -> list[list[int]]:
    new_office = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            new_office[i][j] = office[i][j]
    
    return new_office


def mark(o: list[list[int]], r: int, c: int, d: int):
    nd = d % d_len
    
    # 다른 CCTV가 있는 영역이 마크되든 말든 전혀 상관없다. 
    # 왜냐하면 cctv 좌표 목록을 따로 뽑아 두었기 때문이다.
    nr = r
    nc = c
    while 0 <= nr < n and 0 <= nc < m and o[nr][nc] != 6:
        o[nr][nc] = 7
        
        nr += dr[nd]
        nc += dc[nd]


def find_cctvs() -> list[tuple[int, int, int]]:
    cctvs = []
    for i in range(n):
        for j in range(m):
            if 1 <= office[i][j] <= 5:
                cctvs.append((i, j, office[i][j]))
    return cctvs


def count_no_cctv_zones(o: list[list[int]]) -> int:
    cnt = 0
    for i in range(n):
        for j in range(m):
            if o[i][j] == 0:
                cnt += 1
    return cnt    


cctvs = find_cctvs()
min_count = n * m

for case in range(4**len(cctvs)):
    
    o = copy_office()
    
    for i in range(len(cctvs)):
        direction = case % 4
        case //= 4  # 이거 이렇게 해도 iteration 제대로 잘 된다.
        
        r, c, t = cctvs[i]
        if t == 1:
            mark(o, r, c, direction)
        elif t == 2:
            mark(o, r, c, direction)
            mark(o, r, c, direction + 2)
        elif t == 3:
            mark(o, r, c, direction)
            mark(o, r, c, direction + 1)
        elif t == 4:
            mark(o, r, c, direction)
            mark(o, r, c, direction + 1)
            mark(o, r, c, direction + 2)
        else:
            mark(o, r, c, direction)
            mark(o, r, c, direction + 1)
            mark(o, r, c, direction + 2)
            mark(o, r, c, direction + 3)
    
    min_count = min(min_count, count_no_cctv_zones(o))

print(min_count)