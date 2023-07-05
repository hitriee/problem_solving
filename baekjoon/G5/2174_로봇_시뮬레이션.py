# #230705
# from sys import stdin
# def to_list(): return stdin.readline().split()
#
# A, B = map(int, to_list())
# direction = {'N': ['W', 'E', (1, 0)],
#              'W': ['S', 'N', (0, -1)],
#              'S': ['E', 'W', (-1, 0)],
#              'E': ['N', 'S', (0, 1)],}
# crash = False
# robots = [[]]
# position = [[0] * A for _ in range(B)]
# N, M = map(int, to_list())
#
# for i in range(1, N+1):
#     x, y, way = to_list()
#     x, y = int(x) - 1, int(y) - 1
#     robots.append([y, x, way])
#     position[y][x] = i
#
# for _ in range(M):
#     num, command, cnt = to_list()
#     if not crash:
#         num, cnt = map(int, [num, cnt])
#         if command == 'F':
#             y, x, way = robots[num]
#             dy, dx = direction[way][-1]
#             position[y][x] = 0
#             for _ in range(cnt):
#                 y += dy
#                 x += dx
#                 if not (0 <= y < B and 0 <= x < A):
#                     crash = True
#                     print(f'Robot {num} crashes into the wall')
#                     break
#                 elif position[y][x]:
#                     crash = True
#                     print(f'Robot {num} crashes into robot {position[y][x]}')
#                     break
#             else:
#                 position[y][x] = num
#                 robots[num] = [y, x, way]
#
#         else:
#             cnt %= 4
#             way = robots[num][-1]
#             if command == 'L':
#                 for _ in range(cnt):
#                     way = robots[num][-1] = direction[way][0]
#             else:
#                 for _ in range(cnt):
#                     way = robots[num][-1] = direction[way][1]
#
#
# if not crash:
#     print('OK')
#
#
# #
# def print_result():
#     from sys import stdin
#     def to_list():
#         return stdin.readline().split()
#
#     A, B = map(int, to_list())
#     direction = {'N': ['W', 'E', (1, 0)],
#                  'W': ['S', 'N', (0, -1)],
#                  'S': ['E', 'W', (-1, 0)],
#                  'E': ['N', 'S', (0, 1)], }
#     crash = False
#     robots = [[]]
#     position = [[0] * A for _ in range(B)]
#     N, M = map(int, to_list())
#
#     for i in range(1, N + 1):
#         x, y, way = to_list()
#         x, y = int(x) - 1, int(y) - 1
#         robots.append([y, x, way])
#         position[y][x] = i
#
#     for _ in range(M):
#         num, command, cnt = to_list()
#         if not crash:
#             num, cnt = map(int, [num, cnt])
#             if command == 'F':
#                 y, x, way = robots[num]
#                 dy, dx = direction[way][-1]
#                 position[y][x] = 0
#                 for _ in range(cnt):
#                     y += dy
#                     x += dx
#                     if not (0 <= y < B and 0 <= x < A):
#                         crash = True
#                         print(f'Robot {num} crashes into the wall')
#                         break
#                     elif position[y][x]:
#                         crash = True
#                         print(f'Robot {num} crashes into robot {position[y][x]}')
#                         break
#                 else:
#                     position[y][x] = num
#                     robots[num] = [y, x, way]
#
#             else:
#                 cnt %= 4
#                 way = robots[num][-1]
#                 if command == 'L':
#                     for _ in range(cnt):
#                         way = robots[num][-1] = direction[way][0]
#                 else:
#                     for _ in range(cnt):
#                         way = robots[num][-1] = direction[way][1]
#
#     if not crash:
#         print('OK')
#
# print_result()
#
#
#
def return_result():
    from sys import stdin
    def to_list():
        return stdin.readline().split()

    A, B = map(int, to_list())
    direction = {'N': ['W', 'E', (1, 0)],
                 'W': ['S', 'N', (0, -1)],
                 'S': ['E', 'W', (-1, 0)],
                 'E': ['N', 'S', (0, 1)], }
    result = None
    robots = [[]]
    position = [[0] * A for _ in range(B)]
    N, M = map(int, to_list())

    for i in range(1, N + 1):
        x, y, way = to_list()
        x, y = int(x) - 1, int(y) - 1
        robots.append([y, x, way])
        position[y][x] = i


    def return_new(num, command, cnt):
        num, cnt = map(int, [num, cnt])
        if command == 'F':
            y, x, way = robots[num]
            dy, dx = direction[way][-1]
            position[y][x] = 0
            for _ in range(cnt):
                y += dy
                x += dx
                if not (0 <= y < B and 0 <= x < A):
                    return f'Robot {num} crashes into the wall'
                elif position[y][x]:
                    return f'Robot {num} crashes into robot {position[y][x]}'

            position[y][x] = num
            robots[num] = [y, x, way]
        else:
            cnt %= 4
            way = robots[num][-1]
            if command == 'L':
                for _ in range(cnt):
                    way = robots[num][-1] = direction[way][0]
            else:
                for _ in range(cnt):
                    way = robots[num][-1] = direction[way][1]

    for _ in range(M):
        num, command, cnt = to_list()
        if not result:
            result = return_new(num, command, cnt)

    return result if result else 'OK'

print(return_result())