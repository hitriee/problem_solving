#230824
from sys import stdin
def to_int():
    return map(int, stdin.readline().split())

N, M, K = to_int()
cost = [0] + list(to_int())
root_of = list(range(N+1))
rank = [1] * (N+1)

def find_root(person):
    root = root_of[person]
    if root == person:
        return person
    result = find_root(root)
    root_of[person] = result
    return result

def union_group(person1, person2):
    if person1 == person2:
        return

    group1, group2 = find_root(person1), find_root(person2)

    if group1 == group2:
        return
    elif rank[group1] < rank[group2]:
        rank[group1] += rank[group2]
        root_of[group2] = group1
    else:
        rank[group2] += rank[group1]
        root_of[group1] = group2

for _ in range(M):
    union_group(*to_int())

min_cost = [0] * (N+1)

for i in range(1, N+1):
    root = find_root(i)
    if min_cost[root] == 0 or min_cost[root] > cost[i]:
        min_cost[root] = cost[i]

total = sum(min_cost)
if total > K:
    print('Oh no')
else:
    print(total)


#
from sys import stdin
def to_int():
    return map(int, stdin.readline().split())

N, M, K = to_int()
cost = [0] + list(to_int())
root_of = list(range(N+1))
rank = [1] * (N+1)

def find_root(person):
    root = root_of[person]
    if root == person:
        return person
    result = find_root(root)
    root_of[person] = result
    return result

def union_group(person1, person2):
    if person1 == person2:
        return

    group1, group2 = find_root(person1), find_root(person2)

    if group1 == group2:
        return
    elif rank[group2] > rank[group1]:
        rank[group2] += rank[group1]
        root_of[group1] = group2
    else:
        rank[group1] += rank[group2]
        root_of[group2] = group1

for _ in range(M):
    union_group(*to_int())

min_cost = [0] * (N+1)

for i in range(1, N+1):
    root = find_root(i)
    if min_cost[root] == 0 or min_cost[root] > cost[i]:
        min_cost[root] = cost[i]

total = sum(min_cost)
if total > K:
    print('Oh no')
else:
    print(total)


#
from sys import stdin
def to_int():
    return map(int, stdin.readline().split())

N, M, K = to_int()
cost = [0] + list(to_int())
root_of = [-1] * (N+1)
def find_root(person):
    root = root_of[person]
    if root < 0:
        return person
    result = find_root(root)
    root_of[person] = result
    return result

def union_group(person1, person2):
    if person1 == person2:
        return

    group1, group2 = find_root(person1), find_root(person2)

    if group1 == group2:
        return
    elif root_of[group1] < root_of[group2]:
        root_of[group1] += root_of[group2]
        root_of[group2] = group1
    else:
        root_of[group2] += root_of[group1]
        root_of[group1] = group2

for _ in range(M):
    union_group(*to_int())

min_cost = [0] * (N+1)

for i in range(1, N+1):
    root = find_root(i)
    if min_cost[root] == 0 or min_cost[root] > cost[i]:
        min_cost[root] = cost[i]

total = sum(min_cost)
if total > K:
    print('Oh no')
else:
    print(total)


#
def find_min_cost():
    from sys import stdin
    def to_int():
        return map(int, stdin.readline().split())

    N, M, K = to_int()
    cost = [0] + list(to_int())
    root_of = list(range(N + 1))
    rank = [1] * (N + 1)

    def find_root(person):
        root = root_of[person]
        if root == person:
            return person
        result = find_root(root)
        root_of[person] = result
        return result

    def union_group(person1, person2):
        if person1 == person2:
            return

        group1, group2 = find_root(person1), find_root(person2)

        if group1 == group2:
            return
        elif rank[group2] > rank[group1]:
            rank[group2] += rank[group1]
            root_of[group1] = group2
        else:
            rank[group1] += rank[group2]
            root_of[group2] = group1

    for _ in range(M):
        union_group(*to_int())

    min_cost = [0] * (N + 1)

    for i in range(1, N + 1):
        root = find_root(i)
        if min_cost[root] == 0 or min_cost[root] > cost[i]:
            min_cost[root] = cost[i]

    total = sum(min_cost)

    return 'Oh no' if total > K else total

print(find_min_cost())

#
def find_root(person, root_of):
    root = root_of[person]
    if root == person:
        return person
    result = find_root(root, root_of)
    root_of[person] = result
    return result

def union_group(person1, person2, root_of, rank):
    if person1 == person2:
        return

    group1, group2 = find_root(person1, root_of), find_root(person2, root_of)

    if group1 == group2:
        return
    elif rank[group2] > rank[group1]:
        rank[group2] += rank[group1]
        root_of[group1] = group2
    else:
        rank[group1] += rank[group2]
        root_of[group2] = group1

def find_min_cost():
    from sys import stdin
    def to_int():
        return map(int, stdin.readline().split())

    N, M, K = to_int()
    cost = [0] + list(to_int())
    root_of = list(range(N + 1))
    rank = [1] * (N + 1)

    for _ in range(M):
        union_group(*to_int(), root_of, rank)

    min_cost = [0] * (N + 1)

    for i in range(1, N + 1):
        root = find_root(i, root_of)
        if min_cost[root] == 0 or min_cost[root] > cost[i]:
            min_cost[root] = cost[i]

    total = sum(min_cost)

    return 'Oh no' if total > K else total

print(find_min_cost())


#
def find_root(person, root_of):
    root = root_of[person]
    if root < 0:
        return person
    result = find_root(root, root_of)
    root_of[person] = result
    return result

def union_group(person1, person2, root_of):
    if person1 == person2:
        return

    group1, group2 = find_root(person1, root_of), find_root(person2, root_of)

    if group1 == group2:
        return
    elif root_of[group2] > root_of[group1]:
        root_of[group1] += root_of[group2]
        root_of[group2] = group1
    else:
        root_of[group2] += root_of[group1]
        root_of[group1] = group2

def find_min_cost():
    from sys import stdin
    def to_int():
        return map(int, stdin.readline().split())

    N, M, K = to_int()
    cost = [0] + list(to_int())
    root_of = [-1] * (N+1)

    for _ in range(M):
        union_group(*to_int(), root_of)

    min_cost = [0] * (N + 1)

    for i in range(1, N + 1):
        root = find_root(i, root_of)
        if min_cost[root] == 0 or min_cost[root] > cost[i]:
            min_cost[root] = cost[i]

    total = sum(min_cost)

    return 'Oh no' if total > K else total

print(find_min_cost())


#
def find_root(person, root_of):
    root = root_of[person]
    if root < 0:
        return person
    result = find_root(root, root_of)
    root_of[person] = result
    return result

def union_group(person1, person2, root_of):
    if person1 == person2:
        return

    group1, group2 = find_root(person1, root_of), find_root(person2, root_of)

    if group1 == group2:
        return
    elif root_of[group2] > root_of[group1]:
        root_of[group1] += root_of[group2]
        root_of[group2] = group1
    else:
        root_of[group2] += root_of[group1]
        root_of[group1] = group2

def find_min_cost():
    from sys import stdin
    def to_int():
        return map(int, stdin.readline().split())

    N, M, K = to_int()
    cost = [0] + list(to_int())
    root_of = [-1] * (N+1)

    for _ in range(M):
        union_group(*to_int(), root_of)

    min_cost = [0] * (N + 1)
    total = 0

    for i in range(1, N + 1):
        root = find_root(i, root_of)
        if min_cost[root] == 0:
            min_cost[root] = cost[i]
            total += min_cost[root]
        elif min_cost[root] > cost[i]:
            total += (cost[i] - min_cost[root])
            min_cost[root] = cost[i]

    return 'Oh no' if total > K else total

print(find_min_cost())