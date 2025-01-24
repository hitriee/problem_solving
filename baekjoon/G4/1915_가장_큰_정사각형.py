# 230808
# 250124
# 57636 KB / 624 ms
def main():
    from sys import stdin

    new_input = stdin.readline
    n, m = map(int, new_input().split())
    arr = [new_input().rstrip() for _ in range(n)]
    max_wide = [[0] * m for _ in range(n)]
    dy, dx = (-1, -1, 0), (-1, 0, -1)
    max_area = 0

    max_wide[0] = list(map(int, arr[0]))

    for y in range(1, n):
        max_wide[y][0] = int(arr[y][0])
        for x in range(1, m):
            if arr[y][x] == '1':
                max_wide[y][x] = min([int(max_wide[y+dy[i]][x+dx[i]]) for i in range(3)]) + 1

    for y in range(n):
        for x in range(m):
            area = max_wide[y][x] ** 2
            if area > max_area:
                max_area = area

    return max_area

print(main())



# 57664 KB / 580 ms
def main():
    from sys import stdin

    new_input = stdin.readline
    n, m = map(int, new_input().split())
    arr = [new_input().rstrip() for _ in range(n)]
    wide = [[0] * m for _ in range(n)]
    dy, dx = (-1, -1, 0), (-1, 0, -1)

    wide[0] = list(map(int, arr[0]))
    max_wide = 0

    for y in range(1, n):
        wide[y][0] = int(arr[y][0])
        for x in range(1, m):
            if arr[y][x] == '1':
                now = min([int(wide[y+dy[i]][x+dx[i]]) for i in range(3)]) + 1
                wide[y][x] = now
                if now > max_wide:
                    max_wide = now

    if max_wide == 0:
        for i in range(n):
            if wide[i][0] == 1:
                return 1

        for j in range(1, m):
            if wide[0][j] == 1:
                return 1

    return max_wide * max_wide

print(main())