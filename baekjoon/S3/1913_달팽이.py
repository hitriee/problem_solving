#230420
# 1부터
N = int(input())
target = int(input())
y = x = N//2
delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cnt, i = 1, -1
table = [[0] * N for _ in range(N)]
while cnt <= N*N:
    table[y][x] = cnt
    cnt += 1
    ni = i + 1 if i < 3 else 0
    dy, dx = delta[ni]
    ny, nx = y+dy, x+dx
    if table[ny][nx] == 0:
        y, x = ny, nx
        i = ni
    else:
        dy, dx = delta[i]
        y, x = y+dy, x+dx
y = x = 0
for i in range(N):
    if y == 0:
        for j in range(N):
            if table[i][j] == target:
                y, x = i+1, j+1
    print(*table[i])
print(y, x)


# 1부터 + while문 target 기준으로 끊기
N = int(input())
target = int(input())
y = x = N//2
delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cnt, i = 1, -1
table = [[0] * N for _ in range(N)]
def fill_table(limit):
    global cnt, i, y, x
    while cnt < limit:
        table[y][x] = cnt
        cnt += 1
        ni = i + 1 if i < 3 else 0
        dy, dx = delta[ni]
        ny, nx = y+dy, x+dx
        if table[ny][nx] == 0:
            y, x = ny, nx
            i = ni
        else:
            dy, dx = delta[i]
            y, x = y+dy, x+dx
fill_table(target)
result = (y+1, x+1)
fill_table(N*N+1)
for i in range(N):
    print(*table[i])
print(*result)


# N * N 부터
N = int(input())
target = int(input())
y = x = 0
delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
cnt, i = N*N, 0
table = [[0] * N for _ in range(N)]
def fill_table(limit):
    global cnt, i, y, x
    while cnt > limit:
        table[y][x] = cnt
        cnt -= 1
        dy, dx = delta[i]
        ny, nx = y+dy, x+dx
        if 0 <= ny < N and 0 <= nx < N and table[ny][nx] == 0:
            y, x = ny, nx
        else:
            i = i+1 if i < 3 else 0
            dy, dx = delta[i]
            y, x = y+dy, x+dx
fill_table(target)
result = (y+1, x+1)
fill_table(0)
for i in range(N):
    print(*table[i])
print(*result)


# 함수형
def find_result():
    N = int(input())
    target = int(input())
    y = x = 0
    delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    cnt, i = N*N, 0
    table = [[0] * N for _ in range(N)]
    def fill_table(limit):
        nonlocal cnt, i, y, x
        while cnt > limit:
            table[y][x] = cnt
            cnt -= 1
            dy, dx = delta[i]
            ny, nx = y+dy, x+dx
            if 0 <= ny < N and 0 <= nx < N and table[ny][nx] == 0:
                y, x = ny, nx
            else:
                i = i+1 if i < 3 else 0
                dy, dx = delta[i]
                y, x = y+dy, x+dx
    fill_table(target)
    result = (y+1, x+1)
    fill_table(0)
    for i in range(N):
        print(*table[i])
    print(*result)
find_result()