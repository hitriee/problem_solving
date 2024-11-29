# 241129
# 34132 KB / 56 ms
def main():
    from collections import deque

    def minus_one(num):
        return int(num)-1

    N, M = map(int, input().split())
    arr = [input().split() for _ in range(N)]
    y1, x1, d1 = map(minus_one, input().split())
    y2, x2, d2 = map(minus_one, input().split())
    num_to_d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    right_turn, left_turn = [2, 3, 1, 0], [3, 2, 0,1]

    def bfs():
        q = deque()
        q.append((y1, x1, d1, 0))
        visited = [[[False] * 4 for _ in range(M)] for _ in range(N)]
        visited[y1][x1][d1] = True

        while q:
            y, x, d, cnt = q.popleft()
            if y == y2 and x == x2 and d == d2:
                return cnt

            ny, nx = y, x
            dy, dx = num_to_d[d]
            cnt += 1

            for _ in range(3):
                ny += dy
                nx += dx
                if 0 <= ny < N and 0 <= nx < M and arr[ny][nx] == '0':
                    if not visited[ny][nx][d]:
                        visited[ny][nx][d] = True
                        q.append((ny, nx, d, cnt))
                else:
                    break

            for nd in [left_turn[d], right_turn[d]]:
                if not visited[y][x][nd]:
                    visited[y][x][nd] = True
                    q.append((y, x, nd, cnt))

    return bfs()


print(main())


# 34148 KB / 56 ms
def main():
    def minus_one(num):
        return int(num)-1

    N, M = map(int, input().split())
    arr = [input().split() for _ in range(N)]
    y1, x1, d1 = map(minus_one, input().split())
    y2, x2, d2 = map(minus_one, input().split())
    num_to_d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    right_turn, left_turn = [2, 3, 1, 0], [3, 2, 0,1]

    def bfs():
        from collections import deque

        q = deque()
        q.append((y1, x1, d1, 0))
        visited = [[[False] * 4 for _ in range(M)] for _ in range(N)]
        visited[y1][x1][d1] = True

        while q:
            y, x, d, cnt = q.popleft()
            if y == y2 and x == x2 and d == d2:
                return cnt

            ny, nx = y, x
            dy, dx = num_to_d[d]
            cnt += 1

            for _ in range(3):
                ny += dy
                nx += dx
                if 0 <= ny < N and 0 <= nx < M and arr[ny][nx] == '0':
                    if not visited[ny][nx][d]:
                        visited[ny][nx][d] = True
                        q.append((ny, nx, d, cnt))
                else:
                    break

            for nd in [left_turn[d], right_turn[d]]:
                if not visited[y][x][nd]:
                    visited[y][x][nd] = True
                    q.append((y, x, nd, cnt))

    return bfs()


print(main())


# 34132 KB / 56 ms
def main():
    from sys import stdin
    from collections import deque

    def minus_one(num):
        return int(num)-1

    new_input = stdin.readline

    N, M = map(int, new_input().split())
    arr = [new_input().split() for _ in range(N)]
    y1, x1, d1 = map(minus_one, new_input().split())
    y2, x2, d2 = map(minus_one, new_input().split())
    num_to_d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    right_turn, left_turn = [2, 3, 1, 0], [3, 2, 0,1]

    def bfs():
        q = deque()
        q.append((y1, x1, d1, 0))
        visited = [[[False] * 4 for _ in range(M)] for _ in range(N)]
        visited[y1][x1][d1] = True

        while q:
            y, x, d, cnt = q.popleft()
            if y == y2 and x == x2 and d == d2:
                return cnt

            ny, nx = y, x
            dy, dx = num_to_d[d]
            cnt += 1

            for _ in range(3):
                ny += dy
                nx += dx
                if 0 <= ny < N and 0 <= nx < M and arr[ny][nx] == '0':
                    if not visited[ny][nx][d]:
                        visited[ny][nx][d] = True
                        q.append((ny, nx, d, cnt))
                else:
                    break

            for nd in [left_turn[d], right_turn[d]]:
                if not visited[y][x][nd]:
                    visited[y][x][nd] = True
                    q.append((y, x, nd, cnt))

    return bfs()


print(main())



# 34132 KB / 56 ms
def main():
    from sys import stdin
    from collections import deque

    def minus_one(num):
        return int(num)-1

    new_input = stdin.readline

    N, M = map(int, new_input().split())
    arr = [new_input().split() for _ in range(N)]
    y1, x1, d1 = map(minus_one, new_input().split())
    y2, x2, d2 = map(minus_one, new_input().split())
    num_to_d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    right_turn, left_turn = [2, 3, 1, 0], [3, 2, 0,1]

    q = deque()
    q.append((y1, x1, d1, 0))
    visited = [[[False] * 4 for _ in range(M)] for _ in range(N)]
    visited[y1][x1][d1] = True

    while True:
        y, x, d, cnt = q.popleft()
        if y == y2 and x == x2 and d == d2:
            return cnt

        ny, nx = y, x
        dy, dx = num_to_d[d]
        cnt += 1

        for _ in range(3):
            ny += dy
            nx += dx
            if 0 <= ny < N and 0 <= nx < M and arr[ny][nx] == '0':
                if not visited[ny][nx][d]:
                    visited[ny][nx][d] = True
                    q.append((ny, nx, d, cnt))
            else:
                break

        for nd in [left_turn[d], right_turn[d]]:
            if not visited[y][x][nd]:
                visited[y][x][nd] = True
                q.append((y, x, nd, cnt))


print(main())



# 34140 KB / 64 ms
def main():
    from sys import stdin
    from collections import deque

    def minus_one(num):
        return int(num)-1

    def go_ahead(ny, nx, dy, dx, cnt):
        for _ in range(3):
            ny += dy
            nx += dx
            if 0 <= ny < N and 0 <= nx < M and arr[ny][nx] == '0':
                if not visited[ny][nx][d]:
                    visited[ny][nx][d] = True
                    q.append((ny, nx, d, cnt))
            else:
                return

    def turn(ny, nx, d, cnt):
        for nd in (left_turn[d], right_turn[d]):
            if not visited[ny][nx][nd]:
                visited[ny][nx][nd] = True
                q.append((ny, nx, nd, cnt))

    new_input = stdin.readline

    N, M = map(int, new_input().split())
    arr = [new_input().split() for _ in range(N)]
    y1, x1, d1 = map(minus_one, new_input().split())
    y2, x2, d2 = map(minus_one, new_input().split())
    num_to_d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    right_turn, left_turn = [2, 3, 1, 0], [3, 2, 0,1]

    q = deque()
    q.append((y1, x1, d1, 0))
    visited = [[[False] * 4 for _ in range(M)] for _ in range(N)]
    visited[y1][x1][d1] = True

    while True:
        y, x, d, cnt = q.popleft()
        if y == y2 and x == x2 and d == d2:
            return cnt

        go_ahead(y, x, *num_to_d[d], cnt+1)
        turn(y, x, d, cnt+1)

print(main())