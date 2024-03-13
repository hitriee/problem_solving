# 240313
def solution(land):
    from collections import deque

    n, m = len(land), len(land[0])
    total_list = [0] * m
    visited = [[False] * m for _ in range(n)]
    dy, dx = [-1, 0, 1, 0], [0, -1, 0, 1]
    q = deque()

    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                size = 1
                q.append((i, j))
                x_set = {j}
                visited[i][j] = True
                while q:
                    y, x = q.popleft()
                    for k in range(4):
                        ny, nx = y + dy[k], x + dx[k]
                        if 0 <= ny < n and 0 <= nx < m and land[ny][nx] == 1 and not visited[ny][nx]:
                            size += 1
                            q.append((ny, nx))
                            visited[ny][nx] = True
                            x_set.add(nx)

                for x in x_set:
                    total_list[x] += size

    return max(total_list)