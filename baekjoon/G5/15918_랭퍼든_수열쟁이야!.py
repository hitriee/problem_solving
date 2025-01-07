# 240107
# 32412 KB / 1660 ms
def main():
    n, x, y = map(int, input().split())
    cnt = 0
    arr = [0] * (2*n)
    dif = y-x-1
    arr[x-1] = arr[y-1] = dif
    visited = [False] * (n+1)
    visited[dif] = True

    def fill_arr(level):
        nonlocal cnt
        if level == 2*n:
            cnt += 1
            return

        if arr[level] == 0:
            for i in range(1, n+1):
                if not visited[i] and level+i+1 < 2*n and arr[level+i+1] == 0:
                    visited[i] = True
                    arr[level] = arr[level+i+1] = i
                    fill_arr(level+1)
                    arr[level] = arr[level + i + 1] = 0
                    visited[i] = False
        else:
            fill_arr(level + 1)

    fill_arr(0)
    return cnt

print(main())



# 32412 KB / 4352 ms
def main():
    n, x, y = map(int, input().split())
    cnt = 0
    arr = [0] * (2*n)
    dif = y-x-1
    arr[x-1] = arr[y-1] = dif

    def fill_arr(level):
        nonlocal cnt
        if level == n+1:
            cnt += 1
            return

        if level == dif:
            fill_arr(level + 1)
        else:
            for i in range(2*n-level-1):
                if arr[i] == arr[level+i+1] == 0:
                    arr[i] = arr[level+i+1] = level
                    fill_arr(level+1)
                    arr[i] = arr[level + i + 1] = 0

    fill_arr(1)
    return cnt

print(main())