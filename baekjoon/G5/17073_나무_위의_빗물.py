# 241014
# 126528 KB / 1176 ms
def main():
    from sys import stdin
    from collections import deque

    def int_input():
        return map(int, stdin.readline().split())

    N, W = int_input()
    link = [[] for _ in range(N+1)]
    visited = [False] * (N+1)
    for _ in range(N-1):
        u, v = int_input()
        link[u].append(v)
        link[v].append(u)

    q = deque()
    q.append(1)
    visited[1] = True
    cnt = 0
    while q:
        node = q.popleft()
        has_child = False

        for next_node in link[node]:
            if not visited[next_node]:
                has_child = True
                visited[next_node] = True
                q.append(next_node)

        if not has_child:
            cnt += 1

    return W/cnt

print(main())




# 126496 KB / 1172 ms
def main():
    from sys import stdin
    from collections import deque

    def int_input():
        return map(int, stdin.readline().split())

    N, W = int_input()
    link = [[] for _ in range(N+1)]
    visited = [False] * (N+1)
    for _ in range(N-1):
        u, v = int_input()
        link[u].append(v)
        link[v].append(u)

    q = deque()
    q.append(1)
    visited[1] = True
    cnt = 0
    while q:
        node = q.popleft()
        has_child = False

        for next_node in link[node]:
            if not visited[next_node]:
                has_child = True
                visited[next_node] = True
                q.append(next_node)

        if not has_child:
            cnt += 1

    return round(W/cnt, 4)

print(main())
