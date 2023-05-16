#230516
# 구현
def is_valid_board():
    first_line = second_line = False
    for i in range(3): # 가로
        mark = board[i][0]
        for j in range(1, 3):
            if board[i][j] != mark:
                break
        else:
            if mark == 'X':
                if second_line:
                    return 'invalid'
                first_line = True
            elif mark == 'O':
                if first_line:
                    return 'invalid'
                second_line = True

    for j in range(3): # 세로
        mark = board[0][j]
        for i in range(1, 3):
            if board[i][j] != mark:
                break
        else:
            if mark == 'X':
                if second_line:
                    return 'invalid'
                first_line = True
            elif mark == 'O':
                if first_line:
                    return 'invalid'
                second_line = True

    mark = board[0][0]
    for i in range(1, 3): # 우하 대각선
        if board[i][i] != mark:
            break
    else:
        if mark == 'X':
            if second_line:
                return 'invalid'
            first_line = True
        elif mark == 'O':
            if first_line:
                return 'invalid'
            else:
                second_line = True

    mark = board[0][2]
    for i in range(1, 3): # 좌하 대각선
        if board[i][2 - i] != mark:
            break
    else:
        if mark == 'X':
            if second_line:
                return 'invalid'
            first_line = True
        elif mark == 'O':
            if first_line:
                return 'invalid'
            second_line = True

    if second_line:
        if first_line or first == second+1:
            return 'invalid'
        return 'valid'
    elif first_line:
        if first == second:
            return 'invalid'
        return 'valid'
    elif first + second == 9:
        return 'valid'
    return 'invalid'

while True:
    result = input()
    if result == 'end':
        break
    board = []
    first = second = 0
    for i in range(3):
        board.append(result[3*i:3*i+3])
        for j in range(3):
            if board[-1][j] == 'X':
                first += 1
            elif board[-1][j] == 'O':
                second += 1
    if second <= first <= second+1:
        print(is_valid_board())
    else:
        print('invalid')


#
def check_valid():
    def is_valid_board():
        first_line = second_line = False
        for i in range(3): # 가로
            mark = board[i][0]
            for j in range(1, 3):
                if board[i][j] != mark:
                    break
            else:
                if mark == 'X':
                    if second_line:
                        return 'invalid'
                    first_line = True
                elif mark == 'O':
                    if first_line:
                        return 'invalid'
                    second_line = True

        for j in range(3): # 세로
            mark = board[0][j]
            for i in range(1, 3):
                if board[i][j] != mark:
                    break
            else:
                if mark == 'X':
                    if second_line:
                        return 'invalid'
                    first_line = True
                elif mark == 'O':
                    if first_line:
                        return 'invalid'
                    second_line = True

        mark = board[0][0]
        for i in range(1, 3): # 우하 대각선
            if board[i][i] != mark:
                break
        else:
            if mark == 'X':
                if second_line:
                    return 'invalid'
                first_line = True
            elif mark == 'O':
                if first_line:
                    return 'invalid'
                else:
                    second_line = True

        mark = board[0][2]
        for i in range(1, 3): # 좌하 대각선
            if board[i][2 - i] != mark:
                break
        else:
            if mark == 'X':
                if second_line:
                    return 'invalid'
                first_line = True
            elif mark == 'O':
                if first_line:
                    return 'invalid'
                second_line = True

        if second_line:
            if first_line or first == second+1:
                return 'invalid'
            return 'valid'
        elif first_line:
            if first == second:
                return 'invalid'
            return 'valid'
        elif first + second == 9:
            return 'valid'
        return 'invalid'

    while True:
        result = input()
        if result == 'end':
            break
        board = []
        first = second = 0
        for i in range(3):
            board.append(result[3*i:3*i+3])
            for j in range(3):
                if board[-1][j] == 'X':
                    first += 1
                elif board[-1][j] == 'O':
                    second += 1

        if second <= first <= second+1:
            print(is_valid_board())
        else:
            print('invalid')
check_valid()


#
def check_valid():
    def is_valid_board():
        first_line = second_line = False
        for i in range(3): # 가로
            mark = board[i][0]
            for j in range(1, 3):
                if board[i][j] != mark:
                    break
            else:
                if mark == 'X':
                    if second_line:
                        return 'invalid'
                    first_line = True
                elif mark == 'O':
                    if first_line:
                        return 'invalid'
                    second_line = True

        for j in range(3): # 세로
            mark = board[0][j]
            for i in range(1, 3):
                if board[i][j] != mark:
                    break
            else:
                if mark == 'X':
                    if second_line:
                        return 'invalid'
                    first_line = True
                elif mark == 'O':
                    if first_line:
                        return 'invalid'
                    second_line = True

        mark = board[0][0]
        for i in range(1, 3): # 우하 대각선
            if board[i][i] != mark:
                break
        else:
            if mark == 'X':
                if second_line:
                    return 'invalid'
                first_line = True
            elif mark == 'O':
                if first_line:
                    return 'invalid'
                else:
                    second_line = True

        mark = board[0][2]
        for i in range(1, 3): # 좌하 대각선
            if board[i][2 - i] != mark:
                break
        else:
            if mark == 'X':
                if second_line:
                    return 'invalid'
                first_line = True
            elif mark == 'O':
                if first_line:
                    return 'invalid'
                second_line = True

        if second_line:
            if first_line or first == second+1:
                return 'invalid'
            return 'valid'
        elif first_line:
            if first == second:
                return 'invalid'
            return 'valid'
        elif first + second == 9:
            return 'valid'
        return 'invalid'

    from sys import stdin
    def new_input(): return stdin.readline().rstrip()
    while True:
        result = new_input()
        if result == 'end':
            break
        board = []
        first = second = 0
        for i in range(3):
            board.append(result[3*i:3*i+3])
            for j in range(3):
                if board[-1][j] == 'X':
                    first += 1
                elif board[-1][j] == 'O':
                    second += 1

        if second <= first <= second+1:
            print(is_valid_board())
        else:
            print('invalid')
check_valid()

