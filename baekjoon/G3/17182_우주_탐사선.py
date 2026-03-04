# 260304
# 32412 KB / 348 ms
def main():

    def int_input():
        return map(int, input().split())

    N, K = int_input()
    arr = [list(int_input()) for _ in range(N)]

    for k in range(N):
        for i in range(N):
            for j in range(N):
                via = arr[i][k] + arr[k][j]
                if arr[i][j] > via:
                    arr[i][j] = via


    min_time = int(1e4)
    visited = [False] * N
    visited[K] = True

    def dfs(level, now, time):
        nonlocal min_time
        if level == N:
            if min_time > time:
                min_time = time
            return

        for i in range(N):
            if not visited[i]:
                visited[i] = True
                dfs(level+1, i, time+arr[now][i])
                visited[i] = False

    dfs(1, K, 0)



    return min_time

print(main())







# 32412 KB / 332 ms
def main():

    def int_input():
        return map(int, input().split())

    N, K = int_input()
    arr = [list(int_input()) for _ in range(N)]

    for k in range(N):
        for i in range(N):
            for j in range(N):
                via = arr[i][k] + arr[k][j]
                if arr[i][j] > via:
                    arr[i][j] = via


    min_time = int(1e4)
    visited = [False] * N
    visited[K] = True

    def dfs(level, now, time):
        nonlocal min_time
        if min_time <= time:
            return
        if level == N:
            min_time = time
            return

        for i in range(N):
            if not visited[i]:
                visited[i] = True
                dfs(level+1, i, time+arr[now][i])
                visited[i] = False

    dfs(1, K, 0)

    return min_time

print(main())








# 32412 KB / 324 ms
def main():

    def int_input():
        return map(int, input().split())

    N, K = int_input()
    arr = [list(int_input()) for _ in range(N)]

    for k in range(N):
        for i in range(N):
            if i != k:
                for j in range(N):
                    if i != j and j != k:
                        via = arr[i][k] + arr[k][j]
                        if arr[i][j] > via:
                            arr[i][j] = via


    min_time = int(1e4)
    visited = [False] * N
    visited[K] = True

    def dfs(level, now, time):
        nonlocal min_time
        if min_time <= time:
            return
        if level == N:
            min_time = time
            return

        for i in range(N):
            if not visited[i]:
                visited[i] = True
                dfs(level+1, i, time+arr[now][i])
                visited[i] = False

    dfs(1, K, 0)

    return min_time

print(main())






# 32412 KB / 608 ms
def main():

    def int_input():
        return map(int, input().split())

    N, K = int_input()
    arr = [list(int_input()) for _ in range(N)]

    for k in range(N):
        for i in range(N):
            if i != k:
                for j in range(N):
                    if i != j and j != k:
                        via = arr[i][k] + arr[k][j]
                        if arr[i][j] > via:
                            arr[i][j] = via


    min_time = int(1e4)

    def dfs(level, now, time, visited):
        nonlocal min_time
        if min_time <= time:
            return
        if level == N:
            min_time = time
            return

        for i in range(N):
            added = 1 << i
            if visited & added == 0:
                dfs(level+1, i, time+arr[now][i], visited | added)

    dfs(1, K, 0, 1 << K)

    return min_time

print(main())