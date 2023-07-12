#230629
# N = int(input())
# if N == 1:
#     print(input())
# else:
#     num_cnt = {}
#     for _ in range(N):
#         num = int(input())
#         if num_cnt.get(num):
#             num_cnt[num] += 1
#         else:
#             num_cnt[num] = 1
#     if num_cnt.get(1):
#         result = num_cnt[1]
#         del num_cnt[1]
#     else:
#         result = 0
#
#     if num_cnt.get(0):
#         num_cnt[0] = 1
#
#     num_list = sorted(num_cnt)
#     limit = len(num_list) - 1
#     for i in range(limit):
#         if num_list[i] >= 0:
#             zero_i = i
#             break
#
#     i = 0
#     while i <= end:
#         num = num_list[i]
#         cnt = num_cnt[num]
#         if cnt >= 2:
#             square = num * num
#             result += square * (cnt//2)
#             cnt %= 2
#             # if cnt%2:
#             #     result += num * num_list[i + 1]
#             #     num_cnt[num_list[i + 1]] -= 1
#         if cnt == 1:
#             if i < end:
#                 result += num * num_list[i+1]
#                 num_cnt[num_list[i+1]] -= 1
#             else:
#                 break
#         i += 1
#
#     i_start = i
#
#     i = limit
#     while i >= start:
#         num = num_list[i]
#         cnt = num_cnt[num]
#         if cnt >= 2:
#             square = num * num
#             result += square * (cnt // 2)
#             cnt %= 2
#         if cnt == 1:
#             if i > start:
#                 result += num * num_list[i-1]
#                 num_cnt[num_list[i-1]] -= 1
#             else:
#                 break
#         i -= 1
#
#     i_end = i
#
#     for i in range(i_start, i_end+1):
#         num = num_list[i]
#         cnt = num_cnt[num]
#         if cnt >= 2 and num:
#             square = num * num
#             result += square * (cnt // 2)
#             cnt %= 2
#         if cnt == 1:
#             result += num
#
#     print(result)


#230712
N = int(input())
if N == 1:
    print(input())
else:
    num_list = []
    total = 0
    for _ in range(N):
        num = int(input())
        if num == 1:
            total += 1
            N -= 1
        else:
            num_list.append(num)
    num_list.sort()

    for i in range(N):
        if num_list[i] > 0:
            limit = i
            break
    else:
        limit = N

    if limit == 1:
        total += num_list[0]
    elif limit > 1:
        for i in range(1, limit, 2):
            total += num_list[i-1] * num_list[i]
        if limit%2:
            total += num_list[limit-1]
    for i in range(N-2, limit-1, -2):
        total += num_list[i] * num_list[i+1]
    if (N-limit)%2:
        total += num_list[limit]
    print(total)


#
N = int(input())
if N == 1:
    print(input())
else:
    num_list = []
    total = 0
    for _ in range(N):
        num = int(input())
        if num == 1:
            total += 1
            N -= 1
        else:
            num_list.append(num)
    num_list.sort()

    for i in range(N):
        if num_list[i] > 0:
            limit = i
            break
    else:
        limit = N

    for i in range(1, limit, 2):
        total += num_list[i - 1] * num_list[i]
    if limit % 2:
        total += num_list[limit - 1]

    for i in range(N - 2, limit - 1, -2):
        total += num_list[i] * num_list[i + 1]
    if (N - limit) % 2:
        total += num_list[limit]
    print(total)


#
def return_total():
    N = int(input())
    if N == 1:
        return input()

    num_list = []
    total = 0
    for _ in range(N):
        num = int(input())
        if num == 1:
            total += 1
            N -= 1
        else:
            num_list.append(num)

    num_list.sort()

    for i in range(N):
        if num_list[i] > 0:
            limit = i
            break
    else:
        limit = N

    for i in range(1, limit, 2):
        total += num_list[i - 1] * num_list[i]
    if limit % 2:
        total += num_list[limit - 1]

    for i in range(N - 2, limit - 1, -2):
        total += num_list[i] * num_list[i + 1]
    if (N - limit) % 2:
        total += num_list[limit]

    return total

print(return_total())