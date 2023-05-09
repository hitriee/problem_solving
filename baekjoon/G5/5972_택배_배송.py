#230508
# 다익스트라
from sys import stdin
from heapq import heappop, heappush

def to_int(): return map(int, stdin.readline().rstrip().split())

N, M = to_int()
path = [[] for _ in range(N+1)]
visited = set()
for _ in range(M):
    A, B, C = to_int()
    path[A].append([C, A, B])
    path[B].append([C, B, A])
limit = 6e7
min_cost = [limit] * (N+1)
heap = [(0, 1)]
while heap:
    cost, now = heappop(heap)
    if min_cost[now] < cost:
        continue
    for via in path[now]:
        total = cost + via[0]
        if total < min_cost[via[2]]:
            min_cost[via[2]] = total
            heappush(heap, (total, via[2]))
print(min_cost[N])


#
from sys import stdin
from heapq import heappop, heappush

def to_int(): return map(int, stdin.readline().rstrip().split())

N, M = to_int()
path = [[] for _ in range(N+1)]
visited = set()
for _ in range(M):
    A, B, C = to_int()
    path[A].append([C, B])
    path[B].append([C, A])
limit = 6e7
min_cost = [limit] * (N+1)
heap = [(0, 1)]
while heap:
    cost, now = heappop(heap)
    if min_cost[now] < cost:
        continue
    for via in path[now]:
        total = cost + via[0]
        if total < min_cost[via[1]]:
            min_cost[via[1]] = total
            heappush(heap, (total, via[1]))
print(min_cost[N])


#
from sys import stdin
from heapq import heappop, heappush

def to_int(): return map(int, stdin.readline().rstrip().split())

N, M = to_int()
path = [[] for _ in range(N+1)]
visited = set()
for _ in range(M):
    A, B, C = to_int()
    path[A].append([C, B])
    path[B].append([C, A])
limit = 6e7
min_cost = [limit] * (N+1)
heap = [(0, 1)]
while heap:
    cost, now = heappop(heap)
    if min_cost[now] < cost:
        continue
    for via in path[now]:
        each_cost, farm = via
        total = cost + each_cost
        if total < min_cost[farm]:
            min_cost[farm] = total
            heappush(heap, (total, farm))
print(min_cost[N])


#
def deliver():
    from sys import stdin

    def to_int(): return map(int, stdin.readline().rstrip().split())

    def fill_path():
        for _ in range(M):
            A, B, C = to_int()
            path[A].append([C, B])
            path[B].append([C, A])

    def dijkstra():
        from heapq import heappop, heappush
        limit = 6e7
        min_cost = [limit] * (N+1)
        heap = [(0, 1)]
        while heap:
            cost, now = heappop(heap)
            if min_cost[now] >= cost:
                for via in path[now]:
                    each_cost, farm = via
                    total = cost + each_cost
                    if total < min_cost[farm]:
                        min_cost[farm] = total
                        heappush(heap, (total, farm))
        return min_cost[N]

    N, M = to_int()
    path = [[] for _ in range(N+1)]
    fill_path()
    print(dijkstra())

deliver()


