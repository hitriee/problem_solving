# 250317
# 33672 KB / 92 ms
def main():
    from sys import stdin, setrecursionlimit

    new_input = stdin.readline
    setrecursionlimit(2000)
    N, M = map(int, new_input().split())
    info, num_info = {"main": []}, {"main": [0, 0]}
    # info => 상위 폴더 : [(이름, 유형), ...]
    # num_info => 상위 폴더 : [파일 종류, 파일 개수]
    for _ in range(N+M):
        P, F, C = new_input().split()
        if info.get(P):
            info[P].append((F, C))
        else:
            info[P] = [(F, C)]
            num_info[P] = [0, 0]

        if C == "1" and not num_info.get(F):
            num_info[F] = [0, 0]
            info[F] = []

    def dfs(level, name, type_of, cnt, files):
        if type_of == "0":
            return (1, {name})

        dif = 0
        temp = set()
        for new_name, new_type_of in info[name]:
            result = dfs(level+1, new_name, new_type_of, cnt, set())
            dif += result[0]
            temp.update(result[1])

        cnt += dif
        files.update(temp)
        num_info[name][0] += len(files)
        num_info[name][1] += cnt


        return (cnt, files)

    dfs(0, "main", "1", 0, set())

    Q = int(new_input())
    for _ in range(Q):
        folder = new_input().rstrip().split("/")[-1]
        # 폴더 하위의 파일 종류, 개수
        print(*num_info[folder])

    return

main()



# 33656 KB / 88 ms
def main():
    from sys import stdin, setrecursionlimit

    new_input = stdin.readline
    N, M = map(int, new_input().split())
    info, num_info = {"main": []}, {"main": [0, 0]}
    setrecursionlimit(2000)

    for _ in range(N+M):
        P, F, C = new_input().split()
        if info.get(P):
            info[P].append((F, C))
        else:
            info[P] = [(F, C)]
            num_info[P] = [0, 0]

        if C == "1" and not num_info.get(F):
            num_info[F] = [0, 0]
            info[F] = []

    def dfs(name, type_of, cnt, files):
        if type_of == "0":
            return (1, {name})

        dif = 0
        temp = set()
        for new_name, new_type_of in info[name]:
            result = dfs(new_name, new_type_of, cnt, set())
            dif += result[0]
            temp.update(result[1])

        cnt += dif
        files.update(temp)
        num_info[name][0] += len(files)
        num_info[name][1] += cnt


        return (cnt, files)

    dfs("main", "1", 0, set())

    Q = int(new_input())
    for _ in range(Q):
        folder = new_input().rstrip().split("/")[-1]
        print(*num_info[folder])

    return

main()




# 33656 KB / 88 ms
def main():
    from sys import stdin, setrecursionlimit

    def divide_n_conquer(name, type_of, cnt, files):
        if type_of == "0":
            return (1, {name})

        dif = 0
        temp = set()
        for new_name, new_type_of in info[name]:
            result = divide_n_conquer(new_name, new_type_of, cnt, set())
            dif += result[0]
            temp.update(result[1])

        cnt += dif
        files.update(temp)
        num_info[name][0] += len(files)
        num_info[name][1] += cnt


        return (cnt, files)


    new_input = stdin.readline
    N, M = map(int, new_input().split())
    info, num_info = {"main": []}, {"main": [0, 0]}
    setrecursionlimit(2000)

    for _ in range(N+M):
        P, F, C = new_input().split()
        if info.get(P):
            info[P].append((F, C))
        else:
            info[P] = [(F, C)]
            num_info[P] = [0, 0]

        if C == "1" and not num_info.get(F):
            num_info[F] = [0, 0]
            info[F] = []

    divide_n_conquer("main", "1", 0, set())

    Q = int(new_input())
    for _ in range(Q):
        folder = new_input().rstrip().split("/")[-1]
        print(*num_info[folder])

    return

main()