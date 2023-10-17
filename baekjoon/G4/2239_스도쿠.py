# 231017
# 31120 KB/ 7844 ms
puzzle, empty_list = [], []
found = False
candidates = [[set(range(1, 10)) for _ in range(9)] for _ in range(3)]
for i in range(9):
    puzzle.append(list(map(int, input())))
    for j in range(9):
        value = puzzle[i][j]
        if value == 0:
            empty_list.append((i, j))
        else:
            candidates[0][i].remove(value)
            candidates[1][j].remove(value)
            candidates[2][(i//3)*3+j//3].remove(value)

empty = len(empty_list)

# 가로, 세로, 3x3 내에 숫자가 있는지 여부 파악
def is_possible(y, x, num):
    # 가로
    if num not in candidates[0][y]:
        return False
    # 세로
    if num not in candidates[1][x]:
        return False
    # 3 x 3
    if num not in candidates[2][(y//3)*3+x//3]:
        return False

    return True

# puzzle 내부를 차례대로 채움
def fill_puzzle(level=0):
    global found
    if found:
        return

    if level == empty:
        found = True
        for i in range(9):
            print(*puzzle[i], sep='')
        return

    y, x = empty_list[level]
    for num in range(1, 10):
        if is_possible(y, x, num):
            puzzle[y][x] = num
            candidates[0][y].remove(num)
            candidates[1][x].remove(num)
            candidates[2][(y // 3)*3 + x // 3].remove(num)
            fill_puzzle(level+1)
            candidates[0][y].add(num)
            candidates[1][x].add(num)
            candidates[2][(y // 3)*3 + x // 3].add(num)

fill_puzzle()


# 31120 KB / 7636 ms
puzzle, empty_list = [], []
found = False
already = [[set() for _ in range(9)] for _ in range(3)]
for i in range(9):
    puzzle.append(list(map(int, input())))
    for j in range(9):
        value = puzzle[i][j]
        if value == 0:
            empty_list.append((i, j))
        else:
            already[0][i].add(value)
            already[1][j].add(value)
            already[2][(i//3)*3+j//3].add(value)

empty = len(empty_list)

# 가로, 세로, 3x3 내에 숫자가 있는지 여부 파악
def is_possible(y, x, num):
    # 가로
    if num in already[0][y]:
        return False
    # 세로
    if num in already[1][x]:
        return False
    # 3 x 3
    if num in already[2][(y//3)*3+x//3]:
        return False

    return True

# puzzle 내부를 차례대로 채움
def fill_puzzle(level=0):
    global found
    if found:
        return

    if level == empty:
        found = True
        for i in range(9):
            print(*puzzle[i], sep='')
        return

    y, x = empty_list[level]
    for num in range(1, 10):
        if is_possible(y, x, num):
            puzzle[y][x] = num
            already[0][y].add(num)
            already[1][x].add(num)
            already[2][(y // 3)*3 + x // 3].add(num)
            fill_puzzle(level+1)
            already[0][y].remove(num)
            already[1][x].remove(num)
            already[2][(y // 3)*3 + x // 3].remove(num)

fill_puzzle()


# 31120 KB / 5568 ms (Python 3)
# 117204 KB / 1452 ms (PyPy3)
puzzle, empty_list = [], []
found = False
already = [[[False] * 10 for _ in range(9)] for _ in range(3)]

for i in range(9):
    puzzle.append(list(map(int, input())))
    for j in range(9):
        value = puzzle[i][j]
        if value == 0:
            empty_list.append((i, j))
        else:
            already[0][i][value] = True
            already[1][j][value] = True
            already[2][(i//3)*3+j//3][value] = True

empty = len(empty_list)

# 가로, 세로, 3x3 내에 숫자가 있는지 여부 파악
def is_possible(y, x, num):
    # 가로
    if already[0][y][num]:
        return False
    # 세로
    if already[1][x][num]:
        return False
    # 3 x 3
    if already[2][(y//3)*3+x//3][num]:
        return False

    return True

# puzzle 내부를 차례대로 채움
def fill_puzzle(level=0):
    global found
    if found:
        return

    if level == empty:
        found = True
        for i in range(9):
            print(*puzzle[i], sep='')
        return

    y, x = empty_list[level]
    for num in range(1, 10):
        if is_possible(y, x, num):
            puzzle[y][x] = num
            already[0][y][num] = True
            already[1][x][num] = True
            already[2][(y // 3) * 3 + x // 3][num] = True
            fill_puzzle(level+1)
            already[0][y][num] = False
            already[1][x][num] = False
            already[2][(y // 3)*3 + x // 3][num] = False

fill_puzzle()



# 31120 KB / 5664 ms
def return_puzzle():
    puzzle, empty_list = [], []
    found = False
    already = [[[False] * 10 for _ in range(9)] for _ in range(3)]

    for i in range(9):
        puzzle.append(list(map(int, input())))
        for j in range(9):
            value = puzzle[i][j]
            if value == 0:
                empty_list.append((i, j))
            else:
                already[0][i][value] = True
                already[1][j][value] = True
                already[2][(i//3)*3+j//3][value] = True

    empty = len(empty_list)

    # 가로, 세로, 3x3 내에 숫자가 있는지 여부 파악
    def is_possible(y, x, num):
        # 가로
        if already[0][y][num]:
            return False
        # 세로
        if already[1][x][num]:
            return False
        # 3 x 3
        if already[2][(y//3)*3+x//3][num]:
            return False

        return True

    # puzzle 내부를 차례대로 채움
    def fill_puzzle(level=0):
        nonlocal found
        if found:
            return

        if level == empty:
            found = True
            for i in range(9):
                print(*puzzle[i], sep='')
            return

        y, x = empty_list[level]
        for num in range(1, 10):
            if is_possible(y, x, num):
                puzzle[y][x] = num
                already[0][y][num] = True
                already[1][x][num] = True
                already[2][(y // 3) * 3 + x // 3][num] = True
                fill_puzzle(level+1)
                already[0][y][num] = False
                already[1][x][num] = False
                already[2][(y // 3)*3 + x // 3][num] = False

    fill_puzzle()

return_puzzle()