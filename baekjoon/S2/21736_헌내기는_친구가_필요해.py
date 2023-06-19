#230619
from sys import stdin
from collections import deque
def new_input(): return stdin.readline().rstrip()

N, M = map(int, new_input().split())
campus = []
visited = [[False] * M for _ in range(N)]
q = deque()

for i in range(N):
    campus.append(new_input())
    if not q:
        for j in range(M):
            if campus[-1][j] == 'I':
                q.append((i, j))
                visited[i][j] = True
                break
cnt = 0
while q:
    y, x = q.popleft()
    if campus[y][x] == 'P':
        cnt += 1
    for dy, dx in (-1, 0), (1, 0), (0, -1), (0, 1):
        ny, nx = y+dy, x+dx
        if 0 <= ny < N and 0 <= nx < M:
            if campus[ny][nx] != 'X' and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((ny, nx))

if cnt == 0:
    print('TT')
else:
    print(cnt)



#
from sys import stdin
from collections import deque
def new_input(): return stdin.readline().rstrip()

N, M = map(int, new_input().split())
campus = []
q = deque()

for i in range(N):
    campus.append(list(map(str, new_input())))
    for j in range(M):
        if campus[-1][j] == 'I':
            q.append((i, j))
            campus[-1][j] = 'X'
            break
cnt = 0
while q:
    y, x = q.popleft()
    for dy, dx in (-1, 0), (1, 0), (0, -1), (0, 1):
        ny, nx = y+dy, x+dx
        if 0 <= ny < N and 0 <= nx < M:
            if campus[ny][nx] != 'X':
                if campus[ny][nx] == 'P':
                    cnt += 1
                campus[ny][nx] = 'X'
                q.append((ny, nx))

if cnt == 0:
    print('TT')
else:
    print(cnt)


#
def cnt_people():
    from sys import stdin
    from collections import deque
    def new_input(): return stdin.readline().rstrip()

    N, M = map(int, new_input().split())
    campus = []
    q = deque()

    for i in range(N):
        campus.append(list(map(str, new_input())))
        for j in range(M):
            if campus[-1][j] == 'I':
                q.append((i, j))
                campus[-1][j] = 'X'
                break
    def bfs():
        cnt = 0
        while q:
            y, x = q.popleft()
            for dy, dx in (-1, 0), (1, 0), (0, -1), (0, 1):
                ny, nx = y+dy, x+dx
                if 0 <= ny < N and 0 <= nx < M:
                    if campus[ny][nx] != 'X':
                        if campus[ny][nx] == 'P':
                            cnt += 1
                        campus[ny][nx] = 'X'
                        q.append((ny, nx))

        return cnt if cnt else 'TT'

    return bfs()

print(cnt_people())
