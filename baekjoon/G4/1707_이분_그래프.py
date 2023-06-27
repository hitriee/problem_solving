#230627
from sys import stdin
from collections import deque
def to_int(): return map(int, stdin.readline().split())
new_input = stdin.readline

T = int(new_input())
for _ in range(T):
    V, E = to_int()
    link_info = [[] for _ in range(V + 1)]
    for _ in range(E):
        node1, node2 = to_int()
        link_info[node1].append(node2)
        link_info[node2].append(node1)

    graph = [set() for _ in range(2)]
    start = 1
    visited = set()

    def is_binary_graph():
        global start, visited
        q = deque()
        visited = graph[0] | graph[1]
        for i in range(start, V+1):
            if i not in visited:
                graph[0].add(i)
                q.append((i, 0))
                start = i+1
                break
        while q:
            num, index = q.popleft()
            other = 1 - index
            for i in link_info[num]:
                if i in graph[index]:
                    return False
                elif i not in graph[other]:
                    q.append((i, other))
                    graph[other].add(i)
        return True

    while len(visited) < V:
        if not is_binary_graph():
            print('NO')
            break
    else:
        print('YES')

#
def is_total_binary_graph():
    from sys import stdin
    from collections import deque
    def to_int():
        return map(int, stdin.readline().split())

    new_input = stdin.readline

    T = int(new_input())
    for _ in range(T):
        V, E = to_int()
        link_info = [[] for _ in range(V + 1)]
        for _ in range(E):
            node1, node2 = to_int()
            link_info[node1].append(node2)
            link_info[node2].append(node1)

        graph = [set() for _ in range(2)]
        start = 1
        visited = graph[0] | graph[1]

        def is_binary_graph():
            nonlocal start, visited
            q = deque()
            visited = graph[0] | graph[1]
            for i in range(start, V + 1):
                if i not in visited:
                    graph[0].add(i)
                    q.append((i, 0))
                    start = i + 1
                    break
            while q:
                num, index = q.popleft()
                other = 1 - index
                for i in link_info[num]:
                    if i in graph[index]:
                        return False
                    elif i not in graph[other]:
                        q.append((i, other))
                        graph[other].add(i)
            return True

        while len(visited) < V:
            if not is_binary_graph():
                print('NO')
                break
        else:
            print('YES')

is_total_binary_graph()


# #
def is_total_binary_graph():
    from sys import stdin
    from collections import deque
    def to_int():
        return map(int, stdin.readline().split())

    new_input = stdin.readline

    T = int(new_input())
    for _ in range(T):
        V, E = to_int()
        link_info = [[] for _ in range(V + 1)]
        for _ in range(E):
            node1, node2 = to_int()
            link_info[node1].append(node2)
            link_info[node2].append(node1)

        group = [-1] * (V+1)

        def is_binary_graph(node):
            q = deque()
            q.append(node)
            group[node] = 0
            while q:
                num = q.popleft()
                index = group[num]
                other = 1 - index
                for i in link_info[num]:
                    if group[i] == index:
                        return False
                    elif group[i] == -1:
                        q.append(i)
                        group[i] = other
            return True

        for i in range(1, V+1):
            if group[i] == -1:
                if not is_binary_graph(i):
                    print('NO')
                    break
        else:
            print('YES')

is_total_binary_graph()





'''
1
5 4
1 2
2 4
2 3
3 5
'''

'''
1
5 4
1 2
3 4
3 5
4 5
NO
'''


#
# #
def is_total_binary_graph():
    from sys import stdin
    from collections import deque

    def to_int():
        return map(int, stdin.readline().split())

    new_input = stdin.readline

    T = int(new_input())

    def is_binary_graph(node):
        q = deque()
        q.append(node)
        group[node] = 0
        while q:
            num = q.popleft()
            index = group[num]
            other = 1 - index
            for i in link_info[num]:
                if group[i] == index:
                    return False
                elif group[i] == -1:
                    q.append(i)
                    group[i] = other
        return True

    for _ in range(T):
        V, E = to_int()
        link_info = [[] for _ in range(V + 1)]
        for _ in range(E):
            node1, node2 = to_int()
            link_info[node1].append(node2)
            link_info[node2].append(node1)

        group = [-1] * (V+1)

        for i in range(1, V+1):
            if group[i] == -1:
                if not is_binary_graph(i):
                    print('NO')
                    break
        else:
            print('YES')

is_total_binary_graph()