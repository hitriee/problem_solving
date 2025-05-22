# 250522
# 35052 KB / 3412 ms
def main():
    from collections import deque

    def square_idx(y, x):
        idx = 0
        if y >= 6:
            idx += 6
        elif y >= 3:
            idx += 3

        if x >= 6:
            idx += 2
        elif x >= 3:
            idx += 1

        return idx

    def remove_num(y, x, idx, num):
        rows[y].remove(num)
        cols[x].remove(num)
        squares[idx].remove(num)

    def bfs():
        while empty_position:
            y, x, idx, visited = empty_position.popleft()
            remain = rows[y] & cols[x] & squares[idx]
            if len(remain) == 1:
                num = remain.pop()
                remove_num(y, x, idx, num)
                board[y][x] = num
            elif visited == 0:
                empty_position.append((y, x, idx, 1))
            else:
                temp.append((y, x, idx))


    def dfs(level):
        nonlocal finished

        if finished:
            return
        if level == N:
            finished = True
            return

        y, x, idx = temp[level]
        remain = rows[y] & cols[x] & squares[idx]
        for num in remain:
            board[y][x] = num
            remove_num(y, x, idx, num)
            dfs(level+1)
            if finished:
                break
            rows[y].add(num)
            cols[x].add(num)
            squares[idx].add(num)

    board = []
    finished = False
    empty_position, temp = deque(), []
    total = set(map(str, range(1, 10)))
    rows = [set(total) for _ in range(9)]
    cols = [set(total) for _ in range(9)]
    squares = [set(total) for _ in range(9)]

    for i in range(9):
        row = input().split()
        for j in range(9):
            num = row[j]
            k = square_idx(i, j)
            if num != '0':
                remove_num(i, j, k, num)
            else:
                empty_position.append((i, j, k, 0))
        board.append(row)

    bfs()
    N = len(temp)
    dfs(0)



    return '\n'.join([' '.join(board[i]) for i in range(9)])

print(main())





# 35052 KB / 2800 ms
def main():
    from collections import deque

    def square_idx(y, x):
        idx = 0
        if y >= 6:
            idx += 6
        elif y >= 3:
            idx += 3

        if x >= 6:
            idx += 2
        elif x >= 3:
            idx += 1

        return idx

    def remove_num(y, x, idx, num):
        rows[y].remove(num)
        cols[x].remove(num)
        squares[idx].remove(num)

    def bfs():
        while empty_position:
            y, x, idx, visited = empty_position.popleft()
            remain = rows[y] & cols[x] & squares[idx]
            if len(remain) == 1:
                num = remain.pop()
                remove_num(y, x, idx, num)
                board[y][x] = num
            elif visited <= 1:
                empty_position.append((y, x, idx, visited+1))
            else:
                temp.append((y, x, idx))


    def dfs(level):
        nonlocal finished

        if finished:
            return
        if level == N:
            finished = True
            return

        y, x, idx = temp[level]
        remain = rows[y] & cols[x] & squares[idx]
        for num in remain:
            board[y][x] = num
            remove_num(y, x, idx, num)
            dfs(level+1)
            if finished:
                break
            rows[y].add(num)
            cols[x].add(num)
            squares[idx].add(num)

    board = []
    finished = False
    empty_position, temp = deque(), []
    total = set(map(str, range(1, 10)))
    rows = [set(total) for _ in range(9)]
    cols = [set(total) for _ in range(9)]
    squares = [set(total) for _ in range(9)]

    for i in range(9):
        row = input().split()
        for j in range(9):
            num = row[j]
            k = square_idx(i, j)
            if num != '0':
                remove_num(i, j, k, num)
            else:
                empty_position.append((i, j, k, 0))
        board.append(row)

    bfs()
    N = len(temp)
    dfs(0)



    return '\n'.join([' '.join(board[i]) for i in range(9)])

print(main())



# 35052 KB / 2144 ms
def main():
    from collections import deque

    def square_idx(y, x):
        idx = 0
        if y >= 6:
            idx += 6
        elif y >= 3:
            idx += 3

        if x >= 6:
            idx += 2
        elif x >= 3:
            idx += 1

        return idx

    def remove_num(y, x, idx, num):
        rows[y].remove(num)
        cols[x].remove(num)
        squares[idx].remove(num)

    def bfs():
        while empty_position:
            y, x, idx, visited = empty_position.popleft()
            remain = rows[y] & cols[x] & squares[idx]
            if len(remain) == 1:
                num = remain.pop()
                remove_num(y, x, idx, num)
                board[y][x] = num
            elif visited <= 8:
                empty_position.append((y, x, idx, visited+1))
            else:
                temp.append((y, x, idx))


    def dfs(level):
        nonlocal finished

        if finished:
            return
        if level == N:
            finished = True
            return

        y, x, idx = temp[level]
        remain = rows[y] & cols[x] & squares[idx]
        for num in remain:
            board[y][x] = num
            remove_num(y, x, idx, num)
            dfs(level+1)
            if finished:
                break
            rows[y].add(num)
            cols[x].add(num)
            squares[idx].add(num)

    board = []
    finished = False
    empty_position, temp = deque(), []
    total = set(map(str, range(1, 10)))
    rows = [set(total) for _ in range(9)]
    cols = [set(total) for _ in range(9)]
    squares = [set(total) for _ in range(9)]

    for i in range(9):
        row = input().split()
        for j in range(9):
            num = row[j]
            k = square_idx(i, j)
            if num != '0':
                remove_num(i, j, k, num)
            else:
                empty_position.append((i, j, k, 0))
        board.append(row)

    bfs()
    N = len(temp)
    dfs(0)

    return '\n'.join([' '.join(board[i]) for i in range(9)])

print(main())




# 35068 KB / 3388 ms
def main():
    from collections import deque

    def init():
        for i in range(9):
            row = input().split()
            for j in range(9):
                num = row[j]
                k = (i // 3) * 3 + j // 3
                if num != '0':
                    remove_num(i, j, k, num)
                else:
                    empty_position.append((i, j, k, 0))

    def remove_num(y, x, idx, num):
        rows[y].remove(num)
        cols[x].remove(num)
        squares[idx].remove(num)
        board[y][x] = num

    def bfs():
        while empty_position:
            y, x, idx, visited = empty_position.popleft()
            remain = rows[y] & cols[x] & squares[idx]
            if len(remain) == 1:
                num = remain.pop()
                remove_num(y, x, idx, num)
            elif visited <= 8:
                empty_position.append((y, x, idx, visited+1))
            else:
                temp.append((y, x, idx))


    def dfs(level):
        nonlocal finished

        if finished:
            return
        if level == N:
            finished = True
            return

        y, x, idx = temp[level]
        remain = rows[y] & cols[x] & squares[idx]
        for num in remain:
            remove_num(y, x, idx, num)
            dfs(level+1)
            if finished:
                break
            rows[y].add(num)
            cols[x].add(num)
            squares[idx].add(num)

    board = [['0'] * 9 for _ in range(9)]
    finished = False
    empty_position, temp = deque(), []
    total = set(map(str, range(1, 10)))
    rows = [set(total) for _ in range(9)]
    cols = [set(total) for _ in range(9)]
    squares = [set(total) for _ in range(9)]

    init()
    bfs()
    N = len(temp)
    dfs(0)

    return '\n'.join([' '.join(board[i]) for i in range(9)])

print(main())



# 32412 KB / 4356 ms
def main():
    def init():
        for i in range(9):
            row = input().split()
            for j in range(9):
                num = row[j]
                k = (i // 3) * 3 + j // 3
                if num != '0':
                    remove_num(i, j, k, num)
                else:
                    empty_position.append((i, j, k))

    def remove_num(y, x, idx, num):
        rows[y].remove(num)
        cols[x].remove(num)
        squares[idx].remove(num)
        board[y][x] = num


    def dfs(level):
        nonlocal finished

        if finished:
            return
        if level == N:
            finished = True
            return

        y, x, idx = empty_position[level]
        remain = rows[y] & cols[x] & squares[idx]
        for num in remain:
            remove_num(y, x, idx, num)
            dfs(level+1)
            if finished:
                break
            rows[y].add(num)
            cols[x].add(num)
            squares[idx].add(num)

    board = [['0'] * 9 for _ in range(9)]
    finished = False
    empty_position = []
    total = set(map(str, range(1, 10)))
    rows = [set(total) for _ in range(9)]
    cols = [set(total) for _ in range(9)]
    squares = [set(total) for _ in range(9)]

    init()
    N = len(empty_position)
    dfs(0)

    return '\n'.join([' '.join(board[i]) for i in range(9)])

print(main())