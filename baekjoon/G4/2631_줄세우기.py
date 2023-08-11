#230810
from sys import stdin
def to_int(): return int(stdin.readline())

N = to_int()
children = [to_int() for _ in range(N)]
max_increase = 1
increase = [1] * N
for i in range(1, N):
    num = children[i]
    for j in range(i):
        if num > children[j] and increase[i] <= increase[j]:
            increase[i] = increase[j] + 1
    max_val = max(increase)
    if max_increase < max_val:
        max_increase = max_val

print(N - max_increase)


#
def find_min_cnt():
    from sys import stdin
    def to_int(): return int(stdin.readline())

    N = to_int()
    children = [to_int() for _ in range(N)]
    max_increase = 1
    increase = [1] * N
    for i in range(1, N):
        num = children[i]
        for j in range(i):
            if num > children[j] and increase[i] <= increase[j]:
                increase[i] = increase[j] + 1
        max_val = max(increase)
        if max_increase < max_val:
            max_increase = max_val

    return N - max_increase

print(find_min_cnt())


#
def find_min_cnt():
    from sys import stdin
    def to_int(): return int(stdin.readline())

    N = to_int()
    children = [to_int() for _ in range(N)]
    max_increase = 1
    increase = [1] * N
    for i in range(1, N):
        num = children[i]
        for j in range(i):
            if num > children[j] and increase[i] <= increase[j]:
                increase[i] = increase[j] + 1
        if max_increase < increase[i]:
            max_increase = increase[i]

    return N - max_increase

print(find_min_cnt())


#
def find_min_cnt():
    from sys import stdin
    def to_int(): return int(stdin.readline())

    N = to_int()
    children = [to_int() for _ in range(N)]
    increase = [1] * N
    for i in range(1, N):
        num = children[i]
        for j in range(i):
            if num > children[j] and increase[i] <= increase[j]:
                increase[i] = increase[j] + 1

    return N - max(increase)

print(find_min_cnt())