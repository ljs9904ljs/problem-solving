"""

문제 푸는 데 걸린 시간: 9분 32초

note)
parametric search 문제였다.


"""



import sys


input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))
total = int(input())  # 총 예산


def check(limit: int) -> bool:
    cur_budget = sum([min(num, limit) for num in arr])
    return cur_budget <= total


if sum(arr) <= total:
    print(max(arr))
else:
    l = 0
    r = total

    ans = None
    while l <= r:
        mid = (l + r) // 2
        
        if check(mid):
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
            

    print(ans)

        