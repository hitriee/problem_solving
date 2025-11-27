# 251127
# 111804 KB / 836 ms
def main():
    from sys import stdin
    from collections import deque

    new_input = stdin.readline
    N = int(new_input())
    color_target = list(map(int, new_input().split()))
    link_info = [set() for _ in range(N+1)]

    for _ in range(N-1):
        node1, node2 = map(lambda x: int(x)-1, new_input().split())
        link_info[node1].add(node2)
        link_info[node2].add(node1)

    def find_children():

        visited = [False] * N
        q = deque()
        q.append(0)

        while q:
            node = q.popleft()
            if not visited[node]:
                visited[node] = True
                linked_nodes = set(link_info[node])
                for next_node in linked_nodes:
                    if visited[next_node]:
                        link_info[node].remove(next_node)
                    else:
                        q.append(next_node)


    def find_cnt():
        cnt = 0
        q = deque()

        q.append((0, 0, color_target[0]))

        while q:
            node, present_c, next_c = q.popleft()
            if present_c != next_c:
                cnt += 1

            for next_node in link_info[node]:
                q.append((next_node, next_c, color_target[next_node]))

        return cnt

    find_children()

    return find_cnt()

print(main())





# 110236 KB / 844 ms
def main():
    from sys import stdin
    from collections import deque

    new_input = stdin.readline

    N = int(new_input())
    color_target = list(map(int, new_input().split()))
    link_info = [set() for _ in range(N)]
    q = deque()

    for _ in range(N-1):
        node1, node2 = map(lambda x: int(x)-1, new_input().split())
        link_info[node1].add(node2)
        link_info[node2].add(node1)

    def find_children():

        visited = [False] * N
        q.append(0)

        while q:
            node = q.popleft()
            if not visited[node]:
                visited[node] = True
                linked_nodes = set(link_info[node])
                for next_node in linked_nodes:
                    if visited[next_node]:
                        link_info[node].remove(next_node)
                    else:
                        q.append(next_node)


    def find_cnt():
        cnt = 0
        q.append((0, 0, color_target[0]))

        while q:
            node, present_c, next_c = q.popleft()
            if present_c != next_c:
                cnt += 1

            for next_node in link_info[node]:
                q.append((next_node, next_c, color_target[next_node]))

        return cnt

    find_children()

    return find_cnt()

print(main())