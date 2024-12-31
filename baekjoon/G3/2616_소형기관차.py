# 241231
# 40448 KB / 96 ms
def main():
    N = int(input())
    customers = list(map(int, input().split()))
    limit = int(input())
    acc = [0] * (N+1)
    max_checked = [[0] * 3 for _ in range(N+1)]

    for i in range(N):
        acc[i+1] = acc[i] + customers[i]


    for i in range(limit, N-1):
        max_checked[i][0] = max(acc[i] - acc[i-limit], max_checked[i-1][0])

    for j in range(1, 3):
        for i in range(limit+j, N-1+j):
            max_checked[i][j] = max(acc[i] - acc[i-limit] + max_checked[i-limit][j-1], max_checked[i-1][j])

    return max_checked[-1][-1]

print(main())



# 40448 KB / 84 ms
def main():
    N = int(input())
    customers = list(map(int, input().split()))
    limit = int(input())
    prefix_sum = [0] * (N+1)
    max_checked = [[0] * 3 for _ in range(N+1)]

    for i in range(limit):
        prefix_sum[limit] += customers[i]

    for i in range(limit, N):
        prefix_sum[i+1] = prefix_sum[i] + customers[i] - customers[i-limit]

    for i in range(limit, N-1):
        max_checked[i][0] = max(prefix_sum[i], max_checked[i-1][0])

    for j in range(1, 3):
        for i in range(limit+j, N-1+j):
            max_checked[i][j] = max(prefix_sum[i] + max_checked[i-limit][j-1], max_checked[i-1][j])

    return max_checked[-1][-1]

print(main())


# 39424 KB / 88 ms
def main():
    N = int(input())
    customers = list(map(int, input().split()))
    limit = int(input())
    prefix_sum = [0] * (N+1-limit)
    max_checked = [[0] * 3 for _ in range(N+1-limit)]

    for i in range(limit):
        prefix_sum[0] += customers[i]

    for i in range(limit, N):
        prefix_sum[i-limit+1] = prefix_sum[i-limit] + customers[i] - customers[i-limit]

    for i in range(N-1-limit):
        max_checked[i][0] = max(prefix_sum[i], max_checked[i-1][0])

    for j in range(1, 3):
        for i in range(limit*j, N-1+j-limit):
            max_checked[i][j] = max(prefix_sum[i] + max_checked[i-limit][j-1], max_checked[i-1][j])

    return max_checked[-1][-1]

print(main())