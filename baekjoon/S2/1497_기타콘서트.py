#230405
# bfs
from collections import deque
N, M = map(int, input().split())
guitar = deque()
for i in range(N):
    key, value = input().split()
    value_set = set()
    for j in range(M):
        if value[j] == 'Y':
            value_set.add(j)
    if value_set:
        guitar.append((i, key, value_set, 1))
total_guitar = list(guitar)
length = len(guitar)
max_song = guitar_cnt = 0
while guitar:
    start, name, possible, cnt = guitar.popleft()
    song = len(possible)
    if max_song < song:
        max_song = song
        guitar_cnt = cnt
    elif max_song == song and guitar_cnt > cnt:
        guitar_cnt = cnt
    for i in range(start+1, length):
        guitar.append((i, name, possible | total_guitar[i][2], cnt+1))
else:
    if max_song:
        print(guitar_cnt)
    else:
        print(-1)

# 불필요한 부분 삭제
from collections import deque
N, M = map(int, input().split())
guitar = deque()
for i in range(N):
    value = input().split()[1]
    value_set = set()
    for j in range(M):
        if value[j] == 'Y':
            value_set.add(j)
    if value_set:
        guitar.append((i, value_set, 1))
total_guitar = list(guitar)
length = len(guitar)
max_song = guitar_cnt = 0
while guitar:
    start, possible, cnt = guitar.popleft()
    song = len(possible)
    if max_song < song:
        max_song = song
        guitar_cnt = cnt
    elif max_song == song and guitar_cnt > cnt:
        guitar_cnt = cnt
    for i in range(start+1, length):
        guitar.append((i, possible | total_guitar[i][1], cnt+1))
else:
    if max_song:
        print(guitar_cnt)
    else:
        print(-1)

# bfs 함수형
def find_guitar_cnt():
    N, M = map(int, input().split())
    total_guitar = []
    for i in range(N):
        value = input().split()[1]
        value_set = set()
        for j in range(M):
            if value[j] == 'Y':
                value_set.add(j)
        if value_set:
            total_guitar.append((i, value_set, 1))
    def bfs():
        from collections import deque
        guitar = deque(total_guitar)
        length = len(guitar)
        max_song = guitar_cnt = 0
        while guitar:
            start, possible, cnt = guitar.popleft()
            song = len(possible)
            if max_song < song:
                max_song = song
                guitar_cnt = cnt
            elif max_song == song and guitar_cnt > cnt:
                guitar_cnt = cnt
            for i in range(start+1, length):
                guitar.append((i, possible | total_guitar[i][1], cnt+1))
        return guitar_cnt if max_song else -1
    return bfs()
print(find_guitar_cnt())

# dfs
N, M = map(int, input().split())
guitar = []
for i in range(N):
    key, value = input().split()
    value_set = set()
    for j in range(M):
        if value[j] == 'Y':
            value_set.add(j)
    if value_set:
        guitar.append(value_set)
length = len(guitar)
max_song, guitar_cnt = 0, length

def dfs(level, start, song):
    global max_song, guitar_cnt, total_song
    if max_song < song:
        max_song = song
        guitar_cnt = level
    elif max_song == song and guitar_cnt > level:
        guitar_cnt = level
    for j in range(start, length):
        temp_song = set(total_song)
        total_song = total_song.union(guitar[j])
        dfs(level+1, j+1, len(total_song))
        total_song = set(temp_song)

for i in range(length):
    total_song = set(guitar[i])
    dfs(1, i+1, len(total_song))
if max_song:
    print(guitar_cnt)
else:
    print(-1)


# 함수화
def find_guitar_cnt():
    N, M = map(int, input().split())
    guitar = []
    for i in range(N):
        key, value = input().split()
        value_set = set()
        for j in range(M):
            if value[j] == 'Y':
                value_set.add(j)
        if value_set:
            guitar.append(value_set)
    length = len(guitar)
    max_song, guitar_cnt = 0, length

    def dfs(level, start, song):
        nonlocal max_song, guitar_cnt, total_song
        if max_song < song:
            max_song = song
            guitar_cnt = level
        elif max_song == song and guitar_cnt > level:
            guitar_cnt = level
        for j in range(start, length):
            temp_song = set(total_song)
            total_song = total_song.union(guitar[j])
            dfs(level+1, j+1, len(total_song))
            total_song = set(temp_song)

    for i in range(length):
        total_song = set(guitar[i])
        dfs(1, i+1, len(total_song))

    return guitar_cnt if max_song else -1
print(find_guitar_cnt())


# sort
def find_guitar_cnt():
    N, M = map(int, input().split())
    guitar = []
    for i in range(N):
        key, value = input().split()
        value_set = set()
        for j in range(M):
            if value[j] == 'Y':
                value_set.add(j)
        if value_set:
            guitar.append(value_set)
    guitar.sort(key= lambda x: len(x))
    length = len(guitar)
    max_song, guitar_cnt = 0, length

    def dfs(level, start, song):
        nonlocal max_song, guitar_cnt, total_song
        if max_song < song:
            max_song = song
            guitar_cnt = level
        elif max_song == song and guitar_cnt > level:
            guitar_cnt = level
        for j in range(start, length):
            temp_song = set(total_song)
            total_song = total_song.union(guitar[j])
            dfs(level+1, j+1, len(total_song))
            total_song = set(temp_song)

    for i in range(length):
        total_song = set(guitar[i])
        dfs(1, i+1, len(total_song))

    return guitar_cnt if max_song else -1
print(find_guitar_cnt())