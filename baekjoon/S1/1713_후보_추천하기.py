#230327
# heap 이용해 - X
# from heapq import heappush, heappop, heapify
# N = int(input())
# total_recommend = int(input())
# recommend_list = input().split()
# pictures, already = [], set()
# length = 0
# for i in range(total_recommend):
#     person = recommend_list[i]
#     cnt = 0
#     if person not in already:
#         if length < N:
#             length += 1
#         else:
#             picture = heappop(pictures)
#             already.remove(picture[-1])
#         already.add(person)
#     elif pictures[0][-1] == person:
#         cnt = heappop(pictures)[0]
#     else:
#         for j in range(1, length):
#             picture = pictures[j]
#             if picture[-1] == person:
#                 cnt = picture[0]
#                 pictures.pop(j)
#                 heapify(pictures)
#                 break
#     heappush(pictures, (cnt+1, i, person))
#
# print(' '.join(sorted(already)))

# 230330
# 사진틀 개수, 추천 횟수, 추천받은 학생
# N = int(input())
# vote_num = int(input())
# recommended = list(map(int, input().split()))
# def final_candidate():
#     # 사진틀 개수가 추천된 학생보다 작거나 같을 경우
#     student_set = set(recommended)
#     if N >= len(student_set):
#         return sorted(student_set)
#     # 사진틀, 추천횟수, 학생 횟수와 사진틀 내의 인덱스
#     picture, cnt, num_to_i = [], [0] * N, {}
#     min_i, min_num = 0, 1
#     i = length = 0
#     # 사진틀 채우기
#     while length < N:
#         student = recommended[i]
#         # 이미 올라가 있는 후보
#         if num_to_i.get(student, -1) > -1:
#             index = num_to_i[student]
#             cnt[index] += 1
#             if min_i == index:
#                 for j in range(length):
#                     if 0 < cnt[j] < min_num:
#                         min_num = cnt[j]
#                         min_i = j
#                         break
#                 else:
#                     min_num += 1
#         else:
#             picture.append(student)
#             cnt[length] += 1
#             num_to_i[student] = length
#             if min_num > 1:
#                 min_num = 1
#                 min_i = length
#             length += 1
#         i += 1
#         if i == vote_num:
#             return sorted(picture)
#     # 사진틀이 다 채워진 후
#     start = i
#     for i in range(start, vote_num):
#         student = recommended[i]
#         # 이미 올라가 있는 후보
#         if num_to_i.get(student, -1) > -1:
#             index = num_to_i[student]
#             cnt[index] += 1
#             if min_i == index:
#                 for j in range(length):
#                     if 0 < cnt[j] < min_num:
#                         min_num = cnt[j]
#                         min_i = j
#                         break
#                 else:
#                     min_num += 1
#
#         else:
#             for j in range(min_i):
#                 if cnt[j] == min_num:
#                     num = picture.pop(j)
#                     cnt.pop(j)
#                     min_i = j
#                     break
#             else:
#                 num = picture.pop(min_i)
#                 cnt.pop(min_i)
#             num_to_i[num] = -1
#             if min_num > 1:
#                 min_num = 1
#                 min_i = N-1
#             else:
#                 min_num = vote_num
#                 for j in range(min_i, N-1):
#                     if cnt[j] < min_num:
#                         min_num = cnt[j]
#                         min_i = j
#                     num_to_i[picture[j]] = j
#             picture.append(student)
#             cnt.append(1)
#             num_to_i[student] = N - 1
#     return sorted(picture)
# print(*final_candidate())


#230331
# heapq + pop
def find_candidates():
    from heapq import heappop, heappush, heapify
    N = int(input())
    total_cnt = int(input())
    recommended = list(map(int, input().split()))
    student_set = set(recommended)
    if len(student_set) <= N:
        return sorted(student_set)
    picture = []
    present = set()
    i = length = 0
    while length < N:
        student = recommended[i]
        if student in present:
            for j in range(length):
                if picture[j][-1] == student:
                    cnt, stored_time, num = picture.pop(j)
                    picture.append((cnt+1, stored_time, student))
                    break
        else:
            picture.append((1, length, student))
            present.add(student)
            length += 1
        if i == total_cnt:
            return sorted(present)
        i += 1

    heapify(picture)
    start = i
    for i in range(start, total_cnt):
        student = recommended[i]
        if student in present:
            for j in range(length):
                if picture[j][-1] == student:
                    cnt, stored_time, num = picture.pop(j)
                    heapify(picture)
                    heappush(picture, (cnt + 1, stored_time, num))
                    break
        else:
            info = heappop(picture)
            present.remove(info[-1])
            heappush(picture, (1, length, student))
            present.add(student)
            length += 1
    return sorted(present)
print(*find_candidates())


# heap + pop + 함수
def find_candidates():
    def fill_picture():
        nonlocal length, start
        i = 0
        while length < N:
            student = recommended[i]
            if student in present:
                for j in range(length):
                    if picture[j][-1] == student:
                        cnt, stored_time, num = picture.pop(j)
                        picture.append((cnt+1, stored_time, student))
                        break
            else:
                picture.append((1, length, student))
                present.add(student)
                length += 1
            if i == total_cnt:
                return sorted(present)
            i += 1
        start = i

    def change_picture():
        nonlocal length
        from heapq import heappop, heappush, heapify

        heapify(picture)
        for i in range(start, total_cnt):
            student = recommended[i]
            if student in present:
                for j in range(length):
                    if picture[j][-1] == student:
                        cnt, stored_time, num = picture.pop(j)
                        heapify(picture)
                        heappush(picture, (cnt + 1, stored_time, num))
                        break
            else:
                info = heappop(picture)
                present.remove(info[-1])
                heappush(picture, (1, length, student))
                present.add(student)
                length += 1
        return sorted(present)

    N = int(input())
    total_cnt = int(input())
    recommended = list(map(int, input().split()))
    student_set = set(recommended)
    if len(student_set) <= N:
        return sorted(student_set)
    picture = []
    present = set()
    start = length = 0
    return_val = fill_picture()
    if return_val:
        return return_val
    return change_picture()

print(*find_candidates())