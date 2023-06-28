#230628
from sys import stdin
new_input = stdin.readline
N, M, K = map(int, new_input().split())
world = []
cases = [{} for _ in range(6)]
for i in range(N):
    row = new_input().rstrip()
    world.append(row)

direct = []
for i in range(-1, 2):
    for j in range(-1, 2):
        direct.append((i, j))
direct.remove((0, 0))

def change_cnt(level, y, x, final):
    if level == limit:
        if cases[limit].get(final):
            cases[limit][final] += 1
        else:
            cases[limit][final] = 1
        return

    for dy, dx in direct:
        ny, nx = (y+dy)%N, (x+dx)%M
        change_cnt(level+1, ny, nx, final + world[ny][nx])


for _ in range(K):
    word = new_input().rstrip()
    limit = len(word)
    if not cases[limit]:
        for i in range(N):
            for j in range(M):
                change_cnt(1, i, j, world[i][j])
    print(cases[limit][word] if cases[limit].get(word) else 0)



#
def print_cnt():
    from sys import stdin
    new_input = stdin.readline
    N, M, K = map(int, new_input().split())
    world = []
    cases = [{} for _ in range(6)]
    for i in range(N):
        row = new_input().rstrip()
        world.append(row)

    direct = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            direct.append((i, j))
    direct.remove((0, 0))

    def change_cnt(level, y, x, final):
        if level == limit:
            if cases[limit].get(final):
                cases[limit][final] += 1
            else:
                cases[limit][final] = 1
            return

        for dy, dx in direct:
            ny, nx = (y + dy) % N, (x + dx) % M
            change_cnt(level + 1, ny, nx, final + world[ny][nx])

    for _ in range(K):
        word = new_input().rstrip()
        limit = len(word)
        if not cases[limit]:
            for i in range(N):
                for j in range(M):
                    change_cnt(1, i, j, world[i][j])
        print(cases[limit][word] if cases[limit].get(word) else 0)

print_cnt()


#
from sys import stdin
from collections import defaultdict
new_input = stdin.readline
N, M, K = map(int, new_input().split())
world = []
cases = [defaultdict(int) for _ in range(6)]
for i in range(N):
    row = new_input().rstrip()
    world.append(row)

direct = []
for i in range(-1, 2):
    for j in range(-1, 2):
        direct.append((i, j))
direct.remove((0, 0))

def change_cnt(level, y, x, final):
    if level == limit:
        cases[limit][final] += 1
        return

    for dy, dx in direct:
        ny, nx = (y+dy)%N, (x+dx)%M
        change_cnt(level+1, ny, nx, final + world[ny][nx])


for _ in range(K):
    word = new_input().rstrip()
    limit = len(word)
    if not cases[limit]:
        for i in range(N):
            for j in range(M):
                change_cnt(1, i, j, world[i][j])
    print(cases[limit][word])


#
from sys import stdin
new_input = stdin.readline
N, M, K = map(int, new_input().split())
world, cases = [], {}
visited = [False] * 6
for i in range(N):
    row = new_input().rstrip()
    world.append(row)

direct = []
for i in range(-1, 2):
    for j in range(-1, 2):
        direct.append((i, j))
direct.remove((0, 0))

def change_cnt(level, y, x, final):
    if level == limit:
        if cases.get(final):
            cases[final] += 1
        else:
            cases[final] = 1
        return

    for dy, dx in direct:
        ny, nx = (y+dy)%N, (x+dx)%M
        change_cnt(level+1, ny, nx, final + world[ny][nx])


for _ in range(K):
    word = new_input().rstrip()
    limit = len(word)
    if not visited[limit]:
        visited[limit] = True
        for i in range(N):
            for j in range(M):
                change_cnt(1, i, j, world[i][j])
    print(cases[word] if cases.get(word) else 0)


#
def print_cnt():
    from sys import stdin
    new_input = stdin.readline
    N, M, K = map(int, new_input().split())
    world, cases = [], {}
    visited = [False] * 6
    for i in range(N):
        row = new_input().rstrip()
        world.append(row)

    direct = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            direct.append((i, j))
    direct.remove((0, 0))

    def change_cnt(level, y, x, final):
        if level == limit:
            if cases.get(final):
                cases[final] += 1
            else:
                cases[final] = 1
            return

        for dy, dx in direct:
            ny, nx = (y+dy)%N, (x+dx)%M
            change_cnt(level+1, ny, nx, final + world[ny][nx])


    for _ in range(K):
        word = new_input().rstrip()
        limit = len(word)
        if not visited[limit]:
            visited[limit] = True
            for i in range(N):
                for j in range(M):
                    change_cnt(1, i, j, world[i][j])
        print(cases[word] if cases.get(word) else 0)

print_cnt()


#
def print_cnt():
    from sys import stdin
    new_input = stdin.readline
    N, M, K = map(int, new_input().split())
    direct, cases = [], {}
    world = [new_input().rstrip() for _ in range(N)]
    visited = [False] * 6

    for i in range(-1, 2):
        for j in range(-1, 2):
            direct.append((i, j))
    direct.remove((0, 0))

    def change_cnt(level, y, x, final):
        if level == limit:
            if cases.get(final):
                cases[final] += 1
            else:
                cases[final] = 1
            return

        for dy, dx in direct:
            ny, nx = (y+dy)%N, (x+dx)%M
            change_cnt(level+1, ny, nx, final + world[ny][nx])


    for _ in range(K):
        word = new_input().rstrip()
        limit = len(word)
        if not visited[limit]:
            visited[limit] = True
            for i in range(N):
                for j in range(M):
                    change_cnt(1, i, j, world[i][j])
        print(cases[word] if cases.get(word) else 0)

print_cnt()