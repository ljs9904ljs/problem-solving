"""

문제 푸는 데 걸린 시간: 33분 23초


참고)
원래 풀었던 방식의 풀이로 시간 초과가 발생해서 다른 사람의 풀이를 참고했다.
defaultdict 쓰면 느려서 안 되고,

A,B 각각의 합계 구하고 C,D 각각의 합계를 구한 다음에 for 문을 1번 돌면서 cnt를 계산하면 시간 초과가 발생한다.

2중 fot문 두 개만 써서 풀어야 된다. 마지막에 1중 for문 하나를 더 추가하면 시간 초과다.


"""


import sys


input = sys.stdin.readline


n = int(input())
a = []
b = []
c = []
d = []

arr = []
for _ in range(n):
    a1, b1, c1, d1 = map(int, input().split())
    a.append(a1)
    b.append(b1)
    c.append(c1)
    d.append(d1)


absum = dict()
cdsum = dict()




for i in range(n):
    for j in range(n):
        if a[i] + b[j] in absum:
            absum[a[i] + b[j]] += 1
        else:
            absum[a[i] + b[j]] = 1

cnt = 0        
for i in range(n):
    for j in range(n):
            if -(c[i] + d[j]) in absum:
                cnt += absum[-(c[i] + d[j])]
    

print(cnt)
    

