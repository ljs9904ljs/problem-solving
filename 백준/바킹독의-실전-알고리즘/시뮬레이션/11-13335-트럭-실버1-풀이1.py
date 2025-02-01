
"""

문제 푸는 데 걸린 시간: 49분 58초


note)
맨 처음에는 최대 부하 L 이하의 subarray로 묶어서 다리를 건너게 하면 될 것이라고 생각했으나 틀림.

아래와 같은 모양대로 차량이 다리에 올라 탈 수 있기 때문에 단순히 묶음을 만든다는 발상은 적용될 수 없음.
8 |7 1 0 0 0 0 0 0 0 1| 6 5

위의 생각을 질문 게시판의 랜덤 예제를 돌려보다가 깨닫게 되어서 풀이를 아예 수정함.

한 tick 당 차량을 최대한 다리 위에 올려 태우는 방식으로 시뮬레이션함.
    즉, 한 tick 당 동작을 규정하고 모든 차량을 다 건너편으로 보낼 때까지 tick을 흐르게 한 것임.

"""


import sys


input = sys.stdin.readline


n, w, l = map(int, input().split())
arr = list(map(int, input().split()))

bridge_len = w
max_load = l
time = 0


track = [0] * bridge_len
while len(track) > 0 or len(arr) > 0:
    if len(arr) > 0:
        load = arr.pop(0)
        track.pop(0)
        if sum(track) + load <= max_load:
            track.append(load)
        else:
            track.append(0)
            arr = [load] + arr
    else:
        track.pop(0)
    time += 1

print(time)
