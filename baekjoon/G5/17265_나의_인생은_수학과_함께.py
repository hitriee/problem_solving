# 240913
# 31120 KB / 40 ms
def convert(val):
    return int(val) if val.isdigit() else val

def in_range(y, x, N):
    return 0 <= y < N and 0 <= x < N

def main():
    N = int(input())
    arr = [list(map(convert, input().split())) for _ in range(N)]
    max_val, min_val = -1e5, 1e5

    def dfs(y, x, val):
        nonlocal min_val, max_val
        if y == x == N-1:
            if val < min_val:
                min_val = val
            if val > max_val:
                max_val = val
            return

        for dy1, dx1 in (1, 0), (0, 1):
            ny1, nx1 = y + dy1, x + dx1
            if in_range(ny1, nx1, N):
                oper = arr[ny1][nx1]
                for dy2, dx2 in (1, 0), (0, 1):
                    ny2, nx2 = ny1 + dy2, nx1 + dx2
                    if in_range(ny2, nx2, N):
                        num = arr[ny2][nx2]
                        if oper == '+':
                            new_val = val + num
                        elif oper == '-':
                            new_val = val - num
                        else:
                            new_val = val * num

                        dfs(ny2, nx2, new_val)

    dfs(0, 0, arr[0][0])

    return f'{max_val} {min_val}'

print(main())



# 31120 KB / 40 ms
def convert(val):
    return int(val) if val.isdigit() else val

def in_range(y, x, N):
    return 0 <= y < N and 0 <= x < N

def calc_new_val(val, num, oper):
    if oper == '+':
        return val + num
    
    elif oper == '-':
        return val - num
    
    return val * num
    

def main():
    N = int(input())
    arr = [list(map(convert, input().split())) for _ in range(N)]
    max_val, min_val = -1e5, 1e5

    def dfs(y, x, val):
        nonlocal min_val, max_val
        if y == x == N-1:
            if val < min_val:
                min_val = val
            if val > max_val:
                max_val = val
            return

        for dy1, dx1 in (1, 0), (0, 1):
            ny1, nx1 = y + dy1, x + dx1
            if in_range(ny1, nx1, N):
                for dy2, dx2 in (1, 0), (0, 1):
                    ny2, nx2 = ny1 + dy2, nx1 + dx2
                    if in_range(ny2, nx2, N):
                        new_val = calc_new_val(val, arr[ny2][nx2], arr[ny1][nx1])
                        dfs(ny2, nx2, new_val)

    dfs(0, 0, arr[0][0])

    return f'{max_val} {min_val}'

print(main())


# 31120 KB / 40 ms
def convert(val):
    return int(val) if val.isdigit() else val

def in_range(y, x, N):
    return 0 <= y < N and 0 <= x < N

def calc_new_val(val, num, oper):
    if oper == '+':
        return val + num

    elif oper == '-':
        return val - num

    return val * num


def main():
    N = int(input())
    arr = [list(map(convert, input().split())) for _ in range(N)]
    max_val, min_val = -1e5, 1e5

    def dfs(y, x, val):
        nonlocal min_val, max_val
        if y == x == N-1:
            if val < min_val:
                min_val = val
            if val > max_val:
                max_val = val
            return

        for dy1, dx1 in (1, 0), (0, 1):
            ny1, nx1 = y + dy1, x + dx1
            for dy2, dx2 in (1, 0), (0, 1):
                ny2, nx2 = ny1 + dy2, nx1 + dx2
                if in_range(ny2, nx2, N):
                    new_val = calc_new_val(val, arr[ny2][nx2], arr[ny1][nx1])
                    dfs(ny2, nx2, new_val)

    dfs(0, 0, arr[0][0])

    return f'{max_val} {min_val}'

print(main())




# 31120 KB / 40 ms
def convert(val):
    return int(val) if val.isdigit() else val

def in_range(y, x, N):
    return 0 <= y < N and 0 <= x < N

def calc_new_val(val, num, oper):
    if oper == '+':
        return val + num

    elif oper == '-':
        return val - num

    return val * num


def main():
    N = int(input())
    arr = [list(map(convert, input().split())) for _ in range(N)]
    max_val, min_val = -1e4, 1e4

    def dfs(y, x, val):
        nonlocal min_val, max_val
        if y == x == N-1:
            if val < min_val:
                min_val = val
            if val > max_val:
                max_val = val
            return

        for dy1, dx1 in (1, 0), (0, 1):
            ny1, nx1 = y + dy1, x + dx1
            for dy2, dx2 in (1, 0), (0, 1):
                ny2, nx2 = ny1 + dy2, nx1 + dx2
                if in_range(ny2, nx2, N):
                    new_val = calc_new_val(val, arr[ny2][nx2], arr[ny1][nx1])
                    dfs(ny2, nx2, new_val)

    dfs(0, 0, arr[0][0])

    return f'{max_val} {min_val}'

print(main())
