# 260406
# 180492 KB / 5260 ms (Pypy)
def main():
    max_cnt = 1
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)

    ref = ord('A')
    alp_to_num = {chr(ref+i): 1 << i for i in range(26)}
    R, C = map(int, input().split())
    board = [list(map(lambda x: alp_to_num[x], input())) for _ in range(R)]

    visited = board[0][0]

    def dfs(level, y, x):
        nonlocal max_cnt, visited

        if max_cnt < level:
            max_cnt = level

        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < R and 0 <= nx < C:
                num = board[ny][nx]
                if visited & num == 0:
                    visited += num
                    dfs(level+1, ny, nx)
                    visited -= num

    dfs(1, 0, 0)


    return max_cnt

print(main())





# 180900 KB / 5688 ms (Pypy)
def main():
    max_cnt = 1
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)

    ref = ord('A')
    alp_to_num = {chr(ref+i): i for i in range(26)}
    R, C = map(int, input().split())
    board = [list(map(lambda x: alp_to_num[x], input())) for _ in range(R)]

    visited = 1 << board[0][0]

    def dfs(level, y, x):
        nonlocal max_cnt, visited

        if max_cnt < level:
            max_cnt = level

        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < R and 0 <= nx < C:
                num = 1 << (board[ny][nx])
                if visited & num == 0:
                    visited += num
                    dfs(level+1, ny, nx)
                    visited -= num

    dfs(1, 0, 0)


    return max_cnt

print(main())




# 180504 KB / 5440 ms (Pypy)
def main():
    max_cnt = 1
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)

    ref = ord('A')
    alp_to_num = {chr(ref+i): 1 << i for i in range(26)}
    R, C = map(int, input().split())
    board = [list(map(lambda x: alp_to_num[x], input())) for _ in range(R)]

    visited = board[0][0]

    def dfs(level, y, x):
        nonlocal max_cnt, visited

        if max_cnt == 26:
            return

        if max_cnt < level:
            max_cnt = level

        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < R and 0 <= nx < C:
                num = board[ny][nx]
                if visited & num == 0:
                    visited += num
                    dfs(level+1, ny, nx)
                    visited -= num

    dfs(1, 0, 0)


    return max_cnt

print(main())





# 180504 KB / 5272 ms (Pypy)
def main():
    from sys import stdin

    new_input = stdin.readline
    max_cnt = 1
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)

    ref = ord('A')
    alp_to_num = {chr(ref+i): 1 << i for i in range(26)}
    R, C = map(int, new_input().split())
    board = [list(map(lambda x: alp_to_num[x], new_input().rstrip())) for _ in range(R)]

    visited = board[0][0]

    def dfs(level, y, x):
        nonlocal max_cnt, visited

        if max_cnt < level:
            max_cnt = level

        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < R and 0 <= nx < C:
                num = board[ny][nx]
                if visited & num == 0:
                    visited += num
                    dfs(level+1, ny, nx)
                    visited -= num

    dfs(1, 0, 0)


    return max_cnt

print(main())




# 112284 KB / 3876 ms (Pypy)
def main():
    max_cnt = 1
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)

    ref = ord('A')
    alp_to_num = {chr(ref+i): 1 << i for i in range(26)}
    R, C = map(int, input().split())
    board = [list(map(lambda x: alp_to_num[x], input())) for _ in range(R)]
    stack = [(0, 0, 1, board[0][0])]

    while stack:
        y, x, cnt, visited = stack.pop()

        if max_cnt == 26:
            return max_cnt

        if max_cnt < cnt:
            max_cnt = cnt

        new_cnt = cnt + 1
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < R and 0 <= nx < C:
                num = board[ny][nx]
                if visited & num == 0:
                    new_visited = visited + num
                    stack.append((ny, nx, new_cnt, new_visited))


    return max_cnt

print(main())





# 112284 KB / 3856 ms (Pypy)
def main():
    from sys import stdin

    new_input = stdin.readline
    max_cnt = 1
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)

    ref = ord('A')
    alp_to_num = {chr(ref+i): 1 << i for i in range(26)}
    R, C = map(int, new_input().split())
    board = [list(map(lambda x: alp_to_num[x], new_input().rstrip())) for _ in range(R)]
    stack = [(0, 0, 1, board[0][0])]

    while stack:
        y, x, cnt, visited = stack.pop()

        if max_cnt == 26:
            return max_cnt

        if max_cnt < cnt:
            max_cnt = cnt

        new_cnt = cnt + 1
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < R and 0 <= nx < C:
                num = board[ny][nx]
                if visited & num == 0:
                    new_visited = visited + num
                    stack.append((ny, nx, new_cnt, new_visited))


    return max_cnt

print(main())


