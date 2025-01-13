

import sys


input = sys.stdin.readline


n, m = map(int, input().split())


def backtracking(arr: list[int], count: int, path: list[int]) -> list[list[int]]:
    
    if count == m:
        return [path]
    
    if count > m or len(arr) == 0:
        return []
    
    result = []
    for num in arr:
        result.extend(backtracking(arr, count + 1, path + [num]))
        
    return result



for series in backtracking(range(1, n + 1), 0, []):
    print(" ".join(map(str, series)))
