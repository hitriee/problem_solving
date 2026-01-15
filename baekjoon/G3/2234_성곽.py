# 260115
# 35044 KB / 60 ms
def main():
    from collections import deque

    M, N = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dy = [0, -1, 0, 1]
    dx = [-1, 0, 1, 0]


    q = deque()
    visited = [[0] * M for _ in range(N)]
    max_area1 = max_area2 = cnt = 0
    walls = [1, 2, 4, 8]
    area_arr = [0]

    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0:
                cnt += 1
                visited[i][j] = cnt
                area = 1
                q.append((i, j))
                while q:
                    y, x = q.popleft()
                    val = arr[y][x]
                    for idx in range(4):
                        if val & walls[idx] == 0:
                            ny, nx = y+dy[idx], x+dx[idx]
                            if visited[ny][nx] == 0:
                                area += 1
                                visited[ny][nx] = cnt
                                q.append((ny, nx))

                area_arr.append(area)

                if max_area1 < area:
                    max_area1 = area

    for i in range(N):
        for j in range(M):
            val = arr[i][j]
            for idx in range(2, 4):
                if val & walls[idx]:
                    ni, nj = i+dy[idx], j+dx[idx]
                    if ni < N and nj < M and visited[i][j] != visited[ni][nj]:
                        total = area_arr[visited[i][j]] + area_arr[visited[ni][nj]]
                        if total > max_area2:
                            max_area2 = total

    return f'{cnt}\n{max_area1}\n{max_area2}'


print(main())