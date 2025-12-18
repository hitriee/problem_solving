# 251218
# 123140 KB / 1280 ms
def main():
    from sys import stdin
    from heapq import heappush, heappop

    def minus_one(num):
        return int(num) - 1

    def int_input(func=int):
        return map(func, stdin.readline().split())

    N, M, K = int_input()
    link_info = [[] for _ in range(N)]
    for _ in range(M):
        u, v, c = int_input(minus_one)
        link_info[v].append((c+1, u))

    info = list(int_input(minus_one))
    length = len(info)
    if length == N:
        return 1

    limit = int(5e10)
    arr = [limit] * N
    heap = []

    for node in info:
        heap.append((0, node))
        arr[node] = 0

    while heap:
        dist1, node = heappop(heap)
        if arr[node] >= dist1:
            for dist2, next_node in link_info[node]:
                dist3 = dist1 + dist2
                if arr[next_node] > dist3:
                    arr[next_node] = dist3
                    heappush(heap, (dist3, next_node))

    max_dist = answer = 0
    for i in range(N):
        if arr[i] > max_dist:
            max_dist, answer = arr[i], i

    return f'{answer+1}\n{max_dist}'

print(main())





# 123140 KB / 1188 ms
def main():
    from sys import stdin
    from heapq import heappush, heappop

    def minus_one(num):
        return int(num) - 1

    def int_input(func=int):
        return map(func, stdin.readline().split())

    N, M, K = int_input()
    link_info = [[] for _ in range(N)]
    for _ in range(M):
        u, v, c = int_input(minus_one)
        link_info[v].append((c+1, u))


    limit = int(5e10)
    info = list(int_input(minus_one))
    arr = [limit] * N
    heap = []

    for node in info:
        heap.append((0, node))
        arr[node] = 0

    while heap:
        dist1, node = heappop(heap)
        if arr[node] >= dist1:
            for dist2, next_node in link_info[node]:
                dist3 = dist1 + dist2
                if arr[next_node] > dist3:
                    arr[next_node] = dist3
                    heappush(heap, (dist3, next_node))

    max_dist = answer = 0
    for i in range(N):
        if arr[i] > max_dist:
            max_dist, answer = arr[i], i

    return f'{answer+1}\n{max_dist}'

print(main())





# 123140 KB / 1272 ms
def main():
    from sys import stdin
    from heapq import heappush, heappop

    def minus_one(num):
        return int(num) - 1

    def int_input(func=int):
        return map(func, stdin.readline().split())

    N, M, K = int_input()
    link_info = [[] for _ in range(N)]
    for _ in range(M):
        u, v, c = int_input(minus_one)
        link_info[v].append((c+1, u))


    limit = int(1e10)
    info = list(int_input(minus_one))
    arr = [limit] * N
    heap = []

    for node in info:
        heap.append((0, node))
        arr[node] = 0

    while heap:
        dist1, node = heappop(heap)
        if arr[node] >= dist1:
            for dist2, next_node in link_info[node]:
                dist3 = dist1 + dist2
                if arr[next_node] > dist3:
                    arr[next_node] = dist3
                    heappush(heap, (dist3, next_node))

    max_dist = answer = 0
    for i in range(N):
        if arr[i] > max_dist:
            max_dist, answer = arr[i], i

    return f'{answer+1}\n{max_dist}'

print(main())





# 123140 KB / 1220 ms
def main():
    from sys import stdin
    from heapq import heappush, heappop

    def minus_one(num):
        return int(num) - 1

    def int_input(func=int):
        return map(func, stdin.readline().split())

    N, M, K = int_input()
    link_info = [[] for _ in range(N)]
    for _ in range(M):
        u, v, c = int_input(minus_one)
        link_info[v].append((c+1, u))


    limit = int(5e10)
    info = list(int_input(minus_one))
    arr = [limit] * N
    heap = []

    for node in info:
        heap.append((0, node))
        arr[node] = 0

    while heap:
        dist1, node = heappop(heap)
        if arr[node] >= dist1:
            for dist2, next_node in link_info[node]:
                dist3 = dist1 + dist2
                if arr[next_node] > dist3:
                    arr[next_node] = dist3
                    heappush(heap, (dist3, next_node))

    max_dist = answer = 0
    for i in sorted(set(range(N)) - set(info)):
        if arr[i] > max_dist:
            max_dist, answer = arr[i], i

    return f'{answer+1}\n{max_dist}'

print(main())