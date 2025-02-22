import sys

input = sys.stdin.readline


arr1 = list(map(int, input().strip()))
arr2 = list(map(int, input().strip()))
arr3 = list(map(int, input().strip()))
arr4 = list(map(int, input().strip()))

arr = [None]
arr.append(arr1)
arr.append(arr2)
arr.append(arr3)
arr.append(arr4)

rotation_num = int(input())

# (타겟 arr 톱니바퀴, 회전 방향)의 리스트
rotations = list()
for _ in range(rotation_num):
    target_arr_num, direction = map(int, input().split())
    rotations.append((target_arr_num, direction))
    
"""
톱니바퀴 한 개의 번호는 0 ~ 7 이라고 하자.

아래가 맞닿아있음을 고려해야 한다.

1번 톱니바퀴 2번째
2번 톱니바퀴 2번째와 6번째
3번 톱니바퀴 2번째와 6번째
4번 톱니바퀴 6번째
"""

def spin_arr(arr: list[int], direction):
    if direction == 1:
        last = arr.pop()
        arr[:] = [last] + arr
    else:
        first = arr.pop(0)
        arr[:] = arr + [first]


for rotation in rotations:
    # d == 1이면 시계 , -1이면 반시계 방향
    target_arr, d = rotation
    
    bundle = set()
    bundle.add(target_arr)
    leftcur = target_arr - 1
    rightcur = target_arr + 1
    cur = target_arr
    
    while leftcur >= 1:
        if arr[leftcur][2] != arr[cur][6]:
            bundle.add(leftcur)
            leftcur -= 1
            cur -= 1
        else:
            break
    
    cur = target_arr
    while rightcur <= 4:
        if arr[cur][2] != arr[rightcur][6]:
            bundle.add(rightcur)
            rightcur += 1
            cur += 1
        else:
            break
    
    bundle = list(bundle)
    
    # print(bundle)
    cur_direction = d
    cur_target_arr = target_arr
    
    
    for target in bundle:
        if target == target_arr:
            spin_arr(arr[target_arr], d)
        else:
            if abs(bundle.index(target) - bundle.index(target_arr)) % 2 == 0:
                spin_arr(arr[target], d)
            else:
                spin_arr(arr[target], -d)
        

arr.pop(0)  # dummy data를 제거한다.
score = 0
for i, topni in enumerate(arr):
    if topni[0] == 1:
        score += (2 ** i)

print(score)
        
    
