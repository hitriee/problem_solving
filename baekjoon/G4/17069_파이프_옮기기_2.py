# 250613
# 32544 KB / 40 ms
def main():
    N = int(input())
    home = [input().split() for _ in range(N)]
    # 0 - 가로, 1 - 대각선, 2 - 세로
    direction = [(0, 1), (1, 1), (1, 0)]
    # 방향별 가능한 다음 방향
    idx_list = [(0, 1), (0, 1, 2), (1, 2)]
    # 방향별 비어있어야 하는 칸 (인덱스)
    empty = [[0], [0, 1, 2], [2]]
    arr = [[[0] * 3 for _ in range(N)] for _ in range(N)]
    arr[0][1][0] = 1

    for i in range(N):
        for j in range(1, N):
            for k in range(3):
                if arr[i][j][k] > 0:
                    for l in idx_list[k]:
                        for m in empty[l]:
                            di, dj = direction[m]
                            ni, nj = i+di, j+dj
                            if ni >= N or nj >= N or home[ni][nj] == '1':
                                break
                        else:
                            di, dj = direction[l]
                            ni, nj = i+di, j+dj
                            arr[ni][nj][l] += arr[i][j][k]

    return sum(arr[-1][-1])

print(main())





# 32412 KB / 44 ms
def main():
    N = int(input())
    home = [input().split() for _ in range(N)]
    # 0 - 가로, 1 - 대각선, 2 - 세로
    direction = [(0, 1), (1, 1), (1, 0)]
    # 방향별 가능한 다음 방향
    idx_list = [(0, 1), (0, 1, 2), (1, 2)]
    # 방향별 비어있어야 하는 칸 (인덱스)
    empty = [[0], [0, 1, 2], [2]]
    arr = [[[0] * 3 for _ in range(N-1)] for _ in range(N)]
    arr[0][0][0] = 1

    for i in range(N):
        for j in range(N-1):
            for k in range(3):
                if arr[i][j][k] > 0:
                    for l in idx_list[k]:
                        for m in empty[l]:
                            di, dj = direction[m]
                            ni, nj = i+di, j+dj
                            if ni >= N or nj >= N-1 or home[ni][nj+1] == '1':
                                break
                        else:
                            di, dj = direction[l]
                            ni, nj = i+di, j+dj
                            arr[ni][nj][l] += arr[i][j][k]

    return sum(arr[-1][-1])

print(main())