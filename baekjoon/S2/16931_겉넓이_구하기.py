# 241224
# 32412 KB / 44 ms
def main():
    N, M = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(N)]
    area = N*M*2
    di, dj = [1, -1, 0, 0], [0, 0, 1, -1]
    for i in range(N):
        for j in range(M):
            temp = 0
            for k in range(4):
                ni, nj = i+di[k], j+dj[k]
                if 0 <= ni < N and 0 <= nj < M:
                    dif = info[i][j] - info[ni][nj]
                    if dif > 0:
                        temp += dif
                else:
                    temp += info[i][j]
            area += temp


    return area

print(main())