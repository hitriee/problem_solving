#230510
# 자료구조
p, m = map(int, input().split())
rooms = []
length = []
cnt = 0
for _ in range(p):
    level, name = input().split()
    level = int(level)
    if cnt:
        for i in range(cnt):
            standard = rooms[i][0][0]
            if length[i] == m:
                continue
            elif standard - 10 <= level <= standard + 10:
                rooms[i].append((level, name))
                length[i] += 1
                break
        else:
            rooms.append([(level, name)])
            length.append(1)
            cnt += 1
    else:
        rooms.append([(level, name)])
        length.append(1)
        cnt += 1

for i in range(cnt):
    if length[i] == m:
        print('Started!')
    else:
        print('Waiting!')
    rooms[i].sort(key=lambda info: info[1])
    for info in rooms[i]:
        print(*info)


# standard
p, m = map(int, input().split())
rooms = []
length = []
standard = []
cnt = 0
for _ in range(p):
    level, name = input().split()
    level = int(level)
    for i in range(cnt):
        if length[i] == m:
            continue
        elif standard[i][0] <= level <= standard[i][1]:
            rooms[i].append((level, name))
            length[i] += 1
            break
    else:
        rooms.append([(level, name)])
        standard.append((level-10, level+10))
        length.append(1)
        cnt += 1

for i in range(cnt):
    if length[i] == m:
        print('Started!')
    else:
        print('Waiting!')
    rooms[i].sort(key=lambda info: info[1])
    for info in rooms[i]:
        print(*info)


#
def fill_list():
    global cnt
    for _ in range(p):
        level, name = input().split()
        level = int(level)
        for i in range(cnt):
            if length[i] == m:
                continue
            elif standard[i][0] <= level <= standard[i][1]:
                rooms[i].append((level, name))
                length[i] += 1
                break
        else:
            rooms.append([(level, name)])
            standard.append((level-10, level+10))
            length.append(1)
            cnt += 1

p, m = map(int, input().split())
rooms = []
length = []
standard = []
cnt = 0
fill_list()
for i in range(cnt):
    if length[i] == m:
        print('Started!')
    else:
        print('Waiting!')
    rooms[i].sort(key=lambda info: info[1])
    for info in rooms[i]:
        print(*info)


#
def fill_list():
    global cnt
    for _ in range(p):
        level, name = input().split()
        level = int(level)
        for i in range(cnt):
            if length[i] == m:
                continue
            elif standard[i][0] <= level <= standard[i][1]:
                rooms[i].append((level, name))
                length[i] += 1
                break
        else:
            rooms.append([(level, name)])
            standard.append((level-10, level+10))
            length.append(1)
            cnt += 1

p, m = map(int, input().split())
rooms, length, standard = [], [], []
cnt = 0
fill_list()
for i in range(cnt):
    if length[i] == m:
        print('Started!')
    else:
        print('Waiting!')
    rooms[i].sort(key=lambda info: info[1])
    for info in rooms[i]:
        print(*info)

#
def fill_list():
    global cnt
    standard = []
    for _ in range(p):
        level, name = new_input().split()
        level = int(level)
        for i in range(cnt):
            if length[i] == m:
                continue
            elif standard[i][0] <= level <= standard[i][1]:
                rooms[i].append((level, name))
                length[i] += 1
                break
        else:
            rooms.append([(level, name)])
            standard.append((level-10, level+10))
            length.append(1)
            cnt += 1

from sys import stdin
new_input = stdin.readline
p, m = map(int, new_input().split())
rooms, length = [], []
cnt = 0
fill_list()
for i in range(cnt):
    if length[i] == m:
        print('Started!')
    else:
        print('Waiting!')
    rooms[i].sort(key=lambda info: info[1])
    for info in rooms[i]:
        print(*info)


#
def fill_list():
    cnt = 0
    standard = []
    for _ in range(p):
        level, name = new_input().split()
        level = int(level)
        for i in range(cnt):
            if length[i] == m:
                continue
            elif standard[i][0] <= level <= standard[i][1]:
                rooms[i].append((level, name))
                length[i] += 1
                break
        else:
            rooms.append([(level, name)])
            standard.append((level-10, level+10))
            length.append(1)
            cnt += 1
    return cnt

from sys import stdin
new_input = stdin.readline
p, m = map(int, new_input().split())
rooms, length = [], []
cnt = fill_list()
for i in range(cnt):
    if length[i] == m:
        print('Started!')
    else:
        print('Waiting!')
    rooms[i].sort(key=lambda info: info[1])
    for info in rooms[i]:
        print(*info)


#
def print_info():
    from sys import stdin
    new_input = stdin.readline
    p, m = map(int, new_input().split())
    rooms, length = [], []
    cnt = 0

    def fill_list():
        nonlocal cnt
        standard = []
        for _ in range(p):
            level, name = new_input().split()
            level = int(level)
            for i in range(cnt):
                if length[i] == m:
                    continue
                elif standard[i][0] <= level <= standard[i][1]:
                    rooms[i].append((level, name))
                    length[i] += 1
                    break
            else:
                rooms.append([(level, name)])
                standard.append((level-10, level+10))
                length.append(1)
                cnt += 1

    fill_list()
    for i in range(cnt):
        if length[i] == m:
            print('Started!')
        else:
            print('Waiting!')
        rooms[i].sort(key=lambda info: info[1])
        for info in rooms[i]:
            print(*info)
print_info()