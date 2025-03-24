# 250324
# 32412 KB / 140 ms
def main():
    from sys import stdin

    def minus_one(num):
        return int(num)-1

    def int_input(option=0):
        return map(int if option == 0 else minus_one, stdin.readline().split())

    N, M = int_input()
    num1, num2, min_total = 0, 0, N*N
    road_info = [[N] * N for _ in range(N)]
    for _ in range(M):
        a, b = int_input(1)
        road_info[a][b] = road_info[b][a] = 1

    for k in range(N):
        for i in range(N-1):
            for j in range(i+1, N):
                road_info[i][j] = road_info[j][i] = min(road_info[i][j], road_info[i][k] + road_info[k][j])

    for i in range(N-1):
        for j in range(i+1, N):
            total = 0
            for k in range(N):
                if i != k and j != k:
                    total += min(road_info[i][k], road_info[j][k])

            if min_total > total:
                num1, num2, min_total = i+1, j+1, total

    return f'{num1} {num2} {2*min_total}'

print(main())



# 32412 KB / 136 ms
def main():
    from sys import stdin

    def minus_one(num):
        return int(num)-1

    def int_input(option=0):
        return map(int if option == 0 else minus_one, stdin.readline().split())

    N, M = int_input()
    num1, num2, min_total = 0, 0, N*N
    road_info = [[N] * N for _ in range(N)]
    for _ in range(M):
        a, b = int_input(1)
        road_info[a][b] = road_info[b][a] = 1

    for k in range(N):
        road_info[k][k] = 0
        for i in range(N-1):
            if i != k:
                for j in range(i+1, N):
                    if j != k:
                        road_info[i][j] = road_info[j][i] = min(road_info[i][j], road_info[i][k] + road_info[k][j])

    for i in range(N-1):
        for j in range(i+1, N):
            total = 0
            for k in range(N):
                total += min(road_info[i][k], road_info[j][k])

            if min_total > total:
                num1, num2, min_total = i+1, j+1, total

    return f'{num1} {num2} {2*min_total}'

print(main())






# 32412 KB / 132 ms
def main():
    from sys import stdin

    def minus_one(num):
        return int(num)-1

    def int_input(option=0):
        return map(int if option == 0 else minus_one, stdin.readline().split())

    N, M = int_input()
    num1, num2, min_total = 0, 0, N*N
    road_info = [[N] * N for _ in range(N)]
    for _ in range(M):
        a, b = int_input(1)
        road_info[a][b] = road_info[b][a] = 1

    for k in range(N):
        road_info[k][k] = 0
        for i in range(N-1):
            if i != k and road_info[i][k] != N:
                for j in range(i+1, N):
                    if j != k and road_info[k][j] != N:
                        road_info[i][j] = road_info[j][i] = min(road_info[i][j], road_info[i][k] + road_info[k][j])

    for i in range(N-1):
        for j in range(i+1, N):
            total = 0
            for k in range(N):
                total += min(road_info[i][k], road_info[j][k])

            if min_total > total:
                num1, num2, min_total = i+1, j+1, total

    return f'{num1} {num2} {2*min_total}'

print(main())