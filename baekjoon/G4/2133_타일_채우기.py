#230719
N = int(input())
if N%2:
    print(0)
else:
    path = []
    case = 0
    def dfs(num):
        global case
        if num > N:
            return
        elif num == N:
            case += 2**(path.count(1)//2)
            return
        for j in (1, 2):
            path.append(j)
            dfs(num+j)
            path.pop()
    dfs(0)
    print(case)


#
N = int(input())
if N%2:
    print(0)
else:
    case = 0
    def dfs(num, cnt):
        global case
        if num > N:
            return
        elif num == N:
            case += 2**(cnt//2)
            return
        dfs(num+1, cnt+1)
        dfs(num+2, cnt)

    dfs(0, 0)
    print(case)


#
def fill_tile():
    N = int(input())
    if N % 2:
        return 0

    case = 0
    def dfs(num, cnt):
        nonlocal case
        if num > N:
            return
        elif num == N:
            case += 2 ** (cnt // 2)
            return
        dfs(num + 1, cnt + 1)
        dfs(num + 2, cnt)

    dfs(0, 0)
    return case

print(fill_tile())
