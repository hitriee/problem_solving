# 260106
# 40972 KB / 1696 ms
def main():
    from sys import stdin

    def int_input():
        return map(int, stdin.readline().split())

    N, M = int_input()
    arr = [list(int_input()) for _ in range(N)]
    row = [[0] * 3 for _ in range(M)]
    dx = [-1, 0, 1]
    limit = int(1e5)
    for j in range(M):
        for k in range(3):
            row[j][k] = arr[0][j]

    for i in range(1, N):
        temp = [[limit] * 3 for _ in range(M)]
        for j in range(M):
            for k in range(3):
                nj = j + dx[k]
                if 0 <= nj < M:
                    for l in range(3):
                        if k != l:
                            temp[nj][k] = min(row[j][l] + arr[i][nj], temp[nj][k])
        row = [temp[j][:] for j in range(M)]

    min_val = limit
    for j in range(M):
        min_val = min(min_val, *row[j])
    return min_val

print(main())




# 40972 KB / 1688 ms
def main():
    from sys import stdin

    def int_input():
        return map(int, stdin.readline().split())

    N, M = int_input()
    arr = [list(int_input()) for _ in range(N)]
    row = [[arr[0][j]] * 3 for j in range(M)]
    dx = [-1, 0, 1]
    limit = int(1e5)

    for i in range(1, N):
        temp = [[limit] * 3 for _ in range(M)]
        for j in range(M):
            for k in range(3):
                nj = j + dx[k]
                if 0 <= nj < M:
                    for l in range(3):
                        if k != l:
                            temp[nj][k] = min(row[j][l] + arr[i][nj], temp[nj][k])
        row = [temp[j][:] for j in range(M)]

    min_val = limit
    for j in range(M):
        min_val = min(min_val, *row[j])
    return min_val

print(main())



# 41104 KB / 1536 ms
def main():
    from sys import stdin

    def int_input():
        return map(int, stdin.readline().split())

    N, M = int_input()
    arr = [list(int_input()) for _ in range(N)]
    row = [[arr[0][j]] * 3 for j in range(M)]
    dx = [-1, 0, 1]
    i_arr = [set(range(3)) - {j} for j in range(3)]
    limit = int(1e5)

    for i in range(1, N):
        temp = [[limit] * 3 for _ in range(M)]
        for j in range(M):
            for k in range(3):
                nj = j + dx[k]
                if 0 <= nj < M:
                    for l in i_arr[k]:
                        temp[nj][k] = min(row[j][l] + arr[i][nj], temp[nj][k])
        row = [temp[j][:] for j in range(M)]

    min_val = limit
    for j in range(M):
        min_val = min(min_val, *row[j])
    return min_val

print(main())





# 41104 KB / 1520 ms
def main():
    from sys import stdin

    def int_input():
        return map(int, stdin.readline().split())

    N, M = int_input()
    arr = [list(int_input()) for _ in range(N)]
    row = [[arr[0][j]] * 3 for j in range(M)]
    dx = [-1, 0, 1]
    i_arr = [set(range(3)) - {j} for j in range(3)]
    limit = int(1e5)

    for i in range(1, N):
        temp = [[limit] * 3 for _ in range(M)]
        for j in range(M):
            for k in range(3):
                nj = j + dx[k]
                if 0 <= nj < M:
                    temp[nj][k] = min([row[j][l] for l in i_arr[k]]) + arr[i][nj]
        row = [temp[j][:] for j in range(M)]

    min_val = limit
    for j in range(M):
        min_val = min(min_val, *row[j])
    return min_val

print(main())


# 41120 KB / 1516 ms
def main():
    from sys import stdin

    def int_input():
        return map(int, stdin.readline().split())

    N, M = int_input()
    arr = [list(int_input()) for _ in range(N)]
    row = [[arr[0][j]] * 3 for j in range(M)]
    dx = [-1, 0, 1]
    i_arr = [set(range(3)) - {j} for j in range(3)]
    limit = int(1e5)

    for i in range(1, N):
        temp = [[limit] * 3 for _ in range(M)]
        for j in range(M):
            for k in range(3):
                nj = j + dx[k]
                if 0 <= nj < M:
                    temp[nj][k] = min([row[j][l] for l in i_arr[k]]) + arr[i][nj]
        row = [temp[j][:] for j in range(M)]

    total_vals = []
    for j in range(M):
        total_vals.extend(row[j])
    return min(total_vals)

print(main())