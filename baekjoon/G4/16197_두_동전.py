#230824
from collections import deque
N, M = map(int, input().split())
coin_position = []
board = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if board[i][j] == 'o':
            coin_position.append((i, j))

def is_in_board(y, x):
    return 0 <= y < N and 0 <= x < M

def find_min_cnt():
    while q:
        cnt, y1, x1, y2, x2 = q.popleft()
        if cnt >= 10:
            return -1

        cnt += 1
        for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
            ny1, nx1 = y1 + dy, x1 + dx
            ny2, nx2 = y2 + dy, x2 + dx
            result1, result2 = is_in_board(ny1, nx1), is_in_board(ny2, nx2)
            if result1 and result2:
                value1, value2 = board[ny1][nx1], board[ny2][nx2]
                if value1 != '#' and value2 != '#':
                    q.append((cnt, ny1, nx1, ny2, nx2))
                elif value1 != '#' or value2 != '#':
                    if value1 == '#':
                        ny1, nx1 = y1, x1

                    else:
                        ny2, nx2 = y2, x2

                    q.append((cnt, ny1, nx1, ny2, nx2))
            elif result1 or result2:
                return cnt

    return -1

q = deque()
q.append((0, *coin_position[0], *coin_position[1]))
print(find_min_cnt())


#
def move_coins():
    from collections import deque
    N, M = map(int, input().split())
    coin_position = []
    board = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'o':
                coin_position.append((i, j))

    def is_in_board(y, x):
        return 0 <= y < N and 0 <= x < M

    def find_min_cnt():
        while q:
            cnt, y1, x1, y2, x2 = q.popleft()
            if cnt >= 10:
                return -1

            cnt += 1
            for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
                ny1, nx1 = y1 + dy, x1 + dx
                ny2, nx2 = y2 + dy, x2 + dx
                result1, result2 = is_in_board(ny1, nx1), is_in_board(ny2, nx2)
                if result1 and result2:
                    value1, value2 = board[ny1][nx1], board[ny2][nx2]
                    if value1 != '#' and value2 != '#':
                        q.append((cnt, ny1, nx1, ny2, nx2))
                    elif value1 != '#' or value2 != '#':
                        if value1 == '#':
                            ny1, nx1 = y1, x1

                        else:
                            ny2, nx2 = y2, x2

                        q.append((cnt, ny1, nx1, ny2, nx2))
                elif result1 or result2:
                    return cnt

        return -1

    q = deque()
    q.append((0, *coin_position[0], *coin_position[1]))
    return find_min_cnt()

print(move_coins())


#
def move_coins():
    from collections import deque
    N, M = map(int, input().split())
    coin_position = []
    board = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'o':
                coin_position.append((i, j))

    def find_min_cnt():

        def is_in_board(y, x):
            return 0 <= y < N and 0 <= x < M

        while q:
            cnt, y1, x1, y2, x2 = q.popleft()
            if cnt >= 10:
                return -1

            cnt += 1
            for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
                ny1, nx1 = y1 + dy, x1 + dx
                ny2, nx2 = y2 + dy, x2 + dx
                result1, result2 = is_in_board(ny1, nx1), is_in_board(ny2, nx2)
                if result1 and result2:
                    value1, value2 = board[ny1][nx1], board[ny2][nx2]
                    if value1 != '#' and value2 != '#':
                        q.append((cnt, ny1, nx1, ny2, nx2))
                    elif value1 != '#' or value2 != '#':
                        if value1 == '#':
                            ny1, nx1 = y1, x1

                        else:
                            ny2, nx2 = y2, x2

                        q.append((cnt, ny1, nx1, ny2, nx2))
                elif result1 or result2:
                    return cnt

        return -1

    q = deque()
    q.append((0, *coin_position[0], *coin_position[1]))
    return find_min_cnt()

print(move_coins())


#
def find_min_cnt(q, board, N, M):
    def is_in_board(y, x):
        return 0 <= y < N and 0 <= x < M

    while q:
        cnt, y1, x1, y2, x2 = q.popleft()
        if cnt >= 10:
            return -1

        cnt += 1
        for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
            ny1, nx1 = y1 + dy, x1 + dx
            ny2, nx2 = y2 + dy, x2 + dx
            result1, result2 = is_in_board(ny1, nx1), is_in_board(ny2, nx2)
            if result1 and result2:
                value1, value2 = board[ny1][nx1], board[ny2][nx2]
                if value1 != '#' and value2 != '#':
                    q.append((cnt, ny1, nx1, ny2, nx2))
                elif value1 != '#' or value2 != '#':
                    if value1 == '#':
                        ny1, nx1 = y1, x1

                    else:
                        ny2, nx2 = y2, x2

                    q.append((cnt, ny1, nx1, ny2, nx2))
            elif result1 or result2:
                return cnt

    return -1

def move_coins():
    from collections import deque
    N, M = map(int, input().split())
    q = deque()
    q.append([0])
    board = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'o':
                q[0].extend((i, j))

    return find_min_cnt(q, board, N, M)

print(move_coins())