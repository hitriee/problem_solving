# 260415
# 260416
# 162108 KB / 3416 ms (Pypy 3)
def main():
    N, M = map(int, input().split())
    limit = N*M
    board = [[0] * M for _ in range(N)]
    cnt = 1

    def dfs(level, position):
        nonlocal cnt

        if level == limit:
            return

        for i in range(position+1, limit):
            y, x = divmod(i, M)
            for dy, dx in (0, -1), (-1, 0), (-1, -1):
                ny, nx = y+dy, x+dx
                if ny < 0 or nx < 0 or not board[ny][nx]:
                    break
            else:
                continue

            cnt += 1
            board[y][x] = 1
            dfs(level+1, i)
            board[y][x] = 0


    dfs(0, -1)
    return cnt

print(main())




# 170236 KB / 3660 ms (Pypy 3)
def main():
    N, M = map(int, input().split())
    limit = N*M
    board = [[False] * M for _ in range(N)]
    cnt = 1

    def dfs(level, position):
        nonlocal cnt

        if level == limit:
            return

        for i in range(position+1, limit):
            y, x = divmod(i, M)
            for dy, dx in (0, -1), (-1, 0), (-1, -1):
                ny, nx = y+dy, x+dx
                if ny < 0 or nx < 0 or not board[ny][nx]:
                    break
            else:
                continue

            cnt += 1
            board[y][x] = True
            dfs(level+1, i)
            board[y][x] = False


    dfs(0, -1)
    return cnt

print(main())




# 162964 KB / 3444 ms (Pypy 3)
def main():
    N, M = map(int, input().split())
    limit = N*M
    board = [[0] * M for _ in range(N)]
    cnt = 1

    def dfs(level, y, x):
        nonlocal cnt

        for dy, dx in (0, -1), (-1, 0), (-1, -1):
            ny, nx = y + dy, x + dx
            if ny < 0 or nx < 0 or not board[ny][nx]:
                break
        else:
            return

        cnt += 1

        if level == limit:
            return

        for j in range(x+1, M):
            board[y][x] = 1
            dfs(level + 1, y, j)
            board[y][x] = 0

        for i in range(y+1, N):
            for j in range(M):
                board[y][x] = 1
                dfs(level+1, i, j)
                board[y][x] = 0


    for i in range(N):
        for j in range(M):
            board[i][j] = 1
            dfs(1, i, j)
            board[i][j] = 0
    return cnt

print(main())





# 162964 KB / 3444 ms (Pypy 3)
def main():
    N, M = map(int, input().split())
    limit = N*M
    board = [[0] * M for _ in range(N)]
    cnt = 1

    def dfs(level, y, x):
        nonlocal cnt

        for dy, dx in (0, -1), (-1, 0), (-1, -1):
            ny, nx = y + dy, x + dx
            if ny < 0 or nx < 0 or not board[ny][nx]:
                break
        else:
            return

        cnt += 1

        if level == limit:
            return

        for j in range(x+1, M):
            board[y][x] = 1
            dfs(level + 1, y, j)
            board[y][x] = 0

        for i in range(y+1, N):
            for j in range(M):
                board[y][x] = 1
                dfs(level+1, i, j)
                board[y][x] = 0


    dfs(1, 0, -1)

    return cnt

print(main())




