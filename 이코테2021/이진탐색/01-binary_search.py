from bisect import bisect_left, bisect_right


# 바이너리 서치와 관련된 파이썬 라이브러리를 활용하여, 
# 주어진 범위 [left_value, right_value] 안에 포함된 원소의 개수를 세는 함수를 만들 수 있다.
def count_by_range(arr, left_value, right_value):
    # left_value와 right_value는 inclusive이다.
    
    return bisect_right(arr, right_value) - bisect_left(arr, left_value)


def binary_search(arr, target, start, end):
    # @return: target 값에 해당하는 arr의 index를 반환한다.
    
    if start > end:
        return None

    mid = (start + end) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, end)


def binary_search_2(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None




arr = [ 1, 2, 2, 3, 3, 3, 3 , 4, 4, 8, 9]
print(binary_search(arr, 4, 0, len(arr)-1) )
