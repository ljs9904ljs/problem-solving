"""
문제 푸는데 11분 9초 걸림. (문제 읽기 시작 ~ 백준 제출 후 "맞았습니다!!" 출력)

마지막에 필터링해서 길이가 m인 것들만 추려내서 출력했는데, 이게 과연 옳은 방법일까?
필터링 없이 백트래킹할 때 길이가 딱 m인 것들만 모으는 방법이 없나..

- 문제를 풀고 나서 살펴보니,
    - 오름차순이라는 조건은 사실 조합을 구하라는 것을 나타내는 표현이었다.
        - 순열로 따지면 오른쪽과 같이 나오는 것들이 -> [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]
        - 조합으로 따지면 (오름차순 정렬을 하면 {내림차순 정렬도 마찬가지임.}) -> [1,2,3] 


"""


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