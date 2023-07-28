#230728
N = int(input())
egg_list = [list(map(int, input().split())) for _ in range(N)]
if N == 1:
    print(0)
else:
    max_cnt = 0
    visited = [False] * N
    path = []
    def break_egg(level=0):
        global max_cnt
        if level == N:
            cnt = 0
            for j in range(N):
                if egg_list[j][0] <= 0:
                    cnt += 1
            # print(path, egg_list)
            # print(cnt)
            if max_cnt < cnt:
                max_cnt = cnt
            return
        if egg_list[level][0] <= 0:
            break_egg(level + 1)
        else:
            for i in range(N):
                if i != level and egg_list[i][0] > 0:
                    visited[level] = True
                    egg_list[i][0] -= egg_list[level][1]
                    egg_list[level][0] -= egg_list[i][1]
                    path.append(i)
                    break_egg(level+1)
                    path.pop()
                    egg_list[i][0] += egg_list[level][1]
                    egg_list[level][0] += egg_list[i][1]
            if not visited[level]:
                break_egg(level+1)
            else:
                visited[level] = False

    break_egg()
    print(max_cnt)


#
N = int(input())
egg_list = [list(map(int, input().split())) for _ in range(N)]
if N == 1:
    print(0)
else:
    max_cnt = 0
    visited = [False] * N
    def break_egg(level=0, cnt=0):
        global max_cnt
        if level == N:
            if max_cnt < cnt:
                max_cnt = cnt
            return
        if egg_list[level][0] <= 0:
            break_egg(level + 1, cnt)
        else:
            for i in range(N):
                if i != level and egg_list[i][0] > 0:
                    visited[level] = True
                    egg_list[i][0] -= egg_list[level][1]
                    egg_list[level][0] -= egg_list[i][1]
                    new_cnt = cnt
                    if egg_list[i][0] <= 0:
                        new_cnt += 1
                    if egg_list[level][0] <= 0:
                        new_cnt += 1
                    break_egg(level+1, new_cnt)
                    egg_list[i][0] += egg_list[level][1]
                    egg_list[level][0] += egg_list[i][1]
            if not visited[level]:
                break_egg(level+1, cnt)
            else:
                visited[level] = False

    break_egg()
    print(max_cnt)


#
N = int(input())
egg_list = [list(map(int, input().split())) for _ in range(N)]
if N == 1:
    print(0)
else:
    max_cnt = 0
    visited = [False] * N
    def break_egg(level=0):
        global max_cnt
        if level == N:
            cnt = 0
            for j in range(N):
                if egg_list[j][0] <= 0:
                    cnt += 1
            if max_cnt < cnt:
                max_cnt = cnt
            return
        if egg_list[level][0] <= 0:
            break_egg(level + 1)
        else:
            for i in range(N):
                if i != level and egg_list[i][0] > 0:
                    visited[level] = True
                    egg_list[i][0] -= egg_list[level][1]
                    egg_list[level][0] -= egg_list[i][1]
                    break_egg(level+1)
                    egg_list[i][0] += egg_list[level][1]
                    egg_list[level][0] += egg_list[i][1]
            if not visited[level]:
                break_egg(level+1)
            else:
                visited[level] = False

    break_egg()
    print(max_cnt)


#
def cnt_egg():
    N = int(input())
    if N == 1:
        input()
        return 0

    egg_list = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = 0
    visited = [False] * N

    def break_egg(level=0, cnt=0):
        nonlocal max_cnt
        if level == N:
            if max_cnt < cnt:
                max_cnt = cnt
            return
        if egg_list[level][0] <= 0:
            break_egg(level + 1, cnt)
        else:
            for i in range(N):
                if i != level and egg_list[i][0] > 0:
                    visited[level] = True
                    egg_list[i][0] -= egg_list[level][1]
                    egg_list[level][0] -= egg_list[i][1]
                    new_cnt = cnt
                    if egg_list[i][0] <= 0:
                        new_cnt += 1
                    if egg_list[level][0] <= 0:
                        new_cnt += 1
                    break_egg(level+1, new_cnt)
                    egg_list[i][0] += egg_list[level][1]
                    egg_list[level][0] += egg_list[i][1]
            if not visited[level]:
                break_egg(level+1, cnt)
            else:
                visited[level] = False

    break_egg()

    return max_cnt

print(cnt_egg())


#
def cnt_egg():
    N = int(input())
    if N == 1:
        input()
        return 0

    egg_list = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = 0
    visited = [False] * N

    def break_egg(level=0, cnt=0):
        nonlocal max_cnt
        if level == N:
            if max_cnt < cnt:
                max_cnt = cnt
            return
        if egg_list[level][0] <= 0:
            break_egg(level + 1, cnt)
        else:
            for i in range(N):
                if i != level and egg_list[i][0] > 0:
                    visited[level] = True
                    egg_list[i][0] -= egg_list[level][1]
                    egg_list[level][0] -= egg_list[i][1]
                    new_cnt = cnt
                    if egg_list[i][0] <= 0:
                        new_cnt += 1
                    if egg_list[level][0] <= 0:
                        new_cnt += 1
                    break_egg(level+1, new_cnt)
                    egg_list[i][0] += egg_list[level][1]
                    egg_list[level][0] += egg_list[i][1]
            if not visited[level]:
                break_egg(level+1, cnt)
            else:
                visited[level] = False

    break_egg()

    return max_cnt

print(cnt_egg())


#
def cnt_egg():
    N = int(input())
    if N == 1:
        input()
        return 0

    egg_list = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = 0
    visited = [False] * N

    def break_egg(level=0, cnt=0):
        nonlocal max_cnt
        if level == N:
            if max_cnt < cnt:
                max_cnt = cnt
            return
        if egg_list[level][0] <= 0:
            break_egg(level + 1, cnt)
        else:
            for i in range(N):
                if i != level and egg_list[i][0] > 0:
                    visited[level] = True
                    new_cnt = cnt
                    egg_list[i][0] -= egg_list[level][1]
                    egg_list[level][0] -= egg_list[i][1]

                    for j in (i, level):
                        if egg_list[j][0] <= 0:
                            new_cnt += 1

                    break_egg(level+1, new_cnt)
                    egg_list[i][0] += egg_list[level][1]
                    egg_list[level][0] += egg_list[i][1]

            if not visited[level]:
                break_egg(level+1, cnt)
            else:
                visited[level] = False

    break_egg()

    return max_cnt

print(cnt_egg())


#
def cnt_egg(N):
    if N == 1:
        input()
        return 0

    egg_list = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = 0
    visited = [False] * N

    def break_egg(level=0, cnt=0):
        nonlocal max_cnt
        if level == N:
            if max_cnt < cnt:
                max_cnt = cnt
            return
        if egg_list[level][0] <= 0:
            break_egg(level + 1, cnt)
        else:
            for i in range(N):
                if i != level and egg_list[i][0] > 0:
                    visited[level] = True
                    egg_list[i][0] -= egg_list[level][1]
                    egg_list[level][0] -= egg_list[i][1]
                    new_cnt = cnt
                    if egg_list[i][0] <= 0:
                        new_cnt += 1
                    if egg_list[level][0] <= 0:
                        new_cnt += 1
                    break_egg(level+1, new_cnt)
                    egg_list[i][0] += egg_list[level][1]
                    egg_list[level][0] += egg_list[i][1]
            if not visited[level]:
                break_egg(level+1, cnt)
            else:
                visited[level] = False

    break_egg()

    return max_cnt

print(cnt_egg(int(input())))


#
def cnt_egg(N):
    if N == 1:
        return 0

    egg_list = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = 0
    visited = [False] * N

    def break_egg(level=0, cnt=0):
        nonlocal max_cnt
        if level == N:
            if max_cnt < cnt:
                max_cnt = cnt
            return
        if egg_list[level][0] <= 0:
            break_egg(level + 1, cnt)
        else:
            for i in range(N):
                if i != level and egg_list[i][0] > 0:
                    visited[level] = True
                    egg_list[i][0] -= egg_list[level][1]
                    egg_list[level][0] -= egg_list[i][1]
                    new_cnt = cnt
                    if egg_list[i][0] <= 0:
                        new_cnt += 1
                    if egg_list[level][0] <= 0:
                        new_cnt += 1
                    break_egg(level+1, new_cnt)
                    egg_list[i][0] += egg_list[level][1]
                    egg_list[level][0] += egg_list[i][1]
            if not visited[level]:
                break_egg(level+1, cnt)
            else:
                visited[level] = False

    break_egg()

    return max_cnt

print(cnt_egg(int(input())))


#
def cnt_egg():
    N = int(input())
    if N == 1:
        return 0

    egg_list = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = 0
    visited = [False] * N

    def break_egg(level=0, cnt=0):
        nonlocal max_cnt
        if level == N:
            if max_cnt < cnt:
                max_cnt = cnt
            return
        if egg_list[level][0] <= 0:
            break_egg(level + 1, cnt)
        else:
            for i in range(N):
                if i != level and egg_list[i][0] > 0:
                    visited[level] = True
                    egg_list[i][0] -= egg_list[level][1]
                    egg_list[level][0] -= egg_list[i][1]
                    new_cnt = cnt
                    if egg_list[i][0] <= 0:
                        new_cnt += 1
                    if egg_list[level][0] <= 0:
                        new_cnt += 1
                    break_egg(level+1, new_cnt)
                    egg_list[i][0] += egg_list[level][1]
                    egg_list[level][0] += egg_list[i][1]
            if not visited[level]:
                break_egg(level+1, cnt)
            else:
                visited[level] = False

    break_egg()

    return max_cnt

print(cnt_egg())


#
def cnt_egg():
    N = int(input())
    if N == 1:
        return 0

    egg_list = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = 0
    visited = [False] * N
    broken = [False] * N

    def break_egg(level=0, cnt=0):
        nonlocal max_cnt
        if level == N:
            if max_cnt < cnt:
                max_cnt = cnt
            return
        if broken[level]:
            break_egg(level + 1, cnt)
        else:
            for i in range(N):
                if i != level and not broken[i]:
                    visited[level] = True
                    egg_list[i][0] -= egg_list[level][1]
                    egg_list[level][0] -= egg_list[i][1]
                    new_cnt = cnt
                    if egg_list[i][0] <= 0:
                        new_cnt += 1
                        broken[i] = True
                    if egg_list[level][0] <= 0:
                        new_cnt += 1
                        broken[level] = True
                    break_egg(level+1, new_cnt)
                    egg_list[i][0] += egg_list[level][1]
                    egg_list[level][0] += egg_list[i][1]
                    if new_cnt != cnt:
                        broken[i] = False
                        broken[level] = False
            if not visited[level]:
                break_egg(level+1, cnt)
            else:
                visited[level] = False

    break_egg()

    return max_cnt

print(cnt_egg())