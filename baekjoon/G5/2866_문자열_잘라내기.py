# 260203
# 34500 KB / 588 ms
def main():
    from sys import stdin

    new_input = stdin.readline

    R, C = map(int, new_input().split())
    alp_arr = [new_input().rstrip() for _ in range(R)]
    str_arr = []

    for j in range(C):
        each_str = ''
        for i in range(R):
            each_str += alp_arr[i][j]
        str_arr.append(each_str)

    cnt = 0

    for i in range(1, R):
        str_set = set()
        for j in range(C):
            str_set.add(str_arr[j][i:])

        if len(str_set) < C:
            return cnt

        cnt += 1

    return R-1

print(main())






# 34356 KB / 704 ms
def main():
    from sys import stdin

    new_input = stdin.readline

    R, C = map(int, new_input().split())
    str_arr = ['' for _ in range(C)]

    for _ in range(R):
        row = new_input().rstrip()
        for j in range(C):
            str_arr[j] += row[j]

    cnt = 0

    for i in range(1, R):
        str_set = set()
        for j in range(C):
            str_set.add(str_arr[j][i:])

        if len(str_set) < C:
            return cnt

        cnt += 1

    return R-1

print(main())