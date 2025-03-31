# 250331
# 32544 KB / 1628 ms
def main():
    from sys import stdin

    def int_input():
        return map(int, stdin.readline().split())

    def can_stick(arr, dif_i, dif_j, r, c):
        nonlocal area

        temp = [area[i][:] for i in range(N)]
        for i in range(r):
            for j in range(c):
                if arr[i][j] == 0:
                    continue
                elif temp[dif_i+i][dif_j+j] == 0:
                    temp[dif_i + i][dif_j + j] = 1
                else:
                    return False

        for i in range(dif_i, dif_i + r):
            area[i] = temp[i][:]

        return True

    def stick(arr, r, c):
        for _ in range(4):
            for i in range(N-r+1):
                for j in range(M-c+1):
                    if can_stick(arr, i, j, r, c):
                        return

            result = rotate(arr, r, c)
            r, c = c, r
            arr = [result[i][:] for i in range(r)]

    def rotate(arr, r, c):
        result = [[0] * r for _ in range(c)]
        for i in range(r):
            for j in range(c):
                result[j][r-i-1] = arr[i][j]

        return result

    total_cnt = 0
    N, M, K = int_input()
    area = [[0] * M for _ in range(N)]
    for _ in range(K):
        R, C = int_input()
        sticker = [list(int_input()) for _ in range(R)]
        stick(sticker, R, C)

    for i in range(N):
        total_cnt += sum(area[i])

    return total_cnt

print(main())






# 32412 KB / 1664 ms
def main():
    from sys import stdin

    def int_input():
        return map(int, stdin.readline().split())

    def can_stick(arr, dif_i, dif_j, r, c):
        nonlocal area

        temp = [area[i][:] for i in range(N)]
        for i in range(r):
            for j in range(c):
                if arr[i][j] == '0':
                    continue
                elif not temp[dif_i+i][dif_j+j]:
                    temp[dif_i + i][dif_j + j] = True
                else:
                    return False

        for i in range(dif_i, dif_i + r):
            area[i] = temp[i][:]

        return True

    def stick(arr, r, c):
        for _ in range(4):
            for i in range(N-r+1):
                for j in range(M-c+1):
                    if can_stick(arr, i, j, r, c):
                        return

            result = rotate(arr, r, c)
            r, c = c, r
            arr = [result[i][:] for i in range(r)]

    def rotate(arr, r, c):
        result = [[0] * r for _ in range(c)]
        for i in range(r):
            for j in range(c):
                result[j][r-i-1] = arr[i][j]

        return result

    total_cnt = 0
    N, M, K = int_input()
    area = [[False] * M for _ in range(N)]
    for _ in range(K):
        R, C = int_input()
        sticker = [stdin.readline().split() for _ in range(R)]
        stick(sticker, R, C)

    for i in range(N):
        for j in range(M):
            if area[i][j]:
                total_cnt += 1

    return total_cnt

print(main())




# 32412 KB / 100 ms
def main():
    from sys import stdin

    def int_input():
        return map(int, stdin.readline().split())

    def can_stick(arr, dif_y, dif_x):
        nonlocal area

        temp = []
        for y, x in arr:
            if area[y+dif_y][x+dif_x] == 0:
                temp.append((y+dif_y, x+dif_x))
            else:
                return False

        for y, x in temp:
            area[y][x] = 1

        return True

    def stick(arr, r, c):
        for _ in range(4):
            for i in range(N-r+1):
                for j in range(M-c+1):
                    if can_stick(arr, i, j):
                        return


            arr = [(x, r-y-1) for y, x in arr]
            r, c = c, r

    total_cnt = 0
    N, M, K = int_input()
    area = [[0] * M for _ in range(N)]
    for _ in range(K):
        R, C = int_input()
        sticker = []
        for i in range(R):
            row = list(int_input())
            for j in range(C):
                if row[j] == 1:
                    sticker.append((i, j))

        stick(sticker, R, C)

    for i in range(N):
        total_cnt += sum(area[i])

    return total_cnt

print(main())




# 32412 KB / 100 ms
def main():
    from sys import stdin

    def int_input():
        return map(int, stdin.readline().split())

    def can_stick(arr, dif_y, dif_x):
        nonlocal total_cnt

        temp = []
        for y, x in arr:
            if area[y+dif_y][x+dif_x] == 0:
                temp.append((y+dif_y, x+dif_x))
            else:
                return False

        total_cnt += len(temp)
        for y, x in temp:
            area[y][x] = 1


        return True

    def stick(arr, r, c):
        for _ in range(4):
            for i in range(N-r+1):
                for j in range(M-c+1):
                    if can_stick(arr, i, j):
                        return


            arr = [(x, r-y-1) for y, x in arr]
            r, c = c, r

    total_cnt = 0
    N, M, K = int_input()
    area = [[0] * M for _ in range(N)]
    for _ in range(K):
        R, C = int_input()
        sticker = []
        for i in range(R):
            row = list(int_input())
            for j in range(C):
                if row[j] == 1:
                    sticker.append((i, j))

        stick(sticker, R, C)

    return total_cnt

print(main())





# 32412 KB / 96 ms
def main():
    from sys import stdin

    def int_input():
        return map(int, stdin.readline().split())

    def can_stick(arr, dif_y, dif_x):
        nonlocal total_cnt

        temp = []
        for y, x in arr:
            if area[y+dif_y][x+dif_x]:
                temp.append((y+dif_y, x+dif_x))
            else:
                return False

        total_cnt += len(temp)
        for y, x in temp:
            area[y][x] = False


        return True

    def stick(arr, r, c):
        for _ in range(4):
            for i in range(N-r+1):
                for j in range(M-c+1):
                    if can_stick(arr, i, j):
                        return


            arr = [(x, r-y-1) for y, x in arr]
            r, c = c, r

    total_cnt = 0
    N, M, K = int_input()
    area = [[True] * M for _ in range(N)]
    for _ in range(K):
        R, C = int_input()
        sticker = []
        for i in range(R):
            row = list(int_input())
            for j in range(C):
                if row[j] == 1:
                    sticker.append((i, j))

        stick(sticker, R, C)

    return total_cnt

print(main())