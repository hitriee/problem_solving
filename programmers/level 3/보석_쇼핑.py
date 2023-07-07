#230706
# 틀린 풀이
# def solution(gems):
#     all_jewel = {}
#     min_len = length = len(gems)
#     for i in range(length):
#         gem = gems[i]
#         if all_jewel.get(gem):
#             all_jewel[gem].append(i+1)
#         else:
#             all_jewel[gem] = [i+1]
#
#     len_jewel = len(all_jewel)
#     if len_jewel == length:
#         return [1, length]
#     elif len_jewel == 1:
#         return [1, 1]
#
#     answer = [length, length]
#     jewel_list = list(all_jewel.keys())
#     jewel_list.sort(key=lambda jewel: len(all_jewel[jewel]))
#
#     def own_all_jewel(level=0):
#         nonlocal answer, min_len
#         if level == len_jewel:
#             dif = path[1] - path[0]
#             if dif < min_len:
#                 answer = path[:]
#                 min_len = dif
#             elif path[0] < answer[0]:
#                 answer = path[:]
#             return
#         for j in all_jewel[jewel_list[level]]:
#             if j < path[0]:
#                 if path[1] - j < min_len:
#                     before = path[0]
#                     path[0] = j
#                     own_all_jewel(level+1)
#                     path[0] = before
#             elif j > path[1]:
#                 if j - path[0] < min_len:
#                     before = path[1]
#                     path[1] = j
#                     own_all_jewel(level + 1)
#                     path[1] = before
#             else:
#                 own_all_jewel(level + 1)
#
#     path = [length, 1]
#     own_all_jewel()
#
#     return answer


#
'''
정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.2MB)
테스트 2 〉	통과 (0.09ms, 10.1MB)
테스트 3 〉	통과 (0.28ms, 10.4MB)
테스트 4 〉	통과 (0.16ms, 10.3MB)
테스트 5 〉	통과 (0.13ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.4MB)
테스트 7 〉	통과 (0.01ms, 10.4MB)
테스트 8 〉	통과 (0.32ms, 10.3MB)
테스트 9 〉	통과 (0.44ms, 10.4MB)
테스트 10 〉	통과 (0.51ms, 10.3MB)
테스트 11 〉	통과 (1.08ms, 10.3MB)
테스트 12 〉	통과 (0.97ms, 10.2MB)
테스트 13 〉	통과 (1.50ms, 10.3MB)
테스트 14 〉	통과 (2.07ms, 10.5MB)
테스트 15 〉	통과 (3.57ms, 10.4MB)
효율성  테스트
테스트 1 〉	통과 (2.50ms, 10.5MB)
테스트 2 〉	통과 (3.89ms, 10.6MB)
테스트 3 〉	통과 (8.05ms, 11.1MB)
테스트 4 〉	통과 (7.96ms, 11.5MB)
테스트 5 〉	통과 (13.04ms, 12MB)
테스트 6 〉	통과 (15.07ms, 12.2MB)
테스트 7 〉	통과 (19.01ms, 12.8MB)
테스트 8 〉	통과 (20.12ms, 13MB)
테스트 9 〉	통과 (23.30ms, 13.4MB)
테스트 10 〉	통과 (24.83ms, 13.6MB)
테스트 11 〉	통과 (32.10ms, 14.5MB)
테스트 12 〉	통과 (29.01ms, 15.5MB)
테스트 13 〉	통과 (36.00ms, 16.2MB)
테스트 14 〉	통과 (48.03ms, 16.9MB)
테스트 15 〉	통과 (50.19ms, 17.5MB)
'''
def solution(gems):
    length = len(gems)
    jewel_cnt = {}
    for i in range(length):
        gem = gems[i]
        if jewel_cnt.get(gem, -1) == -1:
            jewel_cnt[gem] = 0

    len_jewel = len(jewel_cnt)
    if len_jewel == length:
        return [1, length]
    elif len_jewel == 1:
        return [1, 1]

    cnt = index = 0
    while cnt < len_jewel:
        if jewel_cnt[gems[index]] == 0:
            cnt += 1
        jewel_cnt[gems[index]] += 1
        index += 1

    answer = [1, index]
    min_len = index - 1
    end = index

    for start in range(length - len_jewel + 1):
        gem = gems[start]
        jewel_cnt[gem] -= 1
        if jewel_cnt[gem] == 0:
            if min_len > end - start:
                min_len = end - start
                answer = [start+1, end]

            cnt -= 1
            index = end
            while index < length:
                if jewel_cnt[gems[index]] == 0:
                    cnt += 1
                jewel_cnt[gems[index]] += 1
                index += 1
                if cnt == len_jewel:
                    end = index
                    break
            else:
                break

    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
