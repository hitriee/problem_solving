# 250417
# 260316
# 34968 KB / 408 ms
def main():
    from collections import deque

    N, M = map(int, input().split())
    arr = [input().split() for _ in range(N)]
    air = deque()
    dy, dx = (0, 1, 0, -1), (1, 0, -1, 0)
    time = 0

    while True:
        visited = [[0] * M for _ in range(N)]

        air.append((0, 0))
        visited[0][0] = 1
        has_cheese = False
        while air:
            y, x = air.popleft()
            for i in range(4):
                ny, nx = y+dy[i], x+dx[i]
                if 0 <= ny < N and 0 <= nx < M:
                    if visited[ny][nx] == 0:
                        if arr[ny][nx] == '0':
                            air.append((ny, nx))
                        visited[ny][nx] = 1

                    elif visited[ny][nx] == 1:
                        if arr[ny][nx] == '1':
                            arr[ny][nx] = '0'
                            has_cheese = True
                        visited[ny][nx] = 2

        if not has_cheese:
            return time

        time += 1


print(main())






# 34944 KB / 408 ms
def main():
    from collections import deque

    N, M = map(int, input().split())
    arr = [input().split() for _ in range(N)]
    air = deque()
    dy, dx = (0, 1, 0, -1), (1, 0, -1, 0)
    time = 0

    while True:
        visited = [[False] * M for _ in range(N)]

        air.append((0, 0))
        visited[0][0] = True
        has_cheese = False
        while air:
            y, x = air.popleft()
            for i in range(4):
                ny, nx = y+dy[i], x+dx[i]
                if 0 <= ny < N and 0 <= nx < M:
                    if not visited[ny][nx]:
                        if arr[ny][nx] == '0':
                            air.append((ny, nx))
                        visited[ny][nx] = True

                    elif arr[ny][nx] == '1':
                        arr[ny][nx] = '0'
                        has_cheese = True

        if not has_cheese:
            return time

        time += 1


print(main())





# 35016 KB / 68 ms
def main():
    from collections import deque

    N, M = map(int, input().split())
    arr = [input().split() for _ in range(N)]
    air, temp = deque(), deque()
    dy, dx = (0, 1, 0, -1), (1, 0, -1, 0)
    visited = [[0] * M for _ in range(N)]

    time = 0
    temp.append((0, 0))
    air.append((0, 0))
    visited[0][0] = 1

    while temp:
        y, x = temp.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if visited[ny][nx] == 0 and arr[ny][nx] == '0':
                    air.append((ny, nx))
                    temp.append((ny, nx))
                    visited[ny][nx] = 1

    while True:
        while air:
            y, x = air.popleft()
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < N and 0 <= nx < M:
                    if visited[ny][nx] == 0:
                        visited[ny][nx] = 1
                        if arr[ny][nx] == '0':
                            air.append((ny, nx))

                    elif visited[ny][nx] == 1:
                        if arr[ny][nx] == '1':
                            temp.append((ny, nx))
                            visited[ny][nx] = 2


        if not temp:
            return time

        for y, x in temp:
            air.append((y, x))
            arr[y][x] = '0'

        temp.clear()

        time += 1


print(main())






# 34976 KB / 68 ms
def main():
    from collections import deque

    N, M = map(int, input().split())
    arr = [input().split() for _ in range(N)]
    air, temp = deque(), deque()
    dy, dx = (0, 1, 0, -1), (1, 0, -1, 0)
    visited = [[0] * M for _ in range(N)]

    time = 0
    air.append((0, 0))
    visited[0][0] = 1

    while True:
        while air:
            y, x = air.popleft()
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < N and 0 <= nx < M:
                    if visited[ny][nx] == 0:
                        visited[ny][nx] = 1
                        if arr[ny][nx] == '0':
                            air.append((ny, nx))

                    elif visited[ny][nx] == 1:
                        if arr[ny][nx] == '1':
                            temp.append((ny, nx))
                            visited[ny][nx] = 2


        if not temp:
            return time

        for y, x in temp:
            air.append((y, x))
            arr[y][x] = '0'

        temp.clear()

        time += 1


print(main())