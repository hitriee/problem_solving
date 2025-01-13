# 250113
# 34984 KB / 68 ms
def main():
    from sys import stdin
    from collections import deque

    new_input = stdin.readline
    dy, dx = [], []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if j != 0 or i != 0:
                dy.append(i)
                dx.append(j)

    def bfs(*initial):
        q = deque()
        q.append(initial)
        while q:
            y, x = q.popleft()
            for i in range(8):
                ny, nx = y+dy[i], x+dx[i]
                if 0 <= ny < h and 0 <= nx < w:
                    if area[ny][nx] == '1' and not visited[ny][nx]:
                        visited[ny][nx] = True
                        q.append((ny, nx))


    while True:
        w, h = map(int, new_input().split())
        if w == 0:
            return

        area = [new_input().split() for _ in range(h)]
        visited = [[False] * w for _ in range(h)]
        cnt = 0

        for i in range(h):
            for j in range(w):
                if area[i][j] == '1' and not visited[i][j]:
                    cnt += 1
                    bfs(i, j)

        print(cnt)

main()