# 260331
def main():
    T = int(input())
    for tc in range(1, T+1):
        N = int(input())
        arr = [list(map(int, input())) for _ in range(N)]
        max_len = [[0] * N for _ in range(N)]

        max_len[0][0] = 1 - arr[0][0]
        for i in range(1, N):
            max_len[i][0] = 1 - arr[i][0]
            max_len[0][i] = 1 - arr[0][i]

        for i in range(1, N):
            for j in range(1, N):
                if arr[i][j] == 0:
                    val = min(max_len[i-1][j], max_len[i][j-1], max_len[i-1][j-1])
                    max_len[i][j] = val + 1

        max_val = 0
        for i in range(N):
            max_val = max(max_val, *max_len[i])

        print(f'#{tc} {max_val}')

main()