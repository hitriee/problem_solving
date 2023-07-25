#230422
N = int(input())
target1, target2 = map(int, input().split())
parent = [0] * (N+1)
M = int(input())
path = [[] for _ in range(2)]


for _ in range(M):
    top, bottom = map(int, input().split())
    parent[bottom] = top

def find_root(node, i, level=0):
    path[i].append(node)
    if parent[node] == 0:
        return
    return find_root(parent[node], i, level+1)

find_root(target1, 0)
find_root(target2, 1)
root1, root2 = path[0][-1], path[1][-1]
if root1 != root2:
    print(-1)
else:
    level1, level2 = len(path[0]), len(path[1])
    answer, dif = 0, 1
    min_level = min(level1, level2)
    for i in range(-2, -min_level-1, -1):
        if path[0][i] != path[1][i]:
            break
        dif += 1
    answer += level1 + level2 - 2*dif
    print(answer)


#
N = int(input())
targets = list(map(int, input().split()))
parent = [0] * (N+1)
M = int(input())
path = [[] for _ in range(2)]


for _ in range(M):
    top, bottom = map(int, input().split())
    parent[bottom] = top

def find_root(node, level=0):
    path[i].append(node)
    if parent[node] == 0:
        return
    return find_root(parent[node], level+1)

for i in range(2):
    find_root(targets[i])

root1, root2 = path[0][-1], path[1][-1]
if root1 != root2:
    print(-1)
else:
    levels = [len(path[0]), len(path[1])]
    answer, dif = 0, 1
    min_level = min(levels)
    for i in range(-2, -min_level-1, -1):
        if path[0][i] != path[1][i]:
            break
        dif += 1
    answer += sum(levels) - 2*dif
    print(answer)


#
def calc_distance():
    N = int(input())
    targets = list(map(int, input().split()))
    parent = [0] * (N + 1)
    M = int(input())
    path = [[] for _ in range(2)]

    for _ in range(M):
        top, bottom = map(int, input().split())
        parent[bottom] = top

    def find_root(node, level=0):
        path[i].append(node)
        if parent[node] == 0:
            return
        return find_root(parent[node], level + 1)

    for i in range(2):
        find_root(targets[i])

    root1, root2 = path[0][-1], path[1][-1]
    if root1 != root2:
        return -1

    levels = [len(path[0]), len(path[1])]
    dif = 1
    min_level = min(levels)
    for i in range(-2, -min_level - 1, -1):
        if path[0][i] != path[1][i]:
            break
        dif += 1
    answer = sum(levels) - 2 * dif
    return answer

print(calc_distance())

#
def calc_distance():
    from sys import stdin

    def to_int(): return int(stdin.readline())

    def to_int_map(): return map(int, stdin.readline().split())

    def find_root(node, level=0):
        path[i].append(node)
        if parent[node] == 0:
            return
        return find_root(parent[node], level + 1)

    N = to_int()
    targets = list(to_int_map())
    parent = [0] * (N + 1)
    M = int(input())
    path = [[] for _ in range(2)]

    for _ in range(M):
        top, bottom = to_int_map()
        parent[bottom] = top

    for i in range(2):
        find_root(targets[i])

    if path[0][-1] != path[1][-1]: return -1

    levels = [len(path[0]), len(path[1])]
    min_level, dif = min(levels), 1
    for i in range(-2, -min_level - 1, -1):
        if path[0][i] != path[1][i]:
            break
        dif += 1
    answer = sum(levels) - 2 * dif
    return answer


print(calc_distance())