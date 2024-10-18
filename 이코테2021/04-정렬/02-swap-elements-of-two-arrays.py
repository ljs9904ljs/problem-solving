"""
출처: https://youtu.be/KGyK-pNvWos?si=HG5iuEHuDXh_bH8-

유형: 정렬
제목: 두 배열의 원소 교체


<문제>
- 입력;
    - 첫 번째 줄에  N, K가 공백을 기준으로 구분되어 입력됩니다. (1<=N<=100,000, 0<=K<=N)
    - 두 번째 줄에 배열 A의 원소들이 공백을 기준으로 구분되어 입력됩니다. 모든 원소는 10,000,00보다 작은 자연수입니다.
    - 세 번째 줄에 배열 B의 원소들이 공백을 기준으로 구분되어 입력됩니다. 모든 원소는 10,000,00보다 작은 자연수입니다.

- 출력;
    - 최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최대값을 출력합니다.



<나의 답안 해석>
입력 값의 범위를 고려했을 때 적어도 O( n log n )이 필요하다. 정렬 알고리즘이 O (n log n )이므로 단순하게 A를 오름차순으로 정렬하고, B를 내림차순으로 정렬해서 두 배열의 앞에서부터 비교하면서 swap하면 A 배열의 원소의 총합을 가장 크게 만들 수 있다.


"""

N, K = map(int, input().split())

arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))


arr_a.sort()
arr_b.sort(reverse=True)

for i in range(K):
    if arr_a[i] < arr_b[i]:
        arr_a[i], arr_b[i] = arr_b[i], arr_a[i]

    else:  # 이 부분을 넣어야 더 빠르게 종료시킬 수 있다. 동영상 속 답에서 가져왔다.
        break

print(sum(arr_a))


### 동영상 속에서 주어진 답 ##

# else: break 부분이 추가된 것을 빼면 거의 동일하다.