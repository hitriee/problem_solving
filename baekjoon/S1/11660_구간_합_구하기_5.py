# 260303
# 106328 KB / 688 ms
def main():
    from sys import stdin

    new_input = stdin.readline
    N, M = map(int, new_input().split())
    arr = [[0] * (N+1)]
    for _ in range(N):
        arr.append([0] + list(map(int, new_input().split())))

    acc = [arr[i][:] for i in range(N+1)]

    for i in range(1, N+1):
        acc[i][1] += acc[i-1][1]
        acc[1][i] += acc[1][i-1]

    for i in range(2, N+1):
        for j in range(2, N+1):
            acc[i][j] += acc[i][j-1] + acc[i-1][j] - acc[i-1][j-1]

    for _ in range(M):
        y1, x1, y2, x2 = map(int, new_input().split())
        total = acc[y2][x2] - acc[y2][x1-1] - acc[y1-1][x2] + acc[y1-1][x1-1]
        print(total)

main()







# 73484 KB / 660 ms
def main():
    from sys import stdin

    new_input = stdin.readline
    N, M = map(int, new_input().split())
    acc = [[0] * (N+1)]
    for _ in range(N):
        acc.append([0] + list(map(int, new_input().split())))

    for i in range(1, N+1):
        acc[i][1] += acc[i-1][1]
        acc[1][i] += acc[1][i-1]

    for i in range(2, N+1):
        for j in range(2, N+1):
            acc[i][j] += acc[i][j-1] + acc[i-1][j] - acc[i-1][j-1]

    for _ in range(M):
        y1, x1, y2, x2 = map(int, new_input().split())
        total = acc[y2][x2] - acc[y2][x1-1] - acc[y1-1][x2] + acc[y1-1][x1-1]
        print(total)

main()






# 73484 KB / 660 ms
def main():
    from sys import stdin

    new_input = stdin.readline
    N, M = map(int, new_input().split())
    acc = [[0] * (N+1)]
    for _ in range(N):
        acc.append([0] + list(map(int, new_input().split())))

    for i in range(1, N+1):
        for j in range(1, N+1):
            acc[i][j] += acc[i][j-1] + acc[i-1][j] - acc[i-1][j-1]

    for _ in range(M):
        y1, x1, y2, x2 = map(int, new_input().split())
        total = acc[y2][x2] - acc[y2][x1-1] - acc[y1-1][x2] + acc[y1-1][x1-1]
        print(total)

main()




# 73484 KB / 644 ms
def main():
    from sys import stdin

    new_input = stdin.readline
    N, M = map(int, new_input().split())
    acc = [[0] * (N+1) for _ in range(N+1)]
    for i in range(1, N+1):
        acc[i][1:] = list(map(int, new_input().split()))

    for i in range(1, N+1):
        for j in range(1, N+1):
            acc[i][j] += acc[i][j-1] + acc[i-1][j] - acc[i-1][j-1]

    for _ in range(M):
        y1, x1, y2, x2 = map(int, new_input().split())
        total = acc[y2][x2] - acc[y2][x1-1] - acc[y1-1][x2] + acc[y1-1][x1-1]
        print(total)

main()







# 81316 KB / 616 ms
def main():
    from sys import stdin

    new_input = stdin.readline
    N, M = map(int, new_input().split())
    acc = [[0] * (N+1) for _ in range(N+1)]
    for i in range(1, N+1):
        acc[i][1:] = list(map(int, new_input().split()))

    for i in range(1, N+1):
        for j in range(1, N+1):
            acc[i][j] += acc[i][j-1] + acc[i-1][j] - acc[i-1][j-1]

    total_arr = []
    for _ in range(M):
        y1, x1, y2, x2 = map(int, new_input().split())
        total = acc[y2][x2] - acc[y2][x1-1] - acc[y1-1][x2] + acc[y1-1][x1-1]
        total_arr.append(str(total))

    return '\n'.join(total_arr)

print(main())