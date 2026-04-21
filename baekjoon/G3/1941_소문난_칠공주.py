# 260420
# 294556 KB / 352 ms
def main():
    students = [input() for _ in range(5)]
    di, dj = (-1, 1, 0, 0), (0, 0, -1, 1)
    cnt = 0
    path = []
    case = [False] * (1 << 25)

    def backtracking(level, y_cnt, visited):
        nonlocal cnt
        if case[visited]:
            return

        if y_cnt >= 4:
            return

        if level == 7:
            if not case[visited]:
                case[visited] = True
                cnt += 1
            return

        case[visited] = True

        for i, j in path:
            for k in range(4):
                ni, nj = i+di[k], j+dj[k]
                if 0 <= ni < 5 and 0 <= nj < 5:
                    now = 1 << (ni * 5 + nj)
                    if visited & now == 0:
                        path.append((ni, nj))
                        new_y_cnt = y_cnt
                        if students[ni][nj] == 'Y':
                            new_y_cnt += 1

                        backtracking(level+1, new_y_cnt, visited + now)
                        path.pop()

    for y in range(5):
        for x in range(5):
            path.append((y, x))
            backtracking(1, 1 if students[y][x] == 'Y' else 0, 1 << (y * 5 + x))
            path.pop()

    return cnt

print(main())