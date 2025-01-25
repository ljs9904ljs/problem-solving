"""

혼자서 못 풀어서 다른 사람 풀이를 보고 재구성하는데 2시간 정도 걸렸다.

채점 환경에 따라 실행 속도 차이로 정답/오답 갈리는 경우가 있는 것 같다.
pypy3로 통과하는 코드가 python3에서는 실패한다.
c++에서 통과하는 로직을 그대로 python3로 구현하였더니 시간 초과로 실패한다.

값이 겹치는 경우를 고민해볼 수 있는 문제이다.
아래 작성한 코드처럼 풀면 O(N^2 * log N) 이기 때문에 문제가 발생하는 것 같은데
O(N^2)짜리 풀이가 있더라.
A_i의 범위가 -1만 이상 ~ 1만이하 라는 것에서 착안한, 배열에 메모해두는 방식의 풀이가 있다.

"""


import sys
from bisect import bisect_left, bisect_right


input = sys.stdin.readline



n = int(input())
arr = list(map(int, input().split()))
# n = 10
# arr = list(map(int,"2 -5 2 3 -4 7 -4 0 1 -6".split()))
#arr = [-6, -5, -4, -4, 0, 1, 2, 2, 3, 3, 3, 7]

arr.sort()


cnt = 0

for i in range(n - 2):
    l = i + 1
    r = n - 1

    while l < r:
        v = arr[i] + arr[l] + arr[r]

        if v == 0:
            if arr[l] == arr[r]:
                cnt += r - l
            else:
                cnt += r - bisect_left(arr, arr[r], lo=l) + 1
            l += 1
        elif v < 0:
            l += 1
        else:
            r -= 1



print(cnt)

