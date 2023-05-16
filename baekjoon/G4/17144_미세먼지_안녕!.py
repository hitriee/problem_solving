# #230516
# # 구현
# from sys import stdin
# def to_int(): return map(int, stdin.readline().split())
#
# R, C, T = to_int()
# room = []
# cleaner = []
# dust = set()
# for i in range(R):
#     room.append(list(to_int()))
#     if room[-1][0] == -1:
#         cleaner.append(i)
#     elif room[-1][0]:
#         dust.add((i, 0))
#
#     for j in range(1, C):
#         if room[-1][j]:
#             dust.add((i, j))
#
# def change_room_state():
#     global room, dust
#     temp_room = [[0] * C for _ in range(R)]
#     temp_dust = set(dust)
#     for i in cleaner:
#         temp_room[i][0] = -1
#     # 먼지 확산
#     while dust:
#         y, x = dust.pop()
#         cnt = 0
#         amount = room[y][x]//5
#         for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
#             ny, nx = y+dy, x+dx
#             if 0 <= ny < R and 0 <= nx < C and room[ny][nx] != -1:
#                 cnt += 1
#                 temp_room[ny][nx] += amount
#                 temp_dust.add((ny, nx))
#         temp_room[y][x] += room[y][x] - amount * cnt
#
#     def vertical_move(start, end, step, col):
#         for ni in range(start, end, step):
#             if (ni, col) in temp_dust:
#                 temp_dust.remove((ni, col))
#                 temp_room[ni-step][col], temp_room[ni][col] = temp_room[ni][col], 0
#                 temp_dust.add((ni - step, col))
#
#     def horizontal_move(start, end, step, row):
#         for j in range(start, end, step):
#             if (row, j) in temp_dust:
#                 temp_dust.remove((row, j))
#                 temp_room[row][j], temp_room[row][j-step] = 0, temp_room[row][j]
#                 temp_dust.add((row, j - step))
#     # 먼지 제거
#     for i in range(2):
#         y = cleaner[i]
#         step = -1 if i == 0 else 1
#         # 위 또는 아래로 이동
#         # 공기 청정기로 들어가는 먼지
#         ny = y+step
#         if (ny, 0) in temp_dust:
#             temp_dust.remove((ny, 0))
#             temp_room[ny][0] = 0
#         # 이동
#         vertical_move(ny+step, (R-1) * i + step, step, 0)
#         # 오른쪽 이동
#         horizontal_move(1, C, 1, (R-1) * i)
#         # 위 또는 아래 이동
#         vertical_move((R-1) * i - step, y - step, -step,  C-1)
#         # 왼쪽 이동
#         horizontal_move(C-2, 0, -1, y)
#
#     # room, dust 갱신
#     room = [temp_room[i][:] for i in range(R)]
#     dust = set(temp_dust)
#
# for _ in range(T):
#     change_room_state()
#
# total_dust = 0
# for i in range(R):
#     total_dust += sum(room[i])
# print(total_dust + 2)
#
#
# # 먼지 들어갈 때마다 계산
# from sys import stdin
# def to_int(): return map(int, stdin.readline().split())
#
# R, C, T = to_int()
# room = []
# cleaner = []
# dust = set()
# total_dust = 0
# for i in range(R):
#     room.append(list(to_int()))
#     state = room[-1][0]
#     if state == -1:
#         cleaner.append(i)
#     elif state:
#         dust.add((i, 0))
#         total_dust += state
#
#     for j in range(1, C):
#         state = room[-1][j]
#         if state:
#             dust.add((i, j))
#             total_dust += state
#
# def change_room_state():
#     global total_dust, room, dust
#     temp_room = [[0] * C for _ in range(R)]
#     temp_dust = set(dust)
#     for i in cleaner:
#         temp_room[i][0] = -1
#     # 먼지 확산
#     while dust:
#         y, x = dust.pop()
#         cnt = 0
#         amount = room[y][x]//5
#         for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
#             ny, nx = y+dy, x+dx
#             if 0 <= ny < R and 0 <= nx < C and room[ny][nx] != -1:
#                 cnt += 1
#                 temp_room[ny][nx] += amount
#                 temp_dust.add((ny, nx))
#         temp_room[y][x] += room[y][x] - amount * cnt
#
#     def vertical_move(start, end, step, col):
#         for ni in range(start, end, step):
#             if (ni, col) in temp_dust:
#                 temp_dust.remove((ni, col))
#                 temp_room[ni-step][col], temp_room[ni][col] = temp_room[ni][col], 0
#                 temp_dust.add((ni - step, col))
#
#     def horizontal_move(start, end, step, row):
#         for j in range(start, end, step):
#             if (row, j) in temp_dust:
#                 temp_dust.remove((row, j))
#                 temp_room[row][j], temp_room[row][j-step] = 0, temp_room[row][j]
#                 temp_dust.add((row, j - step))
#     # 먼지 제거
#     for i in range(2):
#         y = cleaner[i]
#         step = -1 if i == 0 else 1
#         # 위 또는 아래로 이동
#         # 공기 청정기로 들어가는 먼지
#         ny = y+step
#         if (ny, 0) in temp_dust:
#             temp_dust.remove((ny, 0))
#             total_dust -= temp_room[ny][0]
#             temp_room[ny][0] = 0
#
#         # 이동
#         vertical_move(ny+step, (R-1) * i + step, step, 0)
#         # 오른쪽 이동
#         horizontal_move(1, C, 1, (R-1) * i)
#         # 위 또는 아래 이동
#         vertical_move((R-1) * i - step, y - step, -step,  C-1)
#         # 왼쪽 이동
#         horizontal_move(C-2, 0, -1, y)
#
#     # room, dust 갱신
#     room = [temp_room[i][:] for i in range(R)]
#     dust = set(temp_dust)
#
# for _ in range(T):
#     change_room_state()
#
# print(total_dust)
#
#
# #
# from sys import stdin
# def to_int(): return map(int, stdin.readline().split())
#
# R, C, T = to_int()
# room = []
# cleaner = []
# dust = set()
# total_dust = 0
# for i in range(R):
#     room.append(list(to_int()))
#     state = room[-1][0]
#     if state == -1:
#         cleaner.append(i)
#     elif state:
#         dust.add((i, 0))
#         total_dust += state
#
#     for j in range(1, C):
#         state = room[-1][j]
#         if state:
#             dust.add((i, j))
#             total_dust += state
#
# def change_room_state():
#     global total_dust, room, dust
#     temp_room = [[0] * C for _ in range(R)]
#     temp_dust = set(dust)
#     for i in cleaner:
#         temp_room[i][0] = -1
#     # 먼지 확산
#     while dust:
#         y, x = dust.pop()
#         cnt = 0
#         amount = room[y][x]//5
#         for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
#             ny, nx = y+dy, x+dx
#             if 0 <= ny < R and 0 <= nx < C and room[ny][nx] != -1:
#                 cnt += 1
#                 temp_room[ny][nx] += amount
#                 temp_dust.add((ny, nx))
#         temp_room[y][x] += room[y][x] - amount * cnt
#
#     def vertical_move(start, end, step, col):
#         for ni in range(start, end, step):
#             if (ni, col) in temp_dust:
#                 temp_dust.remove((ni, col))
#                 temp_room[ni-step][col] = temp_room[ni][col]
#                 temp_dust.add((ni - step, col))
#
#     def horizontal_move(start, end, step, row):
#         for j in range(start, end, step):
#             if (row, j) in temp_dust:
#                 temp_dust.remove((row, j))
#                 temp_room[row][j-step] = temp_room[row][j]
#                 temp_dust.add((row, j - step))
#     # 먼지 제거
#     for i in range(2):
#         y = cleaner[i]
#         step = -1 if i == 0 else 1
#         # 위 또는 아래로 이동
#         # 공기 청정기로 들어가는 먼지
#         ny = y+step
#         if (ny, 0) in temp_dust:
#             temp_dust.remove((ny, 0))
#             total_dust -= temp_room[ny][0]
#             temp_room[ny][0] = 0
#
#         # 이동
#         vertical_move(ny+step, (R-1) * i + step, step, 0)
#         # 오른쪽 이동
#         horizontal_move(1, C, 1, (R-1) * i)
#         # 위 또는 아래 이동
#         vertical_move((R-1) * i - step, y - step, -step,  C-1)
#         # 왼쪽 이동
#         horizontal_move(C-2, 0, -1, y)
#
#         temp_room[y][1] = 0
#
#     # room, dust 갱신
#     room = [temp_room[i][:] for i in range(R)]
#     dust = set(temp_dust)
#
# for _ in range(T):
#     change_room_state()
#
# print(total_dust)
#
#
# # for문 돌면서 요소에 할당
# from sys import stdin
# def to_int(): return map(int, stdin.readline().split())
#
# R, C, T = to_int()
# room = []
# cleaner = []
# dust = set()
# total_dust = 0
# for i in range(R):
#     room.append(list(to_int()))
#     state = room[-1][0]
#     if state == -1:
#         cleaner.append(i)
#     elif state:
#         dust.add((i, 0))
#         total_dust += state
#
#     for j in range(1, C):
#         state = room[-1][j]
#         if state:
#             dust.add((i, j))
#             total_dust += state
#
# def change_room_state():
#     global total_dust, room, dust
#     temp_room = [[0] * C for _ in range(R)]
#     temp_dust = set(dust)
#     for i in cleaner:
#         temp_room[i][0] = -1
#     # 먼지 확산
#     while dust:
#         y, x = dust.pop()
#         cnt = 0
#         amount = room[y][x]//5
#         for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
#             ny, nx = y+dy, x+dx
#             if 0 <= ny < R and 0 <= nx < C and room[ny][nx] != -1:
#                 cnt += 1
#                 temp_room[ny][nx] += amount
#                 temp_dust.add((ny, nx))
#         temp_room[y][x] += room[y][x] - amount * cnt
#
#     def vertical_move(start, end, step, col):
#         for ni in range(start, end, step):
#             if (ni, col) in temp_dust:
#                 temp_dust.remove((ni, col))
#                 temp_room[ni-step][col] = temp_room[ni][col]
#                 temp_dust.add((ni - step, col))
#
#     def horizontal_move(start, end, step, row):
#         for j in range(start, end, step):
#             if (row, j) in temp_dust:
#                 temp_dust.remove((row, j))
#                 temp_room[row][j-step] = temp_room[row][j]
#                 temp_dust.add((row, j - step))
#     # 먼지 제거
#     for i in range(2):
#         y = cleaner[i]
#         step = -1 if i == 0 else 1
#         # 위 또는 아래로 이동
#         # 공기 청정기로 들어가는 먼지
#         ny = y+step
#         if (ny, 0) in temp_dust:
#             temp_dust.remove((ny, 0))
#             total_dust -= temp_room[ny][0]
#             temp_room[ny][0] = 0
#
#         # 이동
#         vertical_move(ny+step, (R-1) * i + step, step, 0)
#         # 오른쪽 이동
#         horizontal_move(1, C, 1, (R-1) * i)
#         # 위 또는 아래 이동
#         vertical_move((R-1) * i - step, y - step, -step,  C-1)
#         # 왼쪽 이동
#         horizontal_move(C-2, 0, -1, y)
#
#         temp_room[y][1] = 0
#
#     # room, dust 갱신
#     for i in range(R):
#         for j in range(C):
#             room[i][j] = temp_room[i][j]
#     dust = set(temp_dust)
#
# for _ in range(T):
#     change_room_state()
#
# print(total_dust)


# set 제거
from sys import stdin
def to_int(): return map(int, stdin.readline().split())

R, C, T = to_int()
room = []
cleaner = []
total_dust = 0
for i in range(R):
    room.append(list(to_int()))
    state = room[-1][0]
    if state == -1:
        cleaner.append(i)
    elif state:
        total_dust += state

    for j in range(1, C):
        state = room[-1][j]
        if state:
            total_dust += state

def change_room_state():
    global total_dust, room
    temp_room = [[0] * C for _ in range(R)]
    for i in cleaner:
        temp_room[i][0] = -1

    # 먼지 확산
    for y in range(R):
        for x in range(C):
            if room[y][x] > 0:
                cnt = 0
                amount = room[y][x]//5
                for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
                    ny, nx = y+dy, x+dx
                    if 0 <= ny < R and 0 <= nx < C and room[ny][nx] != -1:
                        cnt += 1
                        temp_room[ny][nx] += amount
                temp_room[y][x] += room[y][x] - amount * cnt

    def vertical_move(start, end, step, col):
        for ni in range(start, end, step):
            if temp_room[ni][col]:
                temp_room[ni-step][col] = temp_room[ni][col]
                temp_room[ni][col] = 0

    def horizontal_move(start, end, step, row):
        for j in range(start, end, step):
            if temp_room[row][j]:
                temp_room[row][j-step] = temp_room[row][j]
                temp_room[row][j] = 0
    # 먼지 제거
    for i in range(2):
        y = cleaner[i]
        step = -1 if i == 0 else 1
        # 위 또는 아래로 이동
        # 공기 청정기로 들어가는 먼지
        ny = y+step
        if temp_room[ny][0]:
            total_dust -= temp_room[ny][0]
            temp_room[ny][0] = 0

        # 위 또는 아래 이동
        vertical_move(ny+step, (R-1) * i + step, step, 0)
        # 오른쪽 이동
        horizontal_move(1, C, 1, (R-1) * i)
        # 위 또는 아래 이동
        vertical_move((R-1) * i - step, y - step, -step,  C-1)
        # 왼쪽 이동
        horizontal_move(C-2, 0, -1, y)

        temp_room[y][1] = 0

    # room, dust 갱신
    room.clear()
    room.extend(temp_room[i][:] for i in range(R))

for _ in range(T):
    change_room_state()

print(total_dust)


# append
from sys import stdin
def to_int(): return map(int, stdin.readline().split())

R, C, T = to_int()
room = []
cleaner = []
total_dust = 0
for i in range(R):
    room.append(list(to_int()))
    state = room[-1][0]
    if state == -1:
        cleaner.append(i)
    elif state:
        total_dust += state

    for j in range(1, C):
        state = room[-1][j]
        if state:
            total_dust += state

def change_room_state():
    global total_dust, room
    temp_room = [[0] * C for _ in range(R)]
    for i in cleaner:
        temp_room[i][0] = -1

    # 먼지 확산
    for y in range(R):
        for x in range(C):
            if room[y][x] > 0:
                cnt = 0
                amount = room[y][x]//5
                for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
                    ny, nx = y+dy, x+dx
                    if 0 <= ny < R and 0 <= nx < C and room[ny][nx] != -1:
                        cnt += 1
                        temp_room[ny][nx] += amount
                temp_room[y][x] += room[y][x] - amount * cnt

    def vertical_move(start, end, step, col):
        for ni in range(start, end, step):
            if temp_room[ni][col]:
                temp_room[ni-step][col] = temp_room[ni][col]
                temp_room[ni][col] = 0

    def horizontal_move(start, end, step, row):
        for j in range(start, end, step):
            if temp_room[row][j]:
                temp_room[row][j-step] = temp_room[row][j]
                temp_room[row][j] = 0
    # 먼지 제거
    for i in range(2):
        y = cleaner[i]
        step = -1 if i == 0 else 1
        # 위 또는 아래로 이동
        # 공기 청정기로 들어가는 먼지
        ny = y+step
        if temp_room[ny][0]:
            total_dust -= temp_room[ny][0]
            temp_room[ny][0] = 0

        # 위 또는 아래 이동
        vertical_move(ny+step, (R-1) * i + step, step, 0)
        # 오른쪽 이동
        horizontal_move(1, C, 1, (R-1) * i)
        # 위 또는 아래 이동
        vertical_move((R-1) * i - step, y - step, -step,  C-1)
        # 왼쪽 이동
        horizontal_move(C-2, 0, -1, y)

        temp_room[y][1] = 0

    # room, dust 갱신
    room.clear()
    for i in range(R):
        room.append(temp_room[i][:])

for _ in range(T):
    change_room_state()

print(total_dust)


# 정리
def dust_amount():
    from sys import stdin
    def to_int():
        return map(int, stdin.readline().split())

    def change_room_state(): # 방의 상태 변경
        nonlocal total_dust, room

        # 먼지 확산
        def defuse_dust():
            for y in range(R):
                for x in range(C):
                    if room[y][x] > 0:
                        cnt = 0
                        amount = room[y][x] // 5
                        for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
                            ny, nx = y + dy, x + dx
                            if 0 <= ny < R and 0 <= nx < C and room[ny][nx] != -1:
                                cnt += 1
                                temp_room[ny][nx] += amount
                        temp_room[y][x] += room[y][x] - amount * cnt

        def vertical_move(start, end, step, col): # 행 이동
            for ni in range(start, end, step):
                if temp_room[ni][col]:
                    temp_room[ni - step][col] = temp_room[ni][col]
                    temp_room[ni][col] = 0

        def horizontal_move(start, end, step, row): # 열 이동
            for j in range(start, end, step):
                if temp_room[row][j]:
                    temp_room[row][j - step] = temp_room[row][j]
                    temp_room[row][j] = 0

        # 임시 값 선언
        temp_room = [[0] * C for _ in range(R)]
        for i in cleaner:
            temp_room[i][0] = -1

        defuse_dust() # 먼지 확산

        # 먼지 제거
        for i in range(2):
            y = cleaner[i]
            step = -1 if i == 0 else 1
            # 공기 청정기로 들어가는 먼지
            ny = y + step
            if temp_room[ny][0]:
                total_dust -= temp_room[ny][0]
                temp_room[ny][0] = 0

            # 위 또는 아래 이동
            vertical_move(ny + step, (R - 1) * i + step, step, 0)
            # 오른쪽 이동
            horizontal_move(1, C, 1, (R - 1) * i)
            # 위 또는 아래 이동
            vertical_move((R - 1) * i - step, y - step, -step, C - 1)
            # 왼쪽 이동
            horizontal_move(C - 2, 0, -1, y)

            temp_room[y][1] = 0

        # room, dust 갱신
        room.clear()
        for i in range(R):
            room.append(temp_room[i][:])

    R, C, T = to_int()
    room = []
    cleaner = []
    total_dust = 0
    for i in range(R):
        room.append(list(to_int()))
        state = room[-1][0]
        if state == -1:
            cleaner.append(i)
        elif state:
            total_dust += state

        for j in range(1, C):
            state = room[-1][j]
            if state:
                total_dust += state

    for _ in range(T):
        change_room_state()

    return total_dust

print(dust_amount())
