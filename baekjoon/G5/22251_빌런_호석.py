#230519
# dfs, 백트래킹
# 결과의 최댓값, 최대 자릿수, 바꿀 수 있는 LED 제한, 현재 층 수
target_limit, display_cnt, change_limit, now = input().split()
not_in_num = [
    {1}, {1, 2, 3, 5, 6}, {2, 7}, {2, 5}, {3, 5, 6}, {4, 5}, {4}, {1, 2, 5, 6}, set(), {5}
]
display_cnt = len(target_limit)
change_limit = int(change_limit)
target_limit = int(target_limit)

num_to_other = [[0] * 10 for _ in range(10)]
for i in range(9):
    for j in range(i+1, 10):
        length = len(not_in_num[i].symmetric_difference(not_in_num[j]))
        num_to_other[i][j] = length
        num_to_other[j][i] = length

now = str(now).rjust(display_cnt, '0')
cnt = 0
def find_cases(level, change, result):
    global cnt
    if level == display_cnt:
        if change and 1 <= int(result) <= target_limit:
            cnt += 1
        return
    num = int(now[level])
    for i in range(10):
        if num == i:
            find_cases(level+1, change, result + str(i))
        elif change + num_to_other[num][i] <= change_limit:
            find_cases(level+1, change + num_to_other[num][i], result + str(i))

find_cases(0, 0, '')
print(cnt)


#
# 결과의 최댓값, 최대 자릿수, 바꿀 수 있는 LED 제한, 현재 층 수
input_values = input().split()
display_cnt = len(input_values[0])
change_limit = int(input_values[2])
target_limit = int(input_values[0])
not_in_num = [
    {1}, {1, 2, 3, 5, 6}, {2, 7}, {2, 5}, {3, 5, 6}, {4, 5}, {4}, {1, 2, 5, 6}, set(), {5}
]

num_to_other = [[0] * 10 for _ in range(10)]
for i in range(9):
    for j in range(i+1, 10):
        length = len(not_in_num[i].symmetric_difference(not_in_num[j]))
        num_to_other[i][j] = length
        num_to_other[j][i] = length

now = input_values[3].rjust(display_cnt, '0')
cnt = 0

def find_cases(level, change, result):
    global cnt
    if level == display_cnt:
        if change and 1 <= int(result) <= target_limit:
            cnt += 1
        return
    num = int(now[level])
    for i in range(10):
        new_change, new_result = change + num_to_other[num][i], result + str(i)
        if new_change <= change_limit:
            find_cases(level+1, new_change, new_result)

find_cases(0, 0, '')
print(cnt)


#
def find_cnt():
    def find_cases(level, change, result):
        nonlocal cnt
        if level == display_cnt:
            if change and 1 <= int(result) <= target_limit:
                cnt += 1
            return
        num = int(now[level])
        for i in range(10):
            new_change, new_result = change + num_to_other[num][i], result + str(i)
            if new_change <= change_limit:
                find_cases(level+1, new_change, new_result)

    input_values = input().split()
    display_cnt = len(input_values[0])
    change_limit = int(input_values[2])
    target_limit = int(input_values[0])
    not_in_num = [
        {1}, {1, 2, 3, 5, 6}, {2, 7}, {2, 5}, {3, 5, 6}, {4, 5}, {4}, {1, 2, 5, 6}, set(), {5}
    ]

    num_to_other = [[0] * 10 for _ in range(10)]
    for i in range(9):
        for j in range(i+1, 10):
            length = len(not_in_num[i].symmetric_difference(not_in_num[j]))
            num_to_other[i][j] = length
            num_to_other[j][i] = length

    now = input_values[3].rjust(display_cnt, '0')
    cnt = 0

    find_cases(0, 0, '')
    return cnt
print(find_cnt())


#
def find_cnt():
    def find_cases(level, change, result):
        nonlocal cnt
        if level == display_cnt:
            if change and result != '0'* display_cnt and result <= target_limit:
                cnt += 1
            return
        num = int(now[level])
        for i in range(10):
            new_change, new_result = change + num_to_other[num][i], result + str(i)
            if new_change <= change_limit:
                find_cases(level+1, new_change, new_result)

    input_values = input().split()
    target_limit = input_values[0]
    display_cnt = len(target_limit)
    change_limit = int(input_values[2])
    not_in_num = [
        {1}, {1, 2, 3, 5, 6}, {2, 7}, {2, 5}, {3, 5, 6}, {4, 5}, {4}, {1, 2, 5, 6}, set(), {5}
    ]

    num_to_other = [[0] * 10 for _ in range(10)]
    for i in range(9):
        for j in range(i+1, 10):
            length = len(not_in_num[i].symmetric_difference(not_in_num[j]))
            num_to_other[i][j] = length
            num_to_other[j][i] = length

    now = input_values[3].rjust(display_cnt, '0')
    cnt = 0

    find_cases(0, 0, '')
    return cnt
print(find_cnt())


#
def find_cnt():
    def find_cases(level, change, result):
        nonlocal cnt
        if level == display_cnt:
            if change and result != zero and result <= target_limit:
                cnt += 1
            return
        num = int(now[level])
        for i in range(10):
            new_change, new_result = change + num_to_other[num][i], result + str(i)
            if new_change <= change_limit:
                find_cases(level+1, new_change, new_result)

    target_limit, display_cnt, change_limit, now = input().split()
    display_cnt = len(target_limit)
    change_limit = int(change_limit)
    now = now.rjust(display_cnt, '0')

    not_in_num = [
        {1}, {1, 2, 3, 5, 6}, {2, 7}, {2, 5}, {3, 5, 6}, {4, 5}, {4}, {1, 2, 5, 6}, set(), {5}
    ]

    num_to_other = [[0] * 10 for _ in range(10)]
    for i in range(9):
        for j in range(i+1, 10):
            length = len(not_in_num[i].symmetric_difference(not_in_num[j]))
            num_to_other[i][j] = length
            num_to_other[j][i] = length

    cnt = 0
    zero = '0' * display_cnt
    find_cases(0, 0, '')
    return cnt
print(find_cnt())


#
def find_cnt():

    def find_cases(level, change, result):
        nonlocal cnt
        if level == display_cnt:
            if change and result != zero and result <= target_limit:
                cnt += 1
            return

        num = int_now[level]
        for i in range(10):
            new_change, new_result = change + num_to_other[num][i], result + str(i)
            if new_change <= change_limit:
                find_cases(level+1, new_change, new_result)

    target_limit, display_cnt, change_limit, now = input().split()
    display_cnt = len(target_limit)
    change_limit = int(change_limit)
    now = now.rjust(display_cnt, '0')

    not_in_num = [
        {1}, {1, 2, 3, 5, 6}, {2, 7}, {2, 5}, {3, 5, 6}, {4, 5}, {4}, {1, 2, 5, 6}, set(), {5}
    ]

    num_to_other = [[0] * 10 for _ in range(10)]
    for i in range(9):
        for j in range(i+1, 10):
            length = len(not_in_num[i].symmetric_difference(not_in_num[j]))
            num_to_other[i][j] = length
            num_to_other[j][i] = length

    cnt = 0
    zero = '0' * display_cnt
    int_now = list(map(int, now))
    find_cases(0, 0, '')

    return cnt

print(find_cnt())

#
def find_cnt():

    def find_cases(level, change):
        nonlocal cnt
        if level == display_cnt:
            result = ''.join(path)
            if change and result != zero and result <= target_limit:
                cnt += 1
            return

        num = int_now[level]
        for i in range(10):
            new_change = change + num_to_other[num][i]
            if new_change <= change_limit:
                path.append(str(i))
                find_cases(level+1, new_change)
                path.pop()

    target_limit, display_cnt, change_limit, now = input().split()
    display_cnt = len(target_limit)
    change_limit = int(change_limit)
    now = now.rjust(display_cnt, '0')

    not_in_num = [
        {1}, {1, 2, 3, 5, 6}, {2, 7}, {2, 5}, {3, 5, 6}, {4, 5}, {4}, {1, 2, 5, 6}, set(), {5}
    ]

    num_to_other = [[0] * 10 for _ in range(10)]
    for i in range(9):
        for j in range(i+1, 10):
            length = len(not_in_num[i].symmetric_difference(not_in_num[j]))
            num_to_other[i][j] = length
            num_to_other[j][i] = length

    cnt = 0
    zero = '0' * display_cnt
    int_now = list(map(int, now))
    path = []
    find_cases(0, 0)
    return cnt

print(find_cnt())