# 251001
# 33608 KB / 56 ms
def main():
    from sys import stdin, setrecursionlimit

    new_input = stdin.readline
    setrecursionlimit(1100)

    N = int(new_input())
    arr, path = [], []
    found = False
    visited = [[False] * 10 for _ in range(N+1)]

    for _ in range(N):
        _, *kind_of = map(int, new_input().split())
        arr.append(kind_of)


    def dfs(level, before):
        nonlocal found

        if level == N:
            found = True
            print(*path, sep='\n')
            return

        if visited[level][before]:
            return
        visited[level][before] = True

        for i in arr[level]:
            if before != i:
                path.append(i)
                dfs(level+1, i)
                if found:
                    return
                path.pop()

    dfs(0, 0)

    if not found:
        print('-1')

main()