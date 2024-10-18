"""
출처: https://youtu.be/KGyK-pNvWos?si=58qdZ7RkGp3JbFVX

유형: 
제목: 


<문제>



<나의 답안 해석>



"""

### Quick Sort


def quick_sort(arr, start, end):
    if start >= end:  # There is only one element.
        return

    pivot = start  # set the 'start' as a pivot
    left = start + 1
    right = end

    while left <= right:

        # TODO: 여기 아래 부분 left와 end 사이의 부등호, right와 start 사이의 부등호
        # 이해가 잘 안 된다... @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            right -= 1

        if left > right:
            # left와 right가 엇갈린 경우. 이 아래를 수행 후 while문을 빠져나감.
            # right 자리에 pivot에 있던 친구가 오게 됨.
            # 즉, right 인덱스 왼쪽에 있는 것들은 pivot보다 작은 값들이고
            # right 인덱스 오른쪽에 있는 것들은 pivot보다 큰 값들임.
            # 이제 right 인덱스 자리에 있는 친구는 가만히 내비두고,
            # 왼쪽 파트에 대해 quick sort를 하고
            # 오른쪽 파트에 대해 quick sort를 하면 된다.
            arr[pivot], arr[right] = arr[right], arr[pivot]
        else:
            arr[left], arr[right] = arr[right], arr[left]

    # right 인덱스 자리에 있는 것은 이미 위치가 잘 정해졌으므로 그 왼쪽 파트와 오른쪽 파트만 신경쓰면 된다.
    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)


arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
quick_sort(arr, 0, len(arr) - 1)

print(arr)

### 동영상 속에서 주어진 답 ###
