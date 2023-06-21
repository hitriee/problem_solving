#230621
from sys import stdin
from heapq import heappop, heappush, heapify
new_input = stdin.readline
N = int(new_input())
M = int(new_input())
link_cost = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, cost = map(int, new_input().split())
    if a != b:
        link_cost[a].append((cost, b))
        link_cost[b].append((cost, a))

heapify(link_cost[1])
heap = link_cost[1][:]
visited = [False] * (N+1)
visited[1] = True
total_cost = 0
cnt = 0

while cnt < N-1:
    cost, computer = heappop(heap)
    if not visited[computer]:
        cnt += 1
        total_cost += cost
        visited[computer] = True
        for i in link_cost[computer]:
            if not visited[i[1]]:
                heappush(heap, i)

print(total_cost)



#
def link_network():
    from sys import stdin
    new_input = stdin.readline

    N = int(new_input())
    M = int(new_input())
    link_cost = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b, cost = map(int, new_input().split())
        if a != b:
            link_cost[a].append((cost, b))
            link_cost[b].append((cost, a))


    def calc_cost():
        from heapq import heappop, heappush, heapify

        heapify(link_cost[1])
        heap = link_cost[1][:]
        visited = [False] * (N + 1)
        visited[1] = True
        total_cost = cnt = 0

        while cnt < N - 1:
            cost, computer = heappop(heap)
            if not visited[computer]:
                cnt += 1
                total_cost += cost
                visited[computer] = True
                for i in link_cost[computer]:
                    if not visited[i[1]]:
                        heappush(heap, i)

        return total_cost

    return calc_cost()

print(link_network())


# 병합 정렬로도 시도해보자