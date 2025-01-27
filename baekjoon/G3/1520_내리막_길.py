# 230907
# 250127
# 45496 KB / 112 ms
def main():
    from sys import stdin, setrecursionlimit

    def int_input():
        return map(int, stdin.readline().split())

    N, M = int_input()
    height = [list(int_input()) for _ in range(N)]
    cnt = [[-1] * M for _ in range(N)]
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)

    setrecursionlimit(int(2.5e4))

    def dfs(y, x):
        if y == N-1 and x == M-1:
            return 1

        if cnt[y][x] != -1:
            return cnt[y][x]

        temp, ref = 0, height[y][x]
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < N and 0 <= nx < M and height[ny][nx] < ref:
                temp += dfs(ny, nx)

        cnt[y][x] = temp
        return temp

    return dfs(0, 0)

print(main())