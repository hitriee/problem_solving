#230925
from sys import stdin
N, M = map(int, stdin.readline().split())
group = list(range(N))
depth = [0] * N

def find_root(node):
    if node == group[node]:
        return node
    root = find_root(group[node])
    group[node] = root
    return root

def has_cycle(node1, node2):
    root1, root2 = find_root(node1), find_root(node2)
    if root1 == root2:
        return True
    if depth[root1] <= depth[root2]:
        depth[root2] += depth[root1]
        group[root1] = root2
    else:
        depth[root1] += depth[root2]
        group[root2] = root1

    return False

for i in range(1, min(M, N-1)+1):
    node1, node2 = map(int, stdin.readline().split())
    if has_cycle(node1, node2):
        print(i)
        break

else:
    if M > N-1:
        print(N)
    else:
        print(0)

#
def find_root(node, group):
    if node == group[node]:
        return node
    root = find_root(group[node], group)
    group[node] = root
    return root

def has_cycle(node1, node2, group, depth):
    root1, root2 = find_root(node1, group), find_root(node2, group)
    if root1 == root2:
        return True
    if depth[root1] <= depth[root2]:
        depth[root2] += depth[root1]
        group[root1] = root2
    else:
        depth[root1] += depth[root2]
        group[root2] = root1

    return False

def find_number():
    from sys import stdin
    N, M = map(int, stdin.readline().split())
    group = list(range(N))
    depth = [0] * N

    for i in range(1, min(M, N-1)+1):
        node1, node2 = map(int, stdin.readline().split())
        if has_cycle(node1, node2, group, depth):
            return i

    if M > N-1:
        return N

    return 0

print(find_number())


#
def find_root(node, group):
    if node == group[node]:
        return node
    root = find_root(group[node], group)
    group[node] = root
    return root

def has_cycle(node1, node2, group, depth):
    root1, root2 = find_root(node1, group), find_root(node2, group)
    if root1 == root2:
        return True
    if depth[root1] <= depth[root2]:
        depth[root2] += depth[root1]
        group[root1] = root2
    else:
        depth[root1] += depth[root2]
        group[root2] = root1

    return False

def find_number():
    from sys import stdin
    N, M = map(int, stdin.readline().split())
    group = list(range(N))
    depth = [1] * N

    for i in range(1, min(M, N-1)+1):
        node1, node2 = map(int, stdin.readline().split())
        if has_cycle(node1, node2, group, depth):
            return i

    if M > N-1:
        return N

    return 0

print(find_number())


#
def find_root(node, group):
    if group[node] < 0:
        return node
    root = find_root(group[node], group)
    group[node] = root
    return root

def has_cycle(node1, node2, group):
    root1, root2 = find_root(node1, group), find_root(node2, group)
    if root1 == root2:
        return True
    if group[root1] <= group[root2]:
        group[root1] += group[root2]
        group[root2] = root1
    else:
        group[root2] += group[root1]
        group[root1] = root2

    return False

def find_number():
    from sys import stdin
    N, M = map(int, stdin.readline().split())
    group = [-1] * N

    for i in range(1, min(M, N-1)+1):
        node1, node2 = map(int, stdin.readline().split())
        if has_cycle(node1, node2, group):
            return i

    if M > N-1:
        return N

    return 0

print(find_number())


#
def find_root(node, group):
    if group[node] < 0:
        return node
    root = find_root(group[node], group)
    group[node] = root
    return root

def has_cycle(node1, node2, group):
    root1, root2 = find_root(node1, group), find_root(node2, group)
    if root1 == root2:
        return True
    if group[root1] <= group[root2]:
        group[root1] += group[root2]
        group[root2] = root1
    else:
        group[root2] += group[root1]
        group[root1] = root2

    return False

def find_number():
    from sys import stdin
    N, M = map(int, stdin.readline().split())
    group = [-1] * N

    for i in range(1, min(M, N-1)+1):
        if has_cycle(*map(int, stdin.readline().split()), group):
            return i

    if M > N-1:
        return N

    return 0

print(find_number())


#
def find_root(node, group):
    if group[node] < 0:
        return node
    root = find_root(group[node], group)
    group[node] = root
    return root

def has_cycle(node1, node2, group):
    root1, root2 = find_root(node1, group), find_root(node2, group)
    if root1 == root2:
        return True
    if group[root1] <= group[root2]:
        group[root1] += group[root2]
        group[root2] = root1
    else:
        group[root2] += group[root1]
        group[root1] = root2

    return False

def find_number():
    from sys import stdin
    N, M = map(int, stdin.readline().split())
    group = [-1] * N

    for i in range(1, min(M+1, N)):
        if has_cycle(*map(int, stdin.readline().split()), group):
            return i

    if M > N-1:
        return N

    return 0

print(find_number())


#
def find_root(node, group):
    if group[node] < 0:
        return node
    root = find_root(group[node], group)
    group[node] = root
    return root

def has_cycle(node1, node2, group):
    root1, root2 = find_root(node1, group), find_root(node2, group)
    if root1 == root2:
        return True
    if group[root1] <= group[root2]:
        group[root1] += group[root2]
        group[root2] = root1
    else:
        group[root2] += group[root1]
        group[root1] = root2

    return False

def find_number():
    from sys import stdin
    N, M = map(int, stdin.readline().split())
    group = [-1] * N

    for i in range(1, min(M+1, N)):
        node1, node2 = map(int, stdin.readline().split())
        if has_cycle(node1, node2, group):
            return i

    if M > N-1:
        return N

    return 0

print(find_number())