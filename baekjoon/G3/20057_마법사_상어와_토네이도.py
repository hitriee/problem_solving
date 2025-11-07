# 251107
# 44328 KB / 1300 ms
def main():
    from math import floor

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dy, dx = [0, 1, 0, -1], [-1, 0, 1, 0]
    idx = amount = 0
    ratio = [1/100, 7/100, 2/100, 1/10, 5/100]
    directions = [
        [(1, 2), (3, 2)],
        [(1,), (3,)],
        [(1, 1), (3, 3)],
        [(1, 0), (3, 0)],
        [(0, 0)]
    ]

    def spread_sand(y, x):
        outside = already = 0
        for k in range(5):
            sand = floor(ratio[k] * arr[y][x])
            if sand > 0:
                for direction in directions[k]:
                    ny, nx = y, x
                    for each in direction:
                        ny += dy[(idx+each) % 4]
                        nx += dx[(idx+each) % 4]
                    if 0 <= ny < N and 0 <= nx < N:
                        arr[ny][nx] += sand
                    else:
                        outside += sand
                already += sand * len(directions[k])

        ny, nx = y+dy[idx], x+dx[idx]
        remain = arr[y][x] - already
        if 0 <= ny < N and 0 <= nx < N:
            arr[ny][nx] += remain
        else:
            outside += remain

        arr[y][x] = 0

        return outside

    y = x = N//2
    for i in range(1, N):
        for _ in range(2):
            for _ in range(i):
                ny, nx = y+dy[idx], x+dx[idx]
                amount += spread_sand(ny, nx)
                y, x = ny, nx
            idx = (idx+1) % 4

    for _ in range(N-1):
        ny, nx = y + dy[idx], x + dx[idx]
        amount += spread_sand(ny, nx)
        y, x = ny, nx

    return amount

print(main())



# 44332 KB / 1176 ms
def main():
    from math import floor

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dy, dx = (0, 1, 0, -1), (-1, 0, 1, 0)
    idx = amount = 0
    ratio = [1/100, 7/100, 2/100, 1/10, 5/100]
    directions = [
        [(1, 2), (3, 2)],
        [(1,), (3,)],
        [(1, 1), (3, 3)],
        [(1, 0), (3, 0)],
        [(0, 0)]
    ]

    def spread_sand(y, x):
        outside = already = 0
        val = arr[y][x]
        for k in range(5):
            sand = floor(ratio[k] * val)
            if sand > 0:
                for direction in directions[k]:
                    ny, nx = y, x
                    for each in direction:
                        new_idx = (idx+each) % 4
                        ny += dy[new_idx]
                        nx += dx[new_idx]

                    if 0 <= ny < N and 0 <= nx < N:
                        arr[ny][nx] += sand
                    else:
                        outside += sand

                already += sand * (1 if k == 4 else 2)

        ny, nx = y+dy[idx], x+dx[idx]
        remain = val - already
        if 0 <= ny < N and 0 <= nx < N:
            arr[ny][nx] += remain
        else:
            outside += remain

        arr[y][x] = 0

        return outside

    y = x = N//2
    for i in range(1, N):
        for _ in range(2):
            for _ in range(i):
                ny, nx = y+dy[idx], x+dx[idx]
                amount += spread_sand(ny, nx)
                y, x = ny, nx
            idx = (idx+1) % 4

    for _ in range(N-1):
        ny, nx = y + dy[idx], x + dx[idx]
        amount += spread_sand(ny, nx)
        y, x = ny, nx

    return amount

print(main())