# 250305
# 40224 KB / 40 ms
def main():
    N = int(input())
    if N == 1:
        return '0\n1'

    info = [[N]]
    parent = [0] * N
    for level in range(1, N):
        info.append([])
        for now in info[level-1]:
            if now == 1:
                path = ['1']
                for cnt in range(level-2, -1, -1):
                    now = parent[now]
                    path.append(str(now))
                return f'{level-1}\n{" ".join(path[::-1])}'

            for i in (3, 2):
                quot = now//i
                if now % i == 0 and parent[quot] == 0:
                    parent[quot] = now
                    info[level].append(quot)

            if parent[now-1] == 0:
                parent[now-1] = now
                info[level].append(now-1)

    return f'{N-1}\n{" ".join(list(map(str,range(N, 0, -1))))}'

print(main())





# 40224 KB / 40 ms
def main():
    N = int(input())
    if N == 1:
        return '0\n1'

    def search_tree(now):
        path = ['1']
        for cnt in range(level - 2, -1, -1):
            now = parent[now]
            path.append(str(now))
        return f'{level - 1}\n{" ".join(path[::-1])}'

    def append_next():
        pass

    info = [[N]]
    parent = [0] * N
    for level in range(1, N):
        info.append([])
        for now in info[level-1]:
            if now == 1:
                return search_tree(1)

            append_next()

    return f'{N-1}\n{" ".join(list(map(str,range(N, 0, -1))))}'

print(main())