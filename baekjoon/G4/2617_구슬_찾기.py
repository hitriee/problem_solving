# 260309
# 32412 KB / 64 ms
def main():
    from sys import stdin

    def int_input():
        return map(int, stdin.readline().split())

    N, M = int_input()
    arr = [[0] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        a, b = int_input()
        arr[a][b], arr[b][a] = 1, -1

    for k in range(1, N+1):
        for i in range(1, N):
            if i != k:
                val = arr[i][k]
                for j in range(i+1, N+1):
                    if i != j and j != k:
                        if val != 0 and val== arr[k][j]:
                            arr[i][j], arr[j][i] = val, -val

    cnt = 0

    for i in range(1, N+1):
        rank = cnt_zero = 0
        for j in range(1, N+1):
            if arr[i][j] == 0:
                cnt_zero += 1
            else:
                rank += arr[i][j]

        cnt_zero -= 1
        if rank - cnt_zero > 0 or rank + cnt_zero < 0:
            cnt += 1


    return cnt

print(main())