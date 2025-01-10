# 250110
# 32412 KB / 252 ms
def main():
    N, M = map(int, input().split())
    office = [list(map(int, input().split())) for _ in range(N)]
    camera_list = []
    visited = [[0] * M for _ in range(N)]
    dy, dx = (-1, 0, 1, 0), (0, 1, 0, -1)
    empty_area = N*M
    for i in range(N):
        for j in range(M):
            camera_type = office[i][j]
            if 1 <= camera_type <= 5:
                camera_list.append((i, j, camera_type))
            elif camera_type == 6:
                empty_area -= 1

    limit = len(camera_list)
    min_cnt = empty_area - limit

    def cnt_around(level, cnt, y, x, directions):
        length, total = len(directions), 0
        last = []
        for direction in directions:
            ny, nx = y+dy[direction], x+dx[direction]
            empty_cnt = 0
            while 0 <= ny < N and 0 <= nx < M and office[ny][nx] != 6:
                if office[ny][nx] == 0 and visited[ny][nx] == 0:
                    empty_cnt += 1
                visited[ny][nx] += 1
                ny, nx = ny+dy[direction], nx+dx[direction]
            total += empty_cnt
            last.append((ny, nx))

        dfs(level+1, cnt-total)

        for i in range(length):
            direction = directions[i]
            ny, nx = last[i][0]-dy[direction], last[i][1]-dx[direction]
            while ny != y or nx != x:
                visited[ny][nx] -= 1
                ny, nx = ny-dy[direction], nx-dx[direction]


    def dfs(level, cnt):
        nonlocal min_cnt
        if level == limit:
            if cnt < min_cnt:
                min_cnt = cnt
            return

        y, x, camera_type = camera_list[level]
        if camera_type == 5:
            directions = list(range(4))
            cnt_around(level, cnt, y, x, directions)

        elif camera_type == 2:
            for i in range(2):
                directions = [i, i+2]
                cnt_around(level, cnt, y, x, directions)
        else:
            for i in range(4):
                if camera_type == 1:
                    directions = [i]
                elif camera_type == 3:
                    directions = [i, (i+1)%4]
                else:
                    directions = list(set(range(4))-{i})

                cnt_around(level, cnt, y, x, directions)

    dfs(0, min_cnt)

    return min_cnt

print(main())



# 32412 KB / 252 ms
def main():
    N, M = map(int, input().split())
    office = [list(map(int, input().split())) for _ in range(N)]
    camera_list = []
    visited = [[0] * M for _ in range(N)]
    dy, dx = (-1, 0, 1, 0), (0, 1, 0, -1)
    min_cnt = N*M
    all_directions = range(4)

    for i in range(N):
        for j in range(M):
            camera_type = office[i][j]
            if camera_type != 0:
                min_cnt -= 1
                if camera_type <= 5:
                    camera_list.append((i, j, camera_type))

    limit = len(camera_list)

    def cnt_around(level, cnt, y, x, directions):
        length, total = len(directions), 0
        last = []
        for direction in directions:
            ny, nx = y+dy[direction], x+dx[direction]
            empty_cnt = 0
            while 0 <= ny < N and 0 <= nx < M and office[ny][nx] != 6:
                if office[ny][nx] == 0 and visited[ny][nx] == 0:
                    empty_cnt += 1
                visited[ny][nx] += 1
                ny, nx = ny+dy[direction], nx+dx[direction]
            total += empty_cnt
            last.append((ny, nx))

        dfs(level+1, cnt-total)

        for i in range(length):
            direction = directions[i]
            ny, nx = last[i][0]-dy[direction], last[i][1]-dx[direction]
            while ny != y or nx != x:
                visited[ny][nx] -= 1
                ny, nx = ny-dy[direction], nx-dx[direction]


    def dfs(level, cnt):
        nonlocal min_cnt
        if level == limit:
            if cnt < min_cnt:
                min_cnt = cnt
            return

        y, x, camera_type = camera_list[level]
        if camera_type == 5:
            directions = list(all_directions)
            cnt_around(level, cnt, y, x, directions)

        elif camera_type == 2:
            for i in range(2):
                directions = [i, i+2]
                cnt_around(level, cnt, y, x, directions)
        else:
            for i in range(4):
                if camera_type == 1:
                    directions = [i]
                elif camera_type == 3:
                    directions = [i, (i+1)%4]
                else:
                    directions = list(set(all_directions)-{i})

                cnt_around(level, cnt, y, x, directions)

    dfs(0, min_cnt)

    return min_cnt

print(main())