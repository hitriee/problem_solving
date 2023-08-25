#230825
from collections import deque
N = int(input())
area = []
fish, size = 0, 2
q = deque()
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 9:
            q.append((i, j, 0))
            row[j] = 0
        elif row[j]:
            fish += 1
    area.append(row)

max_time = eaten_fish = 0
if fish:
    def to_fish_position():
        visited = [[False] * N for _ in range(N)]
        visited[q[0][0]][q[0][1]] = True
        result = (0, 0, 0)
        while q:
            y, x, time = q.popleft()
            time += 1
            for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < N:
                    if not visited[ny][nx]:
                        fish_size = area[ny][nx]
                        if fish_size == 0 or fish_size == size:
                            visited[ny][nx] = True
                            q.append((ny, nx, time))
                        elif fish_size < size:
                            visited[ny][nx] = True
                            if result[-1] == 0:
                                result = (ny, nx, time)
                            elif result[-1] == time:
                                if result[0] > ny:
                                    result = (ny, nx, time)
                                elif result[0] == ny and result[1] > nx:
                                    result = (ny, nx, time)
                            elif result[-1] < time:
                                area[result[0]][result[1]] = 0
                                return result
        if result[-1] != 0:
            area[result[0]][result[1]] = 0

        return result

    while fish:
        *result, time = to_fish_position()
        if time:
            max_time += time
            q.clear()
            q.append((*result, 0))
            fish -= 1
            eaten_fish += 1
            if eaten_fish == size:
                size += 1
                eaten_fish = 0
        else:
            print(max_time)
            break
    else:
        print(max_time)
else:
    print(0)


#
def find_max_time():
    from collections import deque

    N = int(input())
    area = []
    fish, size = 0, 2
    q = deque()
    for i in range(N):
        row = list(map(int, input().split()))
        for j in range(N):
            if row[j] == 9:
                q.append((i, j, 0))
                row[j] = 0
            elif row[j]:
                fish += 1
        area.append(row)

    if fish == 0:
        return 0

    max_time = eaten_fish = 0

    def to_fish_position():
        visited = [[False] * N for _ in range(N)]
        visited[q[0][0]][q[0][1]] = True
        result = (0, 0, 0)
        while q:
            y, x, time = q.popleft()
            time += 1
            for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < N:
                    if not visited[ny][nx]:
                        fish_size = area[ny][nx]
                        if fish_size == 0 or fish_size == size:
                            visited[ny][nx] = True
                            q.append((ny, nx, time))
                        elif fish_size < size:
                            visited[ny][nx] = True
                            if result[-1] == 0:
                                result = (ny, nx, time)
                            elif result[-1] == time:
                                if result[0] > ny:
                                    result = (ny, nx, time)
                                elif result[0] == ny and result[1] > nx:
                                    result = (ny, nx, time)
                            elif result[-1] < time:
                                area[result[0]][result[1]] = 0
                                return result

        if result[-1] != 0:
            area[result[0]][result[1]] = 0

        return result


    while fish:
        *result, time = to_fish_position()
        if time:
            max_time += time
            q.clear()
            q.append((*result, 0))
            fish -= 1
            eaten_fish += 1
            if eaten_fish == size:
                size += 1
                eaten_fish = 0
        else:
            return max_time
    else:
        return max_time

print(find_max_time())


#
def to_fish_position(area, N, size, *fish_position):
    from collections import deque
    visited = [[False] * N for _ in range(N)]
    q = deque()
    q.append((*fish_position, 0))
    visited[q[0][0]][q[0][1]] = True
    result = (0, 0, 0)
    while q:
        y, x, time = q.popleft()
        time += 1
        for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N:
                if not visited[ny][nx]:
                    fish_size = area[ny][nx]
                    if fish_size == 0 or fish_size == size:
                        visited[ny][nx] = True
                        q.append((ny, nx, time))
                    elif fish_size < size:
                        visited[ny][nx] = True
                        if result[-1] == 0:
                            result = (ny, nx, time)
                        elif result[-1] == time:
                            if result[0] > ny:
                                result = (ny, nx, time)
                            elif result[0] == ny and result[1] > nx:
                                result = (ny, nx, time)
                        elif result[-1] < time:
                            area[result[0]][result[1]] = 0
                            return result

    if result[-1] != 0:
        area[result[0]][result[1]] = 0

    return result

def find_max_time():

    N = int(input())
    area = []
    fish, size = 0, 2
    fish_position = []
    for i in range(N):
        row = list(map(int, input().split()))
        for j in range(N):
            if row[j] == 9:
                fish_position.extend((i, j))
                row[j] = 0
            elif row[j]:
                fish += 1
        area.append(row)

    max_time = eaten_fish = 0

    while fish:
        *result, time = to_fish_position(area, N, size, *fish_position)
        if time:
            max_time += time
            fish_position = result
            fish -= 1
            eaten_fish += 1
            if eaten_fish == size:
                size += 1
                eaten_fish = 0
        else:
            return max_time

    return max_time

print(find_max_time())


#
def to_fish_position(area, N, size, *fish_position):
    from collections import deque
    visited = [[False] * N for _ in range(N)]
    q = deque()
    q.append((*fish_position, 0))
    visited[q[0][0]][q[0][1]] = True
    result = (0, 0, 0)

    while q:
        y, x, time = q.popleft()
        time += 1
        for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N:
                if not visited[ny][nx]:
                    fish_size = area[ny][nx]
                    if fish_size == 0 or fish_size == size:
                        visited[ny][nx] = True
                        q.append((ny, nx, time))
                    elif fish_size < size:
                        visited[ny][nx] = True
                        if result[-1] == 0:
                            result = (ny, nx, time)
                        elif result[-1] == time:
                            if result[0] > ny:
                                result = (ny, nx, time)
                            elif result[0] == ny and result[1] > nx:
                                result = (ny, nx, time)
                        elif result[-1] < time:
                            area[result[0]][result[1]] = 0
                            return result

    if result[-1] != 0:
        area[result[0]][result[1]] = 0

    return result

def find_max_time():

    N = int(input())
    area = []
    fish_position = []
    size = 2
    for i in range(N):
        row = list(map(int, input().split()))
        if not fish_position:
            for j in range(N):
                if row[j] == 9:
                    fish_position.extend((i, j))
                    row[j] = 0
                    break
        area.append(row)

    max_time = eaten_fish = 0

    while True:
        *result, time = to_fish_position(area, N, size, *fish_position)
        if time:
            max_time += time
            fish_position = result
            eaten_fish += 1
            if eaten_fish == size:
                size += 1
                eaten_fish = 0
        else:
            return max_time

print(find_max_time())
