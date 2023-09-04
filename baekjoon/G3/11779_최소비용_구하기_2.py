#230904
from sys import stdin
from heapq import heappush, heappop
N = int(stdin.readline())
M = int(stdin.readline())
bus_info = [[] for _ in range(N+1)]
min_cost = [2e8] * (N+1)
for _ in range(M):
    start, end, cost = map(int, stdin.readline().split())
    bus_info[start].append((cost, end))

start_city, end_city = map(int, stdin.readline().split())
before_list = list(range(N+1))
heap = [(0, start_city, 0)]
path = []
while heap:
    cost, mid_city, before = heappop(heap)
    if min_cost[mid_city] > cost:
        min_cost[mid_city] = cost
        before_list[mid_city] = before
        for next_cost, next_city in bus_info[mid_city]:
            new_cost = cost+next_cost
            if next_cost < min_cost[next_city]:
                heappush(heap, (new_cost, next_city, mid_city))

print(min_cost[end_city])

city = end_city
while city:
    path.append(city)
    city = before_list[city]

print(len(path))
print(*path[::-1])


#
def dijkstra(min_cost, before_list, bus_info, start_city, end_city):
    from heapq import heappush, heappop
    heap = [(0, start_city, 0)]

    while heap:
        cost, mid_city, before = heappop(heap)
        if min_cost[mid_city] > cost:
            min_cost[mid_city] = cost
            before_list[mid_city] = before
            for next_cost, next_city in bus_info[mid_city]:
                new_cost = cost + next_cost
                if next_cost < min_cost[next_city]:
                    heappush(heap, (new_cost, next_city, mid_city))

    return min_cost[end_city]

def find_path(before_list, city):
    path = []
    while city:
        path.append(str(city))
        city = before_list[city]

    str_path = ' '.join(path[::-1])
    return f'{len(path)}\n{str_path}'

def find_cost_path():
    from sys import stdin
    N = int(stdin.readline())
    M = int(stdin.readline())
    bus_info = [[] for _ in range(N + 1)]
    min_cost = [2e8] * (N + 1)
    for _ in range(M):
        start, end, cost = map(int, stdin.readline().split())
        bus_info[start].append((cost, end))

    start_city, end_city = map(int, stdin.readline().split())
    before_list = list(range(N + 1))

    print(dijkstra(min_cost, before_list, bus_info, start_city, end_city))

    print(find_path(before_list, end_city))

find_cost_path()


#
def dijkstra(min_cost, before_list, bus_info, start_city, end_city):
    from heapq import heappush, heappop
    heap = [(0, start_city, 0)]

    while heap:
        cost, mid_city, before = heappop(heap)
        if min_cost[mid_city] > cost:
            min_cost[mid_city] = cost
            before_list[mid_city] = before
            for next_cost, next_city in bus_info[mid_city]:
                new_cost = cost + next_cost
                if next_cost < min_cost[next_city]:
                    heappush(heap, (new_cost, next_city, mid_city))

    return min_cost[end_city]


def find_path(before_list, city):
    from collections import deque
    path = deque()
    while city:
        path.appendleft(str(city))
        city = before_list[city]

    str_path = ' '.join(path)
    return f'{len(path)}\n{str_path}'


def find_cost_path():
    from sys import stdin
    N = int(stdin.readline())
    M = int(stdin.readline())
    bus_info = [[] for _ in range(N + 1)]
    min_cost = [2e8] * (N + 1)
    for _ in range(M):
        start, end, cost = map(int, stdin.readline().split())
        bus_info[start].append((cost, end))

    start_city, end_city = map(int, stdin.readline().split())
    before_list = list(range(N + 1))

    print(dijkstra(min_cost, before_list, bus_info, start_city, end_city))

    print(find_path(before_list, end_city))


find_cost_path()