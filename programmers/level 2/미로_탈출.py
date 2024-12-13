# 241213
def solution(maps):
    from collections import deque

    N, M = len(maps), len(maps[0])
    start = []
    positions = [[], []]
    min_time = 0
    for i in range(N):
        for j in range(M):
            val = maps[i][j]
            if val == 'S':
                start = [i, j]
            elif val == 'L':
                positions[0] = [i, j]
            elif val == 'E':
                positions[1] = [i, j]

    for idx in range(2):
        q = deque()
        visited = [[False] * M for _ in range(N)]
        visited[start[0]][start[1]] = True
        q.append((*start, min_time))
        final_y, final_x = positions[idx]

        while q:
            y, x, time = q.popleft()
            if y == final_y and x == final_x:
                min_time = time
                start = [final_y, final_x]
                break

            for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < M:
                    if not visited[ny][nx] and maps[ny][nx] != 'X':
                        visited[ny][nx] = True
                        q.append((ny, nx, time + 1))

        else:
            return -1

    return min_time