#230511
# bfs
N, M = map(int, input().split())
planet = [input().split() for _ in range(N)]
cnt = 0

def bfs(*position):
    from collections import deque
    q = deque()
    q.append(position)
    while q:
        y, x = q.popleft()
        for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
            ny, nx = (y+dy)%N, (x+dx)%M
            if planet[ny][nx] == '0':
                planet[ny][nx] = '1'
                q.append((ny, nx))

for i in range(N):
    for j in range(M):
        if planet[i][j] == '0':
            cnt += 1
            planet[i][j] = '1'
            bfs(i,j)
print(cnt)


#
def bfs(*position):
    from collections import deque
    q = deque()
    q.append(position)
    while q:
        y, x = q.popleft()
        for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
            ny, nx = (y + dy) % N, (x + dx) % M
            if planet[ny][nx] == '0':
                planet[ny][nx] = '1'
                q.append((ny, nx))

N, M = map(int, input().split())
planet = [input().split() for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(M):
        if planet[i][j] == '0':
            cnt += 1
            planet[i][j] = '1'
            bfs(i, j)
print(cnt)


#
def calc_road_cnt():
    N, M = map(int, input().split())
    planet = [input().split() for _ in range(N)]
    cnt = 0

    def bfs(*position):
        from collections import deque
        q = deque()
        q.append(position)
        while q:
            y, x = q.popleft()
            for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
                ny, nx = (y+dy)%N, (x+dx)%M
                if planet[ny][nx] == '0':
                    planet[ny][nx] = '1'
                    q.append((ny, nx))

    for i in range(N):
        for j in range(M):
            if planet[i][j] == '0':
                cnt += 1
                planet[i][j] = '1'
                bfs(i, j)
    return cnt
print(calc_road_cnt())


#
def calc_road_cnt():
    def bfs(*position):
        from collections import deque
        q = deque()
        q.append(position)
        while q:
            y, x = q.popleft()
            for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
                ny, nx = (y+dy)%N, (x+dx)%M
                if planet[ny][nx] == '0':
                    planet[ny][nx] = '1'
                    q.append((ny, nx))

    N, M = map(int, input().split())
    planet = [input().split() for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(M):
            if planet[i][j] == '0':
                cnt += 1
                planet[i][j] = '1'
                bfs(i, j)
    return cnt

print(calc_road_cnt())
