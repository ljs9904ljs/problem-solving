"""

문제 푸는 데 걸린 시간: 27분 11초


참고)

python3로 제출하니까 시간초과 뜸. pypy3로 통과함.
    - N이 최대 5000이기 때문에 O(N^2 * Log N) 풀이는 통과해야 함. 하지만 python3가 너무 느린 것인지 시간초과가 발생한다...


실수 1. bisect_left를 사용하기 때문에 input 배열을 정렬했어야 했는데 깜빡하고 안 해서 틀렸었음.
실수 2. idx + k 값이 i나 j와 겹치면 안 되는데(서로 다른 세 용액을 섞는 것이므로) 그것에 대한 체크를 하지 않았었다.


"""



import sys
from bisect import bisect_left
from typing import Union



input = sys.stdin.readline


def main() -> list[int]:
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    
    result = None
    score = int(1e10)


    def check_and_get_value(i: int) -> Union[int, None]:
        if 0 <= i < n:
            return arr[i]
        else:
            return None

    
    def loop():
        nonlocal score, result
        
        for i in range(n):
            for j in range(i + 1, n):
                target = -(arr[i] + arr[j])
                idx = bisect_left(arr, target, lo=j + 1)
                
                for k in range(-1, 2):
                    new_idx = idx + k
                    if new_idx == i or new_idx == j:
                        continue
                    
                    v = check_and_get_value(new_idx)
                    if v is not None:
                        if v == target:
                            result = sorted([arr[i], arr[j], v])
                            return
                        else:
                            if abs(score) > abs(arr[i] + arr[j] + v):
                                score = arr[i] + arr[j] + v
                                result = sorted([arr[i], arr[j], v])
                                
    loop()
    return result
    

print(" ".join(map(str, main())))
            