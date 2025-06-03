# 250310
# 33432 KB / 40 ms
def main():
    from sys import stdin

    new_input = stdin.readline
    N = int(new_input())
    arr = [list(map(int, new_input().split())) for _ in range(N)]
    remain = [set(range(3)) - {i} for i in range(3)]
    min_total = int(1e6)

    for j in range(3):
        total_value = [[1001] * 3 for _ in range(N)]
        total_value[0][j] = arr[0][j]
        for i in range(1, N):
            for k in range(3):
                total_value[i][k] = min(total_value[i-1][l] for l in remain[k]) + arr[i][k]
        for i in remain[j]:
            if min_total > total_value[-1][i]:
                min_total = total_value[-1][i]


    return min_total

print(main())




# 33432 KB / 40 ms
def main():
    from sys import stdin

    new_input = stdin.readline
    N = int(new_input())
    arr = [list(map(int, new_input().split())) for _ in range(N)]
    remain = [set(range(3)) - {i} for i in range(3)]
    min_total = int(1e6)

    for j in range(3):
        total_value = [[1001] * 3 for _ in range(N)]
        total_value[0][j] = arr[0][j]
        for i in range(1, N):
            for k in range(3):
                total_value[i][k] = min(total_value[i-1][l] for l in remain[k]) + arr[i][k]

        min_total = min(min_total, *[total_value[-1][i] for i in remain[j]])


    return min_total

print(main())