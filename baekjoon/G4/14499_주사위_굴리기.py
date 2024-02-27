# 240227
# 31120 KB / 44 ms
N, M, y, x, _ = map(int, input().split())
map_info = [list(map(int, input().split())) for _ in range(N)]
commands = tuple(map(lambda command: int(command)-1,  input().split()))
dy, dx = [0, 0, -1, 1], [1, -1, 0, 0]
dice_ew, dice_ns = [0] * 2, [0] * 2
dice_bt = [0] * 2

for command in commands:
    ny, nx = y+dy[command], x+dx[command]
    if 0 <= ny < N and 0 <= nx < M:
        y, x = ny, nx
        number = map_info[y][x]
        if command < 2:
            idx, opposite = command, 1 - command
            dice_ew[idx], dice_ew[opposite], dice_bt[0], dice_bt[1] = dice_bt[1], dice_bt[0], dice_ew[idx], dice_ew[opposite]
        else:
            idx, opposite = command - 2, 3 - command
            dice_ns[idx], dice_ns[opposite], dice_bt[0], dice_bt[1] = dice_bt[1], dice_bt[0], dice_ns[idx], dice_ns[opposite]

        if number:
            map_info[y][x], dice_bt[0] = 0, number
        else:
            map_info[y][x] = dice_bt[0]

        print(dice_bt[1])

# 31120 KB / 44 ms
N, M, y, x, _ = map(int, input().split())
map_info = [list(map(int, input().split())) for _ in range(N)]
commands = tuple(map(lambda command: int(command)-1,  input().split()))
dy, dx = [0, 0, -1, 1], [1, -1, 0, 0]
dice_info = [0] * 6 # 동서 # 북남 # 아래위

for command in commands:
    ny, nx = y+dy[command], x+dx[command]
    if 0 <= ny < N and 0 <= nx < M:
        y, x = ny, nx
        number = map_info[y][x]
        if command < 2:
            idx, opposite = command, 1 - command
        else:
            idx, opposite = command, 5 - command
        dice_info[idx], dice_info[opposite], dice_info[-2], dice_info[-1] = dice_info[-1], dice_info[-2], dice_info[idx], dice_info[opposite]

        if number:
            map_info[y][x], dice_info[-2] = 0, number
        else:
            map_info[y][x] = dice_info[-2]

        print(dice_info[-1])

