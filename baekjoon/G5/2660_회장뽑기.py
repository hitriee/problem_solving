# #230522
# # bfs
# N = int(input())
# friends = [set() for _ in range(N+1)]
#
# while True: # friends 입력 받기
#     person1, person2 = map(int, input().split())
#     if person1 == -1:
#         break
#     friends[person1].add(person2)
#     friends[person2].add(person1)
#
# min_score = int(1e4) # 회장 후보 점수
# candidates = [] # 회장 후보
# score_list = [1] * (N+1) # 점수
#
# def add_score(person, target): # 점수 계산하기
#     from collections import deque
#     q = deque()
#     q.append((person, 1))
#     visited = [False] * (N+1)
#     while q:
#         num, score = q.popleft()
#         visited[num] = True
#         if target in friends[num]:
#             if score > score_list[person]:
#                 score_list[person] = score
#             return
#         for other in friends[num]:
#             if not visited[other]:
#                 q.append((other, score+1))
#
# # 각 후보별 점수 계산
# for i in range(1, N+1):
#     for j in range(1, N+1):
#         if j != i and j not in friends[i]:
#             add_score(i, j)
#             friendly = False
#
# # 후보, 가장 낮은 점수 찾기
# for i in range(1, N+1):
#     score = score_list[i]
#     if score < min_score:
#         min_score = score
#         candidates.clear()
#         candidates.append(i)
#     elif score == min_score:
#         candidates.append(i)
#
# print(min_score, len(candidates))
# print(*candidates)
#
#
#
# #
# from sys import stdin
# new_input = stdin.readline
# N = int(new_input())
# friends = [set() for _ in range(N+1)]
#
# while True: # friends 입력 받기
#     person1, person2 = map(int, new_input().split())
#     if person1 == -1:
#         break
#     friends[person1].add(person2)
#     friends[person2].add(person1)
#
# min_score = int(1e4) # 회장 후보 점수
# candidates = [] # 회장 후보
# score_list = [1] * (N+1) # 점수
#
# def add_score(person, target): # 점수 계산하기
#     from collections import deque
#     q = deque()
#     q.append((person, 1))
#     visited = [False] * (N+1)
#     while q:
#         num, score = q.popleft()
#         visited[num] = True
#         if target in friends[num]:
#             if score > score_list[person]:
#                 score_list[person] = score
#             return
#         for other in friends[num]:
#             if not visited[other]:
#                 q.append((other, score+1))
#
# # 각 후보별 점수 계산
# for i in range(1, N+1):
#     for j in range(1, N+1):
#         if j != i and j not in friends[i]:
#             add_score(i, j)
#             friendly = False
#
# # 후보, 가장 낮은 점수 찾기
# for i in range(1, N+1):
#     score = score_list[i]
#     if score < min_score:
#         min_score = score
#         candidates.clear()
#         candidates.append(i)
#     elif score == min_score:
#         candidates.append(i)
#
# print(min_score, len(candidates))
# print(*candidates)
#
#
# #
# def return_result():
#     from sys import stdin
#     new_input = stdin.readline
#
#     def add_score(person, target):  # 점수 계산하기
#         from collections import deque
#         q = deque()
#         q.append((person, 1))
#         visited = [False] * (N + 1)
#         while q:
#             num, score = q.popleft()
#             visited[num] = True
#             if target in friends[num]:
#                 if score > score_list[person]:
#                     score_list[person] = score
#                 return
#             for other in friends[num]:
#                 if not visited[other]:
#                     q.append((other, score + 1))
#
#     def calc_min_score():
#         nonlocal min_score
#         for i in range(1, N + 1):
#             score = score_list[i]
#             if score < min_score:
#                 min_score = score
#                 candidates.clear()
#                 candidates.append(str(i))
#             elif score == min_score:
#                 candidates.append(str(i))
#
#     # 입력 받기
#     N = int(new_input())
#     friends = [set() for _ in range(N + 1)]
#
#     while True:
#         person1, person2 = map(int, new_input().split())
#         if person1 == -1:
#             break
#         friends[person1].add(person2)
#         friends[person2].add(person1)
#
#     min_score = int(1e4)  # 회장 후보 점수
#     candidates = []  # 회장 후보
#     score_list = [1] * (N + 1)  # 점수
#
#
#     # 각 후보별 점수 계산
#     for i in range(1, N + 1):
#         for j in range(1, N + 1):
#             if j != i and j not in friends[i]:
#                 add_score(i, j)
#
#     # 후보, 가장 낮은 점수 찾기
#     calc_min_score()
#
#     return f'{min_score} {len(candidates)}\n{" ".join(candidates)}'
#
# print(return_result())


# 2차원 리스트에 시도 중
# def return_result():
#     from sys import stdin
#     new_input = stdin.readline
#
#     def add_score(person, target):  # 점수 계산하기
#         from collections import deque
#         q = deque()
#         q.append((person, 1))
#         visited = [False] * (N + 1)
#         while q:
#             num, score = q.popleft()
#             visited[num] = True
#
#             if friends[target][num] == 1 and score > friends[target][person]:
#                 print(target, num, person, score)
#                 friends[target][person] = score
#                 friends[person][target] = score
#                 return
#
#             for other in friends[num]:
#                 if not visited[other]:
#                     q.append((other, score + 1))
#
#     def calc_min_score():
#         nonlocal min_score
#         for i in range(1, N + 1):
#             score = max(friends[i][1:])
#             if score < min_score:
#                 min_score = score
#                 candidates.clear()
#                 candidates.append(str(i))
#             elif score == min_score:
#                 candidates.append(str(i))
#
#     # 입력 받기
#     N = int(new_input())
#     friends = [[0] * (N+1) for _ in range(N+1)]
#
#     while True:
#         person1, person2 = map(int, new_input().split())
#         if person1 == -1:
#             break
#         friends[person1][person2] = 1
#         friends[person2][person1] = 1
#
#     print(friends)
#     min_score = int(1e4)  # 회장 후보 점수
#     candidates = []  # 회장 후보
#
#
#     # 각 후보별 점수 계산
#     for i in range(1, N):
#         # friends[i][i] = 1
#         for j in range(i+1, N + 1):
#             if friends[i][j] != 1:
#                 add_score(i, j)
#     print(friends)
#     # 후보, 가장 낮은 점수 찾기
#     calc_min_score()
#
#     return f'{min_score} {len(candidates)}\n{" ".join(candidates)}'
#
# print(return_result())
