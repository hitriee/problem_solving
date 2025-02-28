#230616
# 250227
# 180532 KB / 3468 ms
def main():
    from sys import stdin

    new_input = stdin.readline
    N, M = map(int, new_input().split())
    limit = 1.1e6
    map_info = [list(map(int, new_input().rstrip())) for _ in range(N)]

    def bfs():
        from collections import deque

        q = deque()
        dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
        q.append((0, 0, 1, map_info[0][0]))
        min_distance = [[[limit]*2 for _ in range(M)] for _ in range(N)]
        min_distance[0][0][map_info[0][0]] = 1

        while q:
            y, x, distance, chance = q.popleft()
            if y == N-1 and x == M-1:
                return distance

            distance += 1
            for i in range(4):
                ny, nx = y+dy[i], x+dx[i]
                if 0 <= ny < N and 0 <= nx < M:
                    idx = chance + map_info[ny][nx]
                    if idx <= 1 and distance < min_distance[ny][nx][idx]:
                        min_distance[ny][nx][idx] = distance
                        q.append((ny, nx, distance, idx))

        return -1

    return bfs()

print(main())



# 180552 KB / 3420 ms
def main():
    from sys import stdin

    new_input = stdin.readline
    N, M = map(int, new_input().split())
    limit = N*M
    map_info = [list(map(int, new_input().rstrip())) for _ in range(N)]

    def bfs():
        from collections import deque

        q = deque()
        dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
        q.append((0, 0, 1, map_info[0][0]))
        min_distance = [[[limit]*2 for _ in range(M)] for _ in range(N)]
        min_distance[0][0][map_info[0][0]] = 1

        while q:
            y, x, distance, chance = q.popleft()
            if y == N-1 and x == M-1:
                return distance

            distance += 1
            for i in range(4):
                ny, nx = y+dy[i], x+dx[i]
                if 0 <= ny < N and 0 <= nx < M:
                    idx = chance + map_info[ny][nx]
                    if idx <= 1 and distance < min_distance[ny][nx][idx]:
                        min_distance[ny][nx][idx] = distance
                        q.append((ny, nx, distance, idx))

        return -1

    return bfs()

print(main())





# 180552 KB / 3564 ms
def main():
    from sys import stdin

    new_input = stdin.readline
    N, M = map(int, new_input().split())
    limit = N*M
    map_info = [list(map(int, new_input().rstrip())) for _ in range(N)]

    def bfs():
        from collections import deque

        q = deque()
        dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
        q.append((0, 0, 1, map_info[0][0]))
        min_distance = [[[limit]*2 for _ in range(M)] for _ in range(N)]
        min_distance[0][0][map_info[0][0]] = 1

        while q:
            y, x, distance, chance = q.popleft()
            if y == N-1 and x == M-1:
                return distance

            distance += 1
            for i in range(4):
                ny, nx = y+dy[i], x+dx[i]
                if 0 <= ny < N and 0 <= nx < M:
                    idx = chance + map_info[ny][nx]
                    if idx <= 1 and min_distance[ny][nx][idx] == limit:
                        min_distance[ny][nx][idx] = distance
                        q.append((ny, nx, distance, idx))

        return -1

    return bfs()

print(main())




# 180448 KB / 3324 ms
def main():
    from sys import stdin

    new_input = stdin.readline
    N, M = map(int, new_input().split())
    limit = N*M
    map_info = [list(map(int, new_input().rstrip())) for _ in range(N)]

    def bfs():
        from collections import deque

        q = deque()
        dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
        q.append((0, 0, 1, 0))
        min_distance = [[[limit]*2 for _ in range(M)] for _ in range(N)]
        min_distance[0][0][0] = 1

        while q:
            y, x, distance, chance = q.popleft()
            if y == N-1 and x == M-1:
                return distance

            distance += 1
            for i in range(4):
                ny, nx = y+dy[i], x+dx[i]
                if 0 <= ny < N and 0 <= nx < M:
                    idx = chance + map_info[ny][nx]
                    if idx <= 1 and distance < min_distance[ny][nx][idx]:
                        min_distance[ny][nx][idx] = distance
                        q.append((ny, nx, distance, idx))

        return -1

    return bfs()

print(main())
