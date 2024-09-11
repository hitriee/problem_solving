# 240909
# 31120 KB / 48 ms
results = []

def is_possible(level, enemy):
    global result
    if result == '1':
        return

    if level == 5:
        for j in range(3):
            if check_table[level].count(j) != candidate[level*3+j]:
                return

        result = '1'
        return

    if enemy < 6:
        for j in range(3):
            check_table[level][enemy], check_table[enemy][level] = j, 2-j
            is_possible(level, enemy+1)
    else:
        for j in range(3):
            if check_table[level].count(j) != candidate[level*3+j]:
                break
        else:
            is_possible(level + 1, level+2)

for _ in range(4):
    check_table = [[-1] * 6 for i in range(6)]
    candidate = list(map(int, input().split()))
    result = '0'

    for i in range(6):
        if sum(candidate[3*i:3*i+3]) != 5:
            results.append(result)
            break
    else:
        is_possible(0, 1)
        results.append(result)


print(' '.join(results))


# 31120 KB / 56 ms
results = []

def is_possible(level, enemy):
    global result
    if result == '1':
        return

    if level == 5:
        for j in range(3):
            if check_table[level].count(j) != candidate[level*3+j]:
                return

        result = '1'
        return

    if enemy < 6:
        for j in range(3):
            check_table[level][enemy], check_table[enemy][level] = j, 2-j
            is_possible(level, enemy+1)
    else:
        for j in range(3):
            if check_table[level].count(j) != candidate[level*3+j]:
                break
        else:
            is_possible(level + 1, level+2)

for _ in range(4):
    check_table = [[-1] * 6 for i in range(6)]
    candidate = list(map(int, input().split()))
    result = '0'
    is_possible(0, 1)
    results.append(result)


print(' '.join(results))



# 31120 KB / 48 ms
def is_possible(level, enemy):
    global result
    if result == '1':
        return

    if level == 5:
        for j in range(2):
            if check_table[level].count(j) != candidate[level*3+j]:
                return

        result = '1'
        return

    if enemy < 6:
        for j in range(3):
            check_table[level][enemy], check_table[enemy][level] = j, 2-j
            is_possible(level, enemy+1)
    else:
        for j in range(2):
            if check_table[level].count(j) != candidate[level*3+j]:
                break
        else:
            is_possible(level + 1, level+2)


results = []

for _ in range(4):
    check_table = [[-1] * 6 for i in range(6)]
    candidate = list(map(int, input().split()))
    result = '0'

    for i in range(6):
        if sum(candidate[3 * i:3 * i + 3]) != 5:
            results.append(result)
            break
    else:
        is_possible(0, 1)
        results.append(result)


print(' '.join(results))
