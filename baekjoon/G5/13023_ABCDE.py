#230801
from sys import stdin
def to_int(): return map(int, stdin.readline().split())
N, M = to_int()
relation = [[] for _ in range(N)]
visited = [False] * N
result = 0
for _ in range(M):
    person1, person2 = to_int()
    relation[person1].append(person2)
    relation[person2].append(person1)


def dfs(person, level=1):
    global result
    if result == 1:
        return
    if level == 5:
        result = 1
        return
    for i in relation[person]:
        if not visited[i] and relation[i]:
            visited[i] = True
            dfs(i, level+1)
            visited[i] = False

for i in range(N):
    if relation[i]:
        visited[i] = True
        dfs(i)
        visited[i] = False

print(result)


#
def return_result():
    from sys import stdin

    def to_int():
        return map(int, stdin.readline().split())

    def dfs(person, level=1):
        nonlocal result
        if result == 1:
            return
        if level == 5:
            result = 1
            return
        for i in relation[person]:
            if not visited[i] and relation[i]:
                visited[i] = True
                dfs(i, level+1)
                visited[i] = False

    N, M = to_int()
    relation = [[] for _ in range(N)]
    visited = [False] * N
    result = 0
    for _ in range(M):
        person1, person2 = to_int()
        relation[person1].append(person2)
        relation[person2].append(person1)

    for i in range(N):
        if relation[i]:
            visited[i] = True
            dfs(i)
            visited[i] = False

    return result

print(return_result())


#
def return_result():
    from sys import stdin

    def to_int():
        return map(int, stdin.readline().split())

    def dfs(person, level=1):
        nonlocal result
        if result == 1:
            return
        if level == 5:
            result = 1
            return
        for i in relation[person]:
            if not visited[i] and relation[i]:
                visited[i] = True
                dfs(i, level+1)
                visited[i] = False

    N, M = to_int()
    relation = [[] for _ in range(N)]
    visited = [False] * N
    result = 0
    for _ in range(M):
        person1, person2 = to_int()
        relation[person1].append(person2)
        relation[person2].append(person1)

    for i in range(N):
        if result == 1:
            return 1
        elif relation[i]:
            visited[i] = True
            dfs(i)
            visited[i] = False

    return result

print(return_result())


#
def return_result():
    from sys import stdin

    def to_int():
        return map(int, stdin.readline().split())

    def dfs(person, level=1):
        nonlocal result
        if result == 1:
            return
        if level == 5:
            result = 1
            return
        for i in relation[person]:
            if relation.get(i) and not visited[i]:
                visited[i] = True
                dfs(i, level+1)
                visited[i] = False

    N, M = to_int()
    relation = {}
    visited = [False] * N
    result = 0
    for _ in range(M):
        person1, person2 = to_int()
        if relation.get(person1):
            relation[person1].append(person2)
        else:
            relation[person1] = [person2]
        if relation.get(person2):
            relation[person2].append(person1)
        else:
            relation[person2] = [person1]


    for i in range(N):
        if result == 1:
            return 1
        elif relation.get(i):
            visited[i] = True
            dfs(i)
            visited[i] = False

    return result

print(return_result())


#
def return_result():
    from sys import stdin

    def to_int():
        return map(int, stdin.readline().split())

    def dfs(person, level=1):
        nonlocal result
        if result == 1:
            return
        if level == 5:
            result = 1
            return
        for i in relation[person]:
            if not visited[i] and relation[i]:
                visited[i] = True
                dfs(i, level+1)
                visited[i] = False

    N, M = to_int()
    if M < 4:
        return 0
    relation = [[] for _ in range(N)]
    visited = [False] * N
    result = 0
    for _ in range(M):
        person1, person2 = to_int()
        relation[person1].append(person2)
        relation[person2].append(person1)

    for i in range(N):
        if result == 1:
            return 1
        elif relation[i]:
            visited[i] = True
            dfs(i)
            visited[i] = False

    return result

print(return_result())
