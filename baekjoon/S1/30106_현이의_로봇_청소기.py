# 231201
# 46508 KB / 608 ms
from sys import stdin
def to_int():
    return map(int, stdin.readline().split())

N, M, K = to_int()
room = [list(to_int()) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
cnt = 0

def bfs(height, *position):
    from collections import deque
    q = deque()
    q.append((*position, height))
    while q:
        y, x, h = q.popleft()
        for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
            ny, nx = y+dy, x+dx
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                new_h = room[ny][nx]
                if abs(h - new_h) <= K:
                    q.append((ny, nx, new_h))
                    visited[ny][nx] = True

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            cnt += 1
            visited[i][j] = True
            bfs(room[i][j], i, j)

print(cnt)



# 42948 KB / 464 ms
from sys import stdin
from collections import deque

def to_int():
    return map(int, stdin.readline().split())

N, M, K = to_int()
room = [list(to_int()) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
cnt = 0

def bfs(height, *position):
    q = deque()
    q.append((*position, height))
    while q:
        y, x, h = q.popleft()
        for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
            ny, nx = y+dy, x+dx
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                new_h = room[ny][nx]
                if abs(h - new_h) <= K:
                    q.append((ny, nx, new_h))
                    visited[ny][nx] = True

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            cnt += 1
            visited[i][j] = True
            bfs(room[i][j], i, j)

print(cnt)



# 43060 KB / 452 ms
from sys import stdin
from collections import deque

def to_int():
    return map(int, stdin.readline().split())

N, M, K = to_int()
room = [list(to_int()) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
cnt = 0
q = deque()

def bfs(height, *position):
    q.append((*position, height))
    while q:
        y, x, h = q.popleft()
        for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
            ny, nx = y+dy, x+dx
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                new_h = room[ny][nx]
                if abs(h - new_h) <= K:
                    q.append((ny, nx, new_h))
                    visited[ny][nx] = True

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            cnt += 1
            visited[i][j] = True
            bfs(room[i][j], i, j)

print(cnt)