#230922
N = int(input())
picture = [input() for _ in range(N)]
visited = [[False] * N for _ in range(N)]
section_list = [0] * 2

def find_section(possible_set, *start):
    from collections import deque
    q = deque()
    q.append(start)
    while q:
        y, x = q.popleft()
        for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
            ny, nx = y+dy, x+dx
            if 0 <= ny < N and 0 <= nx < N:
                if picture[ny][nx] in possible_set and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((ny, nx))
    return

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            pixel = picture[i][j]
            cnt = find_section({pixel}, i, j)
            section_list[0] += 1
            if pixel == 'B':
                section_list[1] += 1

visited = [[False] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            if picture[i][j] != 'B':
                cnt = find_section({'R', 'G'}, i, j)
                section_list[1] += 1

print(*section_list)

#
N = int(input())
picture = [input() for _ in range(N)]
visited = [[False] * N for _ in range(N)]
section_list = [0] * 2

def find_section(possible_set, *start):
    from collections import deque
    q = deque()
    q.append(start)
    while q:
        y, x = q.popleft()
        for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
            ny, nx = y+dy, x+dx
            if 0 <= ny < N and 0 <= nx < N:
                if picture[ny][nx] in possible_set and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((ny, nx))
    return

# B, 적록색약이 아닌 사람
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            pixel = picture[i][j]
            find_section({pixel}, i, j)
            section_list[0] += 1
            if pixel == 'B':
                section_list[1] += 1

visited = [[False] * N for _ in range(N)]

# 적록색약인 사람의 R, G
for i in range(N):
    for j in range(N):
        if picture[i][j] != 'B' and not visited[i][j]:
            find_section({'R', 'G'}, i, j)
            section_list[1] += 1

print(*section_list)


#
N = int(input())
picture = [input() for _ in range(N)]
visited = [[0] * N for _ in range(N)]
section_list = [0] * 2

def find_section(possible_set, ref, *start):
    from collections import deque
    q = deque()
    q.append(start)
    while q:
        y, x = q.popleft()
        for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
            ny, nx = y+dy, x+dx
            if 0 <= ny < N and 0 <= nx < N:
                if picture[ny][nx] in possible_set and visited[ny][nx] == ref:
                    visited[ny][nx] += 1
                    q.append((ny, nx))
    return

# B, 적록색약이 아닌 사람
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            visited[i][j] += 1
            pixel = picture[i][j]
            section_list[0] += 1
            if pixel == 'B':
                section_list[1] += 1
            find_section({pixel}, 0, i, j)

# 적록색약인 사람의 R, G
for i in range(N):
    for j in range(N):
        if picture[i][j] != 'B' and visited[i][j] == 1:
            visited[i][j] += 1
            section_list[1] += 1
            find_section({'R', 'G'}, 1, i, j)

print(*section_list)


#
def cnt_section():
    N = int(input())
    picture = [input() for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    section_list = [0] * 2

    def find_section(possible_set, ref, *start):
        from collections import deque
        q = deque()
        q.append(start)
        while q:
            y, x = q.popleft()
            for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < N:
                    if picture[ny][nx] in possible_set and visited[ny][nx] == ref:
                        visited[ny][nx] += 1
                        q.append((ny, nx))
        return

    # B, 적록색약이 아닌 사람
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] += 1
                pixel = picture[i][j]
                section_list[0] += 1
                if pixel == 'B':
                    section_list[1] += 1
                find_section({pixel}, 0, i, j)

    # 적록색약인 사람의 R, G
    for i in range(N):
        for j in range(N):
            if picture[i][j] != 'B' and visited[i][j] == 1:
                visited[i][j] += 1
                section_list[1] += 1
                find_section({'R', 'G'}, 1, i, j)

    return f'{section_list[0]} {section_list[1]}'

print(cnt_section())


#
N = int(input())
picture = [input() for _ in range(N)]
visited = [[0] * N for _ in range(N)]
section_list = [0] * 2

def find_section(possible_set, ref, *start):
    from collections import deque
    q = deque()
    q.append(start)
    while q:
        y, x = q.popleft()
        for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
            ny, nx = y+dy, x+dx
            if 0 <= ny < N and 0 <= nx < N:
                if picture[ny][nx] in possible_set and visited[ny][nx] == ref:
                    visited[ny][nx] += 1
                    q.append((ny, nx))
    return

# B, 적록색약이 아닌 사람
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            visited[i][j] += 1
            pixel = picture[i][j]
            section_list[0] += 1
            if pixel == 'B':
                section_list[1] += 1
            find_section({pixel}, 0, i, j)

# 적록색약인 사람의 R, G
for i in range(N):
    for j in range(N):
        if picture[i][j] != 'B' and visited[i][j] == 1:
            visited[i][j] += 1
            section_list[1] += 1
            find_section({'R', 'G'}, 1, i, j)

print(*section_list)


#
def cnt_section():
    N = int(input())
    picture = [input() for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    section_list = [0] * 2

    def find_section(possible_set, ref, plus, *start):
        from collections import deque
        q = deque()
        q.append(start)
        while q:
            y, x = q.popleft()
            for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < N:
                    if picture[ny][nx] in possible_set and visited[ny][nx] == ref:
                        visited[ny][nx] += plus
                        q.append((ny, nx))
        return

    # B, 적록색약이 아닌 사람
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                pixel = picture[i][j]
                section_list[0] += 1
                if pixel == 'B':
                    visited[i][j] += 2
                    section_list[1] += 1
                    find_section({pixel}, 0, 2, i, j)
                else:
                    visited[i][j] += 1
                    find_section({pixel}, 0, 1, i, j)

    # 적록색약인 사람의 R, G
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 1:
                visited[i][j] += 1
                section_list[1] += 1
                find_section({'R', 'G'}, 1, 1, i, j)

    return f'{section_list[0]} {section_list[1]}'

print(cnt_section())