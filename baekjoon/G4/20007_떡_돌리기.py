# 241007
# 52840 KB/ 2272 ms
def main():
    from heapq import heappush, heappop
    N, M, X, Y = map(int, input().split())
    road = [[] for _ in range(N)]

    for _ in range(M):
        A, B, C = map(int, input().split())
        road[A].append((C, B))
        road[B].append((C, A))

    day, limit = 1, (X//2)+1
    gap = [limit] * N
    heap = [(0, Y)]
    gap[Y] = 0

    while heap:
        time, house = heappop(heap)
        if time > gap[house]:
            continue
        for new_time, next_house in road[house]:
            total = time + new_time
            if total < gap[next_house]:
                gap[next_house] = total
                heappush(heap, (total, next_house))

    for i in range(N):
        heappush(heap, (gap[i], i))
    heappop(heap)

    distance = 0
    visited = [False] * N
    while heap:
        time, house = heappop(heap)
        total = distance + time
        if time >= limit:
            return -1
        elif total >= limit:
            day += 1
            distance = time
        else:
            distance = total
            visited[house] = True

    return day

print(main())



# 52832 KB/ 2252 ms
def main():
    from heapq import heappush, heappop
    N, M, X, Y = map(int, input().split())
    road = [[] for _ in range(N)]

    for _ in range(M):
        A, B, C = map(int, input().split())
        road[A].append((C, B))
        road[B].append((C, A))

    day, limit = 1, (X//2)+1
    gap = [limit] * N
    heap = [(0, Y)]
    gap[Y] = 0

    while heap:
        time, house = heappop(heap)
        if time > gap[house]:
            continue
        for new_time, next_house in road[house]:
            total = time + new_time
            if total < gap[next_house]:
                gap[next_house] = total
                heappush(heap, (total, next_house))

    sorted_by_dis = [(gap[i], i) for i in range(N)]
    distance = 0
    sorted_by_dis.sort()
    
    if sorted_by_dis[-1][0] >= limit:
        return -1
    
    for i in range(1, N):
        time, house = sorted_by_dis[i]
        total = distance + time
        if total >= limit:
            day += 1
            distance = time
        else:
            distance = total

    return day

print(main())




# 52840 KB/ 2256 ms
def main():
    from heapq import heappush, heappop
    
    N, M, X, Y = map(int, input().split())
    road = [[] for _ in range(N)]

    for _ in range(M):
        A, B, C = map(int, input().split())
        road[A].append((C, B))
        road[B].append((C, A))

    day, limit = 1, (X//2)+1
    gap = [limit] * N
    heap = [(0, Y)]
    gap[Y] = 0

    while heap:
        time, house = heappop(heap)
        if time > gap[house]:
            continue
        for new_time, next_house in road[house]:
            total = time + new_time
            if total < gap[next_house]:
                gap[next_house] = total
                heappush(heap, (total, next_house))

    sorted_by_dis = [(gap[i], i) for i in range(N)]
    distance = 0
    sorted_by_dis.sort(key=lambda x:x[0])

    if sorted_by_dis[-1][0] >= limit:
        return -1

    for i in range(1, N):
        time, house = sorted_by_dis[i]
        total = distance + time
        if total >= limit:
            day += 1
            distance = time
        else:
            distance = total

    return day

print(main())




# 52852 KB/ 2216 ms
def dijkstra(N, M, Y, limit):
    from heapq import heappush, heappop
    road = [[] for _ in range(N)]

    for _ in range(M):
        A, B, C = map(int, input().split())
        road[A].append((C, B))
        road[B].append((C, A))

    gap = [limit] * N
    heap = [(0, Y)]
    gap[Y] = 0

    while heap:
        time, house = heappop(heap)
        if time > gap[house]:
            continue
        for new_time, next_house in road[house]:
            total = time + new_time
            if total < gap[next_house]:
                gap[next_house] = total
                heappush(heap, (total, next_house))
    
    return gap

def calc_day(gap, N, limit):
    day = 1
    sorted_by_dis = [(gap[i], i) for i in range(N)]
    distance = 0
    sorted_by_dis.sort(key=lambda x: x[0])

    if sorted_by_dis[-1][0] >= limit:
        return -1

    for i in range(1, N):
        time, house = sorted_by_dis[i]
        total = distance + time
        if total >= limit:
            day += 1
            distance = time
        else:
            distance = total

    return day

def main():
    N, M, X, Y = map(int, input().split())
    limit = (X // 2) + 1
    gap = dijkstra(N, M, Y, limit)
    return calc_day(gap, N, limit)

print(main())



# 52800 KB/ 160 ms
def dijkstra(N, M, Y, limit):
    from sys import stdin
    from heapq import heappush, heappop
    
    road = [[] for _ in range(N)]

    for _ in range(M):
        A, B, C = map(int, stdin.readline().split())
        road[A].append((C, B))
        road[B].append((C, A))

    gap = [limit] * N
    heap = [(0, Y)]
    gap[Y] = 0

    while heap:
        time, house = heappop(heap)
        if time > gap[house]:
            continue
        for new_time, next_house in road[house]:
            total = time + new_time
            if total < gap[next_house]:
                gap[next_house] = total
                heappush(heap, (total, next_house))

    return gap

def calc_day(gap, N, limit):
    day = 1
    sorted_by_dis = [(gap[i], i) for i in range(N)]
    distance = 0
    sorted_by_dis.sort(key=lambda x: x[0])

    if sorted_by_dis[-1][0] >= limit:
        return -1

    for i in range(1, N):
        time, house = sorted_by_dis[i]
        total = distance + time
        if total >= limit:
            day += 1
            distance = time
        else:
            distance = total

    return day

def main():
    N, M, X, Y = map(int, input().split())
    limit = (X // 2) + 1
    gap = dijkstra(N, M, Y, limit)
    return calc_day(gap, N, limit)

print(main())



# 52840 KB/ 164 ms
def main():
    from sys import stdin
    from heapq import heappush, heappop
    
    def int_input():
        return map(int, stdin.readline().split())
    
    N, M, X, Y = int_input()
    road = [[] for _ in range(N)]

    for _ in range(M):
        A, B, C = int_input()
        road[A].append((C, B))
        road[B].append((C, A))

    day, limit = 1, (X//2)+1
    gap = [limit] * N
    heap = [(0, Y)]
    gap[Y] = 0

    while heap:
        time, house = heappop(heap)
        if time > gap[house]:
            continue
        for new_time, next_house in road[house]:
            total = time + new_time
            if total < gap[next_house]:
                gap[next_house] = total
                heappush(heap, (total, next_house))

    sorted_by_dis = [(gap[i], i) for i in range(N)]
    distance = 0
    sorted_by_dis.sort(key=lambda x:x[0])

    if sorted_by_dis[-1][0] >= limit:
        return -1

    for i in range(1, N):
        time, house = sorted_by_dis[i]
        total = distance + time
        if total >= limit:
            day += 1
            distance = time
        else:
            distance = total

    return day

print(main())


