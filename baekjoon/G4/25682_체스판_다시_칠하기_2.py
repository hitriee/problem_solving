# 251117
# 222084 KB / 3980 ms
def main():
    from sys import stdin

    new_input = stdin.readline
    N, M, K = map(int, new_input().split())
    min_cnt = K*K
    board = [list(new_input()) for _ in range(N)]
    acc = [[0] * (M+1) for _ in range(N+1)]
    colors = 'BW'
    for dif in range(2):
        for i in range(N):
            idx = (i+dif) % 2
            for j in range(M):
                acc[i+1][j+1] = acc[i][j+1] + acc[i+1][j] - acc[i][j]
                if board[i][j] != colors[idx]:
                    acc[i+1][j+1] += 1
                idx = 1-idx

        for i in range(K, N+1):
            for j in range(K, M+1):
                cnt = acc[i][j] - acc[i-K][j] - acc[i][j-K] + acc[i-K][j-K]
                if min_cnt > cnt:
                    min_cnt = cnt

    return min_cnt

print(main())



# 194964 KB / 3964 ms
def main():
    from sys import stdin

    new_input = stdin.readline
    N, M, K = map(int, new_input().split())
    min_cnt = K*K
    board = [new_input().rstrip() for _ in range(N)]
    acc = [[0] * (M+1) for _ in range(N+1)]
    colors = 'BW'
    for dif in range(2):
        for i in range(N):
            idx = (i+dif) % 2
            for j in range(M):
                acc[i+1][j+1] = acc[i][j+1] + acc[i+1][j] - acc[i][j]
                if board[i][j] != colors[idx]:
                    acc[i+1][j+1] += 1
                idx = 1-idx

        for i in range(K, N+1):
            for j in range(K, M+1):
                cnt = acc[i][j] - acc[i-K][j] - acc[i][j-K] + acc[i-K][j-K]
                if min_cnt > cnt:
                    min_cnt = cnt

    return min_cnt

print(main())