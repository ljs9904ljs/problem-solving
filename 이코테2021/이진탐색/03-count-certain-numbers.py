"""
출처: https://youtu.be/94RC-DsGMLo?si=2kzpSfgoqKafiaaz

유형: 이진탐색
제목: 정렬된 배열에서 특정 수의 개수 구하기


<문제>
N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있습니다. 이 때 이 수열에서 x가 등장하는 횟수를 계산하세요.
예를 들어 수열 {1,1,2,2,2,2,3}이 있을 때 x = 2라면, 현재 수열에서 값이 2인 원소가 4개이므로 4를 출력합니다.

단, 이 문제는 O(logN)으로 알고리즘을 설계해야 한다.

- 입력;
    - 첫째 줄에 N과 x가 정수 형태로 공백으로 구분되어 입력됩니다.
        - (1 <= N <= 1,000,000, -10^9 <= x 10^9)
    - 둘째 줄에 N개의 원소가 정수 형태로 공백으로 구분되어 입력됩니다.
        - (-10^9 <= 각 원소의 값 <= 10^9)

- 출력;
    - 수열의 원소 중에서 값이 x인 원소의 개수를 출력합니다. 
        단, 값이 x인 원소가 하나도 없다면 -1을 출력합니다.

- 입력 예시;
7 2
1 1 2 2 2 2 3

- 출력 예시;
4


<나의 답안 해석>




"""
from bisect import bisect_left, bisect_right


def count_by_range_1(arr: list[int], lo: int, hi: int) -> int:
    """
        @param arr: a list sorted in ascending order
        @param lo: inclusive
        @param hi: inclusive
    """
    return bisect_right(arr, hi) - bisect_left(arr, lo)


def count_by_range_2(arr: list[int], lo: int, hi: int) -> int:
    """
        @param arr: a list sorted in ascending order
        @param lo: inclusive
        @param hi: inclusive
    """
    
    # find the index right before the first 'x' appears
    # It's another kind of 'bisect_left'
    l = 0
    r = len(arr) - 1
    left_idx_of_x = -1
    while l <= r:
        mid = (l + r) // 2
        
        if arr[mid] < lo:
            left_idx_of_x = mid
            l = mid + 1
        else:
            r = mid - 1
    
    left_idx_of_x += 1
    
    # find the index right after the last 'x' appears
    # It's another kind of 'bisect_right'
    l = 0
    r = len(arr) - 1
    right_idx_of_x = len(arr)
    while l <= r:
        mid = (l + r) // 2
        
        if arr[mid] > hi:
            right_idx_of_x = mid
            r = mid - 1
        else:
            l = mid + 1
            
    else:
        # print(f"right_of_x: ({right_idx_of_x}), left_of_x: ({left_idx_of_x})")
        return right_idx_of_x - left_idx_of_x


N, x = map(int, input().split())
numbers = list(map(int, input().split()))

result = count_by_range_2(numbers, x, x)

print(-1 if result == 0 else result)




### 동영상 속에서 주어진 답 ##








