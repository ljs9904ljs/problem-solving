"""

문제 푸는 데 걸린 시간: 3시간 55분 38초


문제 풀기 전 note)
홀수 이닝만 플레이하는 경우와 짝수 이닝만 플레이하는 경우로 나눠서 시뮬레이션해야 한다.

4번 타자로 지명된 선수를 제외한 나머지 8명의 선수 리스트의 permutation 값


문제 풀고 난 후 note)
비트마스킹을 써서 시도했는데도 통과하지 못했다는 질문게시판의 글을 보았다.
코드는 안 읽었으나 비트마스킹이라는 용어를 본 것 자체가 힌트가 되었다.

느렸던 코드(시간 초과 발생)에서는 주자 상태를 배열로 관리하며 1루타는 각 1칸 씩 옮기고, 2루타는 각 2칸 씩 옮기는 식으로 배열을 수정했다.
하지만 이런 방식은 너무 느렸고, 아예 각 주자 상태 당 1/2/3루타/홈런을 맞이한 경우에 옮겨갈 상태를 저장하는 식으로 수정했다.

그리고 함수 안에 함수를 정의하는 식으로 만들어서 썼었는데, 그 함수 호출을 죄다 제거하니까 훨씬 빨라졌다. 2초 대 후반 걸리던 게 0초 대 후반까지 떨어졌다. 
    --->>> 말 안 된다. 함수 호출이 이렇게 비효율적일 수가 있나? 아무리 permutations랑 N개만큼 해서, 총 200만 번 정도 실행한다지만 이게 이렇게 차이가 나네...

"""



import sys
from itertools import permutations
from time import time



input = sys.stdin.readline


n = int(input())
hits_list = []
for _ in range(n):
    hits_list.append(list(map(int, input().split())))

hitter_counter = 0

field_map = [[0] * 5 for _ in range(8)]
# field_map[주자 상황][hit 점수]

field_map = [
    [None, (1, 0), (2, 0), (4, 0), (0, 1)],
    [None, (3, 0), (6, 0), (4, 1), (0, 2)],
    [None, (5, 0), (2, 1), (4, 1), (0, 2)],
    [None, (7, 0), (6, 1), (4, 2), (0, 3)],
    [None, (1, 1), (2, 1), (4, 1), (0, 2)],
    [None, (3, 1), (6, 1), (4, 2), (0, 3)],
    [None, (5, 1), (2, 2), (4, 2), (0, 3)],
    [None, (7, 1), (6, 2), (4, 3), (0, 4)]
]

"""
        1루타       2루타       3루타       4루타(홈런)
000     001        010         100         000 + 1
001     011        110         100 + 1     000 + 2
010     101        010 + 1     100 + 1     000 + 2
011     111        110 + 1     100 + 2     000 + 3

100     001 + 1    010 + 1     100 + 1     000 + 2
101     011 + 1    110 + 1     100 + 2     000 + 3
110     101 + 1    010 + 2     100 + 2     000 + 3
111     111 + 1    110 + 2     100 + 3     000 + 4

"""

def play_one_round(hitters: list[int], hits: list[int]) -> int:
    field = 0
    out_count = 0
    this_round_score = 0
    
    def next_hitter() -> int:
        global hitter_counter
        hitter = hitters[hitter_counter % 9]
        hitter_counter += 1
        return hitter
    
    hitter = next_hitter()
    while True:
        
        if hits[hitter] == 0:
            out_count += 1
        else:
            f, s = field_map[field][hits[hitter]]
            field = f
            this_round_score += s
            
        
        if out_count >= 3:
            break
        hitter = next_hitter()
    
    return this_round_score


def play_rounds(hitters: list[int], hits_for_round: list[list[int]]) -> int:
    total_score = 0
    
    for hits in hits_for_round:
        total_score += play_one_round(hitters, hits)
    
    return total_score


# total_s = time()
candidates = [1,2,3,4,5,6,7,8]
mx = -1
acc = 0
for cur in permutations(candidates, 8):
    hitter_counter = 0
    c = list(cur)
    hitters = c[:3] + [0] + c[3:]

    s = play_rounds(hitters, hits_list)

    mx = max(mx, s)

    
# print("total time : ", time() - total_s)
    
print(mx)
    