#230423
# bfs
from collections import deque
from sys import stdin
to_int = lambda : map(int, stdin.readline().split())
H, W = to_int()
pixel_table = [list(to_int()) for _ in range(H)]
Q = int(stdin.readline())
for _ in range(Q):
    i, j, c = to_int()
    i -= 1
    j -= 1
    ref = pixel_table[i][j]
    if ref != c:
        q = deque()
        q.append((i, j))
        pixel_table[i][j] = c
        while q:
            y, x = q.popleft()
            for dy, dx in (1, 0), (0, 1), (-1, 0), (0, -1):
                ny, nx = y+dy, x+dx
                if 0 <= ny < H and 0 <= nx < W:
                    if pixel_table[ny][nx] == ref:
                        q.append((ny, nx))
                        pixel_table[ny][nx] = c
for i in range(H):
    print(*pixel_table[i])

    
    
# 함수화
def final_image():
    def convert_pixel():
        from collections import deque
        ref = pixel_table[i][j]
        if ref != c:
            q = deque()
            q.append((i, j))
            pixel_table[i][j] = c
            while q:
                y, x = q.popleft()
                for dy, dx in (1, 0), (0, 1), (-1, 0), (0, -1):
                    ny, nx = y+dy, x+dx
                    if 0 <= ny < H and 0 <= nx < W:
                        if pixel_table[ny][nx] == ref:
                            q.append((ny, nx))
                            pixel_table[ny][nx] = c
    
    from sys import stdin
    to_int = lambda : map(int, stdin.readline().split())
    H, W = to_int()
    pixel_table = [list(to_int()) for _ in range(H)]
    Q = int(stdin.readline())
    for _ in range(Q):
        i, j, c = to_int()
        i -= 1
        j -= 1
        convert_pixel()
    for i in range(H):
        print(*pixel_table[i])
final_image()



# 함수화2
def final_image():
    from collections import deque
    from sys import stdin
    to_int = lambda : map(int, stdin.readline().split())
    H, W = to_int()
    pixel_table = [list(to_int()) for _ in range(H)]
    Q = int(stdin.readline())
    for _ in range(Q):
        i, j, c = to_int()
        i -= 1
        j -= 1
        ref = pixel_table[i][j]
        if ref != c:
            q = deque()
            q.append((i, j))
            pixel_table[i][j] = c
            while q:
                y, x = q.popleft()
                for dy, dx in (1, 0), (0, 1), (-1, 0), (0, -1):
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < H and 0 <= nx < W:
                        if pixel_table[ny][nx] == ref:
                            q.append((ny, nx))
                            pixel_table[ny][nx] = c
    for i in range(H):
        print(*pixel_table[i])
final_image()
