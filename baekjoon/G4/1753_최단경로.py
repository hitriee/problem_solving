# 240524
# 68220 KB / 668 ms
from sys import stdin
from heapq import heappush, heappop
new_input = stdin.readline

V, E = map(int, new_input().split())
start = int(new_input())
link_info = [[] for _ in range(V+1)]
limit = 6.1e9
shortest_path = [limit] * (V+1)

for _ in range(E):
    u, v, w = map(int, new_input().split())
    link_info[u].append((w, v))

heap = [(0, start)]
shortest_path[start] = 0

while heap:
    w, u = heappop(heap)
    if w > shortest_path[u]:
        continue

    for nw, nu in link_info[u]:
        tw = w + nw
        if tw < shortest_path[nu]:
            shortest_path[nu] = tw
            heappush(heap, (tw, nu))

for i in range(1, V+1):
    print('INF' if shortest_path[i] == limit else shortest_path[i])




# 68220 KB / 648 ms
from sys import stdin
from heapq import heappush, heappop
new_input = stdin.readline

V, E = map(int, new_input().split())
start = int(new_input())
link_info = [[] for _ in range(V+1)]
limit = 3.1e6
shortest_path = [limit] * (V+1)

for _ in range(E):
    u, v, w = map(int, new_input().split())
    link_info[u].append((w, v))

heap = [(0, start)]
shortest_path[start] = 0

while heap:
    w, u = heappop(heap)
    if w > shortest_path[u]:
        continue

    for nw, nu in link_info[u]:
        tw = w + nw
        if tw < shortest_path[nu]:
            shortest_path[nu] = tw
            heappush(heap, (tw, nu))

for i in range(1, V+1):
    print('INF' if shortest_path[i] == limit else shortest_path[i])


# 68308 KB / 612 ms
def dijkstra(start, shortest_path, link_info):
    from heapq import heappush, heappop

    heap = [(0, start)]
    shortest_path[start] = 0

    while heap:
        w, u = heappop(heap)
        if w > shortest_path[u]:
            continue

        for nw, nu in link_info[u]:
            tw = w + nw
            if tw < shortest_path[nu]:
                shortest_path[nu] = tw
                heappush(heap, (tw, nu))

def main():
    from sys import stdin
    new_input = stdin.readline

    V, E = map(int, new_input().split())
    start = int(new_input())
    link_info = [[] for _ in range(V+1)]
    limit = 3.1e6
    shortest_path = [limit] * (V+1)

    for _ in range(E):
        u, v, w = map(int, new_input().split())
        link_info[u].append((w, v))

    dijkstra(start, shortest_path, link_info)

    for i in range(1, V+1):
        print('INF' if shortest_path[i] == limit else shortest_path[i])

main()