# 240104
# 248 ms / 33980 KB
from sys import stdin
from heapq import heappush, heappop
new_input = stdin.readline

N, M = map(int, new_input().split())
x1, y1, x2, y2 = map(int, new_input().split())
visited = [[False] * (M+1) for _ in range(N+1)]
class_info = [['0'] * (M+1)]
for _ in range(N):
    class_info.append(['0'] + list(new_input().rstrip()))
cnt = 0
min_heap = [(0, x1, y1)]
visited[x1][y1] = True

while True:
    cnt, x, y = heappop(min_heap)
    if x == x2 and y == y2:
        print(cnt)
        break
    for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
        ny, nx = y+dy, x+dx
        if 0 < ny <= M and 0 < nx <= N and not visited[nx][ny]:
            visited[nx][ny] = True
            heappush(min_heap, (cnt if class_info[nx][ny] == '0' else cnt+1, nx, ny))


# 164 ms / 34004 KB
def cnt_jump(x1, y1, x2, y2):
    from heapq import heappush, heappop

    class_info = [['0'] * (M+1)]
    for _ in range(N):
        class_info.append(['0'] + list(new_input().rstrip()))

    visited = [[False] * (M + 1) for _ in range(N + 1)]
    min_heap = [(0, x1, y1)]
    visited[x1][y1] = True

    while True:
        cnt, x, y = heappop(min_heap)
        if x == x2 and y == y2:
            return cnt

        for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
            ny, nx = y+dy, x+dx

            if 0 < ny <= M and 0 < nx <= N and not visited[nx][ny]:
                visited[nx][ny] = True
                heappush(min_heap, (cnt if class_info[nx][ny] == '0' else cnt+1, nx, ny))


from sys import stdin
new_input = stdin.readline

N, M = map(int, new_input().split())

print(cnt_jump(*map(int, new_input().split())))



# 160 ms / 33212 KB
def cnt_jump(x1, y1, x2, y2):
    from heapq import heappush, heappop

    class_info = [new_input().rstrip() for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    min_heap = [(0, x1, y1)]
    visited[x1][y1] = True

    while True:
        cnt, x, y = heappop(min_heap)
        if x == x2 and y == y2:
            return cnt

        for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
            ny, nx = y+dy, x+dx

            if 0 <= ny < M and 0 <= nx < N and not visited[nx][ny]:
                visited[nx][ny] = True
                heappush(min_heap, (cnt if class_info[nx][ny] == '0' else cnt+1, nx, ny))


from sys import stdin
new_input = stdin.readline

N, M = map(int, new_input().split())

print(cnt_jump(*map(lambda num: int(num)-1, new_input().split())))