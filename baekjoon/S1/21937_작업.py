# 240717
# 53072 KB / 364 ms (Python 3)
# 134824 KB / 256 ms (PyPy3)
from sys import stdin
from collections import deque

def int_input():
    return map(int, stdin.readline().split())

N, M = int_input()
pre_work = [[] for _ in range(N+1)]
visited = set()
q = deque()

for _ in range(M):
    a, b = int_input()
    pre_work[b].append(a)

q.append(int(stdin.readline()))

while q:
    now = q.popleft()
    if now not in visited:
        visited.add(now)
        for work in pre_work[now]:
            if work not in visited:
                q.append(work)

print(len(visited)-1)




# 48672 KB / 340 ms
from sys import stdin
from collections import deque

def int_input():
    return map(int, stdin.readline().split())

N, M = int_input()
pre_work = [[] for _ in range(N+1)]
visited = [False] * (N+1)
q = deque()

for _ in range(M):
    a, b = int_input()
    pre_work[b].append(a)

q.append(int(stdin.readline()))

while q:
    now = q.popleft()
    if not visited[now]:
        visited[now] = True
        for work in pre_work[now]:
            if not visited[work]:
                q.append(work)

print(visited.count(True) - 1)
