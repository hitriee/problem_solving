# 260224
# 60868 KB / 332 ms
def main():
    from sys import stdin
    from heapq import heappush, heappop

    def int_input():
        return map(int, stdin.readline().split())

    n, m = int_input()
    linked_info = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = int_input()
        linked_info[a].append((c, b))
        linked_info[b].append((c, a))

    s, t = int_input()
    limit = int(1e7)
    min_distance = [limit] * (n+1)
    min_distance[s] = 0
    heap = [(0, s)]

    while heap:
        dist, present_v = heappop(heap)
        if min_distance[present_v] >= dist:
            min_distance[present_v] = dist

            for next_dist, next_v in linked_info[present_v]:
                new_dist = dist + next_dist
                if min_distance[next_v] > new_dist:
                    heappush(heap, (new_dist, next_v))


    return min_distance[t]

print(main())










# 60868 KB / 336 ms
def main():
    from sys import stdin
    from heapq import heappush, heappop

    def int_input(func=int):
        return map(func, stdin.readline().split())

    def minus_one(num):
        return int(num) - 1

    n, m = int_input()
    linked_info = [[] for _ in range(n)]
    for _ in range(m):
        a, b, c = int_input(minus_one)
        c += 1
        linked_info[a].append((c, b))
        linked_info[b].append((c, a))

    s, t = int_input(minus_one)
    limit = int(1e7)
    min_distance = [limit] * n
    min_distance[s] = 0
    heap = [(0, s)]

    while heap:
        dist, present_v = heappop(heap)
        if min_distance[present_v] >= dist:
            min_distance[present_v] = dist

            for next_dist, next_v in linked_info[present_v]:
                new_dist = dist + next_dist
                if min_distance[next_v] > new_dist:
                    heappush(heap, (new_dist, next_v))


    return min_distance[t]

print(main())






# 60868 KB / 28 ms
def main():
    from sys import stdin
    from heapq import heappush, heappop

    def int_input():
        return map(int, stdin.readline().split())

    n, m = int_input()
    linked_info = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = int_input()
        linked_info[a].append((c, b))
        linked_info[b].append((c, a))

    limit = 100 * m
    s, t = int_input()
    min_distance = [limit] * (n+1)
    min_distance[s] = 0
    heap = [(0, s)]

    while heap:
        dist, present_v = heappop(heap)
        if min_distance[present_v] >= dist:
            min_distance[present_v] = dist

            for next_dist, next_v in linked_info[present_v]:
                new_dist = dist + next_dist
                if min_distance[next_v] > new_dist:
                    heappush(heap, (new_dist, next_v))


    return min_distance[t]

print(main())






# 54964 KB / 192 ms
def main():
    from sys import stdin
    from heapq import heappush, heappop

    def int_input():
        return map(int, stdin.readline().split())

    n, m = int_input()
    linked_info = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = int_input()
        linked_info[a].append((c, b))
        linked_info[b].append((c, a))

    limit = 100 * m
    s, t = int_input()
    min_distance = [limit] * (n+1)
    min_distance[s] = 0
    heap = [(0, s)]

    while heap:
        dist, present_v = heappop(heap)
        if min_distance[present_v] >= dist:

            for next_dist, next_v in linked_info[present_v]:
                new_dist = dist + next_dist
                if min_distance[next_v] > new_dist:
                    min_distance[next_v] = new_dist
                    heappush(heap, (new_dist, next_v))


    return min_distance[t]

print(main())






# 54964 KB / 156 ms
def main():
    from sys import stdin
    from heapq import heappush, heappop

    def int_input():
        return map(int, stdin.readline().split())

    n, m = int_input()
    linked_info = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = int_input()
        linked_info[a].append((c, b))
        linked_info[b].append((c, a))

    limit = 100 * m
    s, t = int_input()
    min_distance = [limit] * (n+1)
    min_distance[s] = 0
    heap = [(0, s)]

    while heap:
        dist, present_v = heappop(heap)
        if present_v == t:
            return min_distance[t]

        if min_distance[present_v] >= dist:

            for next_dist, next_v in linked_info[present_v]:
                new_dist = dist + next_dist
                if min_distance[next_v] > new_dist:
                    min_distance[next_v] = new_dist
                    heappush(heap, (new_dist, next_v))

print(main())