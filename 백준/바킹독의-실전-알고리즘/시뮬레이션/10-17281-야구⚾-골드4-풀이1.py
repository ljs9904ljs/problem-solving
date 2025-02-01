"""




문제 풀기 전 note)
홀수 이닝만 플레이하는 경우와 짝수 이닝만 플레이하는 경우로 나눠서 시뮬레이션해야 한다.

4번 타자로 지명된 선수를 제외한 나머지 8명의 선수 리스트의 permutation 값


"""



import sys
from itertools import permutations
from time import time



input = sys.stdin.readline


n = int(input())
hits_list = []
for _ in range(n):
    hits_list.append(list(map(int, input().split())))


total_set_time = 0
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
    # field = [0, 0, 0]
    field = 0
    out_count = 0
    this_round_score = 0
    
    def next_hitter() -> int:
        global hitter_counter
        hitter = hitters[hitter_counter % 9]
        hitter_counter += 1
        return hitter
    
    
    def set_new_field_and_get_extra_score(hit: int) -> int:
        # new_field = [0, 0, 0]
        # len_field = len(field)
        
        def do(hit: int) -> int:
            nonlocal field
            
            f, s = field_map[field][hit]
            field = f
            return s
        
            # score = 0
            
            # # 홈런은 점수 추가하고 판 초기화
            # if hit == 4:
            #     score = sum(field) + 1
            #     field[:] = [0, 0, 0]
            #     return score
            
            # # 기존 주자들 진루
            # for i in range(len_field - 1, -1, -1):
            #     if field[i] == 1:
            #         if i + hit >= len_field:
            #             score += 1
            #             field[i] = 0
            #         else:
            #             field[i] = 0
            #             field[i + hit] = 1
            
            # # for i in range(len_field):
            # #     if field[i] == 1:
            # #         if i + hit >= len_field:
            # #             score += 1
            # #             new_field[i] == 0
            # #         else:
            # #             new_field[i + hit] = 1

            # # 새로운 주자 추가
            # field[hit - 1] = 1
            # # if 0 <= hit - 1 <= len_field:
            # #     new_field[hit - 1] = 1
            
            # # field[:] = new_field
            # return score
                
        if 1 <= hit <= 4:
            return do(hit)
        else:
            raise Exception("unreachable!")
            
    
    def play_hitter(hitter: int):
        global total_set_time
        nonlocal out_count, this_round_score
        #print(f"hitter number: {hitter}  ", end=" -->>  ")
        if hits[hitter] == 0:
            #print("아웃!")
            out_count += 1
        else:
            set_s = time()
            extra_score = set_new_field_and_get_extra_score(hits[hitter])
            total_set_time += time() - set_s
            #print("extra_score: ", extra_score)
            this_round_score += extra_score
     
    
    hitter = next_hitter()
    while True:
        play_hitter(hitter)
        # print(field)
        if out_count >= 3:
            break
        hitter = next_hitter()
    
    # print("this_round_score: ", this_round_score)
    return this_round_score


def play_rounds(hitters: list[int], hits_for_round: list[list[int]]) -> int:
    total_score = 0
    
    for hits in hits_for_round:
        total_score += play_one_round(hitters, hits)
    
    return total_score


total_s = time()
candidates = [1,2,3,4,5,6,7,8]
mx = -1
acc = 0
for cur in permutations(candidates, 8):
    hitter_counter = 0
    s = time()
    c = list(cur)
    hitters = c[:3] + [0] + c[3:]
    acc += time() - s
    #print("hitters: ", hitters)
    
    # odds = []
    # evens = []
    # is_odd = True
    # while len(hits_list) > 0:
    #     if is_odd:
    #         odds.append(hits_list.pop())
    #     else:
    #         evens.append(hits_list.pop())
    #     is_odd = not is_odd
    s = play_rounds(hitters, hits_list)
    # if s == 53:
    #     print("53찾았다.")
    #     print(hitters)
    #     print([hits_list[0][hitter] for hitter in hitters])
    
    # if s == 46:
    #     print("46찾았따.")
    #     break
    
    #print(f"s: {s}")
    mx = max(mx, s)
    # break
    
print("total time : ", time() - total_s)
print("total set time : ", total_set_time)
    
print("acc time : ", acc)
print(mx)
    