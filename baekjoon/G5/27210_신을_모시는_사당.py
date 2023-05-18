#230512

# 틀림
# N = int(input())
# statue_list = input().split()
# cnt_list = []
# before = statue_list[0]
# cnt = 1
# for i in range(1, N):
#     if statue_list[i] == before:
#         cnt += 1
#     else:
#         cnt_list.append(cnt)
#         before = statue_list[i]
#         cnt = 1
# cnt_list.append(cnt)
#
# length = len(cnt_list)
#
# max_values = [0] * 2
# for start in range(2):
#     for i in range(start, length, 2):
#         cnt = cnt_list[i]
#         if cnt >= max_values[start]:
#             for j in range(i+2, length, 2):
#                 if cnt_list[j-1] < cnt_list[j]:
#                     cnt += cnt_list[j] - cnt_list[j-1]
#                 else:
#                     break
#             max_values[start] = cnt
# print(max(max_values))


# 틀림
# N = int(input())
# statue_list = input().split()
# cnt_list = []
# before = statue_list[0]
# cnt = 1
# for i in range(1, N):
#     if statue_list[i] == before:
#         cnt += 1
#     else:
#         cnt_list.append(cnt)
#         before = statue_list[i]
#         cnt = 1
# cnt_list.append(cnt)
#
# length = len(cnt_list)
# if length == 1:
#     print(cnt_list[0])
# else:
#     max_list = [[], []]
#     for start in range(2):
#         cnt = cnt_list[start]
#         for j in range(start + 2, length, 2):
#             if cnt_list[j - 1] < cnt_list[j]:
#                 cnt += cnt_list[j] - cnt_list[j - 1]
#             else:
#                 break
#         before = cnt_list[start]
#         max_list[start].append(cnt)
#
#         for i in range(start+2, length, 2):
#             cnt = cnt_list[i]
#             if cnt > before:
#                 for j in range(i+2, length, 2):
#                     if cnt_list[j-1] < cnt_list[j]:
#                         cnt += cnt_list[j] - cnt_list[j-1]
#                     else:
#                         break
#                 max_list[start].append(cnt)
#                 before = cnt_list[i]
# print(max(*max_list[0], *max_list[1]))



# 230518
N = int(input())
statue_list = input().split()
straight_list = []
cnt = 1
before = statue_list[0]
for i in range(1, N):
    if statue_list[i] == before:
        cnt += 1
            # if cnt > 0 else -1
    else:
        straight_list.append(cnt)
        before = statue_list[i]
        cnt = 1
            # if cnt > 0 else -1

straight_list.append(cnt)

length = len(straight_list)
if length > 1:
    total_set = set()
    for start in range(2):
        for i in range(start, length, 2): # 인덱스 범위
            total = straight_list[i]
            total_set.add(total)
            for j in range(i+2, length, 2): # i부터 특정 구간까지 계산 (부분합)
                result = straight_list[j] - straight_list[j-1]
                if total + result >= 0:
                    if result < 0:
                        total_set.add(total)
                    total += result
                else:
                    break
                total_set.add(total)

    print(max(total_set))
else:
    print(straight_list[0])


# 함수화
def fill_list():
    cnt = 1
    before = statue_list[0]
    for i in range(1, N):
        if statue_list[i] == before:
            cnt += 1

        else:
            straight_list.append(cnt)
            before = statue_list[i]
            cnt = 1

    straight_list.append(cnt)

def find_max():
    length = len(straight_list)
    if length == 1:
        return straight_list[0]

    total_set = set()
    for start in range(2):
        for i in range(start, length, 2): # 인덱스 범위
            total = straight_list[i]
            total_set.add(total)
            for j in range(i+2, length, 2): # i부터 특정 구간까지 계산 (부분합)
                result = straight_list[j] - straight_list[j-1]
                if total + result >= 0:
                    if result < 0:
                        total_set.add(total)
                    total += result
                else:
                    break
                total_set.add(total)

    return max(total_set)

N = int(input())
statue_list = input().split()
straight_list = []
fill_list()
print(find_max())


# 함수화2
def return_max():
    def fill_list():
        cnt = 1
        before = statue_list[0]
        for i in range(1, N):
            if statue_list[i] == before:
                cnt += 1

            else:
                straight_list.append(cnt)
                before = statue_list[i]
                cnt = 1

        straight_list.append(cnt)

    def find_max():
        length = len(straight_list)
        if length == 1:
            return straight_list[0]

        total_set = set()
        for start in range(2):
            for i in range(start, length, 2): # 인덱스 범위
                total = straight_list[i]
                total_set.add(total)
                for j in range(i+2, length, 2): # i부터 특정 구간까지 계산 (부분합)
                    result = straight_list[j] - straight_list[j-1]
                    if total + result >= 0:
                        if result < 0:
                            total_set.add(total)
                        total += result
                    else:
                        break
                    total_set.add(total)

        return max(total_set)

    N = int(input())
    statue_list = input().split()
    straight_list = []
    fill_list()
    return find_max()

print(return_max())

'''
10
1 2 1 1 2 2 2 1 1 2
'''

# 최적화 시도 중
# N = int(input())
# statue_list = input().split()
# straight_list = []
# cnt = 1
# before = statue_list[0]
# for i in range(1, N):
#     if statue_list[i] == before:
#         cnt += 1
#
#     else:
#         straight_list.append(cnt)
#         before = statue_list[i]
#         cnt += 1
#
# straight_list.append(cnt)
# length = len(straight_list)
#
# if length > 1:
#     acc = [straight_list[0]]
#     for i in range(1, length):
#         if i%2:
#             acc.append(acc[-1] - straight_list[i])
#         else:
#             acc.append(acc[-1] + straight_list[i])
#
#     max_val_set = [{max(*[straight_list[j] for j in range(i, length, 2)])} for i in range(2)]
#
#     max_val_list = [[] for i in range(2)]
#     index_list = [[] for _ in range(2)]
#
#     for i in range(2):
#         for j in range(i, length, 2):
#             acc[j]
#
#
#     while start < length:
#         start = 1
#         for i in range(start, length, 2):
#             pass
#         for i in range(start+1, length, 2):
#             pass
#         start += 2
#
#     for i in range(length):
#         num = acc[i]
#         if i%2 == 0:
#             if num > max_val:
#                 max_val = num
#                 max_i = i
#         elif num < min_val:
#             min_val = num
#             min_i = i
#
#
#     total_set = set()
#     for i in range(2, length, 2):
#         before = acc[i-1]
#         if i > max_i:
#             temp_max = 0
#             for j in range(i, length, 2):
#                 num = acc[j]
#                 if num > temp_max:
#                     temp_max = num
#                     max_i = i
#         value = acc[max_i] - before
#         if max_val < value:
#             max_val = value
#
#     for i in range(1, length, 2):
#         before = acc[i - 1]
#         if i > min_i:
#             temp_min = 0
#             for j in range(i, length, 2):
#                 num = acc[j]
#                 if num < temp_min:
#                     temp_min = num
#                     min_i = i
#         value = acc[min_i] - before
#         if min_val > value:
#             min_val = value
#     print(max(max_val, -min_val))
#     # print(max(total_set))
# else:
#     print(straight_list[0])
