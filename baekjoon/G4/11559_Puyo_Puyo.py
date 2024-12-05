# 241204
# 31120 KB / 32 ms
def main():
    field = [list(input()) for _ in range(12)]
    seq_cnt = 0 # 연쇄 수
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

    def find_seq_puyo():
        visited = [[False] * 6 for _ in range(12)]
        for i in range(12):
            for j in range(6):
                if not visited[i][j] and field[i][j] != '.':
                    temp = [(i, j, field[i][j])]
                    visited[i][j] = True
                    idx = 0
                    while idx < len(temp):
                        y, x, color = temp[idx]
                        idx += 1
                        for ni in range(4):
                            ny, nx = y + dy[ni], x + dx[ni]
                            if 0 <= ny < 12 and 0 <= nx < 6:
                                if not visited[ny][nx] and field[ny][nx] == color:
                                    visited[ny][nx] = True
                                    temp.append((ny, nx, color))

                    if len(temp) >= 4:
                        changed.extend(temp)

    def remove_seq_puyo():
        for y, x, _ in changed:
            field[y][x] = '.'

    def apply_gravity():
        new_field = [['.'] * 6 for _ in range(12)]
        for j in range(6):
            row = 11
            for i in range(11, -1, -1):
                if field[i][j] != '.':
                    new_field[row][j] = field[i][j]
                    row -= 1

            for i in range(11, -1, -1):
                field[i][j] = new_field[i][j]

    while True:
        # 연속된 뿌요 찾기
        changed = []
        find_seq_puyo()

        if not changed:
            return seq_cnt

        seq_cnt += 1

        # 연속된 뿌요 없애기
        remove_seq_puyo()

        # 뿌요 아래로 내리기
        apply_gravity()

print(main())



# 31120 KB / 32 ms
def main():
    field = [list(input()) for _ in range(12)]
    seq_cnt = 0 # 연쇄 수
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

    def remove_seq_puyo(arr):
        for y, x, _ in arr:
            field[y][x] = '.'

    def find_seq_puyo():
        nonlocal changed
        visited = [[False] * 6 for _ in range(12)]
        for i in range(12):
            for j in range(6):
                if not visited[i][j] and field[i][j] != '.':
                    temp = [(i, j, field[i][j])]
                    visited[i][j] = True
                    idx = 0
                    while idx < len(temp):
                        y, x, color = temp[idx]
                        idx += 1
                        for ni in range(4):
                            ny, nx = y + dy[ni], x + dx[ni]
                            if 0 <= ny < 12 and 0 <= nx < 6:
                                if not visited[ny][nx] and field[ny][nx] == color:
                                    visited[ny][nx] = True
                                    temp.append((ny, nx, color))

                    if len(temp) >= 4:
                        changed = True
                        # 연속된 뿌요 없애기
                        remove_seq_puyo(temp)


    def apply_gravity():
        new_field = [['.'] * 6 for _ in range(12)]
        for j in range(6):
            row = 11
            for i in range(11, -1, -1):
                if field[i][j] != '.':
                    new_field[row][j] = field[i][j]
                    row -= 1

            for i in range(11, -1, -1):
                field[i][j] = new_field[i][j]

    while True:
        # 연속된 뿌요 찾기
        changed = False
        find_seq_puyo()

        if not changed:
            return seq_cnt

        seq_cnt += 1

        # 뿌요 아래로 내리기
        apply_gravity()

print(main())
