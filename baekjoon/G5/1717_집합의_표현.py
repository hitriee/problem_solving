#230823
from sys import stdin
def to_int():
    return map(int, stdin.readline().split())

N, M = to_int()
root_of = list(range(N+1))
rank = [0] * (N+1)

def find_root(num):
    root = root_of[num]
    if num == root:
        return num
    result = find_root(root)
    root_of[num] = result
    return result

def union_group(command, num1, num2):
    root1, root2 = find_root(num1), find_root(num2)
    if command == 1:
        print('yes' if root1 == root2 else 'no')
    elif root1 != root2:
        rank1, rank2 = rank[root1], rank[root2]
        if rank1 > rank2:
            rank[root1] += 1
            root_of[num2] = root1
            root_of[root2] = root1
        else:
            rank[root2] += 1
            root_of[num1] = root2
            root_of[root1] = root2

for _ in range(M):
    union_group(*to_int())


#
def practice_command():
    from sys import stdin
    def to_int():
        return map(int, stdin.readline().split())

    N, M = to_int()
    root_of = list(range(N + 1))
    rank = [0] * (N + 1)

    def find_root(num):
        root = root_of[num]
        if num == root:
            return num
        result = find_root(root)
        root_of[num] = result
        return result

    def union_group(command, num1, num2):
        root1, root2 = find_root(num1), find_root(num2)
        if command == 1:
            print('yes' if root1 == root2 else 'no')
        elif root1 != root2:
            rank1, rank2 = rank[root1], rank[root2]
            if rank1 > rank2:
                rank[root1] += 1
                root_of[num2] = root1
                root_of[root2] = root1
            else:
                rank[root2] += 1
                root_of[num1] = root2
                root_of[root1] = root2

    for _ in range(M):
        union_group(*to_int())

practice_command()


#
def practice_command():
    from sys import stdin
    def to_int():
        return map(int, stdin.readline().split())

    N, M = to_int()
    root_of = list(range(N + 1))
    rank = [0] * (N + 1)

    def find_root(num):
        root = root_of[num]
        if num == root:
            return num
        result = find_root(root)
        root_of[num] = result
        return result

    def union_group(command, num1, num2):
        root1, root2 = find_root(num1), find_root(num2)
        if command == 1:
            print('yes' if root1 == root2 else 'no')
        elif root1 != root2:
            rank1, rank2 = rank[root1], rank[root2]
            if rank1 > rank2:
                rank[root1] += 1
                root_of[root2] = root1
            else:
                rank[root2] += 1
                root_of[root1] = root2

    for _ in range(M):
        union_group(*to_int())

practice_command()


#
def practice_command():
    from sys import stdin
    def to_int():
        return map(int, stdin.readline().split())

    N, M = to_int()
    root_of = list(range(N + 1))
    rank = [0] * (N + 1)

    def find_root(num):
        root = root_of[num]
        if num == root:
            return num
        result = find_root(root)
        root_of[num] = result
        return result

    def union_group(command, num1, num2):
        root1, root2 = find_root(num1), find_root(num2)
        if command == 1:
            print('yes' if root1 == root2 else 'no')
        elif root1 != root2:
            rank1, rank2 = rank[root1], rank[root2]
            if rank1 > rank2:
                root_of[root2] = root1
            else:
                if rank1 == rank2:
                    rank[root2] += 1
                root_of[root1] = root2

    for _ in range(M):
        union_group(*to_int())

practice_command()