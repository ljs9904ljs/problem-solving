"""
출처: https://youtu.be/94RC-DsGMLo?si=nDoEKWAwtXXBdGus

유형: 이진탐색
제목: 떡볶이 떡 만들기


<문제>
- 입력;
    - 첫째 줄에 떡의 개수 N과 요청한 떡의 길이 M이 주어집니다. (1 <= N <= 1,000,000, 1<= M <= 2,000,000,000)
    - 둘째 줄에는 떡의 개별 높이가 주어집니다. 떡 높이의 총합은 항상 M 이상이므로, 손님은 필요한 양만큼 떡을 사갈 수 있습니다. 높이는 10억보다 작거나 같은 양의 정수 또는 0입니다.

- 출력;
    - 적어도 M만큼의 떡을 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최대값을 출력합니다.

- 입력 예시;
4 6
19 15 10 17

- 출력 예시;
15

<나의 답안 해석>
파라메트릭 서치 문제이다. log N 으로 줄어들기 때문에 끝 값을 10억으로 설정해도 된다.
떡을 특정 높이 값으로 잘랐을 때 남는 부분의 합을 계산하여 조건을 만족하는지에 따라 값을 저장하고 다음 탐색으로 넘어가거나 값을 저장하지 않고 다음 탐색으로 넘어간다.

mid값으로 계산한 떡 길이의 합이 정확히 요구사항 M과 일치한다면 다음 탐색이 필요없으므로 break한다.


"""

N, M = map(int, input().split())
lengths = list(map(int, input().split()))

l = 0
r = 1_000_000_000


def calculate_length(arr, cutter_height):
    result = sum(map(lambda x: x - cutter_height if (x - cutter_height) > 0 else 0, arr))
    return result

max_height = 0

while l <= r:
    mid = (l + r) // 2

    total_length = calculate_length(lengths, mid)

    if total_length == M:
        max_height = mid
        break
    elif total_length < M:
        r = mid - 1
    else:
        max_height = mid
        l = mid + 1

print(max_height)
    
    
    




### 동영상 속에서 주어진 답 ##


# n, m = list(map(int, input().split(' ')))
# array = list(map(int, input().split()))

# start = 0
# end = max(array)

# result = 0
# while start <= end:
#     total = 0
#     mid = (start + end) // 2
#     for x in array:
#         if x > mid:
#             total += x - mid

#     if total < m:
#         end = mid - 1
#     else:
#         result = mid
#         start = mid + 1

# print(result)








