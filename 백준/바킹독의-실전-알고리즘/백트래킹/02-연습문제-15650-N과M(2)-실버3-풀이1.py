import sys

input = sys.stdin.readline


n, m = map(int, input().split())



def choice(candidates: list[int], count: int) -> list[list[int]]:
    if len(candidates) == 0:
        return []
    
    if count >= m:
        return []
    
    result = []
    for i, candidate in enumerate(candidates):
        cases = choice(candidates[i+1:], count + 1)
        if len(cases) == 0:
            result.append([candidate])
        
        for case in cases:
            result.append([candidate] + case)
    
    
    return result


result = filter(lambda x: len(x) == m, choice(range(1, n + 1), 0))
for case in result:
    print(" ".join(map(str, case)))