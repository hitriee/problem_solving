#230608
N, D = map(int, input().split())
min_time = list(range(D+1))
short_road = [list(map(int, input().split())) for _ in range(N)]
short_road.sort()
for i in range(N):
    start, end, time = short_road[i]
    if end <= D:
        new_time = min_time[start] + time
        if new_time < min_time[end]:
            min_time[end] = new_time
            for i in range(end+1, D+1):
                if new_time + i-end < min_time[i]:
                    min_time[i] = new_time + i - end
print(min_time[-1])


#
def find_min_time():
    N, D = map(int, input().split())
    min_time = list(range(D+1))
    short_road = [list(map(int, input().split())) for _ in range(N)]
    short_road.sort()
    for i in range(N):
        start, end, time = short_road[i]
        if end <= D:
            new_time = min_time[start] + time
            if new_time < min_time[end]:
                min_time[end] = new_time
                for i in range(end+1, D+1):
                    if new_time + i-end < min_time[i]:
                        min_time[i] = new_time + i - end
    return min_time[-1]

print(find_min_time())


#
N, D = map(int, input().split())
min_time = list(range(D+1))
short_road = [list(map(int, input().split())) for _ in range(N)]
short_road.sort()
for start, end, time in short_road:
    if end <= D:
        new_time = min_time[start] + time
        if new_time < min_time[end]:
            min_time[end] = new_time
            for i in range(end+1, D+1):
                if new_time + i-end < min_time[i]:
                    min_time[i] = new_time + i - end
print(min_time[-1])
