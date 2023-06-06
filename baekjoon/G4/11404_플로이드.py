#230606
from sys import stdin
new_input = stdin.readline
N = int(new_input())
M = int(new_input())
limit = int(1e7) + 1
road = [[limit] * (N+1) for _ in range(N+1)]
for _ in range(M):
    start, end, cost = map(int, new_input().split())
    if road[start][end] > cost:
        road[start][end] = cost

for i in range(1, N+1):
    for j in range(1, N+1):
        if i != j:
            for k in range(1, N+1):
                if j != k and i != k:
                    new_cost = road[j][i] + road[i][k]
                    if road[j][k] > new_cost:
                        road[j][k] = new_cost

for i in range(1, N+1):
    for j in range(1, N):
        if road[i][j] == limit:
            print(0, end=' ')
        else:
            print(road[i][j], end=' ')
    if road[i][N] == limit:
        print(0)
    else:
        print(road[i][N])


#
def floyd():
    from sys import stdin
    new_input = stdin.readline
    N = int(new_input())
    M = int(new_input())
    limit = int(1e7) + 1
    road = [[limit] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        start, end, cost = map(int, new_input().split())
        if road[start][end] > cost:
            road[start][end] = cost

    for i in range(1, N+1): # 중간 지점
        for j in range(1, N+1): # 출발점
            if i != j:
                for k in range(1, N+1): # 도착점
                    if j != k and i != k:
                        new_cost = road[j][i] + road[i][k]
                        if road[j][k] > new_cost:
                            road[j][k] = new_cost

    for i in range(1, N+1):
        for j in range(1, N+1):
            if road[i][j] == limit:
                print(0, end=' ')
            else:
                print(road[i][j], end=' ')

        if road[i][N] == limit:
            print(0)
        else:
            print(road[i][N])

floyd()


#
def floyd():
    from sys import stdin
    new_input = stdin.readline

    N = int(new_input())
    M = int(new_input())
    limit = int(1e7) + 1
    road = [[limit] * (N + 1) for _ in range(N + 1)]

    for _ in range(M):
        start, end, cost = map(int, new_input().split())
        if road[start][end] > cost:
            road[start][end] = cost

    for i in range(1, N + 1):  # 중간 지점
        for j in range(1, N + 1):  # 출발점
            if i != j:
                for k in range(1, N + 1):  # 도착점
                    if j != k and i != k:
                        new_cost = road[j][i] + road[i][k]
                        if road[j][k] > new_cost:
                            road[j][k] = new_cost

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if road[i][j] == limit:
                print(0, end=' ')
            else:
                print(road[i][j], end=' ')
        print()


floyd()

#
def floyd():
    from sys import stdin
    new_input = stdin.readline

    N = int(new_input())
    M = int(new_input())
    road = [[0] * (N + 1) for _ in range(N + 1)]

    for _ in range(M):
        start, end, cost = map(int, new_input().split())
        if road[start][end] == 0 or road[start][end] > cost:
            road[start][end] = cost

    for i in range(1, N + 1):  # 중간 지점
        for j in range(1, N + 1):  # 출발점
            if i != j:
                for k in range(1, N + 1):  # 도착점
                    if j != k and i != k:
                        if road[j][i] != 0 and road[i][k] != 0:
                            new_cost = road[j][i] + road[i][k]
                            if road[j][k] == 0 or road[j][k] > new_cost:
                                road[j][k] = new_cost

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            print(road[i][j], end=' ')
        print()

floyd()


#
def floyd():
    from sys import stdin
    new_input = stdin.readline

    N = int(new_input())
    M = int(new_input())
    road = [[0] * (N + 1) for _ in range(N + 1)]

    for _ in range(M):
        start, end, cost = map(int, new_input().split())
        if road[start][end] == 0 or road[start][end] > cost:
            road[start][end] = cost

    for i in range(1, N + 1):  # 중간 지점
        for j in range(1, N + 1):  # 출발점
            if i != j:
                for k in range(1, N + 1):  # 도착점
                    if j != k and i != k:
                        if road[j][i] != 0 and road[i][k] != 0:
                            new_cost = road[j][i] + road[i][k]
                            if road[j][k] == 0 or road[j][k] > new_cost:
                                road[j][k] = new_cost

    for i in range(1, N + 1):
        print(*road[i][1:])

floyd()


#
def print_answer():
    from sys import stdin
    new_input = stdin.readline

    N = int(new_input())
    M = int(new_input())
    limit = int(1e7) + 1
    road = [[limit] * (N + 1) for _ in range(N + 1)]

    for _ in range(M):
        start, end, cost = map(int, new_input().split())
        if road[start][end] > cost:
            road[start][end] = cost

    def floyd():
        for i in range(1, N + 1):  # 중간 지점
            for j in range(1, N + 1):  # 출발점
                if i != j:
                    for k in range(1, N + 1):  # 도착점
                        if j != k and i != k:
                            new_cost = road[j][i] + road[i][k]
                            if road[j][k] > new_cost:
                                road[j][k] = new_cost

    floyd()

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if road[i][j] == limit:
                print(0, end=' ')
            else:
                print(road[i][j], end=' ')
        print()


print_answer()


#
def print_answer():
    from sys import stdin
    new_input = stdin.readline

    N = int(new_input())
    M = int(new_input())
    limit = int(1e7) + 1
    road = [[limit] * (N + 1) for _ in range(N + 1)]

    def fill_road():
        for _ in range(M):
            start, end, cost = map(int, new_input().split())
            if road[start][end] > cost:
                road[start][end] = cost

    def floyd():
        for i in range(1, N + 1):  # 중간 지점
            for j in range(1, N + 1):  # 출발점
                if i != j:
                    for k in range(1, N + 1):  # 도착점
                        if j != k and i != k:
                            new_cost = road[j][i] + road[i][k]
                            if road[j][k] > new_cost:
                                road[j][k] = new_cost

    def print_road():
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if road[i][j] == limit:
                    print(0, end=' ')
                else:
                    print(road[i][j], end=' ')
            print()

    fill_road()
    floyd()
    print_road()

print_answer()