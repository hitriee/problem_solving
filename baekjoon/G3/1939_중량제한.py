#230811
#
from sys import stdin
from collections import defaultdict
from heapq import heappush, heappop
def to_int(): return map(int, stdin.readline().split())
N, M = to_int()
limit = 0
link_info = defaultdict(list)
for _ in range(M):
    A, B, C = to_int()
    heappush(link_info[A], (-C, B))
    heappush(link_info[B], (-C, A))

start, end = to_int()
heap = list(link_info[start])
link_info[start].clear()
while heap:
    max_weight, island = heappop(heap)
    if island == end:
        max_weight = -max_weight
        if limit < max_weight:
            limit = max_weight
    else:
        while link_info[island]:
            weight, new = heappop(link_info[island])
            heappush(heap, (max(max_weight, weight), new))

print(limit)

#
from sys import stdin
from collections import defaultdict
from heapq import heappush, heappop
def to_int(): return map(int, stdin.readline().split())
N, M = to_int()
limit = 0
link_info = defaultdict(list)
for _ in range(M):
    A, B, C = to_int()
    heappush(link_info[A], (-C, B))
    heappush(link_info[B], (-C, A))

start, end = to_int()
heap = list(link_info[start])
link_info[start].clear()
while heap:
    max_weight, island = heappop(heap)
    if island == end:
        max_weight = -max_weight
        if limit < max_weight:
            limit = max_weight
    else:
        while link_info[island]:
            weight, new = heappop(link_info[island])
            max_val = max(max_weight, weight)
            if -max_val > limit:
                heappush(heap, (max_val, new))

print(limit)


#
def find_max_weight():
    from sys import stdin
    from heapq import heappush, heappop

    def to_int(): return map(int, stdin.readline().split())

    N, M = to_int()
    limit = 0
    link_info = {}
    for _ in range(M):
        A, B, C = to_int()
        if link_info.get(A):
            heappush(link_info[A], (-C, B))
        else:
            link_info[A] = [(-C, B)]
        if link_info.get(B):

            heappush(link_info[B], (-C, A))
        else:
            link_info[B] = [(-C, A)]

    start, end = to_int()
    heap = list(link_info[start])
    link_info[start].clear()

    while heap:
        max_weight, island = heappop(heap)
        if island == end:
            max_weight = -max_weight
            if limit < max_weight:
                limit = max_weight
        elif link_info.get(island):
            while link_info[island]:
                weight, new = heappop(link_info[island])
                max_val = max(max_weight, weight)
                if -max_val > limit:
                    heappush(heap, (max_val, new))

    return limit

print(find_max_weight())