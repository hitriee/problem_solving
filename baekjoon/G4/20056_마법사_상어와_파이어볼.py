# 240314
# 1132 ms / 33164 KB
N, M, K = map(int, input().split())
dr, dc = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]
arr = [[[] for _ in range(N)] for _ in range(N)]
d_list = [[0, 2, 4, 6], [1, 3, 5, 7]]

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    arr[r-1][c-1].append((m, s, d))

def move_balls():
    for r in range(N):
        for c in range(N):
            if arr[r][c]:
                for m, s, d in arr[r][c]:
                    nr, nc = (r+dr[d]*s)%N, (c+dc[d]*s)%N
                    new_arr[nr][nc].append((m, s, d))

def split_balls():
    for r in range(N):
        for c in range(N):
            length = len(new_arr[r][c])
            if length < 2:
                arr[r][c] = new_arr[r][c][:]
            else:
                total_m = total_s = total_remain_d = 0
                for fireball in new_arr[r][c]:
                    m, s, d = fireball
                    total_m += m
                    total_s += s
                    total_remain_d += d%2

                if total_remain_d == 0 or total_remain_d == length:
                    idx = 0
                else:
                    idx = 1

                nm, ns = total_m//5, total_s//length
                if nm:
                    arr[r][c] = [(nm, ns, nd) for nd in d_list[idx]]
                else:
                    arr[r][c].clear()

for _ in range(K):
    new_arr = [[[] for _ in range(N)] for _ in range(N)]
    move_balls()
    split_balls()

total_m = 0
for r in range(N):
    for c in range(N):
        if arr[r][c]:
            for m, _, _ in arr[r][c]:
                total_m += m

print(total_m)



# 1032 ms / 33164 KB
N, M, K = map(int, input().split())
dr, dc = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]
arr = [[[] for _ in range(N)] for _ in range(N)]
d_list = [[0, 2, 4, 6], [1, 3, 5, 7]]
positions, new_positions = set(), set()

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    arr[r-1][c-1].append((m, s, d))
    positions.add((r-1, c-1))

def move_balls():
    for r, c in positions:
        for m, s, d in arr[r][c]:
            nr, nc = (r+dr[d]*s)%N, (c+dc[d]*s)%N
            new_arr[nr][nc].append((m, s, d))
            new_positions.add((nr, nc))

def split_balls():
    for r, c in new_positions:
        length = len(new_arr[r][c])
        positions.add((r, c))
        if length == 1:
            arr[r][c] = new_arr[r][c][:]
        else:
            total_m = total_s = total_remain_d = 0
            for fireball in new_arr[r][c]:
                m, s, d = fireball
                total_m += m
                total_s += s
                total_remain_d += d%2

            if total_remain_d == 0 or total_remain_d == length:
                idx = 0
            else:
                idx = 1

            nm, ns = total_m//5, total_s//length
            if nm:
                arr[r][c] = [(nm, ns, nd) for nd in d_list[idx]]
            else:
                arr[r][c].clear()

for _ in range(K):
    new_arr = [[[] for _ in range(N)] for _ in range(N)]
    new_positions.clear()
    move_balls()
    positions.clear()
    arr = [[[] for _ in range(N)] for _ in range(N)]
    split_balls()

total_m = 0
for r, c in positions:
    for m, _, _ in arr[r][c]:
        total_m += m

print(total_m)

# 748 ms / 33296 KB
N, M, K = map(int, input().split())
dr, dc = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]
arr = [[[] for _ in range(N)] for _ in range(N)]
d_list = [[0, 2, 4, 6], [1, 3, 5, 7]]
positions = set()

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    arr[r-1][c-1].append((m, s, d))
    positions.add((r-1, c-1))

def move_balls():
    for r, c in positions:
        for m, s, d in arr[r][c]:
            nr, nc = (r+dr[d]*s)%N, (c+dc[d]*s)%N
            new_arr[nr][nc].append((m, s, d))
            new_positions.add((nr, nc))

def split_balls():
    for r, c in new_positions:
        length = len(new_arr[r][c])
        positions.add((r, c))
        if length >= 2:
            total_m = total_s = total_remain_d = 0
            for fireball in new_arr[r][c]:
                m, s, d = fireball
                total_m += m
                total_s += s
                total_remain_d += d%2

            if total_remain_d == 0 or total_remain_d == length:
                idx = 0
            else:
                idx = 1

            nm, ns = total_m//5, total_s//length
            if nm:
                new_arr[r][c] = [(nm, ns, nd) for nd in d_list[idx]]
            else:
                new_arr[r][c].clear()

for _ in range(K):
    new_arr = [[[] for _ in range(N)] for _ in range(N)]
    new_positions = set()
    move_balls()
    positions.clear()
    split_balls()
    arr = [new_arr[i][:] for i in range(N)]

total_m = 0
for r, c in positions:
    for m, _, _ in arr[r][c]:
        total_m += m

print(total_m)

# 756 ms / 33164 KB
N, M, K = map(int, input().split())
dr, dc = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]
arr = [[[] for _ in range(N)] for _ in range(N)]
d_list = [[0, 2, 4, 6], [1, 3, 5, 7]]
positions = set()

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    arr[r-1][c-1].append((m, s, d))
    positions.add((r-1, c-1))

def move_balls():
    for r, c in positions:
        for m, s, d in arr[r][c]:
            nr, nc = (r+dr[d]*s)%N, (c+dc[d]*s)%N
            new_arr[nr][nc].append((m, s, d))
            new_positions.add((nr, nc))

def split_balls():
    for r, c in new_positions:
        length = len(new_arr[r][c])
        if length == 1:
            positions.add((r, c))
        else:
            total_m = total_s = total_remain_d = 0
            for fireball in new_arr[r][c]:
                m, s, d = fireball
                total_m += m
                total_s += s
                total_remain_d += d%2

            if total_remain_d == 0 or total_remain_d == length:
                idx = 0
            else:
                idx = 1

            nm, ns = total_m//5, total_s//length
            if nm:
                new_arr[r][c] = [(nm, ns, nd) for nd in d_list[idx]]
                positions.add((r, c))
            else:
                new_arr[r][c].clear()


for _ in range(K):
    new_arr = [[[] for _ in range(N)] for _ in range(N)]
    new_positions = set()
    move_balls()
    positions.clear()
    split_balls()
    arr = [new_arr[i][:] for i in range(N)]

total_m = 0
for r, c in positions:
    for m, _, _ in arr[r][c]:
        total_m += m

print(total_m)