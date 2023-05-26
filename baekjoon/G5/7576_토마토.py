#230526
# bfs
from sys import stdin
from collections import deque
new_input = stdin.readline
M, N = map(int, new_input().split())
info = []
aging_tomato = deque()
for i in range(N):
    row = input().split()
    info.append(row)
    for j in range(M):
        if row[j] == '1':
            aging_tomato.append((i, j, 0))

while aging_tomato:
    y, x, day = aging_tomato.popleft()
    for dy, dx in (1, 0), (0, 1), (-1, 0), (0, -1):
        ny, nx = y+dy, x+dx
        if 0 <= ny < N and 0 <= nx < M and info[ny][nx] == '0':
            aging_tomato.append((ny, nx, day+1))
            info[ny][nx] = '1'
for i in range(N):
    for j in range(M):
        if info[i][j] == '0':
            print(-1)
            break
    else:
        continue
    break
else:
    print(day)


# bfs
def final_day():
    from sys import stdin
    from collections import deque
    new_input = stdin.readline
    M, N = map(int, new_input().split())
    info = []
    aging_tomato = deque()
    for i in range(N):
        row = input().split()
        info.append(row)
        for j in range(M):
            if row[j] == '1':
                aging_tomato.append((i, j, 0))

    while aging_tomato:
        y, x, day = aging_tomato.popleft()
        for dy, dx in (1, 0), (0, 1), (-1, 0), (0, -1):
            ny, nx = y+dy, x+dx
            if 0 <= ny < N and 0 <= nx < M and info[ny][nx] == '0':
                aging_tomato.append((ny, nx, day+1))
                info[ny][nx] = '1'

    for i in range(N):
        for j in range(M):
            if info[i][j] == '0':
                return -1
    return day
print(final_day())


#
def final_day():
    from sys import stdin
    from collections import deque
    new_input = stdin.readline
    M, N = map(int, new_input().split())
    info = []
    aging_tomato = deque()
    for i in range(N):
        row = input().split()
        info.append(row)
        for j in range(M):
            if row[j] == '1':
                aging_tomato.append((i, j, 0))

    def return_day():
        while aging_tomato:
            y, x, day = aging_tomato.popleft()
            for dy, dx in (1, 0), (0, 1), (-1, 0), (0, -1):
                ny, nx = y+dy, x+dx
                if 0 <= ny < N and 0 <= nx < M and info[ny][nx] == '0':
                    aging_tomato.append((ny, nx, day+1))
                    info[ny][nx] = '1'

        for i in range(N):
            for j in range(M):
                if info[i][j] == '0':
                    return -1
        return day

    return return_day()

print(final_day())

# bfs
def final_day():
    from sys import stdin
    from collections import deque
    new_input = stdin.readline

    M, N = map(int, new_input().split())
    info, aging_tomato = [], deque()

    for i in range(N):
        row = input().split()
        info.append(row)
        for j in range(M):
            if row[j] == '1':
                aging_tomato.append((i, j, 0))

    direct = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while aging_tomato:
        y, x, day = aging_tomato.popleft()
        for dy, dx in direct:
            ny, nx = y+dy, x+dx
            if 0 <= ny < N and 0 <= nx < M and info[ny][nx] == '0':
                aging_tomato.append((ny, nx, day+1))
                info[ny][nx] = '1'

    for i in range(N):
        for j in range(M):
            if info[i][j] == '0':
                return -1
    return day
print(final_day())


# bfs
def final_day():
    from sys import stdin
    from collections import deque
    new_input = stdin.readline
    M, N = map(int, new_input().split())
    info = []
    aging_tomato = deque()
    for i in range(N):
        row = input().split()
        info.append(row)
        for j in range(M):
            if row[j] == '1':
                aging_tomato.append((i, j, 0))

    def return_day():
        while aging_tomato:
            y, x, day = aging_tomato.popleft()
            for dy, dx in (1, 0), (0, 1), (-1, 0), (0, -1):
                ny, nx = y+dy, x+dx
                if 0 <= ny < N and 0 <= nx < M and info[ny][nx] == '0':
                    aging_tomato.append((ny, nx, day+1))
                    info[ny][nx] = '1'

        for i in range(N):
            for j in range(M):
                if info[i][j] == '0':
                    return -1
        return day

    return return_day()

print(final_day())


#
def final_day():
    from sys import stdin
    from collections import deque

    new_input = stdin.readline
    M, N= map(int,input().split())

    mature, immature = deque(), set()
    for i in range(N):
        box = new_input().split()
        for j in range(M):
            if box[j] == '1':
                mature.append((i, j, 0))
            elif box[j] == '0':
                immature.add((i, j))

    if not immature:
        return 0

    while mature:
        r, c, day = mature.popleft()
        for dr, dc in (-1,0), (1,0), (0,-1), (0,1):
            nr, nc = r+dr, c+dc
            if (nr, nc) in immature:
                mature.append((nr, nc, day + 1))
                immature.remove((nr, nc))
    if immature:
        return -1
    return day

print(final_day())