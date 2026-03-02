# 260302
# 35508 KB / 48 ms
def main():
    from heapq import heappush, heappop

    N = int(input())
    info = [input() for _ in range(N)]
    dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]


    def find_door():
        start, end = (), ()
        for i in range(N):
            for j in range(N):
                if info[i][j] == '#':
                    if start:
                        end = (i, j)
                    else:
                        start = (i, j)

        return (start, end)

    start, end = find_door()
    heap = [(0, i, *start) for i in range(4)]
    visited = [[[False] * 4 for _ in range(N)] for _ in range(N)]

    while heap:
        cnt, d_i, y, x = heappop(heap)
        if (y, x) == end:
            return cnt


        ny, nx = y+dy[d_i], x+dx[d_i]
        if 0 <= ny < N and 0 <= nx < N:
            if not visited[ny][nx][d_i] and info[ny][nx] != '*':
                visited[ny][nx][d_i] = True
                heappush(heap, (cnt, d_i, ny, nx))
                if info[ny][nx] == '!':
                    heappush(heap, (cnt+1, (d_i+1)%4, ny, nx))
                    heappush(heap, (cnt+1, (d_i+3)%4, ny, nx))

print(main())





