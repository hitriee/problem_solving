#230809
from sys import stdin
from collections import deque
new_input = stdin.readline

N = int(new_input())
M = int(new_input())
link_info = [[] for _ in range(N+1)]
for i in range(1, N+1):
    info = new_input().split()
    for j in range(N):
        if info[j] == '1':
            link_info[i].append(j+1)

plan = list(map(int, new_input().split()))
for i in range(M-1):
    visited = [False] * (N+1)
    target = plan[i+1]
    q = deque()
    q.append(plan[i])
    visited[plan[i]] = True
    while q:
        city = q.popleft()
        if city == target:
            break
        for j in link_info[city]:
            if not visited[j]:
                visited[j] = True
                q.append(j)
    else:
        print('NO')
        break
else:
    print('YES')


#
from sys import stdin
from collections import deque
new_input = stdin.readline

N = int(new_input())
M = int(new_input())
able_to_visit = [set() for _ in range(N+1)]
for i in range(1, N+1):
    info = new_input().split()
    for j in range(N):
        if info[j] == '1':
            able_to_visit[i].add(j+1)

plan = list(map(int, new_input().split()))
for i in range(M-1):
    visited = set()
    target = plan[i+1]
    q = deque()
    now = plan[i]
    q.append(now)
    visited.add(now)
    while q:
        city = q.popleft()
        if city == target:
            for j in visited:
                if j not in able_to_visit[now] and j != now:
                    able_to_visit[now].add(j)
            break
        for j in able_to_visit[city]:
            if j not in visited:
                visited.add(j)
                q.append(j)
    else:
        print('NO')
        break
else:
    print('YES')

#
from sys import stdin
from collections import deque
new_input = stdin.readline

N = int(new_input())
M = int(new_input())
able_to_visit = [set() for _ in range(N+1)]
for i in range(1, N+1):
    info = new_input().split()
    for j in range(N):
        if info[j] == '1':
            able_to_visit[i].add(j+1)

plan = list(map(int, new_input().split()))
for i in range(M-1):
    visited = set()
    target = plan[i+1]
    q = deque()
    now = plan[i]
    q.append(now)
    visited.add(now)
    while q:
        city = q.popleft()
        if city == target:
            break
        for j in able_to_visit[city]:
            if j not in visited:
                visited.add(j)
                q.append(j)
                able_to_visit[now].add(j)
    else:
        print('NO')
        break
else:
    print('YES')


#
def is_possible_plan():
    from sys import stdin
    from collections import deque
    new_input = stdin.readline

    N = int(new_input())
    M = int(new_input())
    link_info = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):
        info = new_input().split()
        for j in range(N):
            if info[j] == '1':
                link_info[i].append(j + 1)

    plan = list(map(int, new_input().split()))
    for i in range(M - 1):
        visited = [False] * (N + 1)
        target = plan[i + 1]
        q = deque()
        q.append(plan[i])
        visited[plan[i]] = True
        while q:
            city = q.popleft()
            if city == target:
                break
            for j in link_info[city]:
                if not visited[j]:
                    visited[j] = True
                    q.append(j)
        else:
            return 'NO'
    return 'YES'

print(is_possible_plan())


#
def is_possible_plan():
    from sys import stdin
    from collections import deque
    new_input = stdin.readline

    N = int(new_input())
    M = int(new_input())
    link_info = [list(map(int, new_input().split())) for _ in range(N)]
    plan = list(map(int, new_input().split()))
    for i in range(M - 1):
        now, target = plan[i:i+2]
        now -= 1
        target -= 1
        if link_info[now][target] == 0:
            visited = [False] * (N)
            q = deque()
            q.append(now)
            visited[now] = True
            while q:
                city = q.popleft()
                if city == target:
                    break
                for j in range(N):
                    if not visited[j] and link_info[city][j] == 1:
                        visited[j] = True
                        q.append(j)
                        if link_info[now][j] == 0:
                            link_info[now][j] = 1
                            link_info[j][now] = 1
            else:
                return 'NO'
    return 'YES'

print(is_possible_plan())


#
def is_possible_plan():
    from sys import stdin
    from collections import deque

    def to_int(): return int(stdin.readline())
    def to_int_list(): return list(map(int, stdin.readline().split()))

    N = to_int()
    M = to_int()
    link_info = [to_int_list() for _ in range(N)]
    plan = to_int_list()
    for i in range(M - 1):
        now, target = plan[i:i+2]
        now -= 1
        target -= 1
        if link_info[now][target] == 0:
            visited = [False] * (N)
            q = deque()
            q.append(now)
            visited[now] = True
            while q:
                city = q.popleft()
                if city == target:
                    break
                for j in range(N):
                    if not visited[j] and link_info[city][j] == 1:
                        visited[j] = True
                        q.append(j)
                        if link_info[now][j] == 0:
                            link_info[now][j] = 1
                            link_info[j][now] = 1
            else:
                return 'NO'
    return 'YES'

print(is_possible_plan())


#
def is_possible_plan():
    from sys import stdin
    from collections import deque

    def to_int():
        return int(stdin.readline())

    def to_int_list():
        return list(map(int, stdin.readline().split()))

    N = to_int()
    M = to_int()
    link_info = [to_int_list() for _ in range(N)]
    plan = to_int_list()
    for i in range(M - 1):
        now, target = plan[i:i + 2]
        now -= 1
        target -= 1
        if link_info[now][target] == 0:
            visited = set()
            q = deque()
            q.append(now)
            visited.add(now)
            while q:
                city = q.popleft()
                if city == target:
                    for j in visited:
                        if link_info[j][now] == 0 and j != now:
                            link_info[j][now] = 1
                            link_info[now][j] = 1
                    break
                for j in range(N):
                    if j not in visited and link_info[city][j] == 1:
                        visited.add(j)
                        q.append(j)
            else:
                return 'NO'
    return 'YES'


print(is_possible_plan())


#
def find_root(num, group_info):
    if num == group_info[num]:
        return num
    result = find_root(group_info[num], group_info)
    group_info[num] = result
    return result

def union_group(num1, num2, group_info, rank):
    group1, group2 = find_root(num1, group_info), find_root(num2, group_info)
    if group1 == group2:
        return
    if rank[group1] >= rank[group2]:
        rank[group1] += rank[group2]
        group_info[group2] = group1
    else:
        rank[group2] += rank[group1]
        group_info[group1] = group2

def is_possible_route():
    from sys import stdin
    new_input = stdin.readline
    N = int(new_input())
    M = int(new_input())
    group_info = list(range(N+1))
    rank = [1] * (N+1)
    for i in range(N):
        row = new_input().split()
        for j in range(i+1, N):
            if row[j] == '1':
                union_group(i+1, j+1, group_info, rank)
    route = list(map(int, new_input().split()))
    ref = find_root(route[0], group_info)
    for i in range(1, M):
        root = find_root(route[i], group_info)
        if root != ref:
            return 'NO'

    return 'YES'

print(is_possible_route())

