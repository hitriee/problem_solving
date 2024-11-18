# 241118
# 35756 KB / 768 ms
def main():
    from sys import stdin

    def find(node):
        if root_of[node] == node:
            return node
        result = find(root_of[node])
        root_of[node] = result
        return result

    def union(node1, node2):
        root1, root2 = find(node1), find(node2)
        if root1 == root2:
            return

        if rank_of[root1] <= rank_of[root2]:
            root_of[root2] = root1
            rank_of[root2] += rank_of[root1]
        else:
            root_of[root1] = root2
            rank_of[root1] += rank_of[root2]

    new_input = stdin.readline
    T = int(new_input())

    for i in range(1, T+1):
        N = int(new_input())
        K = int(new_input())
        root_of = list(range(N))
        rank_of = [1] * N
        for _ in range(K):
            union(*map(int, new_input().split()))

        M = int(new_input())
        print(f'Scenario {i}:')
        for _ in range(M):
            u, v = map(int, new_input().split())
            print('1' if find(u) == find(v) else '0')
        print()

main()


# 35756 KB / 776 ms
def main():
    from sys import stdin

    def find(node):
        if root_of[node] == node:
            return node
        result = find(root_of[node])
        root_of[node] = result
        return result

    def union(node1, node2):
        root1, root2 = find(node1), find(node2)
        if root1 == root2:
            return

        if rank_of[root1] <= rank_of[root2]:
            root_of[root1] = root2
            rank_of[root2] += rank_of[root1]
        else:
            root_of[root2] = root1
            rank_of[root1] += rank_of[root2]

    new_input = stdin.readline
    T = int(new_input())

    for i in range(1, T+1):
        N = int(new_input())
        K = int(new_input())
        root_of = list(range(N))
        rank_of = [1] * N
        for _ in range(K):
            union(*map(int, new_input().split()))

        M = int(new_input())
        print(f'Scenario {i}:')
        for _ in range(M):
            u, v = map(int, new_input().split())
            print('1' if find(u) == find(v) else '0')
        print()

main()




# 35756 KB / 768 ms
def main():
    from sys import stdin

    def find(node, root_of):
        if root_of[node] == node:
            return node
        result = find(root_of[node], root_of)
        root_of[node] = result
        return result

    def union(node1, node2, rank_of, root_of):
        root1, root2 = find(node1, root_of), find(node2, root_of)
        if root1 == root2:
            return

        if rank_of[root1] <= rank_of[root2]:
            root_of[root2] = root1
            rank_of[root2] += rank_of[root1]
        else:
            root_of[root1] = root2
            rank_of[root1] += rank_of[root2]

    def print_scenario():
        N = int(new_input())
        K = int(new_input())
        root_of = list(range(N))
        rank_of = [1] * N
        for _ in range(K):
            union(*map(int, new_input().split()), rank_of, root_of)

        M = int(new_input())
        print(f'Scenario {i}:')
        for _ in range(M):
            u, v = map(int, new_input().split())
            print('1' if find(u, root_of) == find(v, root_of) else '0')
        print()

    new_input = stdin.readline
    T = int(new_input())

    for i in range(1, T+1):
        print_scenario()

main()



# 35756 KB / 752 ms
def main():
    from sys import stdin

    def find(node, root_of):
        if root_of[node] == node:
            return node
        result = find(root_of[node], root_of)
        root_of[node] = result
        return result

    def union(node1, node2, rank_of, root_of):
        root1, root2 = find(node1, root_of), find(node2, root_of)
        if root1 == root2:
            return

        if rank_of[root1] <= rank_of[root2]:
            root_of[root2] = root1
            rank_of[root1] += rank_of[root2]
        else:
            root_of[root1] = root2
            rank_of[root2] += rank_of[root1]

    def print_scenario():
        N = int(new_input())
        K = int(new_input())
        root_of = list(range(N))
        rank_of = [1] * N
        for _ in range(K):
            union(*map(int, new_input().split()), rank_of, root_of)

        M = int(new_input())
        print(f'Scenario {i}:')
        for _ in range(M):
            u, v = map(int, new_input().split())
            print('1' if find(u, root_of) == find(v, root_of) else '0')
        print()

    new_input = stdin.readline
    T = int(new_input())

    for i in range(1, T+1):
        print_scenario()

main()
