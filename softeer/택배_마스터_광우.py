#230330
# 완전 탐색
# to_int = lambda : map(int, input().split())
# N, M, K = to_int()
# rail = list(to_int())
# path = []
# visited = [False] * N
# min_weight = M*K
# def dfs(level):
#     global min_weight
#     if level == N:
#         cnt = index = total_weight = 0
#         while cnt < K:
#             weight = path[index]
#             while True:
#                 index += 1
#                 if index == N:
#                     index = 0
#                 future_weight = weight + path[index]
#                 if future_weight > M:
#                     break
#                 weight = future_weight
#             total_weight += weight
#             cnt += 1
#         if total_weight < min_weight:
#             min_weight = total_weight
#         return
#
#     for i in range(N):
#         if not visited[i]:
#             visited[i] = True
#             path.append(rail[i])
#             dfs(level+1)
#             path.pop()
#             visited[i] = False
# dfs(0)
# print(min_weight)

# 완전 탐색 + 함수
# def return_weight():
#     def dfs(level):
#         nonlocal min_weight
#         if level == N:
#             cnt = index = total_weight = 0
#             while cnt < K:
#                 weight = path[index]
#                 while True:
#                     index += 1
#                     if index == N:
#                         index = 0
#                     future_weight = weight + path[index]
#                     if future_weight > M:
#                         break
#                     weight = future_weight
#                 total_weight += weight
#                 cnt += 1
#             if total_weight < min_weight:
#                 min_weight = total_weight
#             return
#
#         for i in range(N):
#             if not visited[i]:
#                 visited[i] = True
#                 path.append(rail[i])
#                 dfs(level + 1)
#                 path.pop()
#                 visited[i] = False
#
#     to_int = lambda : map(int, input().split())
#     N, M, K = to_int()
#     rail = list(to_int())
#     path = []
#     visited = [False] * N
#     min_weight = M*K
#     dfs(0)
#     return min_weight
# print(return_weight())


# 주기 추가
# to_int = lambda : map(int, input().split())
# N, M, K = to_int()
# rail = list(to_int())
# path = []
# visited = [False] * N
# min_weight = M*K
# total = sum(rail)
# def dfs(level):
#     global min_weight
#     if level == N:
#         length = cnt = index = 0
#         period = []
#         while length < K:
#             if index == 0 and cnt != 0:
#                 total_weight = (total*cnt) * (K // length) + sum(period[:K%length])
#                 break
#             weight = path[index]
#             while True:
#                 index += 1
#                 if index == N:
#                     index = 0
#                     cnt += 1
#                 future_weight = weight + path[index]
#                 if future_weight > M:
#                     length += 1
#                     period.append(weight)
#                     break
#                 weight = future_weight
#         else:
#             total_weight = sum(period)
#         if total_weight < min_weight:
#             min_weight = total_weight
#         return
#
#     for i in range(N):
#         if not visited[i]:
#             visited[i] = True
#             path.append(rail[i])
#             dfs(level+1)
#             path.pop()
#             visited[i] = False
# dfs(0)
# print(min_weight)


# 함수화
to_int = lambda : map(int, input().split())
N, M, K = to_int()
rail = list(to_int())
path = []
visited = [False] * N
min_weight = M*K
total = sum(rail)

def return_weight():
    # 배열 cnt번 = 1주기, length는 1주기의 길이
    length = cnt = index = 0
    period = []
    while length < K:
        if index == 0 and cnt != 0:
            # index가 0 => 주기 시작, 주기 끝
            return (total * cnt) * (K // length) + sum(period[:K % length])
        weight = path[index]
        while True:
            index += 1
            if index == N:
                index = 0
                cnt += 1
            future_weight = weight + path[index]
            if future_weight > M:
                length += 1
                period.append(weight)
                break
            weight = future_weight
    return sum(period)
def dfs(level):
    global min_weight
    if level == N:
        total_weight = return_weight()
        if total_weight < min_weight:
            min_weight = total_weight
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            path.append(rail[i])
            dfs(level+1)
            path.pop()
            visited[i] = False
dfs(0)
print(min_weight)
