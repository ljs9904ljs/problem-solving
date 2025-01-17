"""

1시간 조금 더 풀다가 O(N^3)보다 나은 아이디어를 떠올리지 못해서
질문 게시판을 보고 다른 사람의 풀이를 이용했다.

두 수의 합을 미리 저장해두면 빠르게 체크할 수 있다.
힌트보고 푸는데 14분 정도 걸림.


"""




# O(n^3) 정도되는 풀이를 떠올려서, 그 풀이를 한 번 시도해본다.
    # 시간초과가 발생했다.
# 두 수의 합을 미리 계산해서 저장해두고, 
# 그 저장해둔 것에 있는지 체크하는 방식으로 하면 O(n^2)이 가능하다.


import sys

input = sys.stdin.readline


n = int(input())
nums = [int(input()) for _ in range(n)]

nums.sort()
nums_set = set(nums)

two_sums = set()
for i in range(n):
    for j in range(n):
        two_sums.add(nums[i] + nums[j])


def find():
    for target in nums[::-1]:
        for num in nums:
            if target - num in two_sums:
                return target
    
    return None


print(find())