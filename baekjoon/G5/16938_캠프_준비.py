# 251021
# 32412 KB / 44 ms
def main():
    # 문제 개수, 난이도 범위, 난이도 차이
    N, L, R, X = map(int, input().split())
    difficulty = list(map(int, input().split()))
    difficulty.sort()

    def dfs(level, start, end, total):
        nonlocal cnt
        if total > R:
            return

        if total >= L:
            cnt += 1

        if level == N:
            return

        for k in range(start, end):
            dfs(level, k+1, end, total+difficulty[k])


    cnt = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if difficulty[j] - difficulty[i] >= X:
                total = difficulty[i] + difficulty[j]
                dfs(2, i+1, j, total)


    return cnt

print(main())