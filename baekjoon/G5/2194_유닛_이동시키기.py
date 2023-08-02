#230802
from sys import stdin
def to_int(): return map(int, stdin.readline().split())

N, M, A, B, K = to_int()
map_info = [[0]*M for _ in range(N)]
for _ in range(K):
    y, x = to_int()
    map_info[y-1][x-1] = 1
start_y, start_x = to_int()
end_y, end_x = to_int()
visited = [[False]*M for _ in range(N)]

def bfs():
    from collections import deque
    q = deque()
    q.append((start_y-1, start_x-1, 0))
    while q:
        y, x, cnt = q.popleft()
        if y == end_y-1 and x == end_x-1:
            return cnt
        for ny in (y-1, y+1):
            if 0 <= ny <= N-A and not visited[ny][x]:
                new_y = ny if ny == y-1 else y+A
                for nx in range(x, x+B):
                    if map_info[new_y][nx] == 1:
                        break
                else:
                    visited[ny][x] = True
                    q.append((ny, x, cnt+1))

        for nx in (x-1, x+1):
            if 0 <= nx <= M-B and not visited[y][nx]:
                new_x = nx if nx == x-1 else x+B
                for ny in range(y, y + A):
                    if map_info[ny][new_x] == 1:
                        break
                else:
                    visited[y][nx] = True
                    q.append((y, nx, cnt + 1))

    return -1

print(bfs())