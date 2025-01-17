"""
문제
숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다. 두 숫자 카드에 같은 수가 적혀있는 경우는 없다.

셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 넷째 줄에는 상근이가 가지고 있는 숫자 카드인지 아닌지를 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다. 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다

출력
첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 가지고 있으면 1을, 아니면 0을 공백으로 구분해 출력한다.

예제 입력 1 
5
6 3 2 10 -10
8
10 9 -5 2 3 4 5 -10
예제 출력 1 
1 0 0 1 1 0 0 1

"""

import sys


input = sys.stdin.readline


n = int(input())
nums = list(map(int, input().split()))
m = int(input())
checks = list(map(int, input().split()))


# 방법 1
# 처음에 떠올리지 못했다가, 알고리즘 분류를 보고 떠올리게 됨.
# set을 활용하면 특정 원소의 존재 여부를 빠르게 확인할 수 있다!
nums_set = set(nums)
result = []
for check in checks:
    if check in nums_set:
        result.append(1)
    else:
        result.append(0)
    
print(" ".join(map(str, result)))



# 방법 2
from bisect import bisect_left
sorted_nums = sorted(nums)

result = []
for check in checks:
    i = bisect_left(sorted_nums, check)
    if 0 <= i < len(sorted_nums) and sorted_nums[i] == check:
        result.append(1)
    else:
        result.append(0)

print(" ".join(map(str, result)))