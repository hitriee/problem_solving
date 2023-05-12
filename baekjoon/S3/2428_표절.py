#230512
from math import ceil
N = int(input())
size_list = list(map(int, input().split()))
size_list.sort()
before, cnt, before_start = -1, 0, 0
for i in range(N-1, 0, -1):
    start, end = 0, i
    target = ceil(size_list[end] * 9 / 10)

    if before != target:
        while start <= end:
            mid = (start + end)//2
            if size_list[mid] >= target:
                end = mid - 1
            elif size_list[mid] < target:
                start = mid + 1
        cnt += i-start
        before = target
        before_start = start
    else:
        cnt += i-before_start
print(cnt)


#
from math import ceil
N = int(input())
size_list = list(map(int, input().split()))
size_list.sort()
before, cnt, before_start = -1, 0, 0
for i in range(N-1, 0, -1):
    start, end = 0, i
    target = ceil(size_list[end] * 9 / 10)

    if before != target:
        while start <= end:
            mid = (start + end)//2
            if size_list[mid] >= target:
                end = mid - 1
            else:
                start = mid + 1
        cnt += i-start
        before = target
        before_start = start
    else:
        cnt += i-before_start
print(cnt)

#
from math import ceil
N = int(input())
size_list = list(map(int, input().split()))
size_list.sort()
before, cnt, before_start = -1, 0, 0
for i in range(N-1, 0, -1):
    start, end = 0, i
    target = ceil(size_list[end] * 0.9)

    if before != target:
        while start <= end:
            mid = (start + end)//2
            if size_list[mid] >= target:
                end = mid - 1
            else:
                start = mid + 1
        cnt += i-start
        before = target
        before_start = start
    else:
        cnt += i-before_start
print(cnt)


#
N = int(input())
size_list = list(map(int, input().split()))
size_list.sort()
before, cnt, before_start = -1, 0, 0
for i in range(N-1, 0, -1):
    start, end = 0, i
    target, remain = divmod(size_list[end] * 9, 10)
    if remain:
        target += 1

    if before != target:
        while start <= end:
            mid = (start + end)//2
            if size_list[mid] >= target:
                end = mid - 1
            else:
                start = mid + 1
        cnt += i-start
        before = target
        before_start = start
    else:
        cnt += i-before_start
print(cnt)


#
def cnt_pair():
    from math import ceil
    N = int(input())
    size_list = list(map(int, input().split()))
    size_list.sort()
    before, cnt, before_start = -1, 0, 0
    for i in range(N-1, 0, -1):
        start, end = 0, i
        target = ceil(size_list[end] * 0.9)

        if before != target:
            while start <= end:
                mid = (start + end)//2
                if size_list[mid] >= target:
                    end = mid - 1
                else:
                    start = mid + 1
            cnt += i-start
            before = target
            before_start = start
        else:
            cnt += i-before_start
    return cnt
print(cnt_pair())


#
def cnt_pair():
    from math import ceil
    N = int(input())
    size_list = list(map(int, input().split()))
    size_list.sort()
    before, cnt, before_start = -1, 0, N-1
    for i in range(N-1, 0, -1):
        target = ceil(size_list[i] * 0.9)
        if before != target:
            start, end = 0, before_start
            while start <= end:
                mid = (start + end)//2
                if size_list[mid] >= target:
                    end = mid - 1
                else:
                    start = mid + 1
            cnt += i-start
            before = target
            before_start = start
        else:
            cnt += i-before_start
    return cnt
print(cnt_pair())