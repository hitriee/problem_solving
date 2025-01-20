# 250120
# 564388 KB / 3732 ms (Pypy3)
def main():
    from sys import stdin
    from collections import deque

    def int_input():
        return map(int, stdin.readline().split())

    N, M = int_input()
    lab = [list(int_input()) for _ in range(N)]

    dy, dx = (0, 0, -1, 1), (-1, 1, 0, 0)
    visited = [[[False] * 4 for _ in range(M)] for _ in range(N)]
    converted_d = [[], [1, 0, 2, 3], [0, 1, 3, 2], [3, 2, 1, 0], [2, 3, 0, 1]]

    def check_flow():
        while q:
            y, x, d = q.popleft()
            ny, nx = y+dy[d], x+dx[d]
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx][d]:
                visited[ny][nx][d] = True
                type_of = lab[ny][nx]

                if type_of != 9:
                    nd = d if type_of == 0 else converted_d[type_of][d]
                    q.append((ny, nx, nd))

    def find_ac():
        for i in range(N):
            for j in range(M):
                if lab[i][j] == 9:
                    for k in range(4):
                        visited[i][j][k] = True
                        q.append((i, j, k))
                        check_flow()


    def cnt_possible():
        cnt = 0
        for i in range(N):
            for j in range(M):
                for k in range(4):
                    if visited[i][j][k]:
                        cnt += 1
                        break

        return cnt


    q = deque()
    find_ac()

    return cnt_possible()


print(main())




# 588356 KB / 3540 ms (Pypy3)
def main():
    from sys import stdin
    from collections import deque

    def int_input():
        return map(int, stdin.readline().split())

    N, M = int_input()
    lab = [list(int_input()) for _ in range(N)]

    dy, dx = (0, 0, -1, 1), (-1, 1, 0, 0)
    visited = [[[False] * 4 for _ in range(M)] for _ in range(N)]
    converted_d = [[], [1, 0, 2, 3], [0, 1, 3, 2], [3, 2, 1, 0], [2, 3, 0, 1]]

    def check_flow():
        while q:
            y, x, d = q.popleft()
            ny, nx = y+dy[d], x+dx[d]
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx][d]:
                visited[ny][nx][d] = True
                type_of = lab[ny][nx]

                if type_of != 9:
                    nd = d if type_of == 0 else converted_d[type_of][d]
                    q.append((ny, nx, nd))

    def find_ac():
        for i in range(N):
            for j in range(M):
                if lab[i][j] == 9:
                    for k in range(4):
                        visited[i][j][k] = True
                        q.append((i, j, k))
                    check_flow()


    def cnt_possible():
        cnt = 0
        for i in range(N):
            for j in range(M):
                for k in range(4):
                    if visited[i][j][k]:
                        cnt += 1
                        break

        return cnt


    q = deque()
    find_ac()

    return cnt_possible()


print(main())



# 623252 KB / 3896 ms (Pypy 3)
def main():
    from sys import stdin
    from collections import deque

    def int_input():
        return map(int, stdin.readline().split())

    N, M = int_input()
    lab = [list(int_input()) for _ in range(N)]

    dy, dx = (0, 0, -1, 1), (-1, 1, 0, 0)
    visited = [[[False] * 4 for _ in range(M)] for _ in range(N)]
    converted_d = [[], [1, 0, 2, 3], [0, 1, 3, 2], [3, 2, 1, 0], [2, 3, 0, 1]]
    possible = [[0] * M for _ in range(N)]

    def check_flow():
        while q:
            y, x, d = q.popleft()
            ny, nx = y+dy[d], x+dx[d]
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx][d]:
                visited[ny][nx][d] = True
                if possible[ny][nx] == 0:
                    possible[ny][nx] = 1

                type_of = lab[ny][nx]

                if type_of != 9:
                    nd = d if type_of == 0 else converted_d[type_of][d]
                    q.append((ny, nx, nd))

    def find_ac():
        for i in range(N):
            for j in range(M):
                if lab[i][j] == 9:
                    possible[i][j] = 1
                    visited[i][j][0] = True
                    for k in range(4):
                        q.append((i, j, k))
                    check_flow()


    def cnt_possible():
        cnt = 0
        for i in range(N):
            cnt += sum(possible[i])

        return cnt


    q = deque()
    find_ac()

    return cnt_possible()


print(main())