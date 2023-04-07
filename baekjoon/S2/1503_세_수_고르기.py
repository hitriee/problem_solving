#230406
# 틀림
# def find_min_dif():
#     to_int = lambda : map(int, input().split())
#     N, M = to_int()
#     not_in_s = [True] * 1001
#     S = set(to_int())
#     for num in S:
#         not_in_s[num] = False
#     num_set = set(range(1, 1001)) - S
#
#     def can_make_target(target):
#         for num1 in range(1, target):
#             if not_in_s[num1] and target%num1 == 0:
#                 for num2 in range(num1, 1001):
#                     if not_in_s[num2]:
#                         multiple = num1 * num2
#                         if target%multiple == 0 and target//multiple in num_set:
#                             return True
#         return False
#
#     if can_make_target(N):
#         return 0
#
#     dif = 1
#     while True:
#         for target in (N-dif, N+dif):
#             if can_make_target(target):
#                 return dif
#         dif += 1
#
# print(find_min_dif())


# 230407
# def find_min_dif():
#     to_int = lambda : map(int, input().split())
#     N, M = to_int()
#     S = set(to_int()) if M else set()
#
#     def can_make_target(target):
#         from math import isqrt
#         root = isqrt(target)
#         for num1 in range(1, root+1):
#             if num1 not in S and target%num1 == 0:
#                 for num2 in range(num1, root+1):
#                     if num2 not in S:
#                         multiple = num1 * num2
#                         if target%multiple == 0 and target//multiple not in S:
#                             return True
#         return False
#
#     if can_make_target(N):
#         return 0
#
#     dif = 1
#     while True:
#         for target in (N-dif, N+dif):
#             if target > 0 and can_make_target(target):
#                 return dif
#         dif += 1
#
# print(find_min_dif())

#
# def find_min_dif():
#     to_int = lambda : map(int, input().split())
#     N, M = to_int()
#     S = set(to_int()) if M else set()
#
#     def can_make_target(target):
#         from math import isqrt
#         root = isqrt(target)
#         for num1 in range(1, root+1):
#             if num1 not in S and target%num1 == 0:
#                 for num2 in range(num1, root+1):
#                     if num2 not in S:
#                         multiple = num1 * num2
#                         if target%multiple == 0 and target//multiple not in S:
#                             return True
#         return False
#
#     if can_make_target(N):
#         return 0
#
#     dif = 1
#     def find_target():
#         nonlocal dif
#         while True:
#             for target in (N-dif, N+dif):
#                 if target < 0:
#                     return -1
#                 if can_make_target(target):
#                     return dif
#             dif += 1
#
#     if find_target() != -1:
#         return dif
#
#     while True:
#         if can_make_target(N + dif):
#             return dif
#         dif += 1
# print(find_min_dif())



#
def find_min_dif():
    to_int = lambda : map(int, input().split())
    N, M = to_int()
    S = set(to_int()) if M else set()

    def can_make_target(target):
        from math import isqrt
        root = isqrt(target)
        for num1 in range(1, root+1):
            if num1 not in S and target%num1 == 0:
                for num2 in range(num1, root+1):
                    if num2 not in S:
                        multiple = num1 * num2
                        if target%multiple == 0 and target//multiple not in S:
                            return True
        return False

    if can_make_target(N):
        return 0

    for dif in range(1, N):
        for target in (N-dif, N+dif):
            if can_make_target(target):
                return dif
        dif += 1

    dif = N
    while True:
        if can_make_target(N + dif):
            return dif
        dif += 1
print(find_min_dif())


# 이분탐색
def find_min_dif():
    to_int = lambda: map(int, input().split())
    N, M = to_int()
    S = set(to_int()) if M else set()

    def find_sqrt(number):
        start, end = 1, number
        while start <= end:
            mid = (start + end)//2
            square = mid*mid
            if square < number:
                start = mid + 1
            elif square > number:
                end = mid - 1
            else:
                return mid
        return end

    def can_make_target(target):
        root = find_sqrt(target)
        for num1 in range(1, root + 1):
            if num1 not in S and target % num1 == 0:
                for num2 in range(num1, root + 1):
                    if num2 not in S:
                        multiple = num1 * num2
                        if target % multiple == 0 and target // multiple not in S:
                            return True
        return False

    if can_make_target(N):
        return 0

    for dif in range(1, N):
        for target in (N - dif, N + dif):
            if can_make_target(target):
                return dif
        dif += 1

    dif = N
    while True:
        if can_make_target(N + dif):
            return dif
        dif += 1

print(find_min_dif())


#
def find_min_dif():
    to_int = lambda : map(int, input().split())
    N, M = to_int()
    S = set(to_int()) if M else set()

    def can_make_target(target):
        from math import isqrt
        root = isqrt(target)
        new_set = set(range(1, root+1)) - S
        for num1 in new_set:
            if target%num1 == 0:
                for num2 in new_set:
                    multiple = num1 * num2
                    if target%multiple == 0 and target//multiple not in S:
                        return True
        return False

    if can_make_target(N):
        return 0

    for dif in range(1, N):
        for target in (N-dif, N+dif):
            if can_make_target(target):
                return dif
        dif += 1

    dif = N
    while True:
        if can_make_target(N + dif):
            return dif
        dif += 1
print(find_min_dif())