#230426
# bfs
from sys import stdin
from collections import deque
N, M = map(int, stdin.readline().split())
target = ()
total_map = []
for i in range(N):
    map_row = stdin.readline().rstrip().split()
    if not target:
        for j in range(M):
            if map_row[j] == '2':
                target = (i, j)
                break
    total_map.append(map_row)

q = deque()
q.append((*target, 0))
visited = [[False] * M for _ in range(N)]

while q:
    y, x, distance = q.popleft()
    total_map[y][x] = str(distance)
    for dy, dx in (-1, 0), (1, 0), (0, -1), (0, 1):
        ny, nx = y+dy, x+dx
        if 0 <= ny < N and 0 <= nx < M:
            if not visited[ny][nx]:
                visited[ny][nx] = True
                if total_map[ny][nx] != '0':
                    q.append((ny, nx, distance+1))

for i in range(N):
    for j in range(M):
        if not visited[i][j] and total_map[i][j] != '0':
            total_map[i][j] = '-1'
for i in range(N):
    print(' '.join(total_map[i]))


# 함수화
def find_min_distance():
    def fill_map():
        nonlocal target
        for i in range(N):
            map_row = stdin.readline().rstrip().split()
            if not target:
                for j in range(M):
                    if map_row[j] == '2':
                        target = (i, j)
                        break
            total_map.append(map_row)
    def bfs():
        q = deque()
        q.append((*target, 0))

        while q:
            y, x, distance = q.popleft()
            total_map[y][x] = str(distance)
            for dy, dx in (-1, 0), (1, 0), (0, -1), (0, 1):
                ny, nx = y+dy, x+dx
                if 0 <= ny < N and 0 <= nx < M:
                    if not visited[ny][nx]:
                        visited[ny][nx] = True
                        if total_map[ny][nx] != '0':
                            q.append((ny, nx, distance+1))
    def convert_minus():
        for i in range(N):
            for j in range(M):
                if not visited[i][j] and total_map[i][j] != '0':
                    total_map[i][j] = '-1'

    from sys import stdin
    from collections import deque
    N, M = map(int, stdin.readline().split())
    target = ()
    total_map = []
    visited = [[False] * M for _ in range(N)]
    fill_map()
    bfs()
    convert_minus()
    for i in range(N):
        print(' '.join(total_map[i]))

find_min_distance()