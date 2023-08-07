#230807
def calc_probability():
    N, *probability = list(map(int, input().split()))
    if N == 1:
        return 1
    elif (probability[0] == 0 or probability[1] == 0) and (probability[2] == 0 or probability[3] == 0):
        return 1

    def div_100(num):
        return num/100
    direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    case = [0] * 4
    simple = 0
    probability = list(map(div_100, probability))
    result = [{1:probability[i]} for i in range(4)]
    visited = set()
    visited.add((0, 0))

    def calc_simple(base, index, quotient):
        if result[index].get(quotient):
            return result[index][quotient]
        root = calc_simple(base, index, quotient//2)
        if quotient % 2:
            result[index][quotient-1] = root * root
            result[index][quotient] = result[index][quotient-1] * base
        else:
            result[index][quotient] = root * root
        return result[index][quotient]


    def add_cases(level=0, y=0, x=0):
        nonlocal simple
        if level == N:
            each = 1
            for i in range(4):
                if probability[i] and case[i]:
                    each *= calc_simple(probability[i], i, case[i])
            simple += each
            return

        for i in range(4):
            if probability[i] != 0:
                ny, nx = y+direct[i][0], x+direct[i][1]
                if (ny, nx) not in visited:
                    visited.add((ny, nx))
                    case[i] += 1
                    add_cases(level+1, ny, nx)
                    case[i] -= 1
                    visited.remove((ny, nx))

    add_cases()

    return simple

print(calc_probability())



#
def calc_probability():
    N, *probability = list(map(int, input().split()))
    if N == 1:
        return 1
    elif (probability[0] == 0 or probability[1] == 0) and (probability[2] == 0 or probability[3] == 0):
        return 1

    direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    case = [0] * 4
    result = []
    simple = 0
    for i in range(4):
        probability[i] /= 100
        result.append({1:probability[i]})
    visited = set()
    visited.add((0, 0))

    def calc_simple(base, index, quotient):
        if result[index].get(quotient):
            return result[index][quotient]
        root = calc_simple(base, index, quotient//2)
        if quotient % 2:
            result[index][quotient-1] = root * root
            result[index][quotient] = result[index][quotient-1] * base
        else:
            result[index][quotient] = root * root
        return result[index][quotient]


    def add_cases(level=0, y=0, x=0):
        nonlocal simple
        if level == N:
            each = 1
            for i in range(4):
                if probability[i] and case[i]:
                    each *= calc_simple(probability[i], i, case[i])
            simple += each
            return

        for i in range(4):
            if probability[i] != 0:
                ny, nx = y+direct[i][0], x+direct[i][1]
                if (ny, nx) not in visited:
                    visited.add((ny, nx))
                    case[i] += 1
                    add_cases(level+1, ny, nx)
                    case[i] -= 1
                    visited.remove((ny, nx))

    add_cases()

    return simple

print(calc_probability())


#
def calc_probability():
    N, *probability = list(map(int, input().split()))
    if N == 1:
        return 1
    elif (probability[0] == 0 or probability[1] == 0) and (probability[2] == 0 or probability[3] == 0):
        return 1

    def div_100(num):
        return num/100
    direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    case = [0] * 4
    simple = 0
    probability = list(map(div_100, probability))
    result = [{1:probability[i]} for i in range(4)]
    visited = set()
    visited.add((0, 0))

    def calc_simple(base, index, quotient):
        if result[index].get(quotient):
            return result[index][quotient]
        root = calc_simple(base, index, quotient//2)
        result[index][quotient] = root * root * base if quotient % 2 else root * root
        return result[index][quotient]


    def add_cases(level=0, y=0, x=0):
        nonlocal simple
        if level == N:
            each = 1
            for i in range(4):
                if probability[i] and case[i]:
                    each *= calc_simple(probability[i], i, case[i])
            simple += each
            return

        for i in range(4):
            if probability[i] != 0:
                ny, nx = y+direct[i][0], x+direct[i][1]
                if (ny, nx) not in visited:
                    visited.add((ny, nx))
                    case[i] += 1
                    add_cases(level+1, ny, nx)
                    case[i] -= 1
                    visited.remove((ny, nx))

    add_cases()

    return simple

print(calc_probability())


#
def calc_probability():
    N, *probability = list(map(int, input().split()))
    if N == 1:
        return 1
    elif (probability[0] == 0 or probability[1] == 0) and (probability[2] == 0 or probability[3] == 0):
        return 1

    def div_100(num):
        return num/100
    direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    simple = 0
    probability = list(map(div_100, probability))
    visited = [[False] * (2*N+1) for _ in range(2*N+1)]
    visited[N][N] = True

    def add_cases(level=0, y=N, x=N, each=1):
        nonlocal simple
        if level == N:
            simple += each
            return

        for i in range(4):
            if probability[i] != 0:
                ny, nx = y+direct[i][0], x+direct[i][1]
                if 0 <= ny < 2*N+1 and 0 <= nx < 2*N+1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    add_cases(level+1, ny, nx, each*probability[i])
                    visited[ny][nx] = False

    add_cases()

    return simple

print(calc_probability())


#
def calc_probability():
    N, *probability = list(map(int, input().split()))
    def div_100(num):
        return num/100
    direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    simple = 0
    probability = list(map(div_100, probability))
    visited = [[False] * (2*N+1) for _ in range(2*N+1)]
    visited[N][N] = True

    def add_cases(level=0, y=N, x=N, each=1):
        nonlocal simple
        if level == N:
            simple += each
            return

        for i in range(4):
            if probability[i] != 0:
                ny, nx = y+direct[i][0], x+direct[i][1]
                if 0 <= ny < 2*N+1 and 0 <= nx < 2*N+1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    add_cases(level+1, ny, nx, each*probability[i])
                    visited[ny][nx] = False

    add_cases()

    return simple

print(calc_probability())