# 250320
# 33432 KB / 72 ms
def main():
    def determine(student, y, x):
        class_room[y][x] = student
        for idx in range(4):
            ny, nx = y + dy[idx], x + dx[idx]
            if 0 <= ny < N and 0 <= nx < N:
                around[ny][nx].add(student)

    def step1(favorite):
        # 좋아하는 학생이 가장 많이 인접한 칸 찾기
        max_num = 0
        candidate = []
        for i in range(N):
            for j in range(N):
                if class_room[i][j] == 0:
                    # print(i, j, around[i][j], favorite, around[i][j] & favorite)
                    num = len(around[i][j] & favorite)
                    if max_num == num:
                        candidate.append((i, j))
                    elif max_num < num:
                        max_num = num
                        candidate = [(i, j)]

        if len(candidate) == 1:
            return candidate[0]

        return step2(candidate)

    def step2(before):
        # 인접한 칸 중 비어있는 칸 찾기
        max_num = 0
        after = []
        for y, x in before:
            empty_num = 0
            empty_num += 1 if y == 0 or y == N-1 else 2
            empty_num += 1 if x == 0 or x == N-1 else 2
            empty_num -= len(around[y][x])
            if empty_num == max_num:
                after.append((y, x))
            elif empty_num > max_num:
                max_num = empty_num
                after = [(y, x)]


        # 행의 번호가 작은 칸 -> 열의 번호가 가장 작은 칸
        return after[0]


    # 입력
    N = int(input())
    M = N*N
    order = []
    student_info = {}
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    for _ in range(M):
        student, *favorite = map(int, input().split())
        order.append(student)
        student_info[student] = set(favorite)


    # 각 자리별 앉은 학생 번호
    class_room = [[0] * N for _ in range(N)]
    # 인접한 칸에 앉은 학생 번호
    around = [[set() for _ in range(N)] for _ in range(N)]
    # 학생 배치
    for student in order:
        y, x = step1(set(student_info[student]))
        determine(student, y, x)

    # 만족도 합 구하기
    total = 0
    for i in range(N):
        for j in range(N):
            value = len(student_info[class_room[i][j]] & around[i][j])
            total += int(10 ** (value-1))


    return total

print(main())




# 33564 KB / 72 ms
def main():
    def determine(student, y, x):
        class_room[y][x] = student
        for idx in range(4):
            ny, nx = y + dy[idx], x + dx[idx]
            if 0 <= ny < N and 0 <= nx < N:
                around[ny][nx].add(student)

    def step1(favorite):
        max_num = 0
        candidate = []
        for i in range(N):
            for j in range(N):
                if class_room[i][j] == 0:
                    num = len(around[i][j] & favorite)
                    if max_num == num:
                        candidate.append((i, j))
                    elif max_num < num:
                        max_num = num
                        candidate = [(i, j)]

        if len(candidate) == 1:
            return candidate[0]

        return step2(candidate)

    def step2(before):
        max_num = 0
        after = []
        for y, x in before:
            empty_num = 0
            empty_num += 1 if y == 0 or y == N-1 else 2
            empty_num += 1 if x == 0 or x == N-1 else 2
            empty_num -= len(around[y][x])
            if empty_num == max_num:
                after.append((y, x))
            elif empty_num > max_num:
                max_num = empty_num
                after = [(y, x)]

        return after[0]



    N = int(input())
    M = N*N
    order = []
    student_info = {}
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    for _ in range(M):
        student, *favorite = map(int, input().split())
        order.append(student)
        student_info[student] = set(favorite)


    class_room = [[0] * N for _ in range(N)]
    around = [[set() for _ in range(N)] for _ in range(N)]
    for student in order:
        y, x = step1(set(student_info[student]))
        determine(student, y, x)

    total = 0
    for i in range(N):
        for j in range(N):
            value = len(student_info[class_room[i][j]] & around[i][j])
            total += int(10 ** (value-1))


    return total

print(main())




# 33432 KB / 64 ms
def main():
    from sys import stdin

    def determine(student, y, x):
        class_room[y][x] = student
        for idx in range(4):
            ny, nx = y + dy[idx], x + dx[idx]
            if 0 <= ny < N and 0 <= nx < N:
                around[ny][nx].add(student)

    def step1(favorite):
        max_num = 0
        candidate = []
        for i in range(N):
            for j in range(N):
                if class_room[i][j] == 0:
                    num = len(around[i][j] & favorite)
                    if max_num == num:
                        candidate.append((i, j))
                    elif max_num < num:
                        max_num = num
                        candidate = [(i, j)]

        if len(candidate) == 1:
            return candidate[0]

        return step2(candidate)

    def step2(before):
        max_num = 0
        after = []
        for y, x in before:
            empty_num = 0
            empty_num += 1 if y == 0 or y == N-1 else 2
            empty_num += 1 if x == 0 or x == N-1 else 2
            empty_num -= len(around[y][x])
            if empty_num == max_num:
                after.append((y, x))
            elif empty_num > max_num:
                max_num = empty_num
                after = [(y, x)]

        return after[0]



    new_input = stdin.readline
    N = int(new_input())
    M = N*N
    order = []
    student_info = {}
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    for _ in range(M):
        student, *favorite = map(int, new_input().split())
        order.append(student)
        student_info[student] = set(favorite)


    class_room = [[0] * N for _ in range(N)]
    around = [[set() for _ in range(N)] for _ in range(N)]
    for student in order:
        y, x = step1(set(student_info[student]))
        determine(student, y, x)

    total = 0
    for i in range(N):
        for j in range(N):
            value = len(student_info[class_room[i][j]] & around[i][j])
            total += int(10 ** (value-1))


    return total

print(main())



# 33432 KB / 68 ms
def main():
    from sys import stdin

    def determine(student, y, x):
        class_room[y][x] = student
        for idx in range(4):
            ny, nx = y + dy[idx], x + dx[idx]
            if 0 <= ny < N and 0 <= nx < N:
                around[ny][nx].add(student)

    def step1(favorite):
        max_num = 0
        candidate = []
        for i in range(N):
            for j in range(N):
                if class_room[i][j] == 0:
                    num = len(around[i][j] & favorite)
                    if max_num == num:
                        candidate.append((i, j))
                    elif max_num < num:
                        max_num = num
                        candidate = [(i, j)]

        if len(candidate) == 1:
            return candidate[0]

        return step2(candidate)

    def step2(before):
        max_num = 0
        after = []
        for y, x in before:
            empty_num = 0
            empty_num += 1 if y == 0 or y == N-1 else 2
            empty_num += 1 if x == 0 or x == N-1 else 2
            empty_num -= len(around[y][x])
            if empty_num == max_num:
                after.append((y, x))
            elif empty_num > max_num:
                max_num = empty_num
                after = [(y, x)]

        return after[0]



    new_input = stdin.readline
    N = int(new_input())
    M = N*N
    order = []
    student_info = {}
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    for _ in range(M):
        student, *favorite = map(int, new_input().split())
        order.append(student)
        student_info[student] = set(favorite)


    class_room = [[0] * N for _ in range(N)]
    around = [[set() for _ in range(N)] for _ in range(N)]
    for student in order:
        y, x = step1(set(student_info[student]))
        determine(student, y, x)

    total = 0
    for i in range(N):
        for j in range(N):
            value = len(student_info[class_room[i][j]] & around[i][j])
            total += 10 ** (value-1) if value > 1 else value


    return total

print(main())