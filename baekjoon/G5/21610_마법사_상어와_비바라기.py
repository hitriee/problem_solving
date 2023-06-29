#230629
from sys import stdin

def to_int(): return map(int, stdin.readline().split())
def multiply(num1, num2): return num1*num2

N, M = to_int()
bucket_list = [list(to_int()) for _ in range(N)]
cloud = {(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)}
direction = [(), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
cross = [(-1, -1), (-1, 1), (1, 1), (1, -1)]

for _ in range(M):
    d, s = to_int()
    after_move = set()
    dy, dx = map(multiply, direction[d], [s]*2)
    temp_cloud = set()
    while cloud:
        y, x = cloud.pop()
        ny, nx = (y+dy)%N, (x+dx)%N
        bucket_list[ny][nx] += 1
        after_move.add((ny, nx))

    for y, x in after_move:
        cnt = 0
        for dy, dx in cross:
            cross_y, cross_x = y+dy, x+dx
            if 0 <= cross_y < N and 0 <= cross_x < N and bucket_list[cross_y][cross_x]:
                cnt += 1
        bucket_list[y][x] += cnt

    for i in range(N):
        for j in range(N):
            if bucket_list[i][j] >= 2 and (i, j) not in after_move:
                bucket_list[i][j] -= 2
                cloud.add((i, j))

total = 0
for i in range(N):
    for j in range(N):
        total += bucket_list[i][j]

print(total)


#
def amount_of_water():
    from sys import stdin

    def to_int(): return map(int, stdin.readline().split())
    def multiply(num1, num2): return num1*num2

    N, M = to_int()
    bucket_list = [list(to_int()) for _ in range(N)]
    cloud = {(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)}
    direction = [(), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
    cross = [(-1, -1), (-1, 1), (1, 1), (1, -1)]

    for _ in range(M):
        d, s = to_int()
        after_move = set()
        dy, dx = map(multiply, direction[d], [s]*2)
        while cloud:
            y, x = cloud.pop()
            ny, nx = (y+dy)%N, (x+dx)%N
            bucket_list[ny][nx] += 1
            after_move.add((ny, nx))

        for y, x in after_move:
            cnt = 0
            for dy, dx in cross:
                cross_y, cross_x = y+dy, x+dx
                if 0 <= cross_y < N and 0 <= cross_x < N and bucket_list[cross_y][cross_x]:
                    cnt += 1
            bucket_list[y][x] += cnt

        for i in range(N):
            for j in range(N):
                if bucket_list[i][j] >= 2 and (i, j) not in after_move:
                    bucket_list[i][j] -= 2
                    cloud.add((i, j))

    total = 0
    for i in range(N):
        for j in range(N):
            total += bucket_list[i][j]

    return total

print(amount_of_water())


#
def amount_of_water():
    from sys import stdin

    def to_int():
        return map(int, stdin.readline().split())

    def multiply(num1, num2):
        return num1 * num2

    N, M = to_int()
    bucket_list = [list(to_int()) for _ in range(N)]
    cloud = {(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)}
    direction = [(), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
    cross = [(-1, -1), (-1, 1), (1, 1), (1, -1)]

    def change_arr():
        d, s = to_int()
        after_move = set()
        dy, dx = map(multiply, direction[d], [s] * 2)
        # 비 내리기
        while cloud:
            y, x = cloud.pop()
            ny, nx = (y + dy) % N, (x + dx) % N
            bucket_list[ny][nx] += 1
            after_move.add((ny, nx))

        # 물복사버그
        for y, x in after_move:
            cnt = 0
            for dy, dx in cross:
                cross_y, cross_x = y + dy, x + dx
                if 0 <= cross_y < N and 0 <= cross_x < N and bucket_list[cross_y][cross_x]:
                    cnt += 1
            bucket_list[y][x] += cnt

        # 구름 생성
        for i in range(N):
            for j in range(N):
                if bucket_list[i][j] >= 2 and (i, j) not in after_move:
                    bucket_list[i][j] -= 2
                    cloud.add((i, j))

    for _ in range(M):
        change_arr()

    total = 0
    for i in range(N):
        for j in range(N):
            total += bucket_list[i][j]

    return total


print(amount_of_water())