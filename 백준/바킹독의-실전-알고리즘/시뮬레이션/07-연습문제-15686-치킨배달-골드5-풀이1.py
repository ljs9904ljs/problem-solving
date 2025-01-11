"""
푸는데 55분 35초 걸림.

<메모>
- "mn" 변수에 대한 max 값을 잘못 설정해서 제출 시 칼같이 실패했었다. 문제의 조건을 제대로 숙지하고 max값을 설정하는 것이 필요하다.


"""


import sys
from itertools import combinations


input = sys.stdin.readline

n, m = map(int, input().split())

mymap = []
temp_map = [[0] * n for _ in range(n)]

for _ in range(n):
    mymap.append(list(map(int, input().split())))


EMPTY = 0
HOUSE = 1
CHICK = 2

def find_houses(m: list[list[int]]) -> list[tuple[int, int]]:
    result = []
    for i in range(n):
        for j in range(n):
            if m[i][j] == HOUSE:
                result.append((i, j))
    return result


def find_chicks(m: list[list[int]]) -> list[tuple[int, int]]:
    result = []
    for i in range(n):
        for j in range(n):
            if m[i][j] == CHICK:
                result.append((i, j))
    return result


def new_temp_map(deads: list[tuple[int, int]]):
    for i in range(n):
        for j in range(n):
            if (i, j) in deads:
                temp_map[i][j] = EMPTY
            else:
                temp_map[i][j] = mymap[i][j]

def dist_house_and_chick(house: tuple[int, int], chick: tuple[int, int]) -> int:
    return abs(house[0] - chick[0]) + abs(house[1] - chick[1])


def calc_chick_dist(houses: list[int]) -> int:
    chicks = find_chicks(temp_map)
    
    dist = 0
    for house in houses:
        dist += min([dist_house_and_chick(house, c) for c in chicks])
    
    return dist


houses = find_houses(mymap)
chicks = find_chicks(mymap)

if len(chicks) == m:
    new_temp_map([])
    print(calc_chick_dist(houses))
else:
    mn = int(1e9)  # max 값을 잘못 설정해서 제출 시 칼같이 실패했었다. 문제의 조건을 유심히 고민하고 max를 똑바로 설정하자.
    
    # 전부 폐업시키면 사실 상 '치킨 거리'가 무한대가 되는 것이므로 전부 폐업은 제외하고 계산한다.
    for deads_len in range(len(chicks) - m, len(chicks)):
        for deads in combinations(chicks, deads_len):
            new_temp_map(deads)
            mn = min(mn, calc_chick_dist(houses))
        

    print(mn)