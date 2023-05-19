#230519
# 백트래킹
def find_num():
    N = int(input())
    if N < 10:
        return N-1

    def is_decrease_num(num):
        if len(num) == 1:
            return True
        for i in range(len(num)-1, 0, -1):
            if num[i-1] <= num[i]:
                return False
        return True

    start = 1
    cnt = num = 10
    for i in range(1, 10):
        j = start
        while j < num:
            str_j = str(j)
            remain_j = j%10
            if is_decrease_num(str_j):
                if remain_j:
                    if cnt + remain_j >= N:
                        return j * 10 + N - cnt - 1
                    cnt += remain_j
                j += 1
            else:
                j -= remain_j
                j += 10
        start += num * (i+1)
        num *= 10
    return -1

print(find_num())



#
def find_num():
    N = int(input())
    if N <= 10:
        return N-1

    def count_number(level, number, before):
        nonlocal cnt, final_number
        if final_number:
            return
        if level == limit:
            if cnt + before >= N:
                final_number = int(number + str(N - cnt - 1))
            else:
                cnt += before
            return
        for i in range(1, before):
            count_number(level+1, number + str(i), i)


    cnt = 10
    final_number = 0
    # 숫자 길이 - 1
    for limit in range(1, 10):
        count_number(0, '', 10)
        if final_number:
            return final_number
    return -1

print(find_num())

# for N in range(11, 100):
#     print(N, find_num())


#
def find_num():
    N = int(input())
    if N <= 10:
        return N-1

    def count_number(level, number, before):
        nonlocal cnt, final_number
        if final_number:
            return
        if level == limit:
            if cnt + before >= N:
                final_number = number + str(N - cnt - 1)
            else:
                cnt += before
            return
        for i in range(1, before):
            count_number(level+1, number + str(i), i)


    cnt = 10
    final_number = ''
    # 숫자 길이 - 1
    for limit in range(1, 10):
        count_number(0, '', 10)
        if final_number:
            return final_number
    return -1

print(find_num())


#
def find_num(N):
    if N <= 10:
        return N-1

    def count_number(level, number, before):
        nonlocal cnt, final_number
        if final_number:
            return
        if level == limit:
            if cnt + before >= N:
                final_number = number + str(N - cnt - 1)
            else:
                cnt += before
            return
        for i in range(1, before):
            count_number(level+1, number + str(i), i)


    cnt = 10
    final_number = ''
    # 숫자 길이 - 1
    for limit in range(1, 10):
        count_number(0, '', 10)
        if final_number:
            return final_number
    return -1

N = int(input())
print(find_num(N))