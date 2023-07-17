#230716
from sys import stdin
from heapq import heapify, heappop
N = int(input())
table = []
for i in range(N):
    row = list(map(int, stdin.readline().split()))
    table.extend(row)
    heapify(table)
    if len(table) > N:
        for _ in range(N):
            heappop(table)
print(table[0])


#
def n_largest_num():
    from sys import stdin
    from heapq import heapify, heappop
    N = int(input())
    table = []
    for i in range(N):
        row = list(map(int, stdin.readline().split()))
        table.extend(row)
        heapify(table)
        if len(table) > N:
            for _ in range(N):
                heappop(table)
    return table[0]

print(n_largest_num())


#
def n_largest_num():
    from sys import stdin
    from heapq import heapify, heappop
    N = int(input())
    table = list(map(int, stdin.readline().split()))
    heapify(table)
    for _ in range(N-1):
        row = list(map(int, stdin.readline().split()))
        table.extend(row)
        heapify(table)
        for _ in range(N):
            heappop(table)

    return table[0]

print(n_largest_num())