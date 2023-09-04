#230904
N, M, R = map(int, input().split())
item_list = [0] + list(map(int, input().split()))
limit = 2000
road_info = [[limit] * (N+1) for _ in range(N+1)]
for _ in range(R):
    a, b, l = map(int, input().split())
    road_info[a][b] = l
    road_info[b][a] = l

for k in range(1, N+1):
    for i in range(1, N):
        if i != k:
            for j in range(i+1, N+1):
                if j != k:
                    short_distance = road_info[i][k] + road_info[k][j]
                    if short_distance < road_info[i][j]:
                        road_info[i][j] = short_distance
                        road_info[j][i] = short_distance
max_total_item = 0
for j in range(1, N+1):
    max_item = item_list[j]
    for i in range(1, N+1):
        if i != j and road_info[i][j] <= M:
            max_item += item_list[i]
    if max_total_item < max_item:
        max_total_item = max_item

print(max_total_item)


#
def cnt_max_items():
    N, M, R = map(int, input().split())
    item_list = [0] + list(map(int, input().split()))
    limit = 2000
    road_info = [[limit] * (N+1) for _ in range(N+1)]
    for _ in range(R):
        a, b, l = map(int, input().split())
        road_info[a][b] = l
        road_info[b][a] = l

    for k in range(1, N+1):
        for i in range(1, N):
            if i != k:
                for j in range(i+1, N+1):
                    if j != k:
                        short_distance = road_info[i][k] + road_info[k][j]
                        if short_distance < road_info[i][j]:
                            road_info[i][j] = short_distance
                            road_info[j][i] = short_distance
    max_total_item = 0
    for j in range(1, N+1):
        max_item = item_list[j]
        for i in range(1, N+1):
            if i != j and road_info[i][j] <= M:
                max_item += item_list[i]
        if max_total_item < max_item:
            max_total_item = max_item

    return max_total_item

print(cnt_max_items())

