#230401
# dfs 이용
N, M = map(int, input().split())
visited = [False] * (N+1)
path = []
def dfs(level):
    if level == M:
        print(*path)
        return
    for i in range(1, N+1):
        if not visited[i]:
            path.append(i)
            visited[i] = True
            dfs(level+1)
            visited[i] = False
            path.pop()
dfs(0)