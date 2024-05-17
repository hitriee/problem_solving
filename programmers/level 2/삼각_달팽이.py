# 240517
def solution(n):
    triangle = [[0] * (i + 1) for i in range(n)]
    dy, dx = (1, 0, -1), (0, 1, -1)
    y = x = idx = 0
    limit = ((n + 1) * n) // 2

    for i in range(1, limit + 1):
        triangle[y][x] = i

        for _ in range(2):
            ny, nx = y + dy[idx], x + dx[idx]
            if 0 <= ny < n and 0 <= nx <= ny and triangle[ny][nx] == 0:
                y, x = ny, nx
                break

            idx = (idx + 1) % 3

        else:
            y, x = y + dy[idx], x + dx[idx]

    answer = []
    for i in range(n):
        answer.extend(triangle[i])

    return answer