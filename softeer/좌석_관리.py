#230406
# 구현
# dict, set, list, for
# from sys import stdin
# split_input = lambda: stdin.readline().split()
# N, M, Q = map(int, split_input())
# restaurant = {} # 식당 정보 - 사원 번호 : 위치
# already_left = set()
# empty, all_occupied = True, False
# seat_arr = [[False]*(M+1) for _ in range(N+1)]
# for _ in range(Q):
#     command, person = split_input()
#     position = restaurant.get(person)
#     if command == 'In':
#         if position:
#             print(f'{person} already seated.')
#         elif person in already_left:
#             print(f'{person} already ate lunch.')
#         else:
#             if not empty:
#                 if all_occupied:
#                     print(f'There are no more seats.')
#                 else:
#                     possible_seat = ()
#                     max_distance = 0
#                     i = j = 1
#                     while i <= N:
#                         while j <= M:
#                             if not seat_arr[i][j]:
#                                 for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
#                                     nx, ny = i+dx, j+dy
#                                     if 0 < nx <= N and 0 < ny <= M and seat_arr[nx][ny]:
#                                         break
#                                 else:
#                                     each_distance = N*N + M*M + 1
#                                     for x, y in restaurant.values():
#                                         distance = (x-i)*(x-i) + (y-j)*(y-j)
#                                         if distance < each_distance:
#                                             each_distance = distance
#                                     if each_distance > max_distance:
#                                         max_distance = each_distance
#                                         possible_seat = (i, j)
#                                 j += 1
#                             else:
#                                 j += 2
#                         i += 1
#                         j = 1
#                     if max_distance:
#                         x, y = possible_seat
#                         print(f'{person} gets the seat ({x}, {y}).')
#                         restaurant[person] = possible_seat
#                         seat_arr[x][y] = True
#                     else:
#                         print(f'There are no more seats.')
#                         all_occupied = True
#             else:
#                 print(f'{person} gets the seat (1, 1).')
#                 empty = False
#                 restaurant[person] = (1, 1)
#                 seat_arr[1][1] = True
#
#     elif person in already_left:
#         print(f'{person} already left seat.')
#     elif not position:
#         print(f'{person} didn\'t eat lunch.')
#     else:
#         x, y = position
#         print(f'{person} leaves from the seat ({x}, {y}).')
#         del restaurant[person]
#         already_left.add(person)
#         seat_arr[x][y] = False
#         if all_occupied:
#             all_occupied = False


# print 시 tuple 사용
# from sys import stdin
# split_input = lambda: stdin.readline().split()
# N, M, Q = map(int, split_input())
# restaurant = {} # 식당 정보 - 사원 번호 : 위치
# already_left = set()
# empty, all_occupied = True, False
# seat_arr = [[False]*(M+1) for _ in range(N+1)]
# for _ in range(Q):
#     command, person = split_input()
#     position = restaurant.get(person)
#     if command == 'In':
#         if position:
#             print(f'{person} already seated.')
#         elif person in already_left:
#             print(f'{person} already ate lunch.')
#         else:
#             if not empty:
#                 if all_occupied:
#                     print(f'There are no more seats.')
#                 else:
#                     possible_seat = ()
#                     max_distance = 0
#                     i = j = 1
#                     while i <= N:
#                         while j <= M:
#                             if not seat_arr[i][j]:
#                                 for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
#                                     nx, ny = i+dx, j+dy
#                                     if 0 < nx <= N and 0 < ny <= M and seat_arr[nx][ny]:
#                                         break
#                                 else:
#                                     each_distance = N*N + M*M + 1
#                                     for x, y in restaurant.values():
#                                         distance = (x-i)*(x-i) + (y-j)*(y-j)
#                                         if distance < each_distance:
#                                             each_distance = distance
#                                     if each_distance > max_distance:
#                                         max_distance = each_distance
#                                         possible_seat = (i, j)
#                                 j += 1
#                             else:
#                                 j += 2
#                         i += 1
#                         j = 1
#                     if max_distance:
#                         print(f'{person} gets the seat {possible_seat}.')
#                         restaurant[person] = possible_seat
#                         seat_arr[possible_seat[0]][possible_seat[1]] = True
#                     else:
#                         print(f'There are no more seats.')
#                         all_occupied = True
#             else:
#                 print(f'{person} gets the seat (1, 1).')
#                 empty = False
#                 restaurant[person] = (1, 1)
#                 seat_arr[1][1] = True
#
#     elif person in already_left:
#         print(f'{person} already left seat.')
#     elif not position:
#         print(f'{person} didn\'t eat lunch.')
#     else:
#         print(f'{person} leaves from the seat {position}.')
#         del restaurant[person]
#         already_left.add(person)
#         seat_arr[position[0]][position[1]] = False
#         if all_occupied:
#             all_occupied = False


# 비어있을 경우 empty = True 추가
from sys import stdin
split_input = lambda: stdin.readline().split()
N, M, Q = map(int, split_input())
restaurant = {} # 식당 정보 - 사원 번호 : 위치
already_left = set()
empty, all_occupied = True, False
seat_arr = [[False]*(M+1) for _ in range(N+1)]
for _ in range(Q):
    command, person = split_input()
    position = restaurant.get(person)
    if command == 'In':
        if position:
            print(f'{person} already seated.')
        elif person in already_left:
            print(f'{person} already ate lunch.')
        else:
            if not empty:
                if all_occupied:
                    print(f'There are no more seats.')
                else:
                    possible_seat = ()
                    max_distance = 0
                    i = j = 1
                    while i <= N:
                        while j <= M:
                            if not seat_arr[i][j]:
                                for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                                    nx, ny = i+dx, j+dy
                                    if 0 < nx <= N and 0 < ny <= M and seat_arr[nx][ny]:
                                        break
                                else:
                                    each_distance = N*N + M*M + 1
                                    for x, y in restaurant.values():
                                        distance = (x-i)*(x-i) + (y-j)*(y-j)
                                        if distance < each_distance:
                                            each_distance = distance
                                    if each_distance > max_distance:
                                        max_distance = each_distance
                                        possible_seat = (i, j)
                                j += 1
                            else:
                                j += 2
                        i += 1
                        j = 1
                    if max_distance:
                        print(f'{person} gets the seat {possible_seat}.')
                        restaurant[person] = possible_seat
                        seat_arr[possible_seat[0]][possible_seat[1]] = True
                    else:
                        print(f'There are no more seats.')
                        all_occupied = True
            else:
                print(f'{person} gets the seat (1, 1).')
                empty = False
                restaurant[person] = (1, 1)
                seat_arr[1][1] = True

    elif person in already_left:
        print(f'{person} already left seat.')
    elif not position:
        print(f'{person} didn\'t eat lunch.')
    else:
        print(f'{person} leaves from the seat {position}.')
        del restaurant[person]
        already_left.add(person)
        seat_arr[position[0]][position[1]] = False
        if all_occupied:
            all_occupied = False
        if not restaurant:
            empty = True



# 함수화
def manage_seat():
    def print_state():
        nonlocal empty, all_occupied
        if command == 'In':
            if position:
                print(f'{person} already seated.')
            elif person in already_left:
                print(f'{person} already ate lunch.')
            else:
                if not empty:
                    if all_occupied:
                        print(f'There are no more seats.')
                    else:
                        possible_seat = ()
                        max_distance = 0
                        i = j = 1
                        while i <= N:
                            while j <= M:
                                if not seat_arr[i][j]:
                                    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                                        nx, ny = i+dx, j+dy
                                        if 0 < nx <= N and 0 < ny <= M and seat_arr[nx][ny]:
                                            break
                                    else:
                                        each_distance = N*N + M*M + 1
                                        for x, y in restaurant.values():
                                            distance = (x-i)*(x-i) + (y-j)*(y-j)
                                            if distance < each_distance:
                                                each_distance = distance
                                        if each_distance > max_distance:
                                            max_distance = each_distance
                                            possible_seat = (i, j)
                                    j += 1
                                else:
                                    j += 2
                            i += 1
                            j = 1
                        if max_distance:
                            print(f'{person} gets the seat {possible_seat}.')
                            restaurant[person] = possible_seat
                            seat_arr[possible_seat[0]][possible_seat[1]] = True
                        else:
                            print(f'There are no more seats.')
                            all_occupied = True
                else:
                    print(f'{person} gets the seat (1, 1).')
                    empty = False
                    restaurant[person] = (1, 1)
                    seat_arr[1][1] = True

        elif person in already_left:
            print(f'{person} already left seat.')
        elif not position:
            print(f'{person} didn\'t eat lunch.')
        else:
            print(f'{person} leaves from the seat {position}.')
            del restaurant[person]
            already_left.add(person)
            seat_arr[position[0]][position[1]] = False
            if all_occupied:
                all_occupied = False
            if not restaurant:
                empty = True

    from sys import stdin
    split_input = lambda: stdin.readline().split()
    N, M, Q = map(int, split_input()) # 세로, 가로, 쿼리 수
    restaurant = {} # 식당 정보 - 사원 번호 : 위치
    already_left = set() # 이미 떠난 사원 번호
    empty, all_occupied = True, False # 식당이 비어있는지 여부, 식당의 여유 자리 여부
    seat_arr = [[False]*(M+1) for _ in range(N+1)]
    for _ in range(Q):
        command, person = split_input()
        position = restaurant.get(person)
        print_state()

manage_seat()


# 함수화 2
# def manage_seat():
#     def print_state():
#         nonlocal empty, all_occupied
#         command, person = split_input()
#         position = restaurant.get(person)
#         if command == 'In':
#             if position:
#                 print(f'{person} already seated.')
#             elif person in already_left:
#                 print(f'{person} already ate lunch.')
#             else:
#                 if not empty:
#                     if all_occupied:
#                         print(f'There are no more seats.')
#                     else:
#                         possible_seat = ()
#                         max_distance = 0
#                         i = j = 1
#                         while i <= N:
#                             while j <= M:
#                                 if not seat_arr[i][j]:
#                                     for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
#                                         nx, ny = i+dx, j+dy
#                                         if 0 < nx <= N and 0 < ny <= M and seat_arr[nx][ny]:
#                                             break
#                                     else:
#                                         each_distance = N*N + M*M + 1
#                                         for x, y in restaurant.values():
#                                             distance = (x-i)*(x-i) + (y-j)*(y-j)
#                                             if distance < each_distance:
#                                                 each_distance = distance
#                                         if each_distance > max_distance:
#                                             max_distance = each_distance
#                                             possible_seat = (i, j)
#                                     j += 1
#                                 else:
#                                     j += 2
#                             i += 1
#                             j = 1
#                         if max_distance:
#                             print(f'{person} gets the seat {possible_seat}.')
#                             restaurant[person] = possible_seat
#                             seat_arr[possible_seat[0]][possible_seat[1]] = True
#                         else:
#                             print(f'There are no more seats.')
#                             all_occupied = True
#                 else:
#                     print(f'{person} gets the seat (1, 1).')
#                     empty = False
#                     restaurant[person] = (1, 1)
#                     seat_arr[1][1] = True
#
#         elif person in already_left:
#             print(f'{person} already left seat.')
#         elif not position:
#             print(f'{person} didn\'t eat lunch.')
#         else:
#             print(f'{person} leaves from the seat {position}.')
#             del restaurant[person]
#             already_left.add(person)
#             seat_arr[position[0]][position[1]] = False
#             if all_occupied:
#                 all_occupied = False
#             if not restaurant:
#                 empty = True
#
#     from sys import stdin
#     split_input = lambda: stdin.readline().split()
#     N, M, Q = map(int, split_input()) # 세로, 가로, 쿼리 수
#     restaurant = {} # 식당 정보 - 사원 번호 : 위치
#     already_left = set() # 이미 떠난 사원 번호
#     empty, all_occupied = True, False # 식당이 비어있는지 여부, 식당의 여유 자리 여부
#     seat_arr = [[False]*(M+1) for _ in range(N+1)] # 식당
#     for _ in range(Q):
#         print_state()
#
# manage_seat()


#
def manage_seat():
    def find_new_seat():
        nonlocal all_occupied
        if all_occupied:
            print(f'There are no more seats.')
        else:
            possible_seat = () # 앉을 수 있는 좌석
            max_distance = 0 # 근처 자리와의 최대 거리
            i = j = 1 # 좌석의 행과 열
            while i <= N:
                while j <= M:
                    if not seat_arr[i][j]:
                        # 사람이 앉아있지 않은 경우 현재 좌석 주변 탐색
                        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                            nx, ny = i + dx, j + dy
                            # 근처 좌석이 범위를 초과하지 않을 때, 이미 채워진 경우
                            if 0 < nx <= N and 0 < ny <= M and seat_arr[nx][ny]:
                                break
                        else:
                            # 현재 좌석에서 가장 가까운 좌석 찾기
                            each_distance = N * N + M * M + 1
                            for x, y in restaurant.values():
                                distance = (x - i) * (x - i) + (y - j) * (y - j)
                                if distance < each_distance:
                                    each_distance = distance
                            if each_distance > max_distance:
                                max_distance = each_distance
                                possible_seat = (i, j)
                        j += 1
                    else:
                        j += 2
                i += 1
                j = 1
            if max_distance:
                print(f'{person} gets the seat {possible_seat}.')
                restaurant[person] = possible_seat
                seat_arr[possible_seat[0]][possible_seat[1]] = True
            else:
                print(f'There are no more seats.')
                all_occupied = True

    def print_state():
        nonlocal empty, all_occupied
        if command == 'In':
            if position:
                print(f'{person} already seated.')
            elif person in already_left:
                print(f'{person} already ate lunch.')
            else:
                if not empty:
                    find_new_seat()
                else:
                    print(f'{person} gets the seat (1, 1).')
                    empty = False
                    restaurant[person] = (1, 1)
                    seat_arr[1][1] = True

        elif person in already_left:
            print(f'{person} already left seat.')
        elif not position:
            print(f'{person} didn\'t eat lunch.')
        else:
            print(f'{person} leaves from the seat {position}.')
            del restaurant[person]
            already_left.add(person)
            seat_arr[position[0]][position[1]] = False
            if all_occupied:
                all_occupied = False
            if not restaurant:
                empty = True

    from sys import stdin
    split_input = lambda: stdin.readline().split()
    N, M, Q = map(int, split_input()) # 세로, 가로, 쿼리 수
    restaurant = {} # 식당 정보 - 사원 번호 : 위치
    already_left = set() # 이미 떠난 사원 번호
    empty, all_occupied = True, False # 식당이 비어있는지 여부, 식당의 여유 자리 여부
    seat_arr = [[False]*(M+1) for _ in range(N+1)] # 식당
    for _ in range(Q):
        command, person = split_input()
        position = restaurant.get(person)
        print_state()

manage_seat()