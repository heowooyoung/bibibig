import sys
sys.stdin = open('input.txt')

T = 10
N = 100


def is_left(r, c):
    if 0 < c <= N-1 and matrix[r][c-1] == 1:
        return True
    else:
        return False


def is_right(r, c):
    if 0 <= c < N-1 and matrix[r][c+1] == 1:
        return True
    else:
        return False


def is_up(r, c):
    if 0 < r <= N and matrix[r-1][c] == 1:
        return True
    else:
        return False


for tc in range(1, T+1):
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))

    for col in range(N):
        if matrix[N-1][col] == 2:
            row, col = N-1, col
            break

    direction = 'up'

    while row != 0:
        if direction == 'up':
            row, col = row-1, col

            if is_right(row, col):
                direction = 'right'

            elif is_left(row, col):
                direction = 'left'

        elif direction == 'right':
            row, col = row, col+1
            if is_up(row, col):
                direction = 'up'

        elif direction == 'left':
            row, col = row, col-1
            if is_up(row, col):
                direction = 'up'

    print(f'#{tc} {col}')
