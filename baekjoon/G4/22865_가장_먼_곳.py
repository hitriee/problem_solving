#230901
#230904
from sys import stdin
from heapq import heappush, heappop
N = int(stdin.readline())
destinations = set(map(int, stdin.readline().split()))
M = int(stdin.readline())
limit = int(1e9)
link_info = [[] for _ in range(N+1)]
distance_list = [[limit] * (N+1) for _ in range(3)]
for _ in range(M):
    D, E, distance = map(int, stdin.readline().split())
    link_info[D].append((distance, E))
    link_info[E].append((distance, D))

for i in range(len(destinations)):
    heap = [(0, destinations.pop())]
    while heap:
        distance, end = heappop(heap)
        if distance < distance_list[i][end]:
            distance_list[i][end] = distance
            for next_distance, new in link_info[end]:
                new_distance = distance + next_distance
                if new_distance < distance_list[i][new]:
                    heappush(heap, (new_distance, new))

max_distance = num = 0
for i in range(1, N+1):
    min_distance = limit
    for j in range(3):
        if min_distance > distance_list[j][i]:
            min_distance = distance_list[j][i]
    if max_distance < min_distance:
        max_distance = min_distance
        num = i

print(num)


#
def find_ground_num():
    from sys import stdin
    from heapq import heappush, heappop
    N = int(stdin.readline())
    destinations = set(map(int, stdin.readline().split()))
    M = int(stdin.readline())
    limit = int(1e9)
    link_info = [[] for _ in range(N + 1)]
    distance_list = [[limit] * (N + 1) for _ in range(3)]
    for _ in range(M):
        D, E, distance = map(int, stdin.readline().split())
        link_info[D].append((distance, E))
        link_info[E].append((distance, D))

    for i in range(len(destinations)):
        heap = [(0, destinations.pop())]
        while heap:
            distance, end = heappop(heap)
            if distance < distance_list[i][end]:
                distance_list[i][end] = distance
                for next_distance, new in link_info[end]:
                    new_distance = distance + next_distance
                    if new_distance < distance_list[i][new]:
                        heappush(heap, (new_distance, new))

    max_distance = num = 0
    for i in range(1, N + 1):
        min_distance = limit
        for j in range(3):
            if min_distance > distance_list[j][i]:
                min_distance = distance_list[j][i]
        if max_distance < min_distance:
            max_distance = min_distance
            num = i

    return num

print(find_ground_num())


#
def change_distance_list(distance_list, link_info, destinations):
    from heapq import heappush, heappop
    for i in range(len(destinations)):
        heap = [(0, destinations.pop())]
        while heap:
            distance, end = heappop(heap)
            if distance < distance_list[i][end]:
                distance_list[i][end] = distance
                for next_distance, new in link_info[end]:
                    new_distance = distance + next_distance
                    if new_distance < distance_list[i][new]:
                        heappush(heap, (new_distance, new))

def find_ground_num():
    from sys import stdin
    N = int(stdin.readline())
    destinations = set(map(int, stdin.readline().split()))
    M = int(stdin.readline())
    limit = int(1e9)
    link_info = [[] for _ in range(N + 1)]
    distance_list = [[limit] * (N + 1) for _ in range(3)]
    for _ in range(M):
        D, E, distance = map(int, stdin.readline().split())
        link_info[D].append((distance, E))
        link_info[E].append((distance, D))

    change_distance_list(distance_list, link_info, destinations)

    max_distance = num = 0
    for i in range(1, N + 1):
        min_distance = limit
        for j in range(3):
            if min_distance > distance_list[j][i]:
                min_distance = distance_list[j][i]
        if max_distance < min_distance:
            max_distance = min_distance
            num = i

    return num

print(find_ground_num())


#
def find_ground_num():
    from sys import stdin
    from heapq import heappush, heappop
    N = int(stdin.readline())
    destinations = set(map(int, stdin.readline().split()))
    length = len(destinations)
    M = int(stdin.readline())
    limit = int(1e9)
    link_info = [[] for _ in range(N + 1)]
    distance_list = [[limit] * (N + 1) for _ in range(length)]
    for _ in range(M):
        D, E, distance = map(int, stdin.readline().split())
        link_info[D].append((distance, E))
        link_info[E].append((distance, D))

    for i in range(length):
        heap = [(0, destinations.pop())]
        while heap:
            distance, end = heappop(heap)
            if distance < distance_list[i][end]:
                distance_list[i][end] = distance
                for next_distance, new in link_info[end]:
                    new_distance = distance + next_distance
                    if new_distance < distance_list[i][new]:
                        heappush(heap, (new_distance, new))

    max_distance = num = 0
    for i in range(1, N + 1):
        min_distance = limit
        for j in range(length):
            if min_distance > distance_list[j][i]:
                min_distance = distance_list[j][i]
        if max_distance < min_distance:
            max_distance = min_distance
            num = i

    return num

print(find_ground_num())