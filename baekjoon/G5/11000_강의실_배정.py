#230602
from sys import stdin
from heapq import heappush, heappop
new_input = stdin.readline

N = int(new_input())
schedule = [list(map(int, new_input().split())) for _ in range(N)]
schedule.sort(key=lambda time: (time[0], time[1]))
room = [0]

for i in range(N):
    start, end = schedule[i]
    if room[0] <= start:
        heappop(room)
    heappush(room, end)

print(len(room))

#
from sys import stdin
from heapq import heappush, heappop
new_input = stdin.readline

N = int(new_input())
schedule = [list(map(int, new_input().split())) for _ in range(N)]
schedule.sort()
room = [0]

for i in range(N):
    start, end = schedule[i]
    if room[0] <= start:
        heappop(room)
    heappush(room, end)

print(len(room))

#
def cnt_room():
    from sys import stdin
    from heapq import heappush, heappop
    new_input = stdin.readline

    N = int(new_input())
    schedule = [list(map(int, new_input().split())) for _ in range(N)]
    schedule.sort()
    room = [0]

    for i in range(N):
        start, end = schedule[i]
        if room[0] <= start:
            heappop(room)
        heappush(room, end)

    return len(room)
print(cnt_room())
