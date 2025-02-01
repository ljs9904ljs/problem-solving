"""

문제 푸는 데 걸린 시간 (혼자 힘으로 못 품) : 1시간 22분 4초


note)
우선, 가로선의 양끝 좌표를 가지고 어떻게 하는 게 아니라 사다리 배열(가로선 유무 배열) 자체를 들고 다니면서 simulation해야 한다.
그 다음, 후보 가로선 리스트를 따로 만들어서 들고 다녀야 효율적으로 loop를 돌면서 가로선을 놓아보고 해제해 볼 수 있다. --> 이렇게 해야 3중 loop만으로 해결 가능.

그런데 의문인 것은 왜 가로선을 놓을 수 있는 지 아닌 지를 체크할 필요가 없는지 모르겠다. 분명 후보 가로선 리스트는 바로 따닥 따닥 붙어 있는 가로선들이 선택될 수 있는데 이게 백준 테스트 케이스를 통과하네?
    -> 물론 체크해도 백준 통과한다.


"""


import sys
import copy


input = sys.stdin.readline

n, m, h = map(int, input().split())

ladder = [[False] * (n + 5) for _ in range(h + 5)]
ladder_copy = [[False] * (n + 5) for _ in range(h + 5)]
for _ in range(m):
    a, b = map(int, input().split())
    
    ladder[a][b] = True  # 가로선이 놓였다.
    ladder_copy[a][b] = True

choices = []

for i in range(1, h + 1):
    for j in range(1, n):
        if ladder[i][j - 1] or ladder[i][j] or ladder[i][j + 1]:
            continue
        else:
            choices.append((i, j))  # 내가 가로선을 놓을 수 있는 좌표들만 모아둔다. 후보 가로선들의 리스트.


def reset_ladder():
    global ladder
    ladder = copy.deepcopy(ladder_copy)
    # for i in range(1, h + 1):
    #     for j in range(1, n):
    #         ladder[i][j] = ladder_copy[i][j]


def valid_coord(r: int, c: int) -> bool:
    return 1 <= r <= h and 1 <= c <= n - 1


def check(arr: list[list[int]], i: int) -> bool:
    c = i
    for r in range(1, h + 1):
        if arr[r][c - 1]:
            c = c - 1
        elif arr[r][c]:
            c = c + 1
        else:
            c = c
    
    return c == i


def check_all() -> bool:
    for i in range(1, n + 1):
        if not check(ladder, i):
            return False
    return True


def check_ladder_adding(ladder: list[list[int]], i: int, j: int):
    if ladder[i][j] == True:
        return False
    elif ladder[i][j - 1] == True:
        return False
    elif ladder[i][j + 1] == True:
        return False
    else:
        return True


if check_all():
    print(0)
else:
    ans = int(1e9)
    
    for p in range(len(choices)):
        x, y = choices[p]
        # if not check_ladder_adding(ladder, x, y):
        #     continue
        
        ladder[x][y] = True
        if check_all():
            ans = min(ans, 1)

        for q in range(p + 1, len(choices)):
            x2, y2 = choices[q]
            # if not check_ladder_adding(ladder, x2, y2):
            #     continue
            
            ladder[x2][y2] = True
            if check_all():
                ans = min(ans, 2)
            
            for r in range(q + 1, len(choices)):
                x3, y3 = choices[r]
                # if not check_ladder_adding(ladder, x3, y3):
                #     continue
                
                ladder[x3][y3] = True
                if check_all():
                    ans = min(ans, 3)
                ladder[x3][y3] = False
                
            ladder[x2][y2] = False
            
        ladder[x][y] = False
    
    
    if ans == int(1e9):
        print(-1)
    else:
        print(ans)
        
    
    







# arr = [[False] * 5 for _ in range(5)]

# arr[1][1] = True
# arr[2][1] = True
# arr[3][1] = False

# print(check(arr, 1))
