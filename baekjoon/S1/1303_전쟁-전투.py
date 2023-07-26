#230726
N, M = map(int, input().split())
area = [input() for _ in range(M)]
visited = [[False]*N for _ in range(M)]
troops = [0] * 2

def cnt_troop(symbol, *initial):
    from collections import deque
    q = deque()
    q.append(initial)
    cnt = 1
    while q:
        y, x = q.popleft()
        for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
            ny, nx = y+dy, x+dx
            if 0 <= ny < M and 0 <= nx < N:
                if not visited[ny][nx] and area[ny][nx] == symbol:
                    q.append((ny, nx))
                    visited[ny][nx] = True
                    cnt += 1

    troops[0 if symbol == 'W' else 1] += cnt * cnt

for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            visited[i][j] = True
            cnt_troop(area[i][j], i, j)

print(*troops)


#
def calc_power():
    N, M = map(int, input().split())
    area = [input() for _ in range(M)]
    visited = [[False]*N for _ in range(M)]
    troops = [0] * 2

    def cnt_troop(symbol, *initial):
        from collections import deque
        q = deque()
        q.append(initial)
        cnt = 1
        while q:
            y, x = q.popleft()
            for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
                ny, nx = y+dy, x+dx
                if 0 <= ny < M and 0 <= nx < N:
                    if not visited[ny][nx] and area[ny][nx] == symbol:
                        q.append((ny, nx))
                        visited[ny][nx] = True
                        cnt += 1

        troops[0 if symbol == 'W' else 1] += cnt * cnt

    for i in range(M):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                cnt_troop(area[i][j], i, j)

    return troops

print(*calc_power())


#
def calc_power():
    N, M = map(int, input().split())
    area = [input() for _ in range(M)]
    visited = [[False]*N for _ in range(M)]
    symbol_to_i = {'W': 0, 'B': 1}
    troops = [0] * 2

    def cnt_troop(symbol, *initial):
        from collections import deque
        q = deque()
        q.append(initial)
        cnt = 1
        while q:
            y, x = q.popleft()
            for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
                ny, nx = y+dy, x+dx
                if 0 <= ny < M and 0 <= nx < N:
                    if not visited[ny][nx] and area[ny][nx] == symbol:
                        q.append((ny, nx))
                        visited[ny][nx] = True
                        cnt += 1

        troops[symbol_to_i[symbol]] += cnt * cnt

    for i in range(M):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                cnt_troop(area[i][j], i, j)

    return troops

print(*calc_power())


#
def calc_power():
    from sys import stdin

    new_input = stdin.readline
    N, M = map(int, new_input().split())
    area = [new_input().rstrip() for _ in range(M)]

    visited = [[False]*N for _ in range(M)]
    symbol_to_i = {'W': 0, 'B': 1}
    troops = [0] * 2

    def cnt_troop(symbol, *initial):
        from collections import deque
        q = deque()
        q.append(initial)
        cnt = 1
        while q:
            y, x = q.popleft()
            for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
                ny, nx = y+dy, x+dx
                if 0 <= ny < M and 0 <= nx < N:
                    if not visited[ny][nx] and area[ny][nx] == symbol:
                        q.append((ny, nx))
                        visited[ny][nx] = True
                        cnt += 1

        troops[symbol_to_i[symbol]] += cnt * cnt

    for i in range(M):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                cnt_troop(area[i][j], i, j)

    return troops

print(*calc_power())


#
def calc_power():
    from sys import stdin
    from collections import deque

    new_input = stdin.readline
    N, M = map(int, new_input().split())
    area = [new_input().rstrip() for _ in range(M)]

    visited = [[False]*N for _ in range(M)]
    symbol_to_i = {'W': 0, 'B': 1}
    q = deque()
    troops = [0] * 2

    def cnt_troop(symbol, *initial):
        q.append(initial)
        cnt = 1
        while q:
            y, x = q.popleft()
            for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
                ny, nx = y+dy, x+dx
                if 0 <= ny < M and 0 <= nx < N:
                    if not visited[ny][nx] and area[ny][nx] == symbol:
                        q.append((ny, nx))
                        visited[ny][nx] = True
                        cnt += 1

        troops[symbol_to_i[symbol]] += cnt * cnt

    for i in range(M):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                cnt_troop(area[i][j], i, j)

    return troops

print(*calc_power())


#
def calc_power():
    from collections import deque

    N, M = map(int, input().split())
    area = [input() for _ in range(M)]

    visited = [[False]*N for _ in range(M)]
    symbol_to_i = {'W': 0, 'B': 1}
    direct = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    q = deque()
    troops = [0] * 2

    def cnt_troop(symbol):
        cnt = 1
        while q:
            y, x = q.popleft()
            for dy, dx in direct:
                ny, nx = y+dy, x+dx
                if 0 <= ny < M and 0 <= nx < N:
                    if not visited[ny][nx] and area[ny][nx] == symbol:
                        q.append((ny, nx))
                        visited[ny][nx] = True
                        cnt += 1

        troops[symbol_to_i[symbol]] += cnt * cnt

    for i in range(M):
        for j in range(N):
            if not visited[i][j]:
                q.append((i, j))
                visited[i][j] = True
                cnt_troop(area[i][j])

    return troops

print(*calc_power())
