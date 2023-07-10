#230710
from sys import stdin
new_input = stdin.readline
S, C = map(int, new_input().split())
length_list = [int(new_input()) for _ in range(S)]
start, end = 1, max(length_list)

while start <= end:
    mid = (start + end)//2
    cnt = 0
    for length in length_list:
        cnt += length // mid
    if cnt >= C:
        start = mid + 1
    else:
        end = mid - 1

if end:
    remain = cnt = 0
    for length in length_list:
        cnt += length // end
        remain += length % end

    print(remain + (cnt - C) * end)
else:
    print(sum(length_list))


#
from sys import stdin
new_input = stdin.readline
S, C = map(int, new_input().split())
length_list = [int(new_input()) for _ in range(S)]
length_list.sort(reverse=True)
start, end = 1, max(length_list)

while start <= end:
    mid = (start + end)//2
    cnt = 0
    for length in length_list:
        quot = length // mid
        if quot == 0:
            break
        cnt += quot
    if cnt >= C:
        start = mid + 1
    else:
        end = mid - 1

if end:
    remain = cnt = 0
    for i in range(S):
        length = length_list[i]
        quot = length // end
        if quot == 0:
            remain += sum(length_list[i:])
            break
        cnt += quot
        remain += length % end

    print(remain + (cnt - C) * end)
else:
    print(sum(length_list))


#
def return_quantity():
    from sys import stdin
    new_input = stdin.readline
    S, C = map(int, new_input().split())
    length_list = [int(new_input()) for _ in range(S)]
    length_list.sort(reverse=True)
    start, end = 1, max(length_list)

    def find_cnt(target):
        cnt = 0
        for length in length_list:
            quot = length // mid
            if quot == 0:
                return cnt
            cnt += quot
        return cnt

    while start <= end:
        mid = (start + end) // 2
        cnt = find_cnt(mid)
        if cnt >= C:
            start = mid + 1
        else:
            end = mid - 1

    return sum(length_list) - C*end

print(return_quantity())


#
def return_quantity():
    from sys import stdin
    new_input = stdin.readline
    S, C = map(int, new_input().split())
    length_list = [int(new_input()) for _ in range(S)]
    start, end = 1, max(length_list)

    def find_cnt(target):
        cnt = 0
        for length in length_list:
            quot = length // mid
            cnt += quot
        return cnt

    while start <= end:
        mid = (start + end) // 2
        cnt = find_cnt(mid)
        if cnt >= C:
            start = mid + 1
        else:
            end = mid - 1

    return sum(length_list) - C*end

print(return_quantity())


#
def return_quantity():
    from sys import stdin
    new_input = stdin.readline
    S, C = map(int, new_input().split())
    length_list = [int(new_input()) for _ in range(S)]
    start, end = 1, max(length_list)

    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for length in length_list:
            quot = length // mid
            cnt += quot
        if cnt >= C:
            start = mid + 1
        else:
            end = mid - 1

    return sum(length_list) - C*end

print(return_quantity())

#
def return_quantity():
    from sys import stdin
    new_input = stdin.readline
    S, C = map(int, new_input().split())
    length_list = [int(new_input()) for _ in range(S)]
    start, end = 1, max(length_list)

    def find_cnt(target):
        cnt = 0
        for length in length_list:
            quot = length // target
            cnt += quot
        return cnt

    while start <= end:
        mid = (start + end) // 2
        cnt = find_cnt(mid)
        if cnt >= C:
            start = mid + 1
        else:
            end = mid - 1

    return sum(length_list) - C*end

print(return_quantity())


#
def return_quantity():
    from sys import stdin
    new_input = stdin.readline
    S, C = map(int, new_input().split())
    length_list = [int(new_input()) for _ in range(S)]
    start, end = 1, max(length_list)

    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for length in length_list:
            cnt += length // mid

        if cnt >= C:
            start = mid + 1
        else:
            end = mid - 1

    return sum(length_list) - C*end

print(return_quantity())


#
def return_quantity():
    from sys import stdin
    new_input = stdin.readline

    S, C = map(int, new_input().split())
    length_list = [int(new_input()) for _ in range(S)]
    total = sum(length_list)
    start, end = 1, total//S

    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for length in length_list:
            cnt += length // mid

        if cnt >= C:
            start = mid + 1
        else:
            end = mid - 1

    return total - C*end

print(return_quantity())