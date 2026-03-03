# 240724
# 260303
# 37660 KB / 6908 ms
def main():
    from sys import stdin

    def minus_one(num):
        return int(num) - 1

    new_input = stdin.readline
    V, E = map(int, new_input().split())
    limit = int(2e9)
    info = [[limit] * V for _ in range(V)]
    min_total = limit
    for _ in range(E):
        a, b, c = map(minus_one, new_input().split())
        info[a][b] = c+1

    for k in range(V):
        for i in range(V):
            if i != k:
                for j in range(V):
                    if j != k:
                        via = info[i][k] + info[k][j]
                        if via < info[i][j]:
                            info[i][j] = via


    for i in range(V):
        total = info[i][i]
        if total < min_total:
            min_total = total


    return min_total if min_total != limit else -1

print(main())






# 37660 KB / 6672 ms
def main():
    from sys import stdin

    def int_input():
        return map(int, stdin.readline().split())

    V, E = int_input()
    limit = int(2e9)
    info = [[limit] * V for _ in range(V)]
    min_total = limit
    for _ in range(E):
        a, b, c = int_input()
        info[a-1][b-1] = c

    for k in range(V):
        for i in range(V):
            if i != k:
                for j in range(V):
                    if j != k:
                        via = info[i][k] + info[k][j]
                        if via < info[i][j]:
                            info[i][j] = via


    for i in range(V):
        total = info[i][i]
        if total < min_total:
            min_total = total


    return min_total if min_total != limit else -1

print(main())






# 37660 KB / 7100 ms
def main():
    from sys import stdin

    def int_input():
        return map(int, stdin.readline().split())

    V, E = int_input()
    limit = int(8e6)
    info = [[limit] * V for _ in range(V)]
    min_total = limit
    for _ in range(E):
        a, b, c = int_input()
        info[a-1][b-1] = c

    for k in range(V):
        for i in range(V):
            if i != k:
                for j in range(V):
                    if j != k:
                        via = info[i][k] + info[k][j]
                        if via < info[i][j]:
                            info[i][j] = via


    for i in range(V):
        total = info[i][i]
        if total < min_total:
            min_total = total


    return min_total if min_total != limit else -1

print(main())





# 37660 KB / 6452 ms
def main():
    from sys import stdin

    def int_input():
        return map(int, stdin.readline().split())

    V, E = int_input()
    limit = int(2e9)
    info = [[limit] * V for _ in range(V)]
    min_total = limit
    for _ in range(E):
        a, b, c = int_input()
        info[a-1][b-1] = c

    for k in range(V):
        for i in range(V):
            for j in range(V):
                via = info[i][k] + info[k][j]
                if via < info[i][j]:
                    info[i][j] = via


    for i in range(V):
        total = info[i][i]
        if total < min_total:
            min_total = total


    return min_total if min_total != limit else -1

print(main())







# 37660 KB / 7084 ms
def main():
    from sys import stdin

    def int_input():
        return map(int, stdin.readline().split())

    V, E = int_input()
    limit = int(1e9)
    info = [[limit] * V for _ in range(V)]

    for _ in range(E):
        a, b, c = int_input()
        info[a-1][b-1] = c

    for k in range(V):
        for i in range(V):
            for j in range(V):
                via = info[i][k] + info[k][j]
                if via < info[i][j]:
                    info[i][j] = via


    min_total = min([info[i][i] for i in range(V)])

    return min_total if min_total != limit else -1

print(main())






# 37660 KB / 6140 ms
def main():
    from sys import stdin

    def int_input():
        return map(int, stdin.readline().split())

    V, E = int_input()
    limit = int(2e9)
    info = [[limit] * (V+1) for _ in range(V+1)]
    min_total = limit
    for _ in range(E):
        a, b, c = int_input()
        info[a][b] = c

    for k in range(1, V+1):
        for i in range(1, V+1):
            for j in range(1, V+1):
                via = info[i][k] + info[k][j]
                if via < info[i][j]:
                    info[i][j] = via


    for i in range(1, V+1):
        total = info[i][i]
        if total < min_total:
            min_total = total


    return min_total if min_total != limit else -1

print(main())







# 37660 KB / 6254 ms
def main():
    from sys import stdin

    def int_input():
        return map(int, stdin.readline().split())

    V, E = int_input()
    limit = int(E*10000) + 1

    info = [[limit] * (V+1) for _ in range(V+1)]
    min_total = limit
    for _ in range(E):
        a, b, c = int_input()
        info[a][b] = c

    for k in range(1, V+1):
        for i in range(1, V+1):
            for j in range(1, V+1):
                via = info[i][k] + info[k][j]
                if via < info[i][j]:
                    info[i][j] = via


    for i in range(1, V+1):
        total = info[i][i]
        if total < min_total:
            min_total = total


    return min_total if min_total != limit else -1

print(main())






# 37660 KB / 6328 ms
def main():
    from sys import stdin

    def int_input():
        return map(int, stdin.readline().split())

    V, E = int_input()
    limit = min_total = int(2e9)
    info = [[limit] * (V+1) for _ in range(V+1)]

    for _ in range(E):
        a, b, c = int_input()
        info[a][b] = c

    for k in range(1, V+1):
        for i in range(1, V+1):
            for j in range(1, V+1):
                via = info[i][k] + info[k][j]
                if via < info[i][j]:
                    info[i][j] = via


    for i in range(1, V+1):
        total = info[i][i]
        if total < min_total:
            min_total = total


    return min_total if min_total != limit else -1

print(main())






# 37660 KB / 6364 ms
def main():
    from sys import stdin

    def int_input():
        return map(int, stdin.readline().split())

    V, E = int_input()
    limit = min_total = int(1.6e9)
    info = [[limit] * (V+1) for _ in range(V+1)]

    for _ in range(E):
        a, b, c = int_input()
        info[a][b] = c

    for k in range(1, V+1):
        for i in range(1, V+1):
            for j in range(1, V+1):
                via = info[i][k] + info[k][j]
                if via < info[i][j]:
                    info[i][j] = via


    for i in range(1, V+1):
        total = info[i][i]
        if total < min_total:
            min_total = total


    return min_total if min_total != limit else -1

print(main())










# 37660 KB / 6396 ms
def main():
    from sys import stdin

    new_input = stdin.readline

    V, E = map(int, new_input().split())
    limit = int(2e9)
    info = [[limit] * (V+1) for _ in range(V+1)]
    min_total = limit
    for _ in range(E):
        a, b, c = map(int, new_input().split())
        info[a][b] = c

    for k in range(1, V+1):
        for i in range(1, V+1):
            for j in range(1, V+1):
                via = info[i][k] + info[k][j]
                if via < info[i][j]:
                    info[i][j] = via


    for i in range(1, V+1):
        total = info[i][i]
        if total < min_total:
            min_total = total


    return min_total if min_total != limit else -1

print(main())






# 37660 KB / 7440 ms
def main():
    from sys import stdin

    def int_input():
        return map(int, stdin.readline().split())

    def fill_info():
        for _ in range(E):
            a, b, c = int_input()
            info[a][b] = c

    def floyd_warshall():
        for k in range(1, V + 1):
            for i in range(1, V + 1):
                for j in range(1, V + 1):
                    via = info[i][k] + info[k][j]
                    if via < info[i][j]:
                        info[i][j] = via

    def find_min_total():
        min_total = limit

        for i in range(1, V + 1):
            total = info[i][i]
            if total < min_total:
                min_total = total

        return min_total if min_total != limit else -1



    V, E = int_input()
    limit = int(2e9)
    info = [[limit] * (V+1) for _ in range(V+1)]

    fill_info()
    floyd_warshall()

    return find_min_total()

print(main())






# 37660 KB / 5284 ms
def main():
    from sys import stdin

    def int_input():
        return map(int, stdin.readline().split())

    def fill_info():
        for _ in range(E):
            a, b, c = int_input()
            info[a][b] = c

    def floyd_warshall():
        for k in range(1, V + 1):
            row = info[k]
            for i in range(1, V + 1):
                each = info[i][k]
                for j in range(1, V + 1):
                    via = each + row[j]
                    if via < info[i][j]:
                        info[i][j] = via

    def find_min_total():
        min_total = limit

        for i in range(1, V + 1):
            total = info[i][i]
            if total < min_total:
                min_total = total

        return min_total if min_total != limit else -1



    V, E = int_input()
    limit = int(2e9)
    info = [[limit] * (V+1) for _ in range(V+1)]

    fill_info()
    floyd_warshall()

    return find_min_total()

print(main())





