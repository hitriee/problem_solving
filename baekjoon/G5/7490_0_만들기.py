#230713
T = int(input())
for _ in range(T):
    N = int(input())
    path = [''] * (2*N-1)
    for j in range(1, N+1):
        path[2*j-2] = j

    def dfs(level):
        if level == N:
            num = i = 1
            while i < N:
                giho, other = path[2*i-1:2*i+1]
                if giho != ' ':
                    i += 1
                    while i < N and path[2*i-1] == ' ':
                        other = other*10+path[2*i]
                        i += 1
                    if giho == '+':
                        num += other
                    else:
                        num -= other
                else:
                    num = num * 10 + other
                    i += 1

            if num == 0:
                print(*path, sep='')
            return

        path[2*level-1] = ' '
        dfs(level+1)
        path[2*level-1] = '+'
        dfs(level+1)
        path[2*level-1] = '-'
        dfs(level+1)
        path[2*level-1] = ''


    dfs(1)
    print()


#
T = int(input())

def dfs(level):
    if level == N:
        num = i = 1
        while i < N:
            giho, other = path[2 * i - 1:2 * i + 1]
            if giho != ' ':
                i += 1
                while i < N and path[2 * i - 1] == ' ':
                    other = other * 10 + path[2 * i]
                    i += 1
                if giho == '+':
                    num += other
                else:
                    num -= other
            else:
                num = num * 10 + other
                i += 1

        if num == 0:
            print(*path, sep='')
        return

    for op in (' ', '+', '-'):
        path[2 * level - 1] = op
        dfs(level + 1)

for _ in range(T):
    N = int(input())
    path = [''] * (2*N-1)
    for j in range(1, N+1):
        path[2*j-2] = j

    dfs(1)
    print()


#
def print_cases():
    T = int(input())

    def dfs(level):
        if level == N:
            num = i = 1
            while i < N:
                giho, other = path[2 * i - 1:2 * i + 1]
                if giho != ' ':
                    i += 1
                    while i < N and path[2 * i - 1] == ' ':
                        other = other * 10 + path[2 * i]
                        i += 1
                    if giho == '+':
                        num += other
                    else:
                        num -= other
                else:
                    num = num * 10 + other
                    i += 1

            if num == 0:
                print(*path, sep='')
            return

        for op in (' ', '+', '-'):
            path[2 * level - 1] = op
            dfs(level + 1)

    for _ in range(T):
        N = int(input())
        path = [''] * (2*N-1)
        for j in range(1, N+1):
            path[2*j-2] = j

        dfs(1)
        print()

print_cases()


#
T = int(input())

def dfs(level):
    if level == N:
        num = i = 1
        while i < N:
            giho, other = path[2 * i - 1:2 * i + 1]
            if giho != ' ':
                i += 1
                while i < N and path[2 * i - 1] == ' ':
                    other = other * 10 + path[2 * i]
                    i += 1
                if giho == '+':
                    num += other
                else:
                    num -= other
            else:
                num = num * 10 + other
                i += 1

        if num == 0:
            print(*path, sep='')
        return

    for op in (' ', '+', '-'):
        path[2 * level - 1] = op
        dfs(level + 1)

for _ in range(T):
    N = int(input())
    path = [''] * (2*N-1)
    for j in range(1, N+1):
        path[2*j-2] = j

    dfs(1)
    print()
