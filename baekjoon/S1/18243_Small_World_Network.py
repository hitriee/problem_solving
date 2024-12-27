# 241227
# 32412 KB / 64 ms
def main():
    from sys import stdin

    def int_input():
        return map(int, stdin.readline().split())

    N, K = int_input()
    relations = [[7] * (N+1) for _ in range(N+1)]

    for _ in range(K):
        a, b = int_input()
        relations[a][b] = relations[b][a] = 1

    for k in range(1, N+1):
        for i in range(1, N):
            for j in range(i+1, N+1):
                new_relation = relations[i][k] + relations[k][j]
                if new_relation < relations[i][j]:
                    relations[i][j] = relations[j][i] = new_relation

    for i in range(1, N):
        for j in range(i+1, N+1):
            if relations[i][j] == 7:
                return 'Big World!'
    return 'Small World!'

print(main())



# 323412 KB / 68 ms
def main():
    from sys import stdin

    def minus_one(num):
        return int(num)-1

    def int_input(func=int):
        return map(func, stdin.readline().split())

    N, K = int_input()
    relations = [[7] * N for _ in range(N)]

    for _ in range(K):
        a, b = int_input(minus_one)
        relations[a][b] = relations[b][a] = 1

    for k in range(N):
        for i in range(N-1):
            for j in range(i+1, N):
                new_relation = relations[i][k] + relations[k][j]
                if new_relation < relations[i][j]:
                    relations[i][j] = relations[j][i] = new_relation

    for i in range(N-1):
        for j in range(i+1, N):
            if relations[i][j] == 7:
                return 'Big World!'
    return 'Small World!'

print(main())