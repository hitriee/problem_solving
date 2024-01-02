# 240102
from sys import stdin
from collections import deque

def to_int():
    return map(int, stdin.readline().split())

N, M = to_int()
link_info = [set() for _ in range(N+1)]
visited = [False] * (N+1)
parent = [-1] * (N+1)
for _ in range(M):
    u, v = to_int()
    link_info[u].add(v)
    link_info[v].add(u)

def cnt_unnecessary(initial):
    new_cnt = 1
    q.append((initial, 0))
    visited[initial] = True
    parent[initial] = 0
    while q:
        node, level = q.popleft()
        level += 1
        for next_node in link_info[node]:
            if not visited[next_node]:
                q.append((next_node, level))
                visited[next_node] = True
                parent[next_node] = node
            elif parent[node] != next_node:
                new_cnt += 1
                link_info[next_node].remove(node)

    return new_cnt

cnt = -1 # 끊거나 이어야 하는 간선 개수
q = deque()
cnt += cnt_unnecessary(1)
for i in range(2, N+1):
    if not visited[i]:
        cnt += cnt_unnecessary(i)

print(cnt)

