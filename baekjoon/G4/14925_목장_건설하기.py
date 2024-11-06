# 241101
def convert(num):
    return 1 if num == '0' else -1

def main():
    from sys import stdin
    new_input = stdin.readline

    M, N = map(int, new_input().split())
    land = [list(map(convert, new_input().split())) for _ in range(M)]

    def has_one():
        for i in range(M):
            for j in range(N):
                if land[i][-1] == 1:
                    return True
        return False


    def find_max():
        L = 1
        for i in range(M-2, -1, -1):
            for j in range(N-2, -1, -1):
                if land[i][j] != -1:
                    temp = []
                    for di, dj in (1, 0), (0, 1), (1, 1):
                        ni, nj = i + di, j + dj
                        val = land[ni][nj]
                        if val == -1:
                            break

                        temp.append(val)
                    else:
                        new_val = min(temp)+1
                        land[i][j] = new_val
                        if new_val > L:
                            L = new_val

        return L

    if not has_one():
        return 0

    return find_max()

print(main())