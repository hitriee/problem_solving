#230529
H, W = map(int, input().split())
height_list = list(map(int, input().split()))
total_amount = max_end = 0
start, end = 0, 1
start_height, end_height = height_list[start], height_list[end]
while True:
    if start_height <= height_list[end]:
        start = end
        start_height = height_list[start]
        end_height = -1
    else:
        total_amount += (start_height - height_list[end])
    end += 1
    if end >= W:
        break
    if end_height < height_list[end]:
        end_height = height_list[end]
        max_end = end

if start < W - 1:
    while True:
        total_amount -= (start_height - end_height) * (max_end - start)
        end_height = -1
        start = max_end
        for i in range(max_end+1, W):
            if end_height < height_list[i]:
                end_height = height_list[i]
                max_end = i
        if end_height == -1:
            break

print(total_amount)
