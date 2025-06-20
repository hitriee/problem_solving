# 250618
# 1189748 KB / 8864 ms (Pypy3)
def main():
    from sys import stdin

    new_input = stdin.readline
    N = int(new_input())
    arr_list = [[] for _ in range(4)]
    cnt = 0

    for _ in range(N):
        temp = list(map(int, new_input().split()))
        for i in range(4):
            arr_list[i].append(temp[i])

    total_cd = {}

    for i in range(N):
        for j in range(N):
            total = arr_list[2][i] + arr_list[3][j]
            total_cd[total] = total_cd.get(total, 0) + 1

    for i in range(N):
        for j in range(N):
            total = arr_list[0][i] + arr_list[1][j]
            cnt += total_cd.get(-total, 0)

    return cnt

print(main())