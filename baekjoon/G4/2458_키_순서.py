# 241224
# 33332 KB / 4104 ms
def main():
    from sys import stdin

    new_input = stdin.readline
    N, M = map(int, new_input().split())
    height_conf = [[-1] * N for _ in range(N)]
    cnt = 0
    for _ in range(M):
        a, b = map(lambda x: int(x)-1, new_input().split())
        height_conf[a][b], height_conf[b][a] = 0, 1

    for k in range(N):
        for i in range(N):
            val = height_conf[i][k]
            for j in range(i+1, N):
                if val == height_conf[k][j] != -1:
                    height_conf[i][j] = val
                    height_conf[j][i] = 1-val

    for i in range(N):
        if height_conf[i].count(-1) == 1:
            cnt += 1

    return cnt

print(main())


# 33332 KB / 4044 ms
def main():
    from sys import stdin

    def int_input():
        return map(int, stdin.readline().split())

    N, M = int_input()
    height_conf = [[-1] * (N+1) for _ in range(N+1)]
    cnt = 0
    for _ in range(M):
        a, b = int_input()
        height_conf[a][b], height_conf[b][a] = 0, 1

    for k in range(1, N+1):
        for i in range(1, N+1):
            val = height_conf[i][k]
            for j in range(i+1, N+1):
                if val == height_conf[k][j] != -1:
                    height_conf[i][j] = val
                    height_conf[j][i] = 1-val

    for i in range(1, N+1):
        if height_conf[i].count(-1) == 2:
            cnt += 1

    return cnt

print(main())