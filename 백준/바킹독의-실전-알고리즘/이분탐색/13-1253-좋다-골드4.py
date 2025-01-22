"""

문제 푸는 데 30분 정도 걸렸다.


어려웠던 점)
i번째 수를 (j번째 수 + 특정 수)로 만들 수 있는가? 를 체크했다.
그런데 이 때 "특정 수"의 인덱스가 i여도 안 되고 j여도 안 된다. 
    이것을 처리하는 게 까다로웠는데, "특정 수"의 인덱스가 i 혹은 j인 경우는 10 = 5 + 5 혹은 0 = 0 + 0 같이 중복되는 수가 들어가는 경우이다.
    즉, nums 배열 안에 중복된 수가 들어가 있는 경우인데, 이 때는 bisect right와 bisect left를 조합하여 중복된 값이 존재하는 인덱스의 범위를 찾고
    그 범위 안에서 하나라도 (GOOD 조건 && i 아님 && j 아님)을 충족하면 i번째 수를 만들 수 있다고 카운트했다.

"""


import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline


n = int(input())
nums = list(map(int, input().split()))

nums.sort()

cnt = 0
for i in range(n - 1, -1, -1):
    for j in range(n - 1, -1, -1):
        if i == j:
            continue
        
        target = nums[i] - nums[j]
        
        
        lidx = bisect_left(nums, target)
        ridx = bisect_right(nums, target)
        is_break = False
        for k in range(lidx, ridx):
            if 0 <= k < n and k != i and k != j and nums[k] == target:
                # print("찾음.", i)
                cnt += 1
                is_break = True
                break
        
        if is_break:
            break

print(cnt)     
