# 260324
# 59776 KB / 116 ms
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    conditions = [list(map(int, input().split())) for _ in range(N)]
    answer = 0


    def dfs(level, num):
        global answer
        if level == N:
            answer = num
            return

        if level == 0:
            b, n = conditions[0]
            new_num = b
            while True:
                dfs(1, new_num)
                if answer != 0:
                    return
                new_num += n

        b, n = conditions[level]
        if num % n == b:
            dfs(level + 1, num)


    dfs(0, 0)

    print(f'#{test_case} {answer}')


# 59904 KB / 119 ms
def dfs(level, num):
    global answer
    if level == N:
        answer = num
        return

    if level == 0:
        b, n = conditions[0]
        new_num = b
        while True:
            dfs(1, new_num)
            if answer != 0:
                return
            new_num += n

    b, n = conditions[level]
    if num % n == b:
        dfs(level + 1, num)



T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    conditions = [list(map(int, input().split())) for _ in range(N)]
    answer = 0

    dfs(0, 0)

    print(f'#{test_case} {answer}')





# 59904 KB / 124 ms
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    conditions = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    num = conditions[0][0]

    while True:
        for i in range(1, N):
            b, n = conditions[i]
            if num % n != b:
                break
        else:
            print(f'#{test_case} {num}')
            break

        num += conditions[0][1]





# 59904 KB / 124 ms
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    conditions = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    num, step = conditions[0]

    while True:
        for i in range(1, N):
            b, n = conditions[i]
            if num % n != b:
                break
        else:
            print(f'#{test_case} {num}')
            break

        num += step