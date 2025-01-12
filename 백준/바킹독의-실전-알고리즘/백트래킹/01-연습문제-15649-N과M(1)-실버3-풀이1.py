"""
문제 푸는데 16분 31초 걸림. (문제 읽기 시작 ~ 백준 제출 후 "맞았습니다!!" 출력)


"""

import sys


input = sys.stdin.readline

n, m = map(int, input().split())


def choice(available: list[int], count: int) -> list[list[int]]:
    # 선택된 결과물들의 수열을 리턴한다.
    
    if len(available) == 0:
        return []
    
    if count >= m:
        return []
    
    cases = []
    for e in available:
        permutations = choice([elem for elem in available if elem != e], count + 1)
        if len(permutations) == 0:
            cases.append([e])
        else:
            for permutation in permutations:
                cases.append([e] + permutation)
    
    return cases
        

permutations = choice(range(1, n + 1), 0)

for permutation in permutations:
    print(" ".join(map(str, permutation)))


