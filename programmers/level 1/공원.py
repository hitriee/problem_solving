# 260421
# 1.19 ms / 9.31 MB
def solution(mats, park):
    n, m = len(park), len(park[0])
    mats.sort(reverse=True)

    def alp_to_num(alp):
        return 0 if alp == '-1' else 1

    acc = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n):
        for j in range(m):
            acc[i + 1][j + 1] = acc[i][j + 1] + acc[i + 1][j] - acc[i][j] + alp_to_num(park[i][j])

    for width in mats:
        for i in range(width, n + 1):
            for j in range(width, m + 1):
                if acc[i][j] - acc[i - width][j] - acc[i][j - width] + acc[i - width][j - width] == 0:
                    return width

    return -1





# 1.22 ms / 9.37 MB
def solution(mats, park):
    n, m = len(park), len(park[0])
    mats.sort(reverse=True)

    def alp_to_num(alp):
        return 0 if alp == '-1' else 1

    def calc_new_acc(y, x, width):
        return acc[y][x - width] + acc[y - width][x] - acc[y - width][x - width]

    acc = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n):
        for j in range(m):
            acc[i + 1][j + 1] = calc_new_acc(i + 1, j + 1, 1) + alp_to_num(park[i][j])

    for width in mats:
        for i in range(width, n + 1):
            for j in range(width, m + 1):
                if acc[i][j] - calc_new_acc(i, j, width) == 0:
                    return width

    return -1