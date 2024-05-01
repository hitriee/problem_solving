# 240501
def solution(dirs):
    length = 0
    visited = [[[False] * 4 for _ in range(11)] for _ in range(11)]

    x = y = 5
    dir_to_delta = {
        'U': (-1, 0),
        'D': (1, 0),
        'R': (0, 1),
        'L': (0, -1),
    }
    dir_to_i = {
        'U': 0,
        'L': 1,
        'R': 2,
        'D': 3,
    }

    for direction in dirs:
        dy, dx = dir_to_delta[direction]
        ny, nx = y + dy, x + dx
        if 0 <= ny < 11 and 0 <= nx < 11:
            i = dir_to_i[direction]
            if not visited[y][x][i]:
                length += 1
                visited[y][x][i] = True
                visited[ny][nx][3 - i] = True
            y, x = ny, nx

    return length