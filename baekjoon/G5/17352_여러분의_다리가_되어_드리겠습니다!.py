#230825
from sys import stdin
new_input = stdin.readline
N = int(new_input())
root_of = [-1] * (N+1)
def find_root(num):
    if root_of[num] < 0:
        return num
    result = find_root(root_of[num])
    root_of[num] = result
    return result

def link_island(num1, num2):
    root1, root2 = find_root(num1), find_root(num2)
    if root_of[root1] > root_of[root2]:
        root_of[root1] += root_of[root2]
        root_of[root2] = root1
    else:
        root_of[root2] += root_of[root1]
        root_of[root1] = root2


for _ in range(N-2):
    link_island(*map(int, new_input().split()))

answer = []
for i in range(1, N+1):
    if root_of[i] < 0:
        answer.append(i)

print(*answer)


#
from sys import stdin
new_input = stdin.readline
N = int(new_input())
root_of = [-1] * (N+1)
def find_root(num):
    if root_of[num] < 0:
        return num
    result = find_root(root_of[num])
    root_of[num] = result
    return result

def link_island(num1, num2):
    root1, root2 = find_root(num1), find_root(num2)
    if root_of[root1] >= root_of[root2]:
        root_of[root1] += root_of[root2]
        root_of[root2] = root1
    else:
        root_of[root2] += root_of[root1]
        root_of[root1] = root2


for _ in range(N-2):
    link_island(*map(int, new_input().split()))

answer = []
for i in range(1, N+1):
    if root_of[i] < 0:
        answer.append(i)

print(*answer)


#
from sys import stdin
new_input = stdin.readline
N = int(new_input())
root_of = [-1] * (N+1)
def find_root(num):
    if root_of[num] < 0:
        return num
    result = find_root(root_of[num])
    root_of[num] = result
    return result

def link_island(num1, num2):
    root1, root2 = find_root(num1), find_root(num2)
    if root_of[root1] <= root_of[root2]:
        root_of[root1] += root_of[root2]
        root_of[root2] = root1
    else:
        root_of[root2] += root_of[root1]
        root_of[root1] = root2


for _ in range(N-2):
    link_island(*map(int, new_input().split()))

answer = []
for i in range(1, N+1):
    if root_of[i] < 0:
        answer.append(i)

print(*answer)


#
def build_bridge():
    from sys import stdin
    new_input = stdin.readline
    N = int(new_input())
    root_of = [-1] * (N + 1)

    def find_root(num):
        if root_of[num] < 0:
            return num
        result = find_root(root_of[num])
        root_of[num] = result
        return result

    def link_island(num1, num2):
        root1, root2 = find_root(num1), find_root(num2)
        if root_of[root1] <= root_of[root2]:
            root_of[root1] += root_of[root2]
            root_of[root2] = root1
        else:
            root_of[root2] += root_of[root1]
            root_of[root1] = root2

    for _ in range(N - 2):
        link_island(*map(int, new_input().split()))

    answer = []
    for i in range(1, N + 1):
        if root_of[i] < 0:
            answer.append(i)

    return f'{answer[0]} {answer[1]}'

print(build_bridge())


#
def find_root(num, root_of):
    if root_of[num] < 0:
        return num
    result = find_root(root_of[num], root_of)
    root_of[num] = result
    return result

def link_island(num1, num2, root_of):
    root1, root2 = find_root(num1, root_of), find_root(num2, root_of)
    if root_of[root1] <= root_of[root2]:
        root_of[root1] += root_of[root2]
        root_of[root2] = root1
    else:
        root_of[root2] += root_of[root1]
        root_of[root1] = root2

def build_bridge():
    from sys import stdin
    new_input = stdin.readline
    N = int(new_input())
    root_of = [-1] * (N + 1)

    for _ in range(N - 2):
        link_island(*map(int, new_input().split()), root_of)

    answer = []
    for i in range(1, N + 1):
        if root_of[i] < 0:
            answer.append(i)

    return f'{answer[0]} {answer[1]}'

print(build_bridge())