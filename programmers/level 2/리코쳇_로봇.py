# 240530
def init(board, n, m):
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                return (i, j)

def solution(board):
    from collections import deque
    n, m = len(board), len(board[0])
    visited = [[False] * m for _ in range(n)]
    dy, dx = [1, 0, 0, -1], [0, -1, 1, 0]
    q = deque()

    y, x = init(board, n, m)
    visited[y][x] = True
    q.append((y, x, -1, 0))

    while q:
        y, x, idx, cnt = q.popleft()
        if board[y][x] == 'G':
            return cnt

        cnt += 1

        for i in range(4):
            if i != idx:
                del_y, del_x = dy[i], dx[i]
                nny = ny = y
                nnx = nx = x
                while True:
                    nny += del_y
                    nnx += del_x
                    if 0 <= nny < n and 0 <= nnx < m and board[nny][nnx] != 'D':
                        ny += del_y
                        nx += del_x
                    else:
                        break

                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    if board[ny][nx] != 'D':
                        q.append((ny, nx, i, cnt))

    return -1

print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))

'''
테스트 1 〉	통과 (5.71ms, 10.1MB)
테스트 2 〉	통과 (3.48ms, 10.2MB)
테스트 3 〉	통과 (0.38ms, 10.4MB)
테스트 4 〉	통과 (2.22ms, 10.4MB)
테스트 5 〉	통과 (1.40ms, 10.4MB)
테스트 6 〉	통과 (0.27ms, 10.2MB)
테스트 7 〉	통과 (10.99ms, 10.2MB)
테스트 8 〉	통과 (1.25ms, 10.4MB)
테스트 9 〉	통과 (2.30ms, 10.3MB)
테스트 10 〉	통과 (5.06ms, 10.3MB)
테스트 11 〉	통과 (0.07ms, 10.3MB)
테스트 12 〉	통과 (0.04ms, 10.2MB)
테스트 13 〉	통과 (0.07ms, 10.2MB)
테스트 14 〉	통과 (0.38ms, 10.2MB)
테스트 15 〉	통과 (0.28ms, 10.2MB)
테스트 16 〉	통과 (2.40ms, 10.2MB)
테스트 17 〉	통과 (0.73ms, 10.2MB)
테스트 18 〉	통과 (0.48ms, 10.3MB)
테스트 19 〉	통과 (1.95ms, 10.2MB)
테스트 20 〉	통과 (0.09ms, 10.2MB)
테스트 21 〉	통과 (6.70ms, 10.2MB)
테스트 22 〉	통과 (0.85ms, 10.3MB)
테스트 23 〉	통과 (0.49ms, 10.4MB)
테스트 24 〉	통과 (7.04ms, 10.3MB)
테스트 25 〉	통과 (2.77ms, 10.3MB)
테스트 26 〉	통과 (2.22ms, 10.3MB)
테스트 27 〉	통과 (0.73ms, 10.2MB)
'''


#
def init(board, n, m):
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                return (i, j)

def solution(board):
    from collections import deque
    n, m = len(board), len(board[0])
    visited = [[False] * m for _ in range(n)]
    dy, dx = [1, 0, 0, -1], [0, -1, 1, 0]
    q = deque()

    y, x = init(board, n, m)
    visited[y][x] = True
    q.append((y, x, -1, 0))

    while q:
        y, x, idx, cnt = q.popleft()
        if board[y][x] == 'G':
            return cnt

        cnt += 1

        for i in range(4):
            if i != idx:
                del_y, del_x = dy[i], dx[i]
                nny = ny = y
                nnx = nx = x
                while True:
                    nny += del_y
                    nnx += del_x
                    if 0 <= nny < n and 0 <= nnx < m and board[nny][nnx] != 'D':
                        ny += del_y
                        nx += del_x
                    else:
                        break

                if not visited[ny][nx] and board[ny][nx] != 'D':
                    visited[ny][nx] = True
                    q.append((ny, nx, i, cnt))

    return -1

'''
테스트 1 〉	통과 (4.58ms, 10.2MB)
테스트 2 〉	통과 (3.55ms, 10.4MB)
테스트 3 〉	통과 (0.76ms, 10.2MB)
테스트 4 〉	통과 (2.52ms, 10.3MB)
테스트 5 〉	통과 (1.28ms, 10.1MB)
테스트 6 〉	통과 (0.28ms, 10.3MB)
테스트 7 〉	통과 (5.64ms, 10.3MB)
테스트 8 〉	통과 (0.66ms, 10.3MB)
테스트 9 〉	통과 (2.02ms, 10.3MB)
테스트 10 〉	통과 (3.35ms, 10.2MB)
테스트 11 〉	통과 (0.07ms, 10.2MB)
테스트 12 〉	통과 (0.04ms, 10.3MB)
테스트 13 〉	통과 (0.07ms, 10.4MB)
테스트 14 〉	통과 (0.71ms, 10.2MB)
테스트 15 〉	통과 (0.22ms, 10.3MB)
테스트 16 〉	통과 (2.94ms, 10.3MB)
테스트 17 〉	통과 (0.42ms, 10.4MB)
테스트 18 〉	통과 (0.45ms, 10.2MB)
테스트 19 〉	통과 (4.03ms, 10.3MB)
테스트 20 〉	통과 (0.09ms, 10.3MB)
테스트 21 〉	통과 (5.54ms, 10.3MB)
테스트 22 〉	통과 (1.08ms, 10.3MB)
테스트 23 〉	통과 (0.29ms, 10.4MB)
테스트 24 〉	통과 (11.15ms, 10.2MB)
테스트 25 〉	통과 (2.21ms, 10.2MB)
테스트 26 〉	통과 (2.63ms, 10.3MB)
테스트 27 〉	통과 (1.10ms, 10.4MB)
'''