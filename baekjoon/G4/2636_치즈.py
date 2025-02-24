# 250108
# 250224
# 35004 KB / 60 ms
def main():
    from collections import deque

    def around_air():
        while empty:
            y, x = empty.popleft()
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == 'n':
                    if board[ny][nx] == '0':
                        visited[ny][nx] = '.'
                        empty.append((ny, nx))
                    else:
                        visited[ny][nx] = 'm'
                        q.append((ny, nx))

    def melt():
        new_q = deque()
        cnt = 0
        while q:
            y, x = q.popleft()
            cnt += 1
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if visited[ny][nx] == 'n':
                    if board[ny][nx] == '1':
                        visited[ny][nx] = 'm'
                        new_q.append((ny, nx))
                    else:
                        visited[ny][nx] = '.'
                        empty.append((ny, nx))
        q.extend(new_q)
        return cnt

    def calc():
        now = 0
        around_air()

        while q:
            now += 1
            around_air()
            cnt = melt()

        return f'{now}\n{cnt}'

    N, M = map(int, input().split())
    board = [input().split() for _ in range(N)]
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)

    empty, q = deque(), deque()
    visited = [['n'] * M for _ in range(N)]
    empty.append((0, 0))

    return calc()

print(main())




# 35004 KB / 60 ms
def main():
    from collections import deque

    def around_air():
        while empty:
            y, x = empty.popleft()
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == 'n':
                    if board[ny][nx] == '0':
                        visited[ny][nx] = '.'
                        empty.append((ny, nx))
                    else:
                        visited[ny][nx] = 'm'
                        q.append((ny, nx))

    def melt():
        new_q = deque()
        cnt = 0
        while q:
            y, x = q.popleft()
            cnt += 1
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if visited[ny][nx] == 'n':
                    if board[ny][nx] == '1':
                        visited[ny][nx] = 'm'
                        new_q.append((ny, nx))
                    else:
                        visited[ny][nx] = '.'
                        empty.append((ny, nx))
        q.extend(new_q)
        return cnt

    def calc():
        now = 0
        around_air()

        while q:
            now += 1
            cnt = melt()
            around_air()

        return f'{now}\n{cnt}'

    N, M = map(int, input().split())
    board = [input().split() for _ in range(N)]
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)

    empty, q = deque(), deque()
    visited = [['n'] * M for _ in range(N)]
    empty.append((0, 0))

    return calc()

print(main())



# 35044 KB / 56 ms
def main():
    from collections import deque

    def around_air():
        while empty:
            y, x = empty.popleft()
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == 'n':
                    if board[ny][nx] == '0':
                        visited[ny][nx] = '.'
                        empty.append((ny, nx))
                    else:
                        visited[ny][nx] = 'm'
                        q.append((ny, nx))

    def melt():
        new_q = deque()
        cnt = 0
        while q:
            y, x = q.popleft()
            cnt += 1
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if visited[ny][nx] == 'n':
                    if board[ny][nx] == '1':
                        visited[ny][nx] = 'm'
                        new_q.append((ny, nx))
                    else:
                        visited[ny][nx] = '.'
                        empty.append((ny, nx))
        q.extend(new_q)
        return cnt

    def calc():
        now = 0
        around_air()

        while q:
            now += 1
            cnt = melt()
            around_air()

        return f'{now}\n{cnt}'

    N, M = map(int, input().split())
    board = [input().split() for _ in range(N)]
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)

    empty, q = deque(), deque()
    visited = [['n'] * M for _ in range(N)]
    for i in range(N):
        visited[i][0] = visited[i][-1] = '.'
        empty.append((i, 0))
        empty.append((i, M-1))

    for j in range(1, M-1):
        visited[0][j] = visited[-1][j] = '.'
        empty.append((0, j))
        empty.append((N-1, j))

    return calc()

print(main())



# 35044 KB / 60 ms
def main():
    from collections import deque

    def around_air():
        while empty:
            y, x = empty.popleft()
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                    visited[ny][nx] = True
                    if board[ny][nx] == '0':
                        empty.append((ny, nx))
                    else:
                        q.append((ny, nx))

    def melt():
        new_q = deque()
        cnt = 0
        while q:
            y, x = q.popleft()
            cnt += 1
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    if board[ny][nx] == '1':
                        new_q.append((ny, nx))
                    else:
                        empty.append((ny, nx))
        q.extend(new_q)
        return cnt

    def calc():
        now = 0
        around_air()

        while q:
            now += 1
            cnt = melt()
            around_air()

        return f'{now}\n{cnt}'

    N, M = map(int, input().split())
    board = [input().split() for _ in range(N)]
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)

    empty, q = deque(), deque()
    visited = [[False] * M for _ in range(N)]
    for i in range(N):
        visited[i][0] = visited[i][-1] = True
        empty.append((i, 0))
        empty.append((i, M-1))

    for j in range(1, M-1):
        visited[0][j] = visited[-1][j] = True
        empty.append((0, j))
        empty.append((N-1, j))

    return calc()

print(main())