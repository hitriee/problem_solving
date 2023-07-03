# #230703
# N, L, R = map(int, input().split())
# population = [list(map(int, input().split())) for _ in range(N)]
# day = 0
#
# def change_population(total, *initial):
#     global move
#     path = [initial]
#     i = 0
#     while i < len(path):
#         y, x = path[i]
#         ref = population[y][x]
#         for dy, dx in (-1, 0), (0, -1), (0, 1), (1, 0):
#             ny, nx = y+dy, x+dx
#             if 0 <= ny < N and 0 <= nx < N:
#                 if not visited[ny][nx] and L <= abs(population[ny][nx] - ref) <= R:
#                     path.append((ny, nx))
#                     visited[ny][nx] = True
#                     total += population[ny][nx]
#         i += 1
#
#     cnt = len(path)
#     if cnt > 1:
#         if not move:
#             move = True
#         average = total//cnt
#         for y, x in path:
#             population[y][x] = average
#
#
# while True:
#     visited = [[False]*N for _ in range(N)]
#     move = False
#     for i in range(N):
#         for j in range(N):
#             if not visited[i][j]:
#                 visited[i][j] = True
#                 change_population(population[i][j], i, j)
#     if not move:
#         break
#     day += 1
#
# print(day)
#
#
# #
# def return_day():
#     N, L, R = map(int, input().split())
#     population = [list(map(int, input().split())) for _ in range(N)]
#     day = 0
#
#     def change_population(total, *initial):
#         nonlocal move
#         path = [initial]
#         i = 0
#         while i < len(path):
#             y, x = path[i]
#             ref = population[y][x]
#             for dy, dx in (-1, 0), (0, -1), (0, 1), (1, 0):
#                 ny, nx = y + dy, x + dx
#                 if 0 <= ny < N and 0 <= nx < N:
#                     if not visited[ny][nx] and L <= abs(population[ny][nx] - ref) <= R:
#                         path.append((ny, nx))
#                         visited[ny][nx] = True
#                         total += population[ny][nx]
#             i += 1
#
#         cnt = len(path)
#         if cnt > 1:
#             if not move:
#                 move = True
#             average = total // cnt
#             for y, x in path:
#                 population[y][x] = average
#
#     while True:
#         visited = [[False] * N for _ in range(N)]
#         move = False
#         for i in range(N):
#             for j in range(N):
#                 if not visited[i][j]:
#                     visited[i][j] = True
#                     change_population(population[i][j], i, j)
#         if not move:
#             break
#         day += 1
#
#     return day
#
# print(return_day())
#
#
# #
# def return_day():
#     from sys import stdin
#
#     def to_int(): return map(int, stdin.readline().split())
#
#     N, L, R = to_int()
#     population = [list(to_int()) for _ in range(N)]
#     day = 0
#
#     def change_population(total, *initial):
#         nonlocal move
#         path = [initial]
#         i = 0
#         while i < len(path):
#             y, x = path[i]
#             ref = population[y][x]
#             for dy, dx in (-1, 0), (0, -1), (0, 1), (1, 0):
#                 ny, nx = y + dy, x + dx
#                 if 0 <= ny < N and 0 <= nx < N:
#                     if not visited[ny][nx] and L <= abs(population[ny][nx] - ref) <= R:
#                         path.append((ny, nx))
#                         visited[ny][nx] = True
#                         total += population[ny][nx]
#             i += 1
#
#         cnt = len(path)
#         if cnt > 1:
#             if not move:
#                 move = True
#             average = total // cnt
#             for y, x in path:
#                 population[y][x] = average
#
#     while True:
#         visited = [[False] * N for _ in range(N)]
#         move = False
#         for i in range(N):
#             for j in range(N):
#                 if not visited[i][j]:
#                     visited[i][j] = True
#                     change_population(population[i][j], i, j)
#         if not move:
#             break
#         day += 1
#
#     return day
#
# print(return_day())
#
#
# #
# def return_day():
#     from sys import stdin
#
#     def to_int(): return map(int, stdin.readline().split())
#
#     N, L, R = to_int()
#     population = [list(to_int()) for _ in range(N)]
#     day = 0
#
#     def change_population(total, *initial):
#         nonlocal move
#         path = [initial]
#         i = 0
#         while i < len(path):
#             y, x = path[i]
#             ref = population[y][x]
#             for dy, dx in (-1, 0), (0, -1), (0, 1), (1, 0):
#                 ny, nx = y + dy, x + dx
#                 if 0 <= ny < N and 0 <= nx < N:
#                     if not visited[ny][nx] and L <= abs(population[ny][nx] - ref) <= R:
#                         path.append((ny, nx))
#                         visited[ny][nx] = True
#                         total += population[ny][nx]
#             i += 1
#
#         cnt = len(path)
#         if cnt > 1:
#             if not move:
#                 move = True
#             average = total // cnt
#             for y, x in path:
#                 population[y][x] = average
#
#     while True:
#         visited = [[False] * N for _ in range(N)]
#         move = False
#         for i in range(N):
#             for j in range(N):
#                 if not visited[i][j]:
#                     visited[i][j] = True
#                     change_population(population[i][j], i, j)
#         if not move:
#             break
#         day += 1
#
#     return day
#
# print(return_day())
#
#
# #
# def return_day():
#     from sys import stdin
#
#     def to_int(): return map(int, stdin.readline().split())
#
#     N, L, R = to_int()
#     population = [list(to_int()) for _ in range(N)]
#     move = False
#
#     def change_population(total, visited, *initial):
#         nonlocal move
#         path = [initial]
#         i = 0
#         while i < len(path):
#             y, x = path[i]
#             ref = population[y][x]
#             for dy, dx in (-1, 0), (0, -1), (0, 1), (1, 0):
#                 ny, nx = y + dy, x + dx
#                 if 0 <= ny < N and 0 <= nx < N:
#                     if not visited[ny][nx] and L <= abs(population[ny][nx] - ref) <= R:
#                         path.append((ny, nx))
#                         visited[ny][nx] = True
#                         total += population[ny][nx]
#             i += 1
#
#         cnt = len(path)
#         if cnt > 1:
#             if not move:
#                 move = True
#             average = total // cnt
#             for y, x in path:
#                 population[y][x] = average
#
#     def count_day():
#         nonlocal move
#         day = 0
#         while True:
#             visited = [[False] * N for _ in range(N)]
#             for i in range(N):
#                 for j in range(N):
#                     if not visited[i][j]:
#                         visited[i][j] = True
#                         change_population(population[i][j], visited, i, j)
#             if not move:
#                 break
#             day += 1
#             move = False
#         return day
#
#     return count_day()
#
# print(return_day())
#
#
# #
# def return_day():
#     from sys import stdin
#
#     def to_int(): return map(int, stdin.readline().split())
#
#     N, L, R = to_int()
#     population = [list(to_int()) for _ in range(N)]
#     move = False
#
#     def change_population(total, visited, *initial):
#         nonlocal move
#         from collections import deque
#
#         path = [initial]
#         q = deque()
#         q.append(initial)
#         i = 0
#         while q:
#             y, x = q.popleft()
#             ref = population[y][x]
#             for dy, dx in (-1, 0), (0, -1), (0, 1), (1, 0):
#                 ny, nx = y + dy, x + dx
#                 if 0 <= ny < N and 0 <= nx < N:
#                     if not visited[ny][nx] and L <= abs(population[ny][nx] - ref) <= R:
#                         q.append((ny, nx))
#                         path.append((ny, nx))
#                         visited[ny][nx] = True
#                         total += population[ny][nx]
#             i += 1
#
#         cnt = len(path)
#         if cnt > 1:
#             if not move:
#                 move = True
#             average = total // cnt
#             for y, x in path:
#                 population[y][x] = average
#
#     def count_day():
#         nonlocal move
#         day = 0
#         while True:
#             visited = [[False] * N for _ in range(N)]
#             for i in range(N):
#                 for j in range(N):
#                     if not visited[i][j]:
#                         visited[i][j] = True
#                         change_population(population[i][j], visited, i, j)
#             if not move:
#                 break
#             day += 1
#             move = False
#         return day
#
#     return count_day()
#
# print(return_day())
#
#
#
def return_day():
    from sys import stdin

    def to_int(): return map(int, stdin.readline().split())

    N, L, R = to_int()
    population = [list(to_int()) for _ in range(N)]
    possible_position = set()
    move = False
    for i in range(N):
        for j in range(N):
            possible_position.add((i, j))

    def change_population(total, temp, *initial):
        nonlocal move
        path = [initial]
        i = 0
        while i < len(path):
            y, x = path[i]
            ref = population[y][x]
            for dy, dx in (-1, 0), (0, -1), (0, 1), (1, 0):
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < N:
                    if (ny, nx) in possible_position:
                        possible_position.remove((ny, nx))
                    if L <= abs(population[ny][nx] - ref) <= R:
                        path.append((ny, nx))
                        total += population[ny][nx]
            i += 1

        cnt = len(path)
        if cnt > 1:
            if not move:
                move = True
            average = total // cnt
            for y, x in path:
                population[y][x] = average
            temp.update(path)

    def count_day():
        nonlocal move, possible_position
        day = 0
        while True:
            temp = set()
            while possible_position:
                i, j = possible_position.pop()
                change_population(population[i][j], temp, i, j)
            if not move:
                break
            day += 1
            move = False
            possible_position = set(temp)
        return day

    return count_day()

print(return_day())