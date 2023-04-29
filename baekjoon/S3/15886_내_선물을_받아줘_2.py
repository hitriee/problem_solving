#230429
N = int(input())
map_info = input()
visited = [False] * N
cnt = 0
for i in range(N):
    if not visited[i]:
        if map_info[i] == 'E':
            cnt += 1
            j = i + 1
        else:
            j = i - 1
        while not visited[j]:
            visited[j] = True
            j += 1 if map_info[j] == 'E' else -1
print(cnt)


# 함수화
def cnt_position():
    N = int(input())
    map_info = input()
    visited = [False] * N
    cnt = 0
    for i in range(N):
        if not visited[i]:
            if map_info[i] == 'E':
                cnt += 1
                j = i + 1
            else:
                j = i - 1
            while not visited[j]:
                visited[j] = True
                j += 1 if map_info[j] == 'E' else -1
    return cnt
print(cnt_position())


# continue
N = int(input())
map_info = input()
visited = [False] * N
cnt = 0
for i in range(N):
    if visited[i]:
        continue
    if map_info[i] == 'E':
        cnt += 1
        j = i + 1
    else:
        j = i - 1
    while not visited[j]:
        visited[j] = True
        j += 1 if map_info[j] == 'E' else -1
print(cnt)


# visited = True
N = int(input())
map_info = input()
visited = [False] * N
cnt = 0
for i in range(N):
    if visited[i]:
        continue
    visited[i] = True
    if map_info[i] == 'E':
        cnt += 1
        j = i + 1
    else:
        j = i - 1
    while not visited[j]:
        visited[j] = True
        j += 1 if map_info[j] == 'E' else -1
print(cnt)

#
N = int(input())
map_info = input()
visited = [False] * N
cnt = 0
for i in range(N):
    if not visited[i]:
        visited[i] = True
        if map_info[i] == 'E':
            cnt += 1
            j = i + 1
        else:
            j = i - 1
        while not visited[j]:
            visited[j] = True
            j += 1 if map_info[j] == 'E' else -1
print(cnt)

#
def cnt_position():
    N = int(input())
    map_info = input()
    visited = [False] * N
    cnt = 0
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            if map_info[i] == 'E':
                cnt += 1
                j = i + 1
            else:
                j = i - 1
            while not visited[j]:
                visited[j] = True
                j += 1 if map_info[j] == 'E' else -1
    return cnt
print(cnt_position())


#
def cnt_position():
    N = int(input())
    map_info = input()
    visited = [False] * N
    cnt = 0
    for i in range(N):
        if visited[i]:
            continue
        visited[i] = True
        if map_info[i] == 'E':
            cnt += 1
            j = i + 1
        else:
            j = i - 1
        while not visited[j]:
            visited[j] = True
            j += 1 if map_info[j] == 'E' else -1
    return cnt
print(cnt_position())