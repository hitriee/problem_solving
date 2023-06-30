#230630
from sys import stdin

def to_int():return map(int, stdin.readline().split())

N, M = to_int()
limit = 6e6
edges = [tuple(to_int()) for _ in range(M)]
distance = [limit] * (N+1)

def has_negative_cycle():
    distance[1] = 0
    for i in range(N):
        for j in range(M):
            start, end, cost = edges[j]
            if distance[start] != limit and distance[end] > distance[start] + cost:
                distance[end] = distance[start] + cost
                if i == N-1:
                    return True
    return False


if has_negative_cycle():
    print(-1)
else:
    for i in range(2, N+1):
        print(distance[i] if distance[i] != limit else -1)


#
from sys import stdin

def to_int():return map(int, stdin.readline().split())

N, M = to_int()
limit = 6e6
edges = [tuple(to_int()) for _ in range(M)]
distance = [limit] * (N+1)

def has_negative_cycle():
    distance[1] = 0
    for _ in range(N-1):
        for j in range(M):
            start, end, cost = edges[j]
            if distance[start] != limit and distance[end] > distance[start] + cost:
                distance[end] = distance[start] + cost

    for j in range(M):
        start, end, cost = edges[j]
        if distance[start] != limit and distance[end] > distance[start] + cost:
            return True
    return False


if has_negative_cycle():
    print(-1)
else:
    for i in range(2, N+1):
        print(distance[i] if distance[i] != limit else -1)


#
from sys import stdin

def to_int():return map(int, stdin.readline().split())

N, M = to_int()
limit = 6e6
edges = [tuple(to_int()) for _ in range(M)]
distance = [limit] * (N+1)

def has_negative_cycle():
    distance[1] = 0
    for _ in range(N-1):
        for j in range(M):
            start, end, cost = edges[j]
            if distance[end] > distance[start] + cost:
                distance[end] = distance[start] + cost

    for j in range(M):
        start, end, cost = edges[j]
        if distance[end] > distance[start] + cost:
            return True
    return False


if has_negative_cycle():
    print(-1)
else:
    for i in range(2, N+1):
        print(distance[i] if distance[i] != limit else -1)
