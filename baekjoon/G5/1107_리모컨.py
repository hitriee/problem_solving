# 230818
def find_min_cnt():
    N = input()
    int_N = int(N)
    length, dif = len(N), abs(int_N - 100)
    if dif <= length: # 숫자 키 누르는 것보다 +, - 버튼 누르는 게 더 적은 경우
        return dif

    M = int(input())
    if M == 0: # 고장난 버튼이 없을 경우
        return length
    if M == 10: # 숫자 버튼이 모두 고장 난 경우
        return dif

    broken_buttons = set(input().split())
    for num in N:
        if num in broken_buttons:
            break
    else:
        return length

    min_dif = abs(int_N - 100)
    if '0' not in broken_buttons and min_dif > int_N + 1:
        min_dif = int_N + 1
    limit = max(length+2, 7) if int_N > 100 else 3
    start_num, next_start_num = 1, 10
    for i in range(1, limit):
        num = start_num
        while num < next_start_num:
            str_num = str(num)
            for j in range(i):
                if str_num[j] in broken_buttons:
                    break
            else:
                dif = i + abs(int_N - num)
                if dif < min_dif:
                    min_dif = dif
            num += 1

        start_num *= 10
        next_start_num *= 10

    return min_dif

print(find_min_cnt())


#
def find_min_cnt():
    N = input()
    int_N = int(N)
    length, dif = len(N), abs(int_N - 100)
    if dif <= length: # 숫자 키 누르는 것보다 +, - 버튼 누르는 게 더 적은 경우
        return dif

    M = int(input())
    if M == 0: # 고장난 버튼이 없을 경우
        return length
    if M == 10: # 숫자 버튼이 모두 고장 난 경우
        return dif

    broken_buttons = set(input().split())
    for num in N:
        if num in broken_buttons:
            break
    else:
        return length

    min_dif = abs(int_N - 100)
    if '0' not in broken_buttons and min_dif > int_N + 1:
        min_dif = int_N + 1
    limit = max(length+2, 7) if int_N > 100 else 3
    start_num, next_start_num = 1, 10
    for i in range(1, limit):
        num = start_num
        while num < next_start_num:
            dif = abs(int_N - num) + i
            str_num = str(num)
            if dif < min_dif:
                for j in range(i):
                    if str_num[j] in broken_buttons:
                        break
                else:
                    min_dif = dif
            num += 1

        start_num *= 10
        next_start_num *= 10

    return min_dif

print(find_min_cnt())



def find_min_cnt():
    N = input()
    int_N = int(N)
    length, dif = len(N), abs(int_N - 100)
    if dif <= length: # 숫자 키 누르는 것보다 +, - 버튼 누르는 게 더 적은 경우
        return dif

    M = int(input())
    if M == 0: # 고장난 버튼이 없을 경우
        return length
    if M == 10: # 숫자 버튼이 모두 고장 난 경우
        return dif

    broken_buttons = set(input().split())
    for num in N:
        if num in broken_buttons:
            break
    else:
        return length

    min_dif = abs(int_N - 100)
    if '0' not in broken_buttons and min_dif > int_N + 1:
        min_dif = int_N + 1

    left, right = int_N-1, int_N+1
    dif = 1
    limit = 5e5
    def can_visit(num):
        str_num = str(num)
        for j in range(len(str_num)):
            if str_num[j] in broken_buttons:
                return False
        return True

    while dif < min_dif - length + 1:
        if left > 0 and can_visit(left):
            min_dif = dif + len(str(left))
            break
        if right <= limit and can_visit(right):
            min_dif = dif + len(str(right))
            break

        left -= 1
        right += 1
        dif += 1

    return min_dif

print(find_min_cnt())







