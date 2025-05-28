# 250528
# 158544 KB / 1480 ms
def main():
    from heapq import heappush, heappop

    N = int(input())
    tree = [[] for _ in range(N+1)]
    gap_info = [[15001] * (N+1) for _ in range(N+1)]
    heap = []

    for i in range(1, N):
        info = list(map(int, input().split()))
        for j in range(i+1, N+1):
            gap_info[i][j] = gap_info[j][i] = info[j-i-1]


    visited = {1}
    for i in range(2, N+1):
        heappush(heap, (gap_info[1][i], 1, i))

    cnt = 0
    while cnt < N-1:
        gap, node1, node2 = heappop(heap)
        if node2 not in visited:
            tree[node1].append(node2)
            tree[node2].append(node1)
            visited.add(node2)
            cnt += 1
            for i in range(2, N+1):
                heappush(heap, (gap_info[node2][i], node2, i))


    for i in range(1, N+1):
        print(len(tree[i]), *sorted(tree[i]))

main()





# 157508 KB / 1384 ms
def main():
    from heapq import heappush, heappop

    N = int(input())
    tree = [[] for _ in range(N)]
    gap_info = [[15001] * N for _ in range(N)]
    heap = []

    for i in range(N-1):
        info = list(map(int, input().split()))
        for j in range(i+1, N):
            gap_info[i][j] = gap_info[j][i] = info[j-i-1]


    visited = {0}
    for i in range(1, N):
        heappush(heap, (gap_info[0][i], 0, i))

    cnt = 0
    while cnt < N-1:
        gap, node1, node2 = heappop(heap)
        if node2 not in visited:
            tree[node1].append(node2+1)
            tree[node2].append(node1+1)
            visited.add(node2)
            cnt += 1
            for i in range(1, N):
                heappush(heap, (gap_info[node2][i], node2, i))


    for i in range(N):
        print(len(tree[i]), *sorted(tree[i]))

main()




# 109292 KB / 844 ms
def main():
    from heapq import heappush, heappop

    N = int(input())
    tree = [[] for _ in range(N)]
    gap_info = [[15001] * N for _ in range(N)]
    heap = []

    for i in range(N-1):
        info = list(map(int, input().split()))
        for j in range(i+1, N):
            gap_info[i][j] = gap_info[j][i] = info[j-i-1]


    visited = {0}
    for i in range(1, N):
        heappush(heap, (gap_info[0][i], 0, i))

    cnt = 0
    while cnt < N-1:
        gap, node1, node2 = heappop(heap)
        if node2 not in visited:
            tree[node1].append(node2+1)
            tree[node2].append(node1+1)
            visited.add(node2)
            cnt += 1
            for i in range(1, N):
                if i not in visited:
                    heappush(heap, (gap_info[node2][i], node2, i))


    for i in range(N):
        print(len(tree[i]), *sorted(tree[i]))

main()