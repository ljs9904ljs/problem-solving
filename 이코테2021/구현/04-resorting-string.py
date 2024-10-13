"""
출처: https://youtu.be/2zjoKjt97vQ?si=PpaK6DISWRoLL4Id

유형: 구현
제목: 문자열 재정렬


<문제>
- 알파벳 대문자와 숫자(0-9)로만 구성된 문자열이 입력으로 주어진다. 이 때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력한다.
- 입력; 하나의 문자열 S가 주어진다. (1 <= |S| <= 10,000)

- 입력 예시; K1KA5CB7
- 출력 예시; ABCKK13

<나의 답안 해석>
- 주어진 조건을 그대로 구현하였음. 구현한 것은 O(n log n) 이므로 시간 제한 안에 충분히 풀 수 있기 때문임.

"""

S = input()

acc = 0
chars = []
at_least_one_num = False

for char in S:
    if char.isdigit():
        acc += int(char)
        at_least_one_num = True
    else:
        chars.append(char)

chars.sort()
if at_least_one_num:
    chars.append(str(acc))
print("".join(chars))

### 동영상 속에서 주어진 답 ###

# 내 풀이랑 거의 같음. 다만, 주어진 문자열 S 안에 숫자가 단 하나도 없는 경우를 놓치면 안 된다.
