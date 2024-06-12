# 240612
# 31120 KB / 152 ms

from sys import stdin

def to_int():
    return map(int, stdin.readline().split())

N, M = to_int()
max_num = 5001
info = [[max_num] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = to_int()
    info[a][b] = 1
    info[b][a] = 1

for k in range(1, N+1):
    info[k][k] = 0
    for i in range(1, N+1):
        if i != k:
            for j in range(i+1, N+1):
                if j != k:
                    new_val = info[i][k] + info[k][j]
                    if info[i][j] > new_val:
                        info[i][j] = info[j][i] = new_val

min_total, person = max_num, 0
for i in range(1, N+1):
    total = sum(info[i][1:])
    if total < min_total:
        min_total, person = total, i

print(person)


# 33212 KB / 52 ms
from sys import stdin
from heapq import heappush, heappop, heapify

def to_int():
    return map(int, stdin.readline().split())

N, M = to_int()
max_num = 500001
info = [[] for _ in range(N+1)]
min_distance = [[max_num] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = to_int()
    info[a].append((1, b))
    info[b].append((1, a))
    min_distance[a][b] = min_distance[b][a] = 1

for i in range(1, N+1):
    min_distance[i][i] = 0
    heap = info[i][:]
    heapify(heap)
    while heap:
        dist, num = heappop(heap)
        if dist > min_distance[i][num]:
            continue
        for new_dist, new_num in info[num]:
            total_dist = dist + new_dist
            if total_dist < min_distance[i][new_num]:
                min_distance[i][new_num] = total_dist
                heappush(heap, (total_dist, new_num))


min_total, person = max_num, 0
for i in range(1, N+1):
    total = sum(min_distance[i][1:])
    if total < min_total:
        min_total, person = total, i

print(person)


# 33212 KB / 56 ms
from sys import stdin
from heapq import heappush, heappop, heapify

def to_int():
    return map(int, stdin.readline().split())

N, M = to_int()
max_num = 5001
info = [[] for _ in range(N+1)]
min_distance = [[max_num] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = to_int()
    info[a].append((1, b))
    info[b].append((1, a))
    min_distance[a][b] = min_distance[b][a] = 1

for i in range(1, N+1):
    min_distance[i][i] = 0
    heap = info[i][:]
    heapify(heap)
    while heap:
        dist, num = heappop(heap)
        if dist > min_distance[i][num]:
            continue
        for new_dist, new_num in info[num]:
            total_dist = dist + new_dist
            if total_dist < min_distance[i][new_num]:
                min_distance[i][new_num] = total_dist
                heappush(heap, (total_dist, new_num))


min_total, person = max_num, 0
for i in range(1, N+1):
    total = sum(min_distance[i][1:])
    if total < min_total:
        min_total, person = total, i

print(person)


#  33188 KB / 52 ms
from sys import stdin
from heapq import heappush, heappop, heapify

def to_int():
    return map(int, stdin.readline().split())

N, M = to_int()
max_num = 5001
info = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = to_int()
    info[a].append((1, b))
    info[b].append((1, a))

min_total, person = max_num, 0
for i in range(1, N+1):
    min_distance = [max_num] * (N+1)
    heap = [(0, i)]
    min_distance[i] = 0
    while heap:
        dist, num = heappop(heap)
        if dist > min_distance[num]:
            continue
        for new_dist, new_num in info[num]:
            total_dist = dist + new_dist
            if total_dist < min_distance[new_num]:
                min_distance[new_num] = total_dist
                heappush(heap, (total_dist, new_num))

    total = sum(min_distance[1:])
    if total < min_total:
        min_total, person = total, i

print(person)
