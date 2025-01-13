"""

풀이1에서 마지막에 리스트의 길이를 이용해서 필터링하는데 
필터링 없이 한 번에 길이가 M인 것들만 모으고 싶어서 ChatGPT를 이용해 다른 풀이를 알아냈다.

"""

import sys


input = sys.stdin.readline
n, m = map(int, input().split())


def backtracking(arr: list[int], count: int, path: list[int]) -> list[list[int]]:
    
    if count == m:
        return [path]
    
    if len(arr) == 0 or count > m:
        return []
    
    result = []
    for i, num in enumerate(arr):
        result.extend(backtracking(arr[i+1:], count + 1, path + [num]))
        
    return result


series = backtracking(range(1, n + 1), 0, [])

print(series)
        


