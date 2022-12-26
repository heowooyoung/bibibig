import sys
sys.stdin = open('input.txt')

T = int(input())


def get_max_min_diff(numbers):
    max_value = min_value = numbers[0]

    for number in numbers[1:]:
        if number > max_value:
            max_value = number

        elif number < min_value:
            min_value = number

    ans = max_value - min_value
    return ans


for tc in range(1, T+1):
    N = int(input())

    # 생각 => A4 펜으로 그림식으로 생각을 함 => 문제를 축소 => 확장
    # 100 * 100

    # 1. list => 원소 이름 복수형
    # 2. 함수 => 동사 (함축적)
    # 3. 변수 => 담긴 값이 T/F 일경우 is_xxx
    # 4. 함수 => return 값이 T/F => is_xxx()

    numbers = list(map(int, input().split()))

    print(f'#{tc} {get_max_min_diff(numbers)}')
