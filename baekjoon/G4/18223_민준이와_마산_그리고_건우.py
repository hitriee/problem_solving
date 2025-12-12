# 251212
def main():
    from sys import stdin
    from heapq import heappush, heappop, heapify

    def int_input():
        return map(int, stdin.readline().split())

    V, E, P = int_input()
    link_info = [[] for _ in range(V+1)]
    limit = int(1e8)

    for _ in range(E):
        node1, node2, gap = int_input()
        link_info[node1].append((gap, node2))
        link_info[node2].append((gap, node1))

    def dijkstra(start):
        arr = [limit] * (V+1)
        heap = [(0, start)]
        arr[start] = 0

        while heap:
            distance, end = heappop(heap)
            if arr[end] < distance:
                continue

            for gap, new_end in link_info[end]:
                new_distance = distance+gap
                if new_distance < arr[new_end]:
                    arr[new_end] = new_distance
                    heappush(heap, (new_distance, new_end))

        return arr

    min_distances = dijkstra(1)

    return 'SAVE HIM' if min_distances[P] + dijkstra(P)[-1] == min_distances[-1] else 'GOOD BYE'

print(main())








# 37556 KB / 80 ms
def main():
    from sys import stdin
    from heapq import heappush, heappop

    def int_input():
        return map(int, stdin.readline().split())

    V, E, P = int_input()
    link_info = [[] for _ in range(V)]
    P -= 1
    limit = int(1e8)

    for _ in range(E):
        node1, node2, gap = int_input()
        node1 -= 1
        node2 -= 1
        link_info[node1].append((gap, node2))
        link_info[node2].append((gap, node1))

    def dijkstra(start):
        arr = [limit] * V
        heap = [(0, start)]
        arr[start] = 0

        while heap:
            distance, end = heappop(heap)
            if arr[end] < distance:
                continue

            for gap, new_end in link_info[end]:
                new_distance = distance+gap
                if new_distance < arr[new_end]:
                    arr[new_end] = new_distance
                    heappush(heap, (new_distance, new_end))

        return arr

    min_distances = dijkstra(0)

    return 'SAVE HIM' if min_distances[P] + dijkstra(P)[-1] == min_distances[-1] else 'GOOD BYE'

print(main())




# 37556 KB / 68 ms
def main():
    from sys import stdin
    from heapq import heappush, heappop

    def minus_one(num):
        return int(num) - 1

    def int_input(func=int):
        return map(func, stdin.readline().split())

    V, E, P = int_input()
    link_info = [[] for _ in range(V)]
    P -= 1
    limit = int(1e8)

    for _ in range(E):
        node1, node2, gap = int_input(minus_one)
        gap += 1
        link_info[node1].append((gap, node2))
        link_info[node2].append((gap, node1))

    def dijkstra(start):
        arr = [limit] * V
        heap = [(0, start)]
        arr[start] = 0

        while heap:
            distance, end = heappop(heap)
            if arr[end] < distance:
                continue

            for gap, new_end in link_info[end]:
                new_distance = distance+gap
                if new_distance < arr[new_end]:
                    arr[new_end] = new_distance
                    heappush(heap, (new_distance, new_end))

        return arr

    min_distances = dijkstra(0)

    return 'SAVE HIM' if min_distances[P] + dijkstra(P)[-1] == min_distances[-1] else 'GOOD BYE'

print(main())