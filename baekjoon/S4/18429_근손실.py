#230416
N, K = map(int, input().split())
increase_values = list(map(int, input().split()))
visited = [False] * N
cnt = 0
def dfs(level=0, dif=0):
    global cnt
    if level == N:
        cnt += 1
        return
    for i in range(N):
        if not visited[i]:
            new_dif = dif - K + increase_values[i]
            if new_dif >= 0:
                visited[i] = True
                dfs(level+1, new_dif)
                visited[i] = False
dfs()
print(cnt)