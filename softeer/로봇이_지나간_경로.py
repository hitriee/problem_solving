#230330
# 미완료
# H, W = map(int, input().split())
# path = []
# for i in range(H):
#     row = input()
#     for j in range(W):
#         if row[j] == '#':
#             path.append((i, j))
# direct = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# min_command = ''
# min_length = H*W
# def find_command(y, x, index, length=0, command=''):
#     global min_length, min_command
#     if not removed_path:
#         if length < min_length:
#             min_length = length
#             min_command = command
#         return
#     for i in range(4):
#         dy, dx = direct[i]
#         ny, nx = y+2*dy, x+2*dx
#         if (ny, nx) in removed_path:
#             for j in range(1, 3):
#                 removed_path.remove((y+dy*j, x+dx*j))
#             if i != index:
#
#             else:
#                 new_length = length+1
#                 new_command = command + 'A'
#             new_index = i
#             find_command(ny, nx, new_index, new_length, new_command)
#             for j in range(1, 3):
#                 removed_path.add((y+dy*j, x+dx*j))

#230331
# 시작점 결정 후 경로에 맞게 탐색하는지 확인
# 재귀
# H, W = map(int, input().split())
# robot_path = set() # 로봇이 지나간 경로
# direct = [(1, 0), (0, 1), (-1, 0), (0, -1)] # 방향 (dy, dx)
# direct_str = ['v', '>', '^', '<'] # 방향별 출력해야 하는 문자열
# command_list = ['', 'L', 'RR', 'R'] # 명령어
# start_point = () # 시작점
# min_command = '' # 길이가 가장 짧은 명령어
# min_length = H*W*3 # 가장 짧은 명령어 길이
# final_index = -1 # 최종 인덱스 (direct, direct_str)
# # 로봇이 다녀간 곳의 위치를 robot_path에 추가
# for i in range(1, H+1):
#     row = input()
#     for j in range(W):
#         if row[j] == '#':
#             robot_path.add((i, j+1))
# # 재귀함수 - 로봇이 이동한 경로 추측
# def move_robot(y, x, index, command, length):
#     global min_command, min_length, start_point, final_index
#     if not not_visited:
#         if length < min_length:
#             min_length = length
#             min_command = command
#             start_point = (i, j)
#             final_index = direct_i
#         return
#     for dif in (0, 1, -1, 2):
#         new_index = index+dif
#         if new_index >= 4:
#             new_index -= 4
#         elif new_index < 0:
#             new_index += 4
#         dy, dx = direct[new_index]
#         ny, nx = y + dy, x + dx
#         if (ny, nx) in not_visited:
#             not_visited.remove((ny, nx))
#             ny += dy
#             nx += dx
#             not_visited.remove((ny, nx))
#             new_command = command+command_list[dif] + 'A'
#             new_length = length + len(command_list[dif]) + 1
#             return move_robot(ny, nx, new_index, new_command, new_length)
#
# # 로봇이 지나간 곳 중에서 시작점 찾기
# for i, j in robot_path:
#     cnt = 0
#     for k in range(4):
#         di, dj = direct[k]
#         ni, nj = i+di, j+dj
#         # 경로가 한 곳일 때만 시작점이 될 수 있음
#         if (ni, nj) in robot_path:
#             if cnt == 0:
#                 cnt += 1
#                 direct_i = k
#             else:
#                 break
#     else:
#         not_visited = set(robot_path)
#         not_visited.remove((i, j))
#         move_robot(i, j, direct_i, '', 0)
#
# print(*start_point)
# print(direct_str[final_index] ,min_command, sep='\n')


# 반복문
# H, W = map(int, input().split())
# robot_path = set() # 로봇이 지나간 경로
# direct = [(1, 0), (0, 1), (-1, 0), (0, -1)] # 방향 (dy, dx)
# direct_str = ['v', '>', '^', '<'] # 방향별 출력해야 하는 문자열
# command_list = ['', 'L', 'RR', 'R'] # 명령어
# start_point = () # 시작점
# min_command = '' # 길이가 가장 짧은 명령어
# min_length = H*W*3 # 가장 짧은 명령어 길이
# final_index = -1 # 최종 인덱스 (direct, direct_str)
# # 로봇이 다녀간 곳의 위치를 robot_path에 추가
# for i in range(1, H+1):
#     row = input()
#     for j in range(W):
#         if row[j] == '#':
#             robot_path.add((i, j+1))
# # while문 - 로봇이 이동한 경로 추측
# def move_robot(y, x, index):
#     global min_command, min_length, start_point, final_index
#     not_visited = set(robot_path)
#     not_visited.remove((y, x))
#     command = ''
#     length = 0
#     while not_visited:
#         for dif in (0, 1, -1, 2):
#             new_index = index+dif
#             if new_index >= 4:
#                 new_index -= 4
#             elif new_index < 0:
#                 new_index += 4
#             dy, dx = direct[new_index]
#             ny, nx = y + dy, x + dx
#             if (ny, nx) in not_visited:
#                 y, x = ny + dy, nx + dx
#                 not_visited.remove((ny, nx))
#                 not_visited.remove((y, x))
#                 command += command_list[dif] + 'A'
#                 length += len(command_list[dif]) + 1
#                 index = new_index
#                 break
#         else:
#             return
#     if length < min_length:
#         min_length = length
#         min_command = command
#         start_point = (i, j)
#         final_index = direct_i
# # 로봇이 지나간 곳 중에서 시작점 찾기
# for i, j in robot_path:
#     cnt = 0
#     for k in range(4):
#         di, dj = direct[k]
#         ni, nj = i+di, j+dj
#         # 경로가 한 곳일 때만 시작점이 될 수 있음
#         if (ni, nj) in robot_path:
#             if cnt == 0:
#                 cnt += 1
#                 direct_i = k
#             else:
#                 break
#     else:
#         move_robot(i, j, direct_i)
#
# print(*start_point)
# print(direct_str[final_index], min_command, sep='\n')


# 반복문 + f-string
# H, W = map(int, input().split())
# robot_path = set() # 로봇이 지나간 경로
# direct = [(1, 0), (0, 1), (-1, 0), (0, -1)] # 방향 (dy, dx)
# direct_str = ['v', '>', '^', '<'] # 방향별 출력해야 하는 문자열
# command_list = ['', 'L', 'RR', 'R'] # 명령어
# start_point = () # 시작점
# min_command = '' # 길이가 가장 짧은 명령어
# min_length = H*W*3 # 가장 짧은 명령어 길이
# final_index = -1 # 최종 인덱스 (direct, direct_str)
# # 로봇이 다녀간 곳의 위치를 robot_path에 추가
# for i in range(1, H+1):
#     row = input()
#     for j in range(W):
#         if row[j] == '#':
#             robot_path.add((i, j+1))
# # while문 - 로봇이 이동한 경로 추측
# def move_robot(y, x, index):
#     global min_command, min_length, start_point, final_index
#     not_visited = set(robot_path)
#     not_visited.remove((y, x))
#     command = ''
#     length = 0
#     while not_visited:
#         for dif in (0, 1, -1, 2):
#             new_index = index+dif
#             if new_index >= 4:
#                 new_index -= 4
#             elif new_index < 0:
#                 new_index += 4
#             dy, dx = direct[new_index]
#             ny, nx = y + dy, x + dx
#             if (ny, nx) in not_visited:
#                 y, x = ny + dy, nx + dx
#                 not_visited.remove((ny, nx))
#                 not_visited.remove((y, x))
#                 command += command_list[dif] + 'A'
#                 length += len(command_list[dif]) + 1
#                 index = new_index
#                 break
#         else:
#             return
#     if length < min_length:
#         min_length = length
#         min_command = command
#         start_point = f'{i} {j}'
#         final_index = direct_i
# # 로봇이 지나간 곳 중에서 시작점 찾기
# for i, j in robot_path:
#     cnt = 0
#     for k in range(4):
#         di, dj = direct[k]
#         ni, nj = i+di, j+dj
#         # 경로가 한 곳일 때만 시작점이 될 수 있음
#         if (ni, nj) in robot_path:
#             if cnt == 0:
#                 cnt += 1
#                 direct_i = k
#             else:
#                 break
#     else:
#         move_robot(i, j, direct_i)
#
# print(start_point, direct_str[final_index], min_command, sep='\n')

# 반복문 + f-string + 함수
# def find_start():
#     H, W = map(int, input().split())
#     robot_path = set() # 로봇이 지나간 경로
#     direct = [(1, 0), (0, 1), (-1, 0), (0, -1)] # 방향 (dy, dx)
#     direct_str = ['v', '>', '^', '<'] # 방향별 출력해야 하는 문자열
#     command_list = ['A', 'LA', 'RRA', 'RA'] # 명령어
#     length_list = [1, 2, 3, 2]
#     start_point = '' # 시작점
#     min_command = '' # 길이가 가장 짧은 명령어
#     min_length = H*W*3 # 가장 짧은 명령어 길이
#     final_index = -1 # 최종 인덱스 (direct, direct_str)
#     # 로봇이 다녀간 곳의 위치를 robot_path에 추가
#     for i in range(1, H+1):
#         row = input()
#         for j in range(W):
#             if row[j] == '#':
#                 robot_path.add((i, j+1))
#     # while문 - 로봇이 이동한 경로 추측
#     def move_robot(y, x, index):
#         nonlocal min_command, min_length, start_point, final_index
#         not_visited = set(robot_path)
#         not_visited.remove((y, x))
#         command = ''
#         length = 0
#         while not_visited:
#             for dif in (0, 1, -1, 2):
#                 new_index = index+dif
#                 if new_index >= 4:
#                     new_index -= 4
#                 elif new_index < 0:
#                     new_index += 4
#                 dy, dx = direct[new_index]
#                 ny, nx = y + dy, x + dx
#                 if (ny, nx) in not_visited:
#                     y, x = ny + dy, nx + dx
#                     not_visited.remove((ny, nx))
#                     not_visited.remove((y, x))
#                     command += command_list[dif]
#                     length += length_list[dif]
#                     index = new_index
#                     break
#             else:
#                 return
#         if length < min_length:
#             min_length = length
#             min_command = command
#             start_point = f'{i} {j}'
#             final_index = direct_i
#     # 로봇이 지나간 곳 중에서 시작점 찾기
#     for i, j in robot_path:
#         cnt = 0
#         for k in range(4):
#             di, dj = direct[k]
#             ni, nj = i+di, j+dj
#             # 경로가 한 곳일 때만 시작점이 될 수 있음
#             if (ni, nj) in robot_path:
#                 if cnt == 0:
#                     cnt += 1
#                     direct_i = k
#                 else:
#                     break
#         else:
#             move_robot(i, j, direct_i)
#
#     return f'{start_point}\n{direct_str[final_index]}\n{min_command}'
# print(find_start())


# 정리
# def find_start():
#     H, W = map(int, input().split())
#     robot_path = set() # 로봇이 지나간 경로
#     direct = [(1, 0), (0, 1), (-1, 0), (0, -1)] # 방향 (dy, dx)
#     direct_str = ['v', '>', '^', '<'] # 방향별 출력해야 하는 문자열
#     command_list = ['A', 'LA', 'RRA', 'RA'] # 명령어
#     length_list = [1, 2, 3, 2] # 명령어 길이
#     min_length = H*W*3 # 가장 짧은 명령어 길이
#     # 출력할 값 (시작점, 방향, 가장 짧은 명령어)
#     print_info = [''] * 3
#     # 로봇이 다녀간 곳의 위치를 robot_path에 추가
#     for i in range(1, H+1):
#         row = input()
#         for j in range(W):
#             if row[j] == '#':
#                 robot_path.add((i, j+1))
#     # while문 - 로봇이 이동한 경로 추측
#     def move_robot(y, x, index):
#         nonlocal min_length, print_info
#         not_visited = set(robot_path)
#         not_visited.remove((y, x))
#         command = ''
#         length = 0
#         while not_visited:
#             for dif in (0, 1, -1, 2):
#                 new_index = (index+dif)%4
#                 dy, dx = direct[new_index]
#                 ny, nx = y + dy, x + dx
#                 if (ny, nx) in not_visited:
#                     y, x = ny + dy, nx + dx
#                     for position in (ny, nx), (y, x):
#                         not_visited.remove(position)
#                     command += command_list[dif]
#                     length += length_list[dif]
#                     index = new_index
#                     break
#             else:
#                 return
#         if length < min_length:
#             min_length = length
#             print_info = [f'{i} {j}', direct_str[direct_i], command]
#     # 로봇이 지나간 곳 중에서 시작점 찾기
#     for i, j in robot_path:
#         cnt = 0
#         for k in range(4):
#             di, dj = direct[k]
#             ni, nj = i+di, j+dj
#             # 경로가 한 곳일 때만 시작점이 될 수 있음
#             if (ni, nj) in robot_path:
#                 if cnt == 0:
#                     cnt += 1
#                     direct_i = k
#                 else:
#                     break
#         else:
#             move_robot(i, j, direct_i)
#
#     return '\n'.join(print_info)
# print(find_start())


# 정리2
def find_start():
    # 로봇이 다녀간 곳의 위치를 robot_path에 추가
    def fill_path():
        for i in range(1, H+1):
            row = input()
            for j in range(W):
                if row[j] == '#':
                    robot_path.add((i, j+1))
    # while문 - 로봇이 이동한 경로 추측
    def move_robot(y, x, index):
        nonlocal min_length, print_info
        not_visited = set(robot_path)
        not_visited.remove((y, x))
        command = ''
        length = 0
        start_point = f'{y} {x}'
        start_direct = direct_str[index]
        while not_visited:
            for dif in (0, 1, -1, 2):
                new_index = (index+dif)%4
                dy, dx = direct[new_index]
                ny, nx = y + dy, x + dx
                if (ny, nx) in not_visited:
                    y, x = ny + dy, nx + dx
                    for position in (ny, nx), (y, x):
                        not_visited.remove(position)
                    command += command_list[dif]
                    length += length_list[dif]
                    index = new_index
                    break
            else:
                return
        if length < min_length:
            min_length = length
            print_info = [start_point, start_direct, command]

    H, W = map(int, input().split())
    robot_path = set() # 로봇이 지나간 경로
    direct = [(1, 0), (0, 1), (-1, 0), (0, -1)] # 방향 (dy, dx)
    direct_str = ['v', '>', '^', '<'] # 방향별 출력해야 하는 문자열
    command_list = ['A', 'LA', 'RRA', 'RA'] # 명령어
    length_list = [1, 2, 3, 2] # 명령어 길이
    min_length = H*W*3 # 가장 짧은 명령어 길이
    # 출력할 값 (시작점, 방향, 가장 짧은 명령어)
    print_info = [''] * 3
    fill_path()
    # 로봇이 지나간 곳 중에서 시작점 찾기
    for i, j in robot_path:
        cnt = 0
        for k in range(4):
            di, dj = direct[k]
            ni, nj = i+di, j+dj
            # 경로가 한 곳일 때만 시작점이 될 수 있음
            if (ni, nj) in robot_path:
                if cnt == 0:
                    cnt += 1
                    direct_i = k
                else:
                    break
        else:
            move_robot(i, j, direct_i)

    return '\n'.join(print_info)
print(find_start())