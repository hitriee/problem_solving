#230412
# dfs
to_int = lambda : int(input())
N = to_int()
K = to_int()
cards = [input() for _ in range(N)]
visited = [False] * N
results = set()
def dfs(level, number):
    if level == K:
        results.add(number)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dfs(level+1, number + cards[i])
            visited[i] = False

dfs(0, '')
print(len(results))

# to_int 삭제
N = int(input())
K = int(input())
cards = [input() for _ in range(N)]
visited = [False] * N
results = set()
def dfs(level, number):
    if level == K:
        results.add(number)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dfs(level+1, number + cards[i])
            visited[i] = False

dfs(0, '')
print(len(results))

