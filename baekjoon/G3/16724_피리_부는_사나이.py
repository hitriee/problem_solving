# 250210
# 106248 KB / 1508 ms
def main():
    from sys import stdin

    def pos_to_num(y, x):
        return y*M + x

    def find(y, x, num):
        new_num = root_of[y][x]
        if new_num == num:
            return num
        new_root = find(*divmod(new_num, M), new_num)
        root_of[y][x] = new_root
        return new_root

    def union(y, x, ny, nx):
        num1, num2 = pos_to_num(y, x), pos_to_num(ny, nx)
        root1, root2 = find(y, x, num1), find(ny, nx, num2)
        if root1 != root2:
            if rank_of[y][x] <= rank_of[ny][nx]:
                rank_of[y][x] += 1
                root_of[y][x] = root2
            else:
                rank_of[ny][nx] += 1
                root_of[ny][nx] = root1

    new_input = stdin.readline
    N, M = map(int, new_input().split())
    map_info = [new_input().rstrip() for _ in range(N)]
    root_of = [[i*M+j for j in range(M)] for i in range(N)]
    rank_of = [[0] * M for _ in range(N)]
    dif = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1),
    }

    for i in range(N):
        for j in range(M):
            ni = i+dif[map_info[i][j]][0]
            nj = j+dif[map_info[i][j]][1]
            union(i, j, ni, nj)

    safe_zone = set()
    for i in range(N):
        for j in range(M):
            safe_zone.add(find(i, j, i*M+j))

    return len(safe_zone)


print(main())




# 106312 KB / 1528 ms
def main():
    from sys import stdin

    def pos_to_num(y, x):
        return y*M + x

    def find(y, x):
        num, new_num = pos_to_num(y, x), root_of[y][x]
        if new_num == num:
            return num
        new_root = find(*divmod(new_num, M))
        root_of[y][x] = new_root
        return new_root

    def union(y, x, ny, nx):
        root1, root2 = find(y, x), find(ny, nx)
        if root1 != root2:
            if rank_of[y][x] <= rank_of[ny][nx]:
                rank_of[y][x] += 1
                root_of[y][x] = root2
            else:
                rank_of[ny][nx] += 1
                root_of[ny][nx] = root1

    new_input = stdin.readline
    N, M = map(int, new_input().split())
    map_info = [new_input().rstrip() for _ in range(N)]
    root_of = [[i*M+j for j in range(M)] for i in range(N)]
    rank_of = [[0] * M for _ in range(N)]
    dif = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1),
    }

    for i in range(N):
        for j in range(M):
            ni = i+dif[map_info[i][j]][0]
            nj = j+dif[map_info[i][j]][1]
            union(i, j, ni, nj)

    safe_zone = set()
    for i in range(N):
        for j in range(M):
            safe_zone.add(find(i, j))

    return len(safe_zone)


print(main())



# 105348 KB / 712 ms
def main():
    from sys import stdin

    def find(num):
        new_num = root_of[num]
        if new_num == num:
            return num
        new_root = find(new_num)
        root_of[num] = new_root
        return new_root

    def union(num1, num2):
        root1, root2 = find(num1), find(num2)
        if root1 != root2:
            if rank_of[num1] <= rank_of[num2]:
                rank_of[num1] += 1
                root_of[num1] = root2
            else:
                rank_of[num2] += 1
                root_of[num2] = root1

    new_input = stdin.readline
    N, M = map(int, new_input().split())
    limit = N*M
    map_info = ''
    for _ in range(N):
        map_info += new_input().rstrip()

    root_of, rank_of = list(range(limit)), [0] * limit
    dif = {
        'U': -M,
        'D': M,
        'L': -1,
        'R': 1,
    }

    for i in range(limit):
        union(i, i+dif[map_info[i]])

    safe_zone = set()
    for i in range(limit):
        safe_zone.add(find(i))

    return len(safe_zone)


print(main())




# 105348 KB / 696 ms
def main():
    from sys import stdin

    def find(num):
        new_num = root_of[num]
        if new_num == num:
            return num
        new_root = find(new_num)
        root_of[num] = new_root
        return new_root

    def union(num1, num2):
        root1, root2 = find(num1), find(num2)
        if root1 != root2:
            if rank_of[num1] <= rank_of[num2]:
                rank_of[num1] += 1
                root_of[num1] = root2
            else:
                rank_of[num2] += 1
                root_of[num2] = root1

    new_input = stdin.readline
    N, M = map(int, new_input().split())
    limit = N*M
    map_info = ''.join([new_input().rstrip() for _ in range(N)])
    root_of, rank_of = list(range(limit)), [0] * limit
    dif = {
        'U': -M,
        'D': M,
        'L': -1,
        'R': 1,
    }

    for i in range(limit):
        union(i, i+dif[map_info[i]])

    safe_zone = set(find(i) for i in range(limit))

    return len(safe_zone)


print(main())