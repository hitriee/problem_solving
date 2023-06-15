#230615
def to_int(): return map(int, input().split())
N, K = to_int()
heights = list(to_int())
if K == 1:
    print(heights[-1] - heights[0])
elif K == N:
    print(0)
else:
    gap = [heights[i] - heights[i-1] for i in range(1, N)]
    gap.sort()
    cost = sum(gap[:N-K])
    print(cost)



#
def return_cost():
    def to_int(): return map(int, input().split())

    N, K = to_int()
    heights = list(to_int())

    if K == 1:
        return heights[-1] - heights[0]
    elif K == N:
        return 0

    gap = [heights[i] - heights[i-1] for i in range(1, N)]
    gap.sort()
    cost = sum(gap[:N-K])
    return cost

print(return_cost())


#
def return_cost():
    def to_int():
        return map(int, input().split())

    N, K = to_int()
    heights = list(to_int())

    if K == 1:
        return heights[-1] - heights[0]
    elif K == N:
        return 0

    gap = [heights[i] - heights[i - 1] for i in range(1, N)]
    gap.sort()
    return sum(gap[:N - K])

print(return_cost())


#
def return_cost():
    def to_int():
        return map(int, input().split())

    N, K = to_int()
    heights = list(to_int())

    if K == 1:
        return heights[-1] - heights[0]
    elif K == N:
        return 0

    gap = [heights[i] - heights[i - 1] for i in range(1, N)]
    gap.sort()
    for _ in range(K-1):
        gap.pop()
    return sum(gap)

print(return_cost())



#
def return_cost():
    from heapq import heappush, heappop
    def to_int():
        return map(int, input().split())

    N, K = to_int()
    heights = list(to_int())

    if K == 1:
        return heights[-1] - heights[0]
    elif K == N:
        return 0

    gap = []
    for i in range(1, N):
        heappush(gap, heights[i-1] - heights[i])
    for _ in range(K-1):
        heappop(gap)
    return -sum(gap)

print(return_cost())