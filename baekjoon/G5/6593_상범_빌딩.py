#230603
from collections import deque
while True:
    L, R, C = map(int, input().split())
    if L == 0:
        break
    building = []
    start = deque()
    final_floor = final_y = final_x = -1

    for floor in range(L):
        stair = []
        for i in range(R):
            row = list(map(str, input()))
            if not start or final_floor == -1:
                for j in range(C):
                    if not start and row[j] == 'S':
                        start.append((floor, i, j, 0))
                        row[j] = '#'
                        if final_floor:
                            break
                    elif final_floor == -1 and row[j] == 'E':
                        final_floor, final_y, final_x = floor, i, j
                        row[j] = '.'
                        if start:
                            break
            stair.append(row)
        building.append(stair)
        input()
    while start:
        floor, y, x, time = start.popleft()
        if floor == final_floor and y == final_y and x == final_x:
            print(f'Escaped in {time} minute(s).')
            break
        time += 1
        for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
            ny, nx = y+dy, x+dx
            if 0 <= ny < R and 0 <= nx < C and building[floor][ny][nx] == '.':
                start.append((floor, ny, nx, time))
                building[floor][ny][nx] = '#'

        for new_floor in (floor+1, floor-1):
            if 0 <= new_floor < L and building[new_floor][y][x] == '.':
                start.append((new_floor, y, x, time))
                building[new_floor][y][x] = '#'

    else:
        print('Trapped!')


#
from collections import deque
from sys import stdin
new_input = stdin.readline
while True:
    L, R, C = map(int, new_input().split())
    if L == 0:
        break
    building = []
    start = deque()
    final_floor = final_y = final_x = -1

    for floor in range(L):
        stair = []
        for i in range(R):
            row = list(map(str, new_input().rstrip()))
            if not start or final_floor == -1:
                for j in range(C):
                    if not start and row[j] == 'S':
                        start.append((floor, i, j, 0))
                        row[j] = '#'
                        if final_floor:
                            break
                    elif final_floor == -1 and row[j] == 'E':
                        final_floor, final_y, final_x = floor, i, j
                        row[j] = '.'
                        if start:
                            break
            stair.append(row)
        building.append(stair)
        new_input()

    while start:
        floor, y, x, time = start.popleft()
        if floor == final_floor and y == final_y and x == final_x:
            print(f'Escaped in {time} minute(s).')
            break
        time += 1
        for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
            ny, nx = y+dy, x+dx
            if 0 <= ny < R and 0 <= nx < C and building[floor][ny][nx] == '.':
                start.append((floor, ny, nx, time))
                building[floor][ny][nx] = '#'

        for new_floor in (floor+1, floor-1):
            if 0 <= new_floor < L and building[new_floor][y][x] == '.':
                start.append((new_floor, y, x, time))
                building[new_floor][y][x] = '#'

    else:
        print('Trapped!')


#
from collections import deque
from sys import stdin
new_input = stdin.readline
building = []
start = deque()
stair = []

while True:
    L, R, C = map(int, new_input().split())
    if L == 0:
        break

    final_floor = final_y = final_x = -1

    for floor in range(L):
        for i in range(R):
            row = list(map(str, new_input().rstrip()))
            if not start or final_floor == -1:
                for j in range(C):
                    if not start and row[j] == 'S':
                        start.append((floor, i, j, 0))
                        row[j] = '#'
                        if final_floor:
                            break
                    elif final_floor == -1 and row[j] == 'E':
                        final_floor, final_y, final_x = floor, i, j
                        row[j] = '.'
                        if start:
                            break
            stair.append(row)
        building.append(stair[:])
        stair.clear()
        new_input()

    while start:
        floor, y, x, time = start.popleft()
        if floor == final_floor and y == final_y and x == final_x:
            print(f'Escaped in {time} minute(s).')
            start.clear()
            break
        time += 1
        for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
            ny, nx = y+dy, x+dx
            if 0 <= ny < R and 0 <= nx < C and building[floor][ny][nx] == '.':
                start.append((floor, ny, nx, time))
                building[floor][ny][nx] = '#'

        for new_floor in (floor+1, floor-1):
            if 0 <= new_floor < L and building[new_floor][y][x] == '.':
                start.append((new_floor, y, x, time))
                building[new_floor][y][x] = '#'

    else:
        print('Trapped!')

    building.clear()


#
def print_can_exit():
    from collections import deque
    from sys import stdin
    new_input = stdin.readline
    building = []
    start = deque()
    stair = []

    while True:
        L, R, C = map(int, new_input().split())
        if L == 0:
            break

        final_floor = final_y = final_x = -1

        for floor in range(L):
            for i in range(R):
                row = list(map(str, new_input().rstrip()))
                if not start or final_floor == -1:
                    for j in range(C):
                        if row[j] == 'S':
                            start.append((floor, i, j, 0))
                            row[j] = '#'
                            if final_floor:
                                break
                        elif row[j] == 'E':
                            final_floor, final_y, final_x = floor, i, j
                            row[j] = '.'
                            if start:
                                break
                stair.append(row)
            building.append(stair[:])
            stair.clear()
            new_input()

        while start:
            floor, y, x, time = start.popleft()
            if floor == final_floor and y == final_y and x == final_x:
                print(f'Escaped in {time} minute(s).')
                start.clear()
                break
            time += 1
            for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
                ny, nx = y + dy, x + dx
                if 0 <= ny < R and 0 <= nx < C and building[floor][ny][nx] == '.':
                    start.append((floor, ny, nx, time))
                    building[floor][ny][nx] = '#'

            for new_floor in (floor + 1, floor - 1):
                if 0 <= new_floor < L and building[new_floor][y][x] == '.':
                    start.append((new_floor, y, x, time))
                    building[new_floor][y][x] = '#'

        else:
            print('Trapped!')

        building.clear()

print_can_exit()