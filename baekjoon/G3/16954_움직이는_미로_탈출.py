# 241107
# 34148 KB / 60 ms
def main():
    from collections import deque

    board = [list(input()) for _ in range(8)]
    walls = [set() for _ in range(9)]
    for i in range(8):
        for j in range(8):
            if board[i][j] == '#':
                walls[0].add((i, j))

    q = deque()
    around = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            around.append((i, j))

    q.append((7, 0, 0))
    visited = [[0] * 8 for _ in range(8)]

    # sec <= 8
    while q:
        y, x, sec = q.popleft()
        if y == 0 and x == 7:
            return '1'
        if sec == 9:
            q.append((y, x, sec))
            break
        if (y, x) in walls[sec]:
            continue

        sec += 1
        for dy, dx in around:
            ny, nx = y+dy, x+dx
            if 0 <= ny < 8 and 0 <= nx < 8:
                if visited[ny][nx] < sec and (ny, nx) not in walls[sec-1]:
                    visited[ny][nx] = sec
                    q.append((ny, nx, sec))


        for ny, nx in walls[sec-1]:
            if ny != 7:
                walls[sec].add((ny+1, nx))

    # sec > 8
    while q:
        y, x, sec = q.popleft()
        if y == 0 and x == 7:
            return '1'

        sec += 1
        for dy, dx in around:
            ny, nx = y + dy, x + dx
            if 0 <= ny < 8 and 0 <= nx < 8:
                if visited[ny][nx] < sec:
                    visited[ny][nx] = sec
                    q.append((ny, nx, sec))

    return '0'

print(main())



# 34088 KB / 64 ms
def main():
    from collections import deque

    board = [list(input()) for _ in range(8)]
    walls = [set() for _ in range(9)]
    for i in range(8):
        for j in range(8):
            if board[i][j] == '#':
                walls[0].add((i, j))

    q = deque()
    around = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            around.append((i, j))

    q.append((7, 0, 0))
    visited = [[0] * 8 for _ in range(8)]

    # sec <= 8
    while q:
        y, x, sec = q.popleft()
        if y == 0 and x == 7:
            return '1'

        if sec < 9 and (y, x) in walls[sec]:
            continue

        sec += 1
        for dy, dx in around:
            ny, nx = y+dy, x+dx
            if 0 <= ny < 8 and 0 <= nx < 8:
                if visited[ny][nx] < sec and (sec >= 9 or (ny, nx) not in walls[sec-1]):
                    visited[ny][nx] = sec
                    q.append((ny, nx, sec))

        if sec < 9:
            for ny, nx in walls[sec-1]:
                if ny != 7:
                    walls[sec].add((ny+1, nx))

    return '0'

print(main())
