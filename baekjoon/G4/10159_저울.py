# 260305
# 32412 KB / 68 ms
def main():
    from sys import stdin

    new_input = stdin.readline

    N = int(new_input())
    M = int(new_input())
    arr = [[0] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, new_input().split())
        arr[a][b], arr[b][a] = 1, -1

    for k in range(1, N+1):
        for i in range(1, N):
            if i != k:
                for j in range(i+1, N+1):
                    if j != k and j != i:
                        val = arr[i][k]
                        if val != 0 and val == arr[k][j]:
                            arr[i][j], arr[j][i] = val, -val

    cnt = [str(arr[i].count(0) - 2) for i in range(1, N+1)]

    return '\n'.join(cnt)

print(main())





# 32412 KB / 76 ms
def main():
    from sys import stdin

    new_input = stdin.readline

    N = int(new_input())
    M = int(new_input())
    arr = [[0] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, new_input().split())
        arr[a][b], arr[b][a] = 1, -1

    for k in range(1, N+1):
        for i in range(1, N):
            if i != k:
                for j in range(i+1, N+1):
                    if j != k:
                        val = arr[i][k]
                        if val != 0 and val == arr[k][j]:
                            arr[i][j], arr[j][i] = val, -val

    cnt = [str(arr[i].count(0) - 2) for i in range(1, N+1)]

    return '\n'.join(cnt)

print(main())






# 32412 KB / 64 ms
def main():
    from sys import stdin

    new_input = stdin.readline

    N = int(new_input())
    M = int(new_input())
    arr = [[0] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, new_input().split())
        arr[a][b], arr[b][a] = 1, -1

    for k in range(1, N+1):
        for i in range(1, N):
            if i != k:
                for j in range(i+1, N+1):
                    if j != k:
                        val = arr[i][k]
                        if val != 0 and val == arr[k][j]:
                            arr[i][j], arr[j][i] = val, -val

    cnt = [0] * (N+1)

    for i in range(1, N):
        for j in range(i+1, N+1):
            if arr[i][j] == 0:
                cnt[i] += 1
                cnt[j] += 1


    return '\n'.join(map(str, cnt[1:]))

print(main())







# 32544 KB / 64 ms
def main():
    from sys import stdin

    new_input = stdin.readline

    def minus_one(num):
        return int(num) - 1

    N = int(new_input())
    M = int(new_input())
    arr = [[0] * N for _ in range(N)]
    for _ in range(M):
        a, b = map(minus_one, new_input().split())
        arr[a][b], arr[b][a] = 1, -1

    for k in range(N):
        for i in range(N-1):
            if i != k:
                for j in range(i+1, N):
                    if j != k:
                        val = arr[i][k]
                        if val != 0 and val == arr[k][j]:
                            arr[i][j], arr[j][i] = val, -val

    cnt = [0] * N

    for i in range(N-1):
        for j in range(i+1, N):
            if arr[i][j] == 0:
                cnt[i] += 1
                cnt[j] += 1


    return '\n'.join(map(str, cnt))

print(main())





# 32412 KB / 60 ms
def main():
    from sys import stdin

    new_input = stdin.readline

    N = int(new_input())
    M = int(new_input())
    arr = [[0] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, new_input().split())
        arr[a][b], arr[b][a] = 1, -1

    for k in range(1, N+1):
        row1 = arr[k]
        for i in range(1, N):
            if i != k:
                row2 = arr[i]
                for j in range(i+1, N+1):
                    if j != k:
                        val = row2[k]
                        if val != 0 and val == row1[j]:
                            arr[i][j], arr[j][i] = val, -val

    cnt = [0] * (N+1)

    for i in range(1, N):
        for j in range(i+1, N+1):
            if arr[i][j] == 0:
                cnt[i] += 1
                cnt[j] += 1


    return '\n'.join(map(str, cnt[1:]))

print(main())