# 251211
# 51864 KB / 692 ms
def main():
    from sys import stdin

    def int_input():
        return map(int, stdin.readline().split())

    N, M = int_input()
    arr = [list(int_input()) for _ in range(N)]
    up_arr = [arr[i][:] for i in range(N)]
    down_arr = [arr[i][:] for i in range(N)]
    max_val = int(-1e4) * N * M

    for i in range(N-2, -1, -1):
        down_arr[i][-1] += down_arr[i+1][-1]
        up_arr[i][0] += up_arr[i+1][0]

    for j in range(M-2, -1, -1):
        down_arr[-1][j] += down_arr[-1][j+1]
        up_arr[-1][M-1-j] += up_arr[-1][M-2-j]


    for i in range(N-2, -1, -1):
        for j in range(M-2, -1, -1):
            down_arr[i][j] += max(down_arr[i+1][j], down_arr[i][j+1])

    for i in range(N-2, -1, -1):
        for j in range(1, M):
            up_arr[i][j] += max(up_arr[i+1][j], up_arr[i][j-1])

    for i in range(N):
        for j in range(M):
            val = up_arr[i][j] + down_arr[i][j]
            if max_val < val:
                max_val = val

    return max_val

print(main())


# 151864 KB / 684 ms
def main():
    from sys import stdin

    def int_input():
        return map(int, stdin.readline().split())

    N, M = int_input()
    arr = [list(int_input()) for _ in range(N)]
    up_arr = [arr[i][:] for i in range(N)]
    down_arr = [arr[i][:] for i in range(N)]
    max_val = int(-1e10)

    for i in range(N-2, -1, -1):
        down_arr[i][-1] += down_arr[i+1][-1]
        up_arr[i][0] += up_arr[i+1][0]

    for j in range(M-2, -1, -1):
        down_arr[-1][j] += down_arr[-1][j+1]
        up_arr[-1][M-1-j] += up_arr[-1][M-2-j]


    for i in range(N-2, -1, -1):
        for j in range(M-2, -1, -1):
            down_arr[i][j] += max(down_arr[i+1][j], down_arr[i][j+1])

    for i in range(N-2, -1, -1):
        for j in range(1, M):
            up_arr[i][j] += max(up_arr[i+1][j], up_arr[i][j-1])

    for i in range(N):
        for j in range(M):
            val = up_arr[i][j] + down_arr[i][j]
            if max_val < val:
                max_val = val

    return max_val

print(main())



# 151864 KB / 784 ms
def main():
    from sys import stdin

    def int_input():
        return map(int, stdin.readline().split())

    N, M = int_input()
    arr = [list(int_input()) for _ in range(N)]
    up_arr = [arr[i][:] for i in range(N)]
    down_arr = [arr[i][:] for i in range(N)]
    max_val = int(-1e10)

    for i in range(N-2, -1, -1):
        down_arr[i][-1] += down_arr[i+1][-1]
        up_arr[i][0] += up_arr[i+1][0]

    for j in range(M-2, -1, -1):
        down_arr[-1][j] += down_arr[-1][j+1]
        up_arr[-1][M-1-j] += up_arr[-1][M-2-j]


    for i in range(N-2, -1, -1):
        for j in range(M-2, -1, -1):
            down_arr[i][j] += max(down_arr[i+1][j], down_arr[i][j+1])
            up_arr[i][M-1-j] += max(up_arr[i+1][M-1-j], up_arr[i][M-2-j])

    for i in range(N):
        for j in range(M):
            val = up_arr[i][j] + down_arr[i][j]
            if max_val < val:
                max_val = val

    return max_val

print(main())


# 151868 KB / 652 ms
def main():
    from sys import stdin

    def int_input():
        return map(int, stdin.readline().split())

    N, M = int_input()
    arr = [list(int_input()) for _ in range(N)]
    up_arr = [arr[i][:] for i in range(N)]
    down_arr = [arr[i][:] for i in range(N)]
    max_val = int(-1e10)

    for i in range(N-2, -1, -1):
        down_arr[i][-1] += down_arr[i+1][-1]
        up_arr[i][0] += up_arr[i+1][0]

    for j in range(M-2, -1, -1):
        down_arr[-1][j] += down_arr[-1][j+1]

    for j in range(1, M):
        up_arr[-1][j] += up_arr[-1][j-1]


    for i in range(N-2, -1, -1):
        for j in range(M-2, -1, -1):
            down_arr[i][j] += max(down_arr[i+1][j], down_arr[i][j+1])

        for j in range(1, M):
            up_arr[i][j] += max(up_arr[i+1][j], up_arr[i][j-1])

    for i in range(N):
        for j in range(M):
            val = up_arr[i][j] + down_arr[i][j]
            if max_val < val:
                max_val = val

    return max_val

print(main())




# 112268 KB / 640 ms
def main():
    from sys import stdin

    def int_input():
        return map(int, stdin.readline().split())

    N, M = int_input()
    up_arr = [list(int_input()) for _ in range(N)]
    down_arr = [up_arr[i][:] for i in range(N)]
    max_val = int(-1e10)

    for i in range(N - 2, -1, -1):
        down_arr[i][-1] += down_arr[i + 1][-1]
        up_arr[i][0] += up_arr[i + 1][0]

    for j in range(M - 2, -1, -1):
        down_arr[-1][j] += down_arr[-1][j + 1]

    for j in range(1, M):
        up_arr[-1][j] += up_arr[-1][j - 1]

    for i in range(N - 2, -1, -1):
        for j in range(M - 2, -1, -1):
            down_arr[i][j] += max(down_arr[i + 1][j], down_arr[i][j + 1])

        for j in range(1, M):
            up_arr[i][j] += max(up_arr[i + 1][j], up_arr[i][j - 1])

    for i in range(N):
        for j in range(M):
            val = up_arr[i][j] + down_arr[i][j]
            if max_val < val:
                max_val = val

    return max_val


print(main())