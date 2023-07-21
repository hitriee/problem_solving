#230721
from sys import stdin
new_input = stdin.readline
R, C = map(int, new_input().split())
field = [new_input().rstrip() for _ in range(R)]
visited = [[False]*C for _ in range(R)]
lamb_wolves = [0, 0]

def in_fence(option, *initial):
    from collections import deque
    q = deque()
    q.append(initial)
    temp_lamb_wolves = [0, 0]
    temp_lamb_wolves[option] = 1
    while q:
        y, x = q.popleft()
        for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
            ny, nx = y+dy, x+dx
            if 0 <= ny < R and 0 <= nx < C:
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    value = field[ny][nx]
                    if value == 'v':
                        temp_lamb_wolves[1] += 1
                        q.append((ny, nx))
                    elif value == 'k':
                        temp_lamb_wolves[0] += 1
                        q.append((ny, nx))
                    elif value == '.':
                        q.append((ny, nx))

    lamb, wolves = temp_lamb_wolves
    if lamb > wolves:
        lamb_wolves[0] += lamb
    else:
        lamb_wolves[1] += wolves


for i in range(R):
    for j in range(C):
        if not visited[i][j]:
            if field[i][j] == 'k':
                visited[i][j] = True
                in_fence(0, i, j)
            elif field[i][j] == 'v':
                visited[i][j] = True
                in_fence(1, i, j)

print(*lamb_wolves)


#
def find_lamb_wolves():
    from sys import stdin
    new_input = stdin.readline
    R, C = map(int, new_input().split())
    field = [new_input().rstrip() for _ in range(R)]
    visited = [[False] * C for _ in range(R)]
    lamb_wolves = [0, 0]

    def in_fence(option, *initial):
        from collections import deque
        q = deque()
        q.append(initial)
        temp_lamb_wolves = [0, 0]
        temp_lamb_wolves[option] = 1
        while q:
            y, x = q.popleft()
            for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
                ny, nx = y + dy, x + dx
                if 0 <= ny < R and 0 <= nx < C:
                    if not visited[ny][nx]:
                        visited[ny][nx] = True
                        value = field[ny][nx]
                        if value == 'v':
                            temp_lamb_wolves[1] += 1
                            q.append((ny, nx))
                        elif value == 'k':
                            temp_lamb_wolves[0] += 1
                            q.append((ny, nx))
                        elif value == '.':
                            q.append((ny, nx))

        lamb, wolves = temp_lamb_wolves
        if lamb > wolves:
            lamb_wolves[0] += lamb
        else:
            lamb_wolves[1] += wolves

    for i in range(R):
        for j in range(C):
            if not visited[i][j]:
                if field[i][j] == 'k':
                    visited[i][j] = True
                    in_fence(0, i, j)
                elif field[i][j] == 'v':
                    visited[i][j] = True
                    in_fence(1, i, j)

    return lamb_wolves

print(*find_lamb_wolves())