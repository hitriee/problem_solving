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

    else:
        straight_list.append(cnt)
        before = statue_list[i]
        cnt = 1

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

#230522
def return_max():
    def find_max():
        for direction in ('1', '2'):
            now = 0
            max_list.append([])
            for i in range(N): # 인덱스 범위
                now += 1 if statue_list[i] == direction else -1
                if now < 0:
                    now = 0
                max_list[-1].append(now)

        return max(*max_list[0], *max_list[-1])

    N = int(input())
    statue_list = input().split()
    max_list = []
    return find_max()

print(return_max())


#
def return_max():
    def find_max():
        max_list = [[] for _ in range(2)]
        now_list = [0] * 2
        for direction in statue_list:
            index = 0 if direction == '1' else 1
            now_list[index] += 1
            now_list[1-index] -= 1
            for i in range(2):
                if now_list[i] < 0:
                    now_list[i] = 0
                max_list[i].append(now_list[i])
        return max(*max_list[0], *max_list[-1])

    N = int(input())
    statue_list = input().split()
    return find_max()

print(return_max())


#
def return_max():

    N = int(input())
    statue_list = input().split()
    max_list = [0] * 2
    now_list = [0] * 2

    for direction in statue_list:
        index = 0 if direction == '1' else 1
        now_list[index] += 1
        now_list[1 - index] -= 1

        for i in range(2):
            now = now_list[i]
            if now < 0:
                now_list[i] = 0
            elif now > max_list[i]:
                max_list[i] = now

    return max(max_list[0], max_list[1])

print(return_max())