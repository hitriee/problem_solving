#230418
# bfs
from collections import deque
N, M = map(int, input().split())
fuel = [list(map(int, input().split())) for _ in range(N)]
path = deque((fuel[0][i], 0, i, -2) for i in range(M))
final_values = []
while path:
    fuel_value, i, j, direction = path.popleft()
    if i == N-1:
        final_values.append(fuel_value)
    else:
        addition = fuel[i+1]
        for dj in range(-1, 2):
            nj = j+dj
            if direction != dj and 0 <= nj < M:
                path.append((fuel_value + addition[nj], i+1, nj, dj))
print(min(final_values))


# 함수화
def bfs():
    from collections import deque
    N, M = map(int, input().split())
    fuel = [list(map(int, input().split())) for _ in range(N)]
    path = deque((fuel[0][i], 0, i, -2) for i in range(M))
    final_values = []
    while path:
        fuel_value, i, j, direction = path.popleft()
        if i == N-1:
            final_values.append(fuel_value)
        else:
            addition = fuel[i+1]
            for dj in range(-1, 2):
                nj = j+dj
                if direction != dj and 0 <= nj < M:
                    path.append((fuel_value + addition[nj], i+1, nj, dj))
    return min(final_values)
print(bfs())
