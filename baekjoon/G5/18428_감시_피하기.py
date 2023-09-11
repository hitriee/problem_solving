#230911
N = int(input())
area = [input().split() for _ in range(N)]
visited = [[False] * N for _ in range(N)]
teachers = []
answer = 'NO'
for i in range(N):
    for j in range(N):
        if area[i][j] == 'T':
            teachers.append((i, j))

def dfs(level, before_i, before_j):
    global answer
    if answer == 'YES':
        return
    if level == 3:
        has_student = False
        for y, x in teachers:
            for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
                ny, nx = y+dy, x+dx
                while 0 <= ny < N and 0 <= nx < N:
                    if area[ny][nx] == 'S':
                        has_student = True
                        break
                    if area[ny][nx] == 'O':
                        break
                    ny += dy
                    nx += dx
                else:
                    continue
                if has_student:
                    return
        answer = 'YES'
        return

    for j in range(before_j+1, N):
        if area[before_i][j] == 'X' and not visited[before_i][j]:
            area[before_i][j] = 'O'
            dfs(level+1, before_i, j)
            area[before_i][j] = 'X'

    for i in range(before_i+1, N):
        for j in range(N):
            if area[i][j] == 'X' and not visited[i][j]:
                area[i][j] = 'O'
                dfs(level+1, i, j)
                area[i][j] = 'X'

dfs(0, 0, -1)

print(answer)


#
N = int(input())
area = [input().split() for _ in range(N)]
visited = [[False] * N for _ in range(N)]
teachers = []
answer = 'NO'
for i in range(N):
    for j in range(N):
        if area[i][j] == 'T':
            teachers.append((i, j))

def dfs(level, before_i, before_j):
    global answer
    if answer == 'YES':
        return
    if level == 3:
        for y, x in teachers:
            for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
                ny, nx = y+dy, x+dx
                while 0 <= ny < N and 0 <= nx < N:
                    if area[ny][nx] == 'S':
                        return
                    if area[ny][nx] == 'O':
                        break
                    ny += dy
                    nx += dx

        answer = 'YES'
        return

    for j in range(before_j+1, N):
        if area[before_i][j] == 'X' and not visited[before_i][j]:
            area[before_i][j] = 'O'
            dfs(level+1, before_i, j)
            area[before_i][j] = 'X'

    for i in range(before_i+1, N):
        for j in range(N):
            if area[i][j] == 'X' and not visited[i][j]:
                area[i][j] = 'O'
                dfs(level+1, i, j)
                area[i][j] = 'X'

dfs(0, 0, -1)

print(answer)


#
N = int(input())
area = [input().split() for _ in range(N)]
visited = [[False] * N for _ in range(N)]
teachers = []
answer = 'NO'
for i in range(N):
    for j in range(N):
        if area[i][j] == 'T':
            teachers.append((i, j))

def dfs(level, before_i, before_j):
    global answer
    if answer == 'YES':
        return
    if level == 3:
        for y, x in teachers:
            for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
                ny, nx = y+dy, x+dx
                while 0 <= ny < N and 0 <= nx < N and area[ny][nx] != 'O':
                    if area[ny][nx] == 'S':
                        return
                    ny += dy
                    nx += dx

        answer = 'YES'
        return

    for j in range(before_j+1, N):
        if area[before_i][j] == 'X' and not visited[before_i][j]:
            area[before_i][j] = 'O'
            dfs(level+1, before_i, j)
            area[before_i][j] = 'X'

    for i in range(before_i+1, N):
        for j in range(N):
            if area[i][j] == 'X' and not visited[i][j]:
                area[i][j] = 'O'
                dfs(level+1, i, j)
                area[i][j] = 'X'

dfs(0, 0, -1)

print(answer)


#
N = int(input())
area = [input().split() for _ in range(N)]
teachers = []
answer = 'NO'
for i in range(N):
    for j in range(N):
        if area[i][j] == 'T':
            teachers.append((i, j))

def dfs(level, before_i, before_j):
    global answer
    if answer == 'YES':
        return
    if level == 3:
        for y, x in teachers:
            for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
                ny, nx = y+dy, x+dx
                while 0 <= ny < N and 0 <= nx < N and area[ny][nx] != 'O':
                    if area[ny][nx] == 'S':
                        return
                    ny += dy
                    nx += dx

        answer = 'YES'
        return

    for j in range(before_j+1, N):
        if area[before_i][j] == 'X':
            area[before_i][j] = 'O'
            dfs(level+1, before_i, j)
            area[before_i][j] = 'X'

    for i in range(before_i+1, N):
        for j in range(N):
            if area[i][j] == 'X':
                area[i][j] = 'O'
                dfs(level+1, i, j)
                area[i][j] = 'X'

dfs(0, 0, -1)

print(answer)


#
N = int(input())
area = [input().split() for _ in range(N)]
teachers = []
answer = 'NO'
for i in range(N):
    for j in range(N):
        if area[i][j] == 'T':
            teachers.append((i, j))

def dfs(level, before_i, before_j):
    global answer
    if answer == 'YES':
        return
    if level == 3:
        has_student = False
        for y, x in teachers:
            for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
                ny, nx = y+dy, x+dx
                while 0 <= ny < N and 0 <= nx < N:
                    if area[ny][nx] == 'S':
                        has_student = True
                        break
                    if area[ny][nx] == 'O':
                        break
                    ny += dy
                    nx += dx
                else:
                    continue
                if has_student:
                    return
        answer = 'YES'
        return

    for j in range(before_j+1, N):
        if area[before_i][j] == 'X':
            area[before_i][j] = 'O'
            dfs(level+1, before_i, j)
            area[before_i][j] = 'X'

    for i in range(before_i+1, N):
        for j in range(N):
            if area[i][j] == 'X':
                area[i][j] = 'O'
                dfs(level+1, i, j)
                area[i][j] = 'X'

dfs(0, 0, -1)

print(answer)


#
def is_possible():
    N = int(input())
    area = [input().split() for _ in range(N)]
    teachers = []
    answer = 'NO'
    for i in range(N):
        for j in range(N):
            if area[i][j] == 'T':
                teachers.append((i, j))

    def dfs(level, before_i, before_j):
        nonlocal answer
        if answer == 'YES':
            return
        if level == 3:
            for y, x in teachers:
                for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
                    ny, nx = y + dy, x + dx
                    while 0 <= ny < N and 0 <= nx < N and area[ny][nx] != 'O':
                        if area[ny][nx] == 'S':
                            return
                        ny += dy
                        nx += dx

            answer = 'YES'
            return

        for j in range(before_j + 1, N):
            if area[before_i][j] == 'X':
                area[before_i][j] = 'O'
                dfs(level + 1, before_i, j)
                area[before_i][j] = 'X'

        for i in range(before_i + 1, N):
            for j in range(N):
                if area[i][j] == 'X':
                    area[i][j] = 'O'
                    dfs(level + 1, i, j)
                    area[i][j] = 'X'

    dfs(0, 0, -1)

    return answer

print(is_possible())
