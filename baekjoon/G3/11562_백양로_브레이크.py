# 241120
# 31120 KB / 1296 ms
def main():
    from sys import stdin

    new_input = stdin.readline
    N, M = map(int, new_input().split())
    min_cnt = [[M + 1] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        u, v, b = map(int, new_input().split())
        min_cnt[u][v] = 0
        min_cnt[v][u] = 1 - b

    for k in range(1, N + 1):
        min_cnt[k][k] = 0
        for i in range(1, N + 1):
            if i != k:
                for j in range(1, N + 1):
                    if i != j and j != k:
                        new_val = min_cnt[i][k] + min_cnt[k][j]
                        if new_val < min_cnt[i][j]:
                            min_cnt[i][j] = new_val

    K = int(input())
    for _ in range(K):
        s, e = map(int, new_input().split())
        print(min_cnt[s][e])


main()

# 31120 KB / 1344 ms

def minus_one(num):
    return int(num)-1

def main():
    from sys import stdin

    # 입력
    new_input = stdin.readline
    N, M = map(int, new_input().split())
    # 도로 정보
    min_cnt = [[M+1] * N for _ in range(N)]
    for _ in range(M):
        u, v, b = map(minus_one, new_input().split())
        min_cnt[u][v] = 0
        min_cnt[v][u] = -b

    for k in range(N):
        min_cnt[k][k] = 0
        for i in range(N):
            if i != k:
                for j in range(N):
                    if i != j and j != k:
                        new_val = min_cnt[i][k] + min_cnt[k][j]
                        if new_val < min_cnt[i][j]:
                            min_cnt[i][j] = new_val

    K = int(input())
    for _ in range(K):
        s, e = map(minus_one, new_input().split())
        print(min_cnt[s][e])


main()



# 31120 KB / 1104 ms
def main():
    from sys import stdin

    new_input = stdin.readline
    N, M = map(int, new_input().split())
    min_cnt = [[M + 1] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        u, v, b = map(int, new_input().split())
        min_cnt[u][v] = 0
        min_cnt[v][u] = 1 - b

    for k in range(1, N + 1):
        min_cnt[k][k] = 0
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                new_val = min_cnt[i][k] + min_cnt[k][j]
                if new_val < min_cnt[i][j]:
                    min_cnt[i][j] = new_val

    K = int(input())
    for _ in range(K):
        s, e = map(int, new_input().split())
        print(min_cnt[s][e])


main()



# 33408 KB / 1060 ms
def main():
    from sys import stdin

    new_input = stdin.readline
    N, M = map(int, new_input().split())
    min_cnt = [[M + 1] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        u, v, b = map(int, new_input().split())
        min_cnt[u][v] = 0
        min_cnt[v][u] = 1 - b

    for k in range(1, N + 1):
        min_cnt[k][k] = 0
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                new_val = min_cnt[i][k] + min_cnt[k][j]
                if new_val < min_cnt[i][j]:
                    min_cnt[i][j] = new_val

    K = int(input())
    arr = []
    for _ in range(K):
        s, e = map(int, new_input().split())
        arr.append(str(min_cnt[s][e]))

    return '\n'.join(arr)

print(main())
