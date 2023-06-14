#230614
# mst
from heapq import heappop, heapify, heappush
N = int(input())
visited = [False] * N
cost_list = []
min_cost = 0
flow = [list(map(int, input().split())) for i in range(N)]
for j in range(1, N):
    cost_list.append((flow[0][j], j))

visited[0] = True
heapify(cost_list)
for _ in range(N-1):
    while True:
        cost, planet = heappop(cost_list)
        if not visited[planet]:
            visited[planet] = True
            min_cost += cost
            for j in range(N):
                if j != planet:
                    heappush(cost_list, (flow[planet][j], j))
            break

print(min_cost)


#
def link_planet():
    N = int(input())
    flow = [list(map(int, input().split())) for _ in range(N)]
    cost_list = [(flow[0][j], j) for j in range(1, N)]

    def calc_min_cost():
        from heapq import heappop, heapify, heappush
        nonlocal cost_list

        min_cost = 0
        heapify(cost_list)
        visited = [False] * N
        visited[0] = True

        for _ in range(N-1):
            while True:
                cost, planet = heappop(cost_list)
                if not visited[planet]:
                    visited[planet] = True
                    min_cost += cost
                    for j in range(N):
                        if j != planet:
                            heappush(cost_list, (flow[planet][j], j))
                    break

        return min_cost

    return calc_min_cost()

print(link_planet())



#
def link_planet():
    N = int(input())
    flow = [list(map(int, input().split())) for _ in range(N)]
    cost_list = [(flow[0][j], j) for j in range(1, N)]

    def calc_min_cost():
        from heapq import heappop, heapify, heappush
        nonlocal cost_list

        min_cost = 0
        heapify(cost_list)
        visited = [False] * N
        visited[0] = True

        def find_cost():
            nonlocal min_cost
            while True:
                cost, planet = heappop(cost_list)
                if not visited[planet]:
                    visited[planet] = True
                    min_cost += cost
                    for j in range(N):
                        if j != planet:
                            heappush(cost_list, (flow[planet][j], j))
                    return

        for _ in range(N-1):
            find_cost()

        return min_cost

    return calc_min_cost()

print(link_planet())


#
def link_planet():
    N = int(input())
    flow = [list(map(int, input().split())) for _ in range(N)]
    cost_list = [(flow[0][j], j) for j in range(1, N)]

    def calc_min_cost():
        from heapq import heappop, heapify, heappush
        nonlocal cost_list

        min_cost = 0
        heapify(cost_list)
        visited = [False] * N
        visited[0] = True

        def find_cost():
            nonlocal min_cost
            while True:
                cost, planet = heappop(cost_list)
                if not visited[planet]:
                    visited[planet] = True
                    min_cost += cost
                    for j in range(N):
                        if not visited[j]:
                            heappush(cost_list, (flow[planet][j], j))
                    return

        for _ in range(N - 1):
            find_cost()

        return min_cost

    return calc_min_cost()


print(link_planet())


#
def link_planet():
    N = int(input())
    flow = [list(map(int, input().split())) for _ in range(N)]
    cost_list = []

    def calc_min_cost():
        from heapq import heappop, heappush
        for j in range(1, N):
            heappush(cost_list, (flow[0][j], j))

        min_cost = 0
        visited = [False] * N
        visited[0] = True

        def find_cost():
            nonlocal min_cost
            while True:
                cost, planet = heappop(cost_list)
                if not visited[planet]:
                    visited[planet] = True
                    min_cost += cost
                    for j in range(N):
                        if not visited[j]:
                            heappush(cost_list, (flow[planet][j], j))
                    return

        for _ in range(N - 1):
            find_cost()

        return min_cost

    return calc_min_cost()

print(link_planet())