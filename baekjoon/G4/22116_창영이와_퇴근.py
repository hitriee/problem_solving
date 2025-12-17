# 251217
# 176404 KB / 5392 ms
def main():
    from sys import stdin
    from heapq import heappush, heappop

    new_input = stdin.readline
    N = int(new_input())
    limit = int(1e9)
    delta_arr = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    arr = [list(map(int, new_input().split())) for _ in range(N)]
    dif_arr = [[limit] * N for _ in range(N)]
    heap = [(0, arr[0][0], 0, 0)]
    dif_arr[0][0] = 0

    def in_range(idx):
        return 0 <= idx < N

    while heap:
        dif, val, y, x = heappop(heap)
        if dif <= dif_arr[y][x]:
            for dy, dx in delta_arr:
                ny, nx = y+dy, x+dx
                if in_range(ny) and in_range(nx):
                    new_val = arr[ny][nx]
                    new_dif = max(abs(val - new_val), dif)
                    if new_dif < dif_arr[ny][nx]:
                        dif_arr[ny][nx] = new_dif
                        heappush(heap, (new_dif, new_val, ny, nx))

    return dif_arr[-1][-1]

print(main())


# 176420 KB / 5684 ms
def main():
    from sys import stdin
    from heapq import heappush, heappop

    new_input = stdin.readline
    N = int(new_input())
    limit = int(1e9)
    delta_arr = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    arr = [list(map(int, new_input().split())) for _ in range(N)]
    dif_arr = [[limit] * N for _ in range(N)]
    heap = [(0, arr[0][0], 0, 0)]
    dif_arr[0][0] = 0

    def in_range(idx):
        return 0 <= idx < N

    while heap:
        dif, val, y, x = heappop(heap)
        if dif > dif_arr[y][x]:
            continue

        for dy, dx in delta_arr:
            ny, nx = y+dy, x+dx
            if in_range(ny) and in_range(nx):
                new_val = arr[ny][nx]
                new_dif = max(abs(val - new_val), dif)
                if new_dif < dif_arr[ny][nx]:
                    dif_arr[ny][nx] = new_dif
                    heappush(heap, (new_dif, new_val, ny, nx))

    return dif_arr[-1][-1]

print(main())





# 166184 KB / 4916 ms
def main():
    from sys import stdin
    from heapq import heappush, heappop

    new_input = stdin.readline
    N = int(new_input())
    limit = int(1e9)
    delta_arr = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    arr = [list(map(int, new_input().split())) for _ in range(N)]
    dif_arr = [[limit] * N for _ in range(N)]
    heap = [(0, 0, 0)]
    dif_arr[0][0] = 0

    def in_range(idx):
        return 0 <= idx < N

    while heap:
        dif, y, x = heappop(heap)
        if dif > dif_arr[y][x]:
            continue

        val = arr[y][x]

        for dy, dx in delta_arr:
            ny, nx = y + dy, x + dx
            if in_range(ny) and in_range(nx):
                new_val = arr[ny][nx]
                new_dif = max(abs(val - new_val), dif)
                if new_dif < dif_arr[ny][nx]:
                    dif_arr[ny][nx] = new_dif
                    heappush(heap, (new_dif, ny, nx))

    return dif_arr[-1][-1]


print(main())




# 166184 KB / 4892 ms
def main():
    from sys import stdin
    from heapq import heappush, heappop

    new_input = stdin.readline
    N = int(new_input())
    limit = int(1e9)
    delta_arr = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    arr = [list(map(int, new_input().split())) for _ in range(N)]
    dif_arr = [[limit] * N for _ in range(N)]
    heap = [(0, 0, 0)]
    dif_arr[0][0] = 0

    def in_range(idx):
        return 0 <= idx < N

    while heap:
        dif, y, x = heappop(heap)
        if dif <= dif_arr[y][x]:
            val = arr[y][x]

            for dy, dx in delta_arr:
                ny, nx = y + dy, x + dx
                if in_range(ny) and in_range(nx):
                    new_val = arr[ny][nx]
                    new_dif = max(abs(val - new_val), dif)
                    if new_dif < dif_arr[ny][nx]:
                        dif_arr[ny][nx] = new_dif
                        heappush(heap, (new_dif, ny, nx))

    return dif_arr[-1][-1]


print(main())




# 166176 KB / 5052 ms
def main():
    from sys import stdin
    from heapq import heappush, heappop

    new_input = stdin.readline
    N = int(new_input())
    limit = int(1e9)
    delta_arr = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    arr = [list(map(int, new_input().split())) for _ in range(N)]
    dif_arr = [[limit] * N for _ in range(N)]
    heap = [(0, 0, 0)]
    dif_arr[0][0] = 0

    def in_range(idx):
        return 0 <= idx < N

    while heap:
        dif, y, x = heappop(heap)
        if dif <= dif_arr[y][x]:
            val = arr[y][x]

            for dy, dx in delta_arr:
                ny, nx = y + dy, x + dx
                if in_range(ny) and in_range(nx):
                    origin_dif = dif_arr[ny][nx]
                    new_dif = abs(val - arr[ny][nx])
                    if new_dif <= dif:
                        if origin_dif > dif:
                            dif_arr[ny][nx] = dif
                            heappush(heap, (dif, ny, nx))

                    elif origin_dif > new_dif:
                        dif_arr[ny][nx] = new_dif
                        heappush(heap, (new_dif, ny, nx))

    return dif_arr[-1][-1]


print(main())




# 166176 KB / 3472 ms
def main():
    from sys import stdin
    from heapq import heappush, heappop

    new_input = stdin.readline
    N = int(new_input())
    limit = int(1e9)
    delta_arr = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    arr = [list(map(int, new_input().split())) for _ in range(N)]
    dif_arr = [[limit] * N for _ in range(N)]
    heap = [(0, 0, 0)]
    dif_arr[0][0] = 0

    def in_range(idx):
        return 0 <= idx < N

    while heap:
        dif, y, x = heappop(heap)

        if dif > dif_arr[y][x]:
            continue
        if y == N-1 and x == N-1:
            return dif

        val = arr[y][x]

        for dy, dx in delta_arr:
            ny, nx = y + dy, x + dx
            if in_range(ny) and in_range(nx):
                new_val = arr[ny][nx]
                new_dif = max(abs(val - new_val), dif)
                if new_dif < dif_arr[ny][nx]:
                    dif_arr[ny][nx] = new_dif
                    heappush(heap, (new_dif, ny, nx))

    return dif_arr[-1][-1]


print(main())




# 166164 KB / 3428 ms
def main():
    from sys import stdin
    from heapq import heappush, heappop

    new_input = stdin.readline
    N = int(new_input())
    limit = int(1e9)
    delta_arr = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    arr = [list(map(int, new_input().split())) for _ in range(N)]
    dif_arr = [[limit] * N for _ in range(N)]
    heap = [(0, 0, 0)]
    dif_arr[0][0] = 0

    def in_range(idx):
        return 0 <= idx < N

    while heap:
        dif, y, x = heappop(heap)

        if dif > dif_arr[y][x]:
            continue
        if y == N-1 and x == N-1:
            return dif

        val = arr[y][x]

        for dy, dx in delta_arr:
            ny, nx = y + dy, x + dx
            if in_range(ny) and in_range(nx):
                new_val = arr[ny][nx]
                new_dif = max(abs(val - new_val), dif)
                if new_dif < dif_arr[ny][nx]:
                    dif_arr[ny][nx] = new_dif
                    heappush(heap, (new_dif, ny, nx))


print(main())





# 166164 KB / 3436 ms
def main():
    from sys import stdin
    from heapq import heappush, heappop

    new_input = stdin.readline
    N = int(new_input())
    limit = 1e9
    delta_arr = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    arr = [list(map(int, new_input().split())) for _ in range(N)]
    dif_arr = [[limit] * N for _ in range(N)]
    heap = [(0, 0, 0)]
    dif_arr[0][0] = 0

    def in_range(idx):
        return 0 <= idx < N

    while heap:
        dif, y, x = heappop(heap)

        if dif > dif_arr[y][x]:
            continue
        if y == N-1 and x == N-1:
            return dif

        val = arr[y][x]

        for dy, dx in delta_arr:
            ny, nx = y + dy, x + dx
            if in_range(ny) and in_range(nx):
                new_val = arr[ny][nx]
                new_dif = max(abs(val - new_val), dif)
                if new_dif < dif_arr[ny][nx]:
                    dif_arr[ny][nx] = new_dif
                    heappush(heap, (new_dif, ny, nx))


print(main())





# 166164 KB / 3144 ms
def main():
    from sys import stdin
    from heapq import heappush, heappop

    new_input = stdin.readline
    N = int(new_input())
    limit = int(1e9)
    delta_arr = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    arr = [list(map(int, new_input().split())) for _ in range(N)]
    dif_arr = [[limit] * N for _ in range(N)]
    heap = [(0, 0, 0)]
    dif_arr[0][0] = 0

    while heap:
        dif, y, x = heappop(heap)

        if dif > dif_arr[y][x]:
            continue
        if y == N-1 and x == N-1:
            return dif

        val = arr[y][x]

        for dy, dx in delta_arr:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N:
                new_val = arr[ny][nx]
                new_dif = max(abs(val - new_val), dif)
                if new_dif < dif_arr[ny][nx]:
                    dif_arr[ny][nx] = new_dif
                    heappush(heap, (new_dif, ny, nx))


print(main())






# 166164 KB / 3120 ms
def main():
    from sys import stdin
    from heapq import heappush, heappop

    new_input = stdin.readline
    N = int(new_input())
    limit = int(1e9)
    delta_arr = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    arr = [list(map(int, new_input().split())) for _ in range(N)]
    dif_arr = [[limit] * N for _ in range(N)]
    heap = [(0, 0, 0)]
    dif_arr[0][0] = 0

    while heap:
        dif, y, x = heappop(heap)

        if dif > dif_arr[y][x]:
            continue
        if y == N-1 and x == N-1:
            return dif

        val = arr[y][x]

        for dy, dx in delta_arr:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N:
                new_dif = max(abs(val - arr[ny][nx]), dif)
                if new_dif < dif_arr[ny][nx]:
                    dif_arr[ny][nx] = new_dif
                    heappush(heap, (new_dif, ny, nx))


print(main())