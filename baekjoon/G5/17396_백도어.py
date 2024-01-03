# 240103
from sys import stdin
from heapq import heappush, heappop
from collections import defaultdict
def to_int(): return map(int, stdin.readline().split())

N, M = to_int()
sections = list(to_int()) # 지점별 이동 불가 여부 (도착점은 1이어도 이동 가능)
limit = N * int(1e5) # 최대 시간
path_info = defaultdict(list) # 길 정보
destinations = [limit] * N # 각 지점까지 걸리는 최소 시간
for _ in range(M):
    a, b, t = to_int()
    path_info[a].append((t, b))
    path_info[b].append((t, a))

destinations[0] = 0

heap = [(0, 0)]
while heap:
    time, end = heappop(heap)
    if sections[end] == 0 or end == N-1: # 도착점이거나 보이지 않는 지점

        if destinations[end] >= time:
            for each_time, next_position in path_info[end]:

                if sections[next_position] == 0 or next_position == N-1: # 도착점이거나 보이지 않는 지점
                    new_time = time + each_time

                    if new_time < destinations[next_position]:
                        destinations[next_position] = new_time
                        heappush(heap, (new_time, next_position))

print(destinations[-1] if destinations[-1] != limit else -1)



#
from sys import stdin
from heapq import heappush, heappop

def to_int(): return map(int, stdin.readline().split())


N, M = to_int()
sections = list(to_int())  # 지점별 이동 불가 여부 (도착점은 1이어도 이동 가능)
limit = N * int(1e5)  # 최대 시간
path_info = {i: [] for i in range(N)} # 길 정보
destinations = [limit] * N  # 각 지점까지 걸리는 최소 시간
for _ in range(M):
    a, b, t = to_int()
    path_info[a].append((t, b))
    path_info[b].append((t, a))

destinations[0] = 0

heap = [(0, 0)]
while heap:
    time, end = heappop(heap)
    if sections[end] == 0 or end == N - 1:  # 도착점이거나 보이지 않는 지점

        if destinations[end] >= time:
            for each_time, next_position in path_info[end]:

                if sections[next_position] == 0 or next_position == N - 1:  # 도착점이거나 보이지 않는 지점
                    new_time = time + each_time

                    if new_time < destinations[next_position]:
                        destinations[next_position] = new_time
                        heappush(heap, (new_time, next_position))

print(destinations[-1] if destinations[-1] != limit else -1)