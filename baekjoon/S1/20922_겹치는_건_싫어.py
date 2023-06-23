# #230513
# # 자료 구조
# N, M = map(int, input().split())
# number_list = input().split()
# check = {}
# max_len_list = []
# cnt = start = 0
# for i in range(N):
#     num = number_list[i]
#     if check.get(num):
#         if check[num] < M:
#             check[num] += 1
#             cnt += 1
#         else:
#             max_len_list.append(cnt)
#             for j in range(start, i):
#                 key = number_list[j]
#                 if key != num:
#                     check[key] -= 1
#                     cnt -= 1
#                 else:
#                     start = j+1
#                     break
#     else:
#         check[num] = 1
#         cnt += 1
#
# max_len_list.append(cnt)
# print(max(max_len_list))
#
#
# # max 값 찾기
# N, M = map(int, input().split())
# number_list = input().split()
# check = {}
# max_len = 0
# cnt = start = 0
# for i in range(N):
#     num = number_list[i]
#     if check.get(num):
#         if check[num] < M:
#             check[num] += 1
#             cnt += 1
#         else:
#             if max_len < cnt:
#                 max_len = cnt
#             for j in range(start, i):
#                 key = number_list[j]
#                 if key != num:
#                     check[key] -= 1
#                     cnt -= 1
#                 else:
#                     start = j+1
#                     break
#     else:
#         check[num] = 1
#         cnt += 1
#
# if max_len < cnt:
#     max_len = cnt
# print(max_len)
#
#
# # 함수화
# N, M = map(int, input().split())
# number_list = input().split()
#
#
# def find_max_len():
#     check = {}
#     max_len = cnt = start = 0
#
#
#     def renew_start():
#         nonlocal start, cnt
#         for j in range(start, i):
#             key = number_list[j]
#             if key != num:
#                 check[key] -= 1
#                 cnt -= 1
#             else:
#                 start = j + 1
#                 return
#
#
#     for i in range(N):
#         num = number_list[i]
#         if check.get(num):
#             if check[num] < M:
#                 check[num] += 1
#                 cnt += 1
#             else:
#                 if max_len < cnt:
#                     max_len = cnt
#                 renew_start()
#         else:
#             check[num] = 1
#             cnt += 1
#
#     if max_len < cnt:
#         max_len = cnt
#     return max_len
#
#
# print(find_max_len())
#
#
#230623
N, K = map(int, input().split())
num_arr = list(map(int, input().split()))
start = end = 0
check = {}
max_len = 1
while end < N:
    end_val = num_arr[end]
    is_existed = check.get(end_val)
    if not is_existed:
        check[end_val] = 1
        end += 1
    elif is_existed < K:
        check[end_val] += 1
        end += 1
    else:
        if max_len < end - start:
            max_len = end - start
        check[num_arr[start]] -= 1
        start += 1

if max_len < end - start:
    max_len = end - start

print(max_len)


#
def find_max_len():
    N, K = map(int, input().split())
    num_arr = list(map(int, input().split()))
    start = end = 0
    check = {}
    max_len = 1

    while end < N:
        end_val = num_arr[end]
        is_existed = check.get(end_val)
        if not is_existed:
            check[end_val] = 1
            end += 1
        elif is_existed < K:
            check[end_val] += 1
            end += 1
        else:
            if max_len < end - start:
                max_len = end - start
            check[num_arr[start]] -= 1
            start += 1

    if max_len < end - start:
        return end - start

    return max_len

print(find_max_len())


#
N, M = map(int, input().split())
number_list = input().split()


def find_max_len():
    check = {}
    max_len = cnt = start = 0

    def renew_start():
        nonlocal start, cnt
        for j in range(start, i):
            key = number_list[j]
            if key != num:
                check[key] -= 1
                cnt -= 1
            else:
                start = j + 1
                return

    for i in range(N):
        num = number_list[i]
        if not check.get(num):
            check[num] = 1
            cnt += 1
        elif check[num] < M:
            check[num] += 1
            cnt += 1
        else:
            if max_len < cnt:
                max_len = cnt
            renew_start()

    if max_len < cnt:
        max_len = cnt
    return max_len


print(find_max_len())