#230704
R, C, K = map(int, input().split())
road = [input() for _ in range(R)]
if K < R+C - 1:
    print(0)
else:
    def dfs(level=1, y=R-1, x=0):
        global cnt
        if level == K:
            if y == 0 and x == C-1:
                cnt += 1
            return
        elif y == 0 and x == C-1:
            return
        for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
            ny, nx = y + dy, x + dx
            if 0 <= ny < R and 0 <= nx < C:
                if not visited[ny][nx] and road[ny][nx] != 'T':
                    visited[ny][nx] = True
                    dfs(level+1, ny, nx)
                    visited[ny][nx] = False

    visited = [[False] * C for _ in range(R)]
    visited[R-1][0] = True
    cnt = 0
    dfs()

    print(cnt)


#
R, C, K = map(int, input().split())
road = [input() for _ in range(R)]
if K < R + C - 1:
    print(0)
else:
    def dfs(level=1, y=R - 1, x=0):
        global cnt
        if level == K:
            if y == 0 and x == C - 1:
                cnt += 1
            return

        for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
            ny, nx = y + dy, x + dx
            if 0 <= ny < R and 0 <= nx < C:
                if not visited[ny][nx] and road[ny][nx] != 'T':
                    visited[ny][nx] = True
                    dfs(level + 1, ny, nx)
                    visited[ny][nx] = False


    visited = [[False] * C for _ in range(R)]
    visited[R - 1][0] = True
    cnt = 0
    dfs()

    print(cnt)


#
R, C, K = map(int, input().split())
road = [input() for _ in range(R)]
if K < R+C - 1:
    print(0)
else:
    def dfs(level=1, y=R-1, x=0):
        global cnt
        if level == K:
            if y == 0 and x == C-1:
                cnt += 1
            return
        elif y == 0 and x == C-1:
            return
        for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
            ny, nx = y + dy, x + dx
            if 0 <= ny < R and 0 <= nx < C and not visited[ny][nx]:
                visited[ny][nx] = True
                if road[ny][nx] != 'T':
                    dfs(level+1, ny, nx)
                    visited[ny][nx] = False

    visited = [[False] * C for _ in range(R)]
    visited[R-1][0] = True
    cnt = 0
    dfs()

    print(cnt)


#
R, C, K = map(int, input().split())
road = [input() for _ in range(R)]

def dfs(level=1, y=R-1, x=0):
    global cnt
    if level == K:
        if y == 0 and x == C-1:
            cnt += 1
        return
    elif y == 0 and x == C-1:
        return
    for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
        ny, nx = y + dy, x + dx
        if 0 <= ny < R and 0 <= nx < C:
            if not visited[ny][nx] and road[ny][nx] != 'T':
                visited[ny][nx] = True
                dfs(level+1, ny, nx)
                visited[ny][nx] = False

visited = [[False] * C for _ in range(R)]
visited[R-1][0] = True
cnt = 0
dfs()

print(cnt)


#
R, C, K = map(int, input().split())
road = [input() for _ in range(R)]
if K < R+C - 1:
    print(0)
else:
    def dfs(level=1, y=R-1, x=0):
        global cnt
        if level == K:
            if y == 0 and x == C-1:
                cnt += 1
            return

        elif y == 0 and x == C-1:
            return

        new_level = level+1
        for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
            ny, nx = y + dy, x + dx
            if 0 <= ny < R and 0 <= nx < C:
                if not visited[ny][nx] and road[ny][nx] != 'T':
                    visited[ny][nx] = True
                    dfs(new_level, ny, nx)
                    visited[ny][nx] = False

    visited = [[False] * C for _ in range(R)]
    visited[R-1][0] = True
    cnt = 0
    dfs()

    print(cnt)