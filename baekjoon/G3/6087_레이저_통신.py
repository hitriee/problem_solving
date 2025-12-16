# 251216
# 36532 KB / 96 ms
def main():
    from heapq import heappush, heappop

    W, H = map(int, input().split())
    map_info = [input() for _ in range(H)]
    limit = 10000
    end_y, end_x, heap = 0, 0, []
    delta_arr = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    arr = [[[limit] * 4 for _ in range(W)] for _ in range(H)]

    for i in range(H):
        for j in range(W):
            if map_info[i][j] == 'C':
                if not heap:
                    for k in range(4):
                        heap.append((0, k, i, j))
                        arr[i][j][k] = 0
                else:
                    end_y, end_x = i, j

    while heap:
        cnt, idx, y, x = heappop(heap)
        if arr[y][x][idx] < cnt:
            continue

        for i in range(4):
            dy, dx = delta_arr[i]
            ny, nx = y+dy, x+dx
            if 0 <= ny < H and 0 <= nx < W and map_info[ny][nx] != '*':
                if i == idx:
                    new_cnt = cnt
                elif i != 3-idx:
                    new_cnt = cnt+1
                else:
                    continue

                if arr[ny][nx][i] > new_cnt:
                    arr[ny][nx][i] = new_cnt
                    heappush(heap, (new_cnt, i, ny, nx))

    return min(arr[end_y][end_x])

print(main())





# 36532 KB / 96 ms
def main():
    from heapq import heappush, heappop

    W, H = map(int, input().split())
    map_info = [input() for _ in range(H)]
    limit = 10000
    end_y, end_x, heap = 0, 0, []
    delta_arr = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    arr = [[[limit] * 4 for _ in range(W)] for _ in range(H)]

    for i in range(H):
        for j in range(W):
            if map_info[i][j] == 'C':
                if not heap:
                    for k in range(4):
                        heap.append((0, k, i, j))
                        arr[i][j][k] = 0
                else:
                    end_y, end_x = i, j

    while heap:
        cnt, idx, y, x = heappop(heap)
        if arr[y][x][idx] < cnt:
            continue

        for i in range(4):
            dy, dx = delta_arr[i]
            ny, nx = y+dy, x+dx
            if 0 <= ny < H and 0 <= nx < W and map_info[ny][nx] != '*':
                if i == 3-idx:
                    continue
                if i == idx:
                    new_cnt = cnt
                else:
                    new_cnt = cnt+1

                if arr[ny][nx][i] > new_cnt:
                    arr[ny][nx][i] = new_cnt
                    heappush(heap, (new_cnt, i, ny, nx))

    return min(arr[end_y][end_x])

print(main())



# 36532 KB / 92 ms
def main():
    from heapq import heappush, heappop
    from sys import stdin

    new_input = stdin.readline

    W, H = map(int, new_input().split())
    map_info = [new_input().rstrip() for _ in range(H)]
    limit = 10000
    end_y, end_x, heap = 0, 0, []
    delta_arr = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    arr = [[[limit] * 4 for _ in range(W)] for _ in range(H)]

    for i in range(H):
        for j in range(W):
            if map_info[i][j] == 'C':
                if not heap:
                    for k in range(4):
                        heap.append((0, k, i, j))
                        arr[i][j][k] = 0
                else:
                    end_y, end_x = i, j

    while heap:
        cnt, idx, y, x = heappop(heap)
        if arr[y][x][idx] < cnt:
            continue

        for i in range(4):
            dy, dx = delta_arr[i]
            ny, nx = y+dy, x+dx
            if 0 <= ny < H and 0 <= nx < W and map_info[ny][nx] != '*':
                if i == 3-idx:
                    continue
                if i == idx:
                    new_cnt = cnt
                else:
                    new_cnt = cnt+1

                if arr[ny][nx][i] > new_cnt:
                    arr[ny][nx][i] = new_cnt
                    heappush(heap, (new_cnt, i, ny, nx))

    return min(arr[end_y][end_x])

print(main())




# 36532 KB / 88 ms
def main():
    from heapq import heappush, heappop
    from sys import stdin

    new_input = stdin.readline

    W, H = map(int, new_input().split())
    map_info = [new_input().rstrip() for _ in range(H)]
    limit = 10000
    end_y, end_x, heap = 0, 0, []
    delta_arr = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    arr = [[[limit] * 4 for _ in range(W)] for _ in range(H)]

    for i in range(H):
        for j in range(W):
            if map_info[i][j] == 'C':
                if not heap:
                    for k in range(4):
                        heap.append((0, k, i, j))
                        arr[i][j][k] = 0
                else:
                    end_y, end_x = i, j

    while heap:
        cnt, idx, y, x = heappop(heap)
        if arr[y][x][idx] < cnt:
            continue

        for i in range(4):
            dy, dx = delta_arr[i]
            ny, nx = y+dy, x+dx
            if 0 <= ny < H and 0 <= nx < W:
                if map_info[ny][nx] != '*' and i != 3-idx:
                    if i == idx:
                        new_cnt = cnt
                    else:
                        new_cnt = cnt+1

                    if arr[ny][nx][i] > new_cnt:
                        arr[ny][nx][i] = new_cnt
                        heappush(heap, (new_cnt, i, ny, nx))

    return min(arr[end_y][end_x])

print(main())