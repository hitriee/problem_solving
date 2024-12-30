# 230803
# 241230
# 199840 KB / 1780 ms
def main():
    from sys import stdin
    from collections import deque

    new_input = stdin.readline

    N = int(new_input())
    link_info = [[] for _ in range(N+1)]
    children = [[] for _ in range(N+1)]
    levels = [0] * (N+1)
    for _ in range(N-1):
        a, b = map(int, new_input().split())
        link_info[a].append(b)
        link_info[b].append(a)

    q = deque()
    visited = [False] * (N+1)
    q.append((1, 0))
    visited[1] = True

    while q:
        node, level = q.popleft()
        level += 1
        for child in link_info[node]:
            if not visited[child]:
                visited[child] = True
                children[node].append(child)
                q.append((child, level))
                levels[child] = level

    total = 0

    for i in range(2, N + 1):
        if not children[i]:
            total += levels[i]


    return 'Yes' if total % 2 else 'No'

print(main())



# 159788 KB / 1396 ms
def main():
    from sys import stdin
    from collections import deque

    new_input = stdin.readline

    N = int(new_input())
    link_info = [[] for _ in range(N+1)]
    levels = [0] * (N+1)
    for _ in range(N-1):
        a, b = map(int, new_input().split())
        link_info[a].append(b)
        link_info[b].append(a)

    q = deque()
    visited = [False] * (N+1)
    q.append((1, 0))
    visited[1] = True

    while q:
        node, level = q.popleft()
        level += 1
        for child in link_info[node]:
            if not visited[child]:
                visited[child] = True
                q.append((child, level))
                levels[child] = level

    total = 0

    for i in range(2, N + 1):
        if len(link_info[i]) == 1:
            total += levels[i]


    return 'Yes' if total % 2 else 'No'

print(main())


# 158776 KB / 1412 ms
def main():
    from sys import stdin
    from collections import deque

    new_input = stdin.readline

    def bfs():
        q = deque()
        visited = [False] * (N+1)
        q.append((1, 0))
        visited[1] = True

        while q:
            node, level = q.popleft()
            level += 1
            for child in link_info[node]:
                if not visited[child]:
                    visited[child] = True
                    q.append((child, level))
                    levels[child] = level

    def calc_total():
        total = 0
        for i in range(2, N + 1):
            if len(link_info[i]) == 1:
                total += levels[i]
        return total


    N = int(new_input())
    link_info = [[] for _ in range(N + 1)]
    levels = [0] * (N + 1)
    for _ in range(N - 1):
        a, b = map(int, new_input().split())
        link_info[a].append(b)
        link_info[b].append(a)

    bfs()
    total = calc_total()

    return 'Yes' if total % 2 else 'No'

print(main())



# 154760 KB / 1240 ms
def main():
    from sys import stdin
    from collections import deque

    new_input = stdin.readline

    N = int(new_input())
    link_info = [[] for _ in range(N+1)]
    total = 0
    for _ in range(N-1):
        a, b = map(int, new_input().split())
        link_info[a].append(b)
        link_info[b].append(a)

    q = deque()
    visited = [False] * (N+1)
    q.append((1, 0))
    visited[1] = True

    while q:
        node, level = q.popleft()
        is_leaf = True
        for child in link_info[node]:
            if not visited[child]:
                is_leaf = False
                visited[child] = True
                q.append((child, level+1))

        if is_leaf:
            total += level

    return 'Yes' if total % 2 else 'No'

print(main())