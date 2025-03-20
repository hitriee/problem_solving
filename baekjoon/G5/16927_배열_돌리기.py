# 250319
# 46672 KB / 88 ms
def main():
    from sys import stdin

    def fill_order():
        for i in range(min_val):
            for j in range(i, M-1-i):
                order[i].append((i, j))
            for j in range(i, N-1-i):
                order[i].append((j, M-1-i))
            for j in range(M-1-i, i, -1):
                order[i].append((N-1-i, j))
            for j in range(N-1-i, i, -1):
                order[i].append((j, i))

    def rotate():
        new_arr = [[''] * M for _ in range(N)]
        for i in range(min_val):
            length = len(order[i])
            k = R % length
            for j in range(length):
                y, x = order[i][(j+k) % length]
                ny, nx = order[i][j]
                new_arr[ny][nx] = arr[y][x]

        for i in range(N):
            arr[i] = new_arr[i][:]


    new_input = stdin.readline
    N, M, R = map(int, new_input().split())
    min_val = min(N, M) // 2
    arr = [new_input().rstrip().split() for _ in range(N)]
    order = [[] for _ in range(min_val)]
    fill_order()
    rotate()

    return '\n'.join(' '.join(arr[i]) for i in range(N))

print(main())




# 46672 KB / 80 ms
def main():
    from sys import stdin

    def fill_order():
        for i in range(min_val):
            for j in range(i, M-1-i):
                order[i].append((i, j))
            for j in range(i, N-1-i):
                order[i].append((j, M-1-i))
            for j in range(M-1-i, i, -1):
                order[i].append((N-1-i, j))
            for j in range(N-1-i, i, -1):
                order[i].append((j, i))

    def rotate():
        new_arr = [[''] * M for _ in range(N)]
        for i in range(min_val):
            length = len(order[i])
            k = R % length
            for j in range(length):
                y, x = order[i][(j+k) % length]
                ny, nx = order[i][j]
                new_arr[ny][nx] = arr[y][x]

        for i in range(N):
            arr[i] = new_arr[i][:]


    new_input = stdin.readline
    N, M, R = map(int, new_input().split())
    min_val = min(N, M) // 2
    arr = [new_input().split() for _ in range(N)]
    order = [[] for _ in range(min_val)]
    fill_order()
    rotate()

    return '\n'.join(' '.join(arr[i]) for i in range(N))

print(main())



# 45648 KB / 88 ms
def main():
    from sys import stdin

    def fill_order():
        for i in range(min_val):
            limit1, limit2 = M-1-i, N-1-i
            for j in range(i, limit1):
                order[i].append((i, j))
            for j in range(i, limit2):
                order[i].append((j, limit1))
            for j in range(limit1, i, -1):
                order[i].append((limit2, j))
            for j in range(limit2, i, -1):
                order[i].append((j, i))

    def rotate():
        new_arr = [[''] * M for _ in range(N)]
        for i in range(min_val):
            length = len(order[i])
            k = R % length
            for j in range(length):
                y, x = order[i][(j+k) % length]
                ny, nx = order[i][j]
                new_arr[ny][nx] = arr[y][x]

        for i in range(N):
            arr[i] = new_arr[i][:]


    new_input = stdin.readline
    N, M, R = map(int, new_input().split())
    min_val = min(N, M) // 2
    arr = [new_input().split() for _ in range(N)]
    order = [[] for _ in range(min_val)]
    fill_order()
    rotate()

    return '\n'.join(' '.join(arr[i]) for i in range(N))

print(main())





# 45648 KB / 88 ms
def main():
    from sys import stdin

    def fill_order():
        limit1, limit2 = M - 1, N - 1
        for i in range(min_val):
            for j in range(i, limit1):
                order[i].append((i, j))
            for j in range(i, limit2):
                order[i].append((j, limit1))
            for j in range(limit1, i, -1):
                order[i].append((limit2, j))
            for j in range(limit2, i, -1):
                order[i].append((j, i))

            limit1 -= 1
            limit2 -= 1

    def rotate():
        new_arr = [[''] * M for _ in range(N)]
        for i in range(min_val):
            length = len(order[i])
            k = R % length
            for j in range(length):
                y, x = order[i][(j+k) % length]
                ny, nx = order[i][j]
                new_arr[ny][nx] = arr[y][x]

        for i in range(N):
            arr[i] = new_arr[i][:]


    new_input = stdin.readline
    N, M, R = map(int, new_input().split())
    min_val = min(N, M) // 2
    arr = [new_input().split() for _ in range(N)]
    order = [[] for _ in range(min_val)]
    fill_order()
    rotate()

    return '\n'.join(' '.join(arr[i]) for i in range(N))

print(main())