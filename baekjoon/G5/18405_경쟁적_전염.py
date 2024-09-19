# 240919
# 34104 KB / 100 ms

def main():
    from collections import deque

    def int_input(func=int):
        return map(func, input().split())
    def in_range(y, x):
        return 0 <= y < N and 0 <= x < N

    N, K = int_input()
    arr = [list(int_input()) for _ in range(N)]
    virus = [deque() for _ in range(K+1)]
    S, X, Y = int_input(func=lambda x: int(x)-1)
    if arr[X][Y]:
        return arr[X][Y]

    for i in range(N):
        for j in range(N):
            idx = arr[i][j]
            if idx:
                virus[idx].append((i, j))

    q = deque()
    dy, dx = (1, 0, 0, -1), (0, -1, 1, 0)
    for _ in range(S+1):
        for i in range(1, K+1):
            q.extend(virus[i])
            virus[i].clear()
            while q:
                y, x = q.popleft()
                for j in range(4):
                    ny, nx = y+dy[j], x+dx[j]
                    if in_range(ny, nx) and arr[ny][nx] == 0:
                        virus[i].append((ny, nx))
                        arr[ny][nx] = i

        if arr[X][Y]:
            return arr[X][Y]

    return 0

print(main())



# 34096 KB / 632 ms

def main():
    from collections import deque

    def int_input(func=int):
        return map(func, input().split())
    def in_range(y, x):
        return 0 <= y < N and 0 <= x < N

    N, K = int_input()
    arr = [list(int_input()) for _ in range(N)]
    virus = [deque() for _ in range(K+1)]
    S, X, Y = int_input(func=lambda x: int(x)-1)
    if arr[X][Y]:
        return arr[X][Y]

    for i in range(N):
        for j in range(N):
            idx = arr[i][j]
            if idx:
                virus[idx].append((i, j))

    q = deque()
    dy, dx = (1, 0, 0, -1), (0, -1, 1, 0)
    for _ in range(S+1):
        for i in range(1, K+1):
            q.extend(virus[i])
            virus[i].clear()
            while q:
                y, x = q.popleft()
                for j in range(4):
                    ny, nx = y+dy[j], x+dx[j]
                    if in_range(ny, nx) and arr[ny][nx] == 0:
                        virus[i].append((ny, nx))
                        arr[ny][nx] = i

    return arr[X][Y]

print(main())




# 34096 KB / 100 ms

def main():
    from collections import deque

    def int_input(func=int):
        return map(func, input().split())

    def in_range(y, x):
        return 0 <= y < N and 0 <= x < N

    def bfs(q, i):
        virus[i].clear()
        while q:
            y, x = q.popleft()
            for j in range(4):
                ny, nx = y + dy[j], x + dx[j]
                if in_range(ny, nx) and arr[ny][nx] == 0:
                    virus[i].append((ny, nx))
                    arr[ny][nx] = i

    N, K = int_input()
    arr = [list(int_input()) for _ in range(N)]
    virus = [[] for _ in range(K+1)]
    S, X, Y = int_input(func=lambda x: int(x)-1)
    if arr[X][Y]:
        return arr[X][Y]

    for i in range(N):
        for j in range(N):
            idx = arr[i][j]
            if idx:
                virus[idx].append((i, j))

    dy, dx = (1, 0, 0, -1), (0, -1, 1, 0)
    for _ in range(S+1):
        for i in range(1, K+1):
            bfs(deque(virus[i]), i)

        if arr[X][Y]:
            return arr[X][Y]

    return 0

print(main())



# 34112 KB / 100 ms

def main():
    from collections import deque

    def int_input(func=int):
        return map(func, input().split())

    def in_range(y, x):
        return 0 <= y < N and 0 <= x < N

    def bfs(q, i):
        virus[i].clear()
        while q:
            y, x = q.popleft()
            for j in range(4):
                ny, nx = y + dy[j], x + dx[j]
                if in_range(ny, nx) and arr[ny][nx] == 0:
                    virus[i].append((ny, nx))
                    arr[ny][nx] = i

    N, K = int_input()
    arr = [list(int_input()) for _ in range(N)]
    virus = [[] for _ in range(K+1)]
    S, X, Y = int_input(func=lambda x: int(x)-1)
    if arr[X][Y]:
        return arr[X][Y]

    limit = 0
    for i in range(N):
        for j in range(N):
            idx = arr[i][j]
            if idx:
                virus[idx].append((i, j))
                if limit < idx:
                    limit = idx

    dy, dx = (1, 0, 0, -1), (0, -1, 1, 0)
    for _ in range(S+1):
        for i in range(1, limit+1):
            bfs(deque(virus[i]), i)

        if arr[X][Y]:
            return arr[X][Y]

    return 0

print(main())




# 34096 KB / 96 ms

def main():
    from sys import stdin
    from collections import deque

    def int_input(func=int):
        return map(func, stdin.readline().split())

    def in_range(y, x):
        return 0 <= y < N and 0 <= x < N

    def bfs(q, i):
        virus[i].clear()
        while q:
            y, x = q.popleft()
            for j in range(4):
                ny, nx = y + dy[j], x + dx[j]
                if in_range(ny, nx) and arr[ny][nx] == 0:
                    virus[i].append((ny, nx))
                    arr[ny][nx] = i

    N, K = int_input()
    arr = [list(int_input()) for _ in range(N)]
    virus = [[] for _ in range(K+1)]
    S, X, Y = int_input(func=lambda x: int(x)-1)
    if arr[X][Y]:
        return arr[X][Y]

    for i in range(N):
        for j in range(N):
            idx = arr[i][j]
            if idx:
                virus[idx].append((i, j))

    dy, dx = (1, 0, 0, -1), (0, -1, 1, 0)
    for _ in range(S+1):
        for i in range(1, K+1):
            bfs(deque(virus[i]), i)

        if arr[X][Y]:
            return arr[X][Y]

    return 0

print(main())


# 34096 KB / 92 ms

def main():
    from sys import stdin
    from collections import deque

    def int_input(func=int):
        return map(func, stdin.readline().split())

    def in_range(y, x):
        return 0 <= y < N and 0 <= x < N

    def bfs(q, i):
        virus[i].clear()
        while q:
            y, x = q.popleft()
            for j in range(4):
                ny, nx = y + dy[j], x + dx[j]
                if in_range(ny, nx) and arr[ny][nx] == 0:
                    virus[i].append((ny, nx))
                    arr[ny][nx] = i

    N, K = int_input()
    arr = [list(int_input()) for _ in range(N)]
    virus = [[] for _ in range(K+1)]
    S, X, Y = int_input(func=lambda x: int(x)-1)
    if arr[X][Y] or S == -1:
        return arr[X][Y]

    for i in range(N):
        for j in range(N):
            idx = arr[i][j]
            if idx:
                virus[idx].append((i, j))

    dy, dx = (1, 0, 0, -1), (0, -1, 1, 0)
    for _ in range(S+1):
        for i in range(1, K+1):
            bfs(deque(virus[i]), i)

        if arr[X][Y]:
            return arr[X][Y]

    return 0

print(main())
