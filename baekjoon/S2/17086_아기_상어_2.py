#230404
# bfs
from collections import deque
N, M = map(int, input().split())
space, baby_shark, position = [], deque(), set()
for i in range(N):
    row = input().split()
    space.append(row)
    for j in range(M):
        if row[j] == '1':
            baby_shark.append((i, j, 0))
        else:
            position.add((i, j))
direct = []
for i in range(-1, 2):
    for j in range(-1, 2):
        direct.append((i, j))
direct.remove((0, 0))

while baby_shark:
    y, x, cnt = baby_shark.popleft()
    for dy, dx in direct:
        new_position = (y+dy, x+dx)
        if new_position in position:
            position.remove(new_position)
            baby_shark.append((*new_position, cnt+1))
print(cnt)

# 함수화
def return_cnt():
    from collections import deque
    N, M = map(int, input().split())
    space, baby_shark, position = [], deque(), set()
    for i in range(N):
        row = input().split()
        space.append(row)
        for j in range(M):
            if row[j] == '1':
                baby_shark.append((i, j, 0))
            else:
                position.add((i, j))
    direct = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            direct.append((i, j))
    direct.remove((0, 0))

    while baby_shark:
        y, x, cnt = baby_shark.popleft()
        for dy, dx in direct:
            new_position = (y + dy, x + dx)
            if new_position in position:
                position.remove(new_position)
                baby_shark.append((*new_position, cnt + 1))
    return cnt

print(return_cnt())

# flood fill
def return_cnt():
    from collections import deque
    N, M = map(int, input().split())
    space, baby_shark, position = [], deque(), set()
    for i in range(N):
        space.append(input().split())
        for j in range(M):
            if space[i][j] == '1':
                baby_shark.append((i, j, 0))
                space[i][j] = 0

    direct = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            direct.append((i, j))
    direct.remove((0, 0))

    while baby_shark:
        y, x, cnt = baby_shark.popleft()
        for dy, dx in direct:
            ny, nx = y+dy, x+dx
            if 0 <= ny < N and 0 <= nx < M and type(space[ny][nx]) == str:
                baby_shark.append((ny, nx, cnt+1))
                space[ny][nx] = cnt+1
    return cnt
print(return_cnt())


# space 리스트 없애기
def return_cnt():
    from collections import deque
    N, M = map(int, input().split())
    baby_shark, position = deque(), set()
    for i in range(N):
        row = input().split()
        for j in range(M):
            if row[j] == '1':
                baby_shark.append((i, j, 0))
            else:
                position.add((i, j))
    direct = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            direct.append((i, j))
    direct.remove((0, 0))

    while baby_shark:
        y, x, cnt = baby_shark.popleft()
        for dy, dx in direct:
            new_position = (y+dy, x+dx)
            if new_position in position:
                position.remove(new_position)
                baby_shark.append((*new_position, cnt+1))
    return cnt
print(return_cnt())