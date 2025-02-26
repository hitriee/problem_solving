#230630
# 250225
# 35004 KB / 1536 ms
def main():
    from collections import deque

    def initiate():
        for i in range(N):
            for j in range(M):
                val = institute[i][j]
                if val == '2':
                    virus.append((i, j))
                elif val == '0':
                    empty.append((i, j))

    def spread_virus():
        q = deque(virus)
        cnt = 0
        visited = [[False] * M for _ in range(N)]

        while q:
            y, x = q.popleft()
            for i in range(4):
                ny, nx = y+dy[i], x+dx[i]
                if 0 <= ny < N and 0 <= nx < M:
                    if institute[ny][nx] == '0' and not visited[ny][nx]:
                        cnt += 1
                        visited[ny][nx] = True
                        q.append((ny, nx))


        return cnt

    def build_wall(level, num):
        nonlocal max_size

        if level == 3:
            size = empty_cnt - spread_virus()
            if size > max_size:
                max_size = size
            return

        for i in range(num, empty_cnt):
            y, x = empty[i]
            institute[y][x] = '1'
            build_wall(level + 1, i + 1)
            institute[y][x] = '0'


    N, M = map(int, input().split())
    institute = [input().split() for _ in range(N)]
    virus, empty = [], []
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    initiate()
    empty_cnt = len(empty)
    max_size = 0
    build_wall(0, 0)

    return max_size - 3

print(main())





# 35004 KB / 1376 ms
def main():
    from collections import deque

    def initiate():
        for i in range(N):
            for j in range(M):
                val = institute[i][j]
                if val == '2':
                    virus.append((i, j))
                elif val == '0':
                    empty.append((i, j))

    def spread_virus():
        q = deque(virus)
        cnt = 0
        visited = [[False] * M for _ in range(N)]

        while q:
            y, x = q.popleft()
            if cnt >= min_cnt:
                return min_cnt

            for i in range(4):
                ny, nx = y+dy[i], x+dx[i]
                if 0 <= ny < N and 0 <= nx < M:
                    if institute[ny][nx] == '0' and not visited[ny][nx]:
                        cnt += 1
                        visited[ny][nx] = True
                        q.append((ny, nx))


        return cnt

    def build_wall(level, num):
        nonlocal min_cnt

        if level == 3:
            min_cnt = spread_virus()
            return

        for i in range(num, empty_cnt):
            y, x = empty[i]
            institute[y][x] = '1'
            build_wall(level + 1, i + 1)
            institute[y][x] = '0'


    N, M = map(int, input().split())
    institute = [input().split() for _ in range(N)]
    virus, empty = [], []
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    initiate()
    min_cnt = empty_cnt = len(empty)
    build_wall(0, 0)

    return empty_cnt - min_cnt - 3

print(main())




# 35036 KB / 1380 ms
def main():
    from collections import deque

    def initiate():
        for i in range(N):
            for j in range(M):
                val = institute[i][j]
                if val == '2':
                    virus.append((i, j))
                elif val == '0':
                    empty.append((i, j))

    def spread_virus(min_cnt):
        q = deque(virus)
        cnt = 0
        visited = [[False] * M for _ in range(N)]

        while q:
            y, x = q.popleft()
            if cnt >= min_cnt:
                return min_cnt

            for i in range(4):
                ny, nx = y+dy[i], x+dx[i]
                if 0 <= ny < N and 0 <= nx < M:
                    if institute[ny][nx] == '0' and not visited[ny][nx]:
                        cnt += 1
                        visited[ny][nx] = True
                        q.append((ny, nx))


        return cnt

    def build_wall():
        min_cnt = empty_cnt

        for i in range(empty_cnt-2):
            y1, x1 = empty[i]
            institute[y1][x1] = '1'
            for j in range(i+1, empty_cnt-1):
                y2, x2 = empty[j]
                institute[y2][x2] = '1'
                for k in range(j+1, empty_cnt):
                    y3, x3 = empty[k]
                    institute[y3][x3] = '1'
                    min_cnt = spread_virus(min_cnt)
                    institute[y3][x3] = '0'
                institute[y2][x2] = '0'
            institute[y1][x1] = '0'

        return min_cnt

    N, M = map(int, input().split())
    institute = [input().split() for _ in range(N)]
    virus, empty = [], []
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    initiate()
    empty_cnt = len(empty)

    return empty_cnt - build_wall() - 3

print(main())


