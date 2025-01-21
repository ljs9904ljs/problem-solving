"""

문제 푸는 데 걸린 시간: 14분 26초


"""


import sys


input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))


# arr.sort()

mn = int(1e9)
i = 0
j = n - 1
while i < j:
    B = arr[i] + arr[j]
    if abs(mn) > abs(B):
        mn = B
    
    if B == 0:
        break
    elif B > 0:
        j -= 1
    else:
        i += 1
        
print(mn)