# 251017
# 32696 KB / 2396 ms
def main():
    from sys import stdin

    new_input = stdin.readline
    N, K = map(int, new_input().split())
    arr = [[0] * (N+1) for _ in range(N+1)]

    for _ in range(K):
        case1, case2 = map(int, new_input().split())
        arr[case1][case2] = -1
        arr[case2][case1] = 1

    for k in range(1, N+1):
        for i in range(1, N):
            if i != k and arr[i][k]:
                for j in range(i+1, N+1):
                    if arr[i][k] == arr[k][j] != 0:
                        arr[i][j] = arr[i][k]
                        arr[j][i] = -arr[i][k]

    S = int(new_input())
    for _ in range(S):
        case1, case2 = map(int, new_input().split())
        print(arr[case1][case2])

main()



# 36152 KB / 2352 ms
def main():
    from sys import stdin

    new_input = stdin.readline
    N, K = map(int, new_input().split())
    arr = [[0] * (N+1) for _ in range(N+1)]

    for _ in range(K):
        case1, case2 = map(int, new_input().split())
        arr[case1][case2] = -1
        arr[case2][case1] = 1

    for k in range(1, N+1):
        for i in range(1, N):
            if i != k and arr[i][k]:
                for j in range(i+1, N+1):
                    if arr[i][k] == arr[k][j] != 0:
                        arr[i][j] = arr[i][k]
                        arr[j][i] = -arr[i][k]

    S = int(new_input())
    result = []
    for _ in range(S):
        case1, case2 = map(int, new_input().split())
        result.append(str(arr[case1][case2]))

    return '\n'.join(result)

print(main())



# 36144 KB / 2384 ms
def main():
    from sys import stdin

    new_input = stdin.readline
    N, K = map(int, new_input().split())
    arr = [[0] * N for _ in range(N)]

    def minus_one(num):
        return int(num) - 1

    for _ in range(K):
        case1, case2 = map(minus_one, new_input().split())
        arr[case1][case2] = -1
        arr[case2][case1] = 1

    for k in range(N):
        for i in range(N-1):
            if i != k and arr[i][k]:
                for j in range(i+1, N):
                    if arr[i][k] == arr[k][j] != 0:
                        arr[i][j] = arr[i][k]
                        arr[j][i] = -arr[i][k]

    S = int(new_input())
    result = []
    for _ in range(S):
        case1, case2 = map(minus_one, new_input().split())
        result.append(str(arr[case1][case2]))

    return '\n'.join(result)

print(main())



# 36152 KB / 2412 ms
def main():
    from sys import stdin

    new_input = stdin.readline
    N, K = map(int, new_input().split())
    arr = [[0] * (N+1) for _ in range(N+1)]

    for _ in range(K):
        case1, case2 = map(int, new_input().split())
        arr[case1][case2] = -1
        arr[case2][case1] = 1

    for k in range(1, N+1):
        for i in range(1, N):
            for j in range(i+1, N+1):
                if arr[i][k] == arr[k][j] != 0:
                    arr[i][j] = arr[i][k]
                    arr[j][i] = -arr[i][k]

    S = int(new_input())
    result = []
    for _ in range(S):
        case1, case2 = map(int, new_input().split())
        result.append(str(arr[case1][case2]))

    return '\n'.join(result)

print(main())




# 36152 KB / 2132 ms
def main():
    from sys import stdin

    new_input = stdin.readline
    N, K = map(int, new_input().split())
    arr = [[0] * (N+1) for i in range(N+1)]

    for _ in range(K):
        case1, case2 = map(int, new_input().split())
        arr[case1][case2] = -1
        arr[case2][case1] = 1

    for k in range(1, N+1):
        for i in range(1, N):
            if arr[i][k]:
                for j in range(i+1, N+1):
                    if arr[i][k] == arr[k][j]:
                        arr[i][j] = arr[i][k]
                        arr[j][i] = -arr[i][k]

    S = int(new_input())
    result = []
    for _ in range(S):
        case1, case2 = map(int, new_input().split())
        result.append(str(arr[case1][case2]))

    return '\n'.join(result)

print(main())





# 36152 KB / 2100 ms
def main():
    from sys import stdin

    new_input = stdin.readline
    N, K = map(int, new_input().split())
    arr = [[0] * (N+1) for _ in range(N+1)]

    for _ in range(K):
        case1, case2 = map(int, new_input().split())
        arr[case1][case2], arr[case2][case1] = -1, 1

    for k in range(1, N+1):
        for i in range(1, N):
            if arr[i][k]:
                for j in range(i+1, N+1):
                    if arr[i][k] == arr[k][j]:
                        arr[i][j], arr[j][i] = arr[i][k], -arr[i][k]

    S = int(new_input())
    result = []
    for _ in range(S):
        case1, case2 = map(int, new_input().split())
        result.append(str(arr[case1][case2]))

    return '\n'.join(result)

print(main())