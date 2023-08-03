#230803
N, M = map(int, input().split())
info = [input().split() for _ in range(N)]
length = 0
direct = set()
for i in range(-1, 2):
    for j in range(-1, 2):
        direct.add((i, j))
direct.remove((0, 0))
visited = [[False]*M for _ in range(N)]

def each_str(*initial):
    from collections import deque
    q = deque()
    q.append(initial)
    while q:
        y, x = q.popleft()
        for dy, dx in direct:
            ny, nx = y+dy, x+dx
            if 0 <= ny < N and 0 <= nx < M:
                if info[ny][nx] == '1' and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((ny, nx))

for i in range(N):
    for j in range(M):
        if info[i][j] == '1' and not visited[i][j]:
            length += 1
            visited[i][j] = True
            each_str(i, j)

print(length)


#
def find_length():
    N, M = map(int, input().split())
    info = [input().split() for _ in range(N)]
    length = 0
    direct = set()
    for i in range(-1, 2):
        for j in range(-1, 2):
            direct.add((i, j))
    direct.remove((0, 0))
    visited = [[False]*M for _ in range(N)]

    def each_str(*initial):
        from collections import deque
        q = deque()
        q.append(initial)
        while q:
            y, x = q.popleft()
            for dy, dx in direct:
                ny, nx = y+dy, x+dx
                if 0 <= ny < N and 0 <= nx < M:
                    if info[ny][nx] == '1' and not visited[ny][nx]:
                        visited[ny][nx] = True
                        q.append((ny, nx))

    for i in range(N):
        for j in range(M):
            if info[i][j] == '1' and not visited[i][j]:
                length += 1
                visited[i][j] = True
                each_str(i, j)

    return length

print(find_length())