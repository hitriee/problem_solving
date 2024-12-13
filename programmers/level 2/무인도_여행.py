# 241213
def solution(maps):
    from collections import deque

    N, M = len(maps), len(maps[0])
    answer = []
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    visited = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            val = maps[i][j]
            if val != 'X' and not visited[i][j]:
                q = deque()
                visited[i][j] = True
                q.append((i, j))
                day = int(val)

                while q:
                    y, x = q.popleft()
                    for idx in range(4):
                        ny, nx = y + dy[idx], x + dx[idx]
                        if 0 <= ny < N and 0 <= nx < M:
                            val = maps[ny][nx]
                            if not visited[ny][nx] and val != 'X':
                                visited[ny][nx] = True
                                day += int(val)
                                q.append((ny, nx))

                answer.append(day)

    if answer:
        return sorted(answer)

    return [-1]