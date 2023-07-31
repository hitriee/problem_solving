#230725
#230731
from sys import stdin
def to_int(): return map(int, stdin.readline().split())
N, M = to_int()
ocean, ice = [], set()
for i in range(N):
    ocean.append(list(to_int()))
    for j in range(M):
        if ocean[-1][j]:
            ice.add((i, j))

def bfs():
    direction = (-1, 0), (0, -1), (1, 0), (0, 1)
    melted = set()
    temp = set(ice)

    while temp:
        temp_y, temp_x = temp.pop()
        cnt = 0
        for dy, dx in direction:
            ny, nx = temp_y+dy, temp_x+dx
            if ocean[ny][nx] == 0:
                cnt += 1

        if cnt >= ocean[temp_y][temp_x]:
            ice.remove((temp_y, temp_x))
            melted.add((temp_y, temp_x))
            ocean[temp_y][temp_x] = -1
        else:
            ocean[temp_y][temp_x] -= cnt

    if melted:
        visited_ice = set()
        for y, x in melted:
            ocean[y][x] = 0

        for y, x in ice:
            visited_ice.add((y, x))
            temp = {(y, x)}
            while temp:
                temp_y, temp_x = temp.pop()
                for dy, dx in direction:
                    ny, nx = temp_y + dy, temp_x + dx
                    if ocean[ny][nx] and (ny, nx) not in visited_ice:
                        visited_ice.add((ny, nx))
                        temp.add((ny, nx))
            return visited_ice == ice

    return True

duration = 1
while bfs():
    duration += 1
    if not ice:
        duration = 0
        break

print(duration)


#
def find_duration():
    from sys import stdin
    def to_int(): return map(int, stdin.readline().split())
    N, M = to_int()
    ocean, ice = [], set()
    for i in range(N):
        ocean.append(list(to_int()))
        for j in range(M):
            if ocean[-1][j]:
                ice.add((i, j))

    def bfs():
        direction = (-1, 0), (0, -1), (1, 0), (0, 1)
        melted = set()
        temp = set(ice)

        while temp:
            temp_y, temp_x = temp.pop()
            cnt = 0
            for dy, dx in direction:
                ny, nx = temp_y+dy, temp_x+dx
                if ocean[ny][nx] == 0:
                    cnt += 1

            if cnt >= ocean[temp_y][temp_x]:
                ice.remove((temp_y, temp_x))
                melted.add((temp_y, temp_x))
                ocean[temp_y][temp_x] = -1
            else:
                ocean[temp_y][temp_x] -= cnt

        if melted:
            visited_ice = set()
            for y, x in melted:
                ocean[y][x] = 0

            for y, x in ice:
                visited_ice.add((y, x))
                temp = {(y, x)}
                while temp:
                    temp_y, temp_x = temp.pop()
                    for dy, dx in direction:
                        ny, nx = temp_y + dy, temp_x + dx
                        if ocean[ny][nx] and (ny, nx) not in visited_ice:
                            visited_ice.add((ny, nx))
                            temp.add((ny, nx))
                return visited_ice == ice

        return True

    duration = 1
    while bfs():
        duration += 1
        if not ice:
            return 0

    return duration

print(find_duration())


#
def find_duration():
    from sys import stdin
    def to_int(): return map(int, stdin.readline().split())
    N, M = to_int()
    ocean, ice = [], set()
    for i in range(N):
        ocean.append(list(to_int()))
        for j in range(M):
            if ocean[-1][j]:
                ice.add((i, j))

    def bfs():
        direction = (-1, 0), (0, -1), (1, 0), (0, 1)
        melted = set()
        temp = set(ice)

        while temp:
            temp_y, temp_x = temp.pop()
            cnt = 0
            for dy, dx in direction:
                ny, nx = temp_y+dy, temp_x+dx
                if ocean[ny][nx] == 0:
                    cnt += 1

            if cnt >= ocean[temp_y][temp_x]:
                ice.remove((temp_y, temp_x))
                melted.add((temp_y, temp_x))
                ocean[temp_y][temp_x] = -1
            else:
                ocean[temp_y][temp_x] -= cnt

        if melted:
            visited_ice = set()
            for y, x in melted:
                ocean[y][x] = 0

            for y, x in ice:
                visited_ice.add((y, x))
                temp.add((y, x))
                while temp:
                    temp_y, temp_x = temp.pop()
                    for dy, dx in direction:
                        ny, nx = temp_y + dy, temp_x + dx
                        if ocean[ny][nx] and (ny, nx) not in visited_ice:
                            visited_ice.add((ny, nx))
                            temp.add((ny, nx))
                return visited_ice == ice

        return True

    duration = 1
    while bfs():
        duration += 1
        if not ice:
            return 0

    return duration

print(find_duration())