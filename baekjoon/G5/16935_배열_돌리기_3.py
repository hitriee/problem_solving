# 251111
# 33432 KB / 620 ms
def main():
    N, M, R = map(int, input().split())
    arr = [input().split() for _ in range(N)]

    def convert(num):
        nonlocal N, M

        temp = [[''] * 100 for _ in range(100)]
        half_N, half_M = N//2, M//2
        if num == '1':
            for i in range(half_N):
                for j in range(M):
                    temp[i][j], temp[N-1-i][j] = arr[N-1-i][j], arr[i][j]
        elif num == '2':
            for i in range(N):
                for j in range(half_M):
                    temp[i][j], temp[i][M-1-j] = arr[i][M-1-j], arr[i][j]
        elif num == '3':
            for i in range(N):
                for j in range(M):
                    temp[j][N-1-i] = arr[i][j]
            N, M = M, N
        elif num == '4':
            for i in range(N):
                for j in range(M):
                    temp[M-1-j][i] = arr[i][j]
            N, M = M, N
        else:
            di_arr, dj_arr = [0, half_N, 0, -half_N], [half_M, 0, -half_M, 0]
            start_i_arr, start_j_arr = [0, 0, half_N, half_N], [0, half_M, half_M, 0]
            if num == '5':
                for k in range(4):
                    start_i, start_j = start_i_arr[k], start_j_arr[k]
                    di, dj = di_arr[k], dj_arr[k]
                    for i in range(start_i, start_i+half_N):
                        for j in range(start_j, start_j+half_M):
                            temp[i+di][j+dj] = arr[i][j]


            else:
                for k in range(4):
                    start_i, start_j = start_i_arr[k], start_j_arr[k]
                    di, dj = di_arr[k], dj_arr[k]
                    for i in range(start_i, start_i+half_N):
                        for j in range(start_j, start_j+half_M):
                            temp[i][j] = arr[i+di][j+dj]

        return temp

    info = input().split()
    for num in info:
        new_arr = convert(num)
        arr = [new_arr[i][:M] for i in range(N)]

    return '\n'.join([' '.join(arr[i]) for i in range(N)])

print(main())
# main()



# 335644 KB / 608 ms
def main():
    from sys import stdin

    new_input = stdin.readline
    N, M, R = map(int, new_input().split())
    arr = [new_input().split() for _ in range(N)]

    def convert(num):
        nonlocal N, M

        temp = [[''] * 100 for _ in range(100)]
        half_N, half_M = N//2, M//2
        if num == '1':
            for i in range(half_N):
                for j in range(M):
                    temp[i][j], temp[N-1-i][j] = arr[N-1-i][j], arr[i][j]
        elif num == '2':
            for i in range(N):
                for j in range(half_M):
                    temp[i][j], temp[i][M-1-j] = arr[i][M-1-j], arr[i][j]
        elif num == '3':
            for i in range(N):
                for j in range(M):
                    temp[j][N-1-i] = arr[i][j]
            N, M = M, N
        elif num == '4':
            for i in range(N):
                for j in range(M):
                    temp[M-1-j][i] = arr[i][j]
            N, M = M, N
        else:
            di_arr, dj_arr = [0, half_N, 0, -half_N], [half_M, 0, -half_M, 0]
            start_i_arr, start_j_arr = [0, 0, half_N, half_N], [0, half_M, half_M, 0]
            if num == '5':
                for k in range(4):
                    start_i, start_j = start_i_arr[k], start_j_arr[k]
                    di, dj = di_arr[k], dj_arr[k]
                    for i in range(start_i, start_i+half_N):
                        for j in range(start_j, start_j+half_M):
                            temp[i+di][j+dj] = arr[i][j]


            else:
                for k in range(4):
                    start_i, start_j = start_i_arr[k], start_j_arr[k]
                    di, dj = di_arr[k], dj_arr[k]
                    for i in range(start_i, start_i+half_N):
                        for j in range(start_j, start_j+half_M):
                            temp[i][j] = arr[i+di][j+dj]

        return temp

    info = new_input().split()
    for num in info:
        new_arr = convert(num)
        arr = [new_arr[i][:M] for i in range(N)]

    return '\n'.join([' '.join(arr[i]) for i in range(N)])

print(main())
# main()