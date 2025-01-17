"""

푸는 데 걸린 시간: 48분 26초


혼자 힘으로 풀지 못했다.
알고리즘 분류를 보고 좌표 압축이라는 것을 알게 되었고, 그 좌표 압축이 무엇인지 찾아본 다음에야 풀 수 있었다.
문제에서 요구했던 것은 결국 하나의 우주 안에 있는 행성들의 증가, 유지, 감소라는 상대적인 개념들이다.
그렇기에 41, 10, 13 이러한 값들은 쓸모없고 각각의 값의 순서 번호가 중요하다.
41, 10, 13 -> 2, 0, 1 이라는 값으로 치환될 수 있는 것이다. 
그렇게 모든 우주를 상대적인 순서 번호로 치환한 뒤, 같은 것들의 개수를 세서 조합 경우의 수를 계산하면 문제의 답을 구할 수 있게 된다.

굳이 우주마다 itertools.combinations를 써서 압축된 좌표로 비교할 필요가 없다.
같은 tuple들의 개수를 알면 조합 가지 수를 세는 수식으로 간편하게 계산할 수 있다.

"""


from collections import defaultdict
from itertools import combinations
import sys
import math


input = sys.stdin.readline


m, n = map(int, input().split())
mags = []

for _ in range(m):
    mags.append(list(map(int, input().split())))


def comb(n: int) -> int:
    return int(n * (n - 1) / 2)


# 좌표 압축
new_mags = []
for mag in mags:
    
    cache = dict()
    for i, val in enumerate(sorted(mag)):
        if val not in cache:
            cache[val] = i
    
    new_mag = tuple([cache[val] for val in mag])
    new_mags.append(new_mag)
    

d = defaultdict(int)

for mag in new_mags:
    d[mag] += 1


result = 0
for val in [val for val in d.values() if val >= 2]:
    result += comb(val)

print(result)

    
        
        
    