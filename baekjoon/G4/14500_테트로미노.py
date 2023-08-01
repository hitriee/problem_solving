#230801
from sys import stdin
def to_int(): return map(int, stdin.readline().split())
N, M = to_int()
paper = [list(to_int()) for _ in range(N)]
max_total = 0
one_direct = [(1, 0), (1, 1), (1, 2), (0, 3), (-1, 0), (-1, 1), (-1, 2)]
two_direct = [(1, -1), (1, 0), (1, 1), (0, 2), (-1, -1), (-1, 0), (-1, 1)]
# 가로 3, 4
for i in range(N):
    total = sum(paper[i][:2])
    for j in range(M-2):
        total += paper[i][j+2]
        for di, dj in one_direct:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < M:
                new_total = total + paper[ni][nj]
                if new_total > max_total:
                    max_total = new_total
        total -= paper[i][j]

# 세로 3, 4
for j in range(M):
    total = paper[0][j] + paper[1][j]
    for i in range(N-2):
        total += paper[i+2][j]
        for dj, di in one_direct:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < M:
                new_total = total + paper[ni][nj]
                if new_total > max_total:
                    max_total = new_total
        total -= paper[i][j]
# 가로 2
for i in range(N):
    total = paper[i][0]
    for j in range(M-1):
        total += paper[i][j+1]
        for di, dj in two_direct:
            ni, nj = i+di, j+dj
            if 0 <= ni < N-1 and 0 <= nj < M-1:
                new_total = total + sum(paper[ni][nj:nj+2])
                if new_total > max_total:
                    max_total = new_total
        total -= paper[i][j]
# 세로 2
for j in range(M):
    total = paper[0][j]
    for i in range(N-1):
        total += paper[i+1][j]
        for dj, di in two_direct:
            ni, nj = i+di, j+dj
            if 0 <= ni < N-1 and 0 <= nj < M-1:
                new_total = total + paper[ni][nj] + paper[ni+1][nj]
                if new_total > max_total:
                    max_total = new_total
        total -= paper[i][j]

print(max_total)


#
from sys import stdin
def to_int(): return map(int, stdin.readline().split())
N, M = to_int()
max_total = 0
max_num, max_two = [0]*2, [0]*2
paper = []
one_direct = [(1, 0), (1, 1), (1, 2), (0, 3), (-1, 0), (-1, 1), (-1, 2)]
two_direct = [(1, -1), (1, 0), (1, 1), (0, 2), (-1, -1), (-1, 0), (-1, 1)]

for _ in range(N):
    paper.append(list(to_int()))
    temp_total = paper[-1][0]
    for j in range(M-1):
        num = paper[-1][j]
        temp_total += paper[-1][j+1]
        if max_num[0] < num:
            max_num[0] = num
        if max_two[0] < temp_total:
            max_two[0] = temp_total
        temp_total -= num

for j in range(M):
    temp_total = paper[0][j]
    for i in range(N-1):
        num = paper[i][j]
        temp_total += paper[i+1][j]
        if max_num[1] < num:
            max_num[1] = num
        if max_two[1] < temp_total:
            max_two[1] = temp_total
        temp_total -= num



# 가로 3, 4
for i in range(N):
    total = sum(paper[i][:2])
    for j in range(M-2):
        total += paper[i][j+2]
        if max_total - total < max_num[0]:
            for di, dj in one_direct:
                ni, nj = i+di, j+dj
                if 0 <= ni < N and 0 <= nj < M:
                    new_total = total + paper[ni][nj]
                    if new_total > max_total:
                        max_total = new_total
        total -= paper[i][j]

# 세로 3, 4
for j in range(M):
    total = paper[0][j] + paper[1][j]
    for i in range(N-2):
        total += paper[i+2][j]
        if max_total - total < max_num[1]:
            for dj, di in one_direct:
                ni, nj = i+di, j+dj
                if 0 <= ni < N and 0 <= nj < M:
                    new_total = total + paper[ni][nj]
                    if new_total > max_total:
                        max_total = new_total
        total -= paper[i][j]
# 가로 2
for i in range(N):
    total = paper[i][0]
    for j in range(M-1):
        total += paper[i][j+1]
        if max_total - total < max_two[0]:
            for di, dj in two_direct:
                ni, nj = i+di, j+dj
                if 0 <= ni < N-1 and 0 <= nj < M-1:
                    new_total = total + sum(paper[ni][nj:nj+2])
                    if new_total > max_total:
                        max_total = new_total
        total -= paper[i][j]
# 세로 2
for j in range(M):
    total = paper[0][j]
    for i in range(N-1):
        total += paper[i+1][j]
        if max_total - total < max_two[1]:
            for dj, di in two_direct:
                ni, nj = i+di, j+dj
                if 0 <= ni < N-1 and 0 <= nj < M-1:
                    new_total = total + paper[ni][nj] + paper[ni+1][nj]
                    if new_total > max_total:
                        max_total = new_total
        total -= paper[i][j]

print(max_total)


#
def find_max_total():
    from sys import stdin
    def to_int():
        return map(int, stdin.readline().split())

    N, M = to_int()
    max_total = 0
    max_num, max_two = [0] * 2, [0] * 2
    paper = []
    one_direct = [(1, 0), (1, 1), (1, 2), (0, 3), (-1, 0), (-1, 1), (-1, 2)]
    two_direct = [(1, -1), (1, 0), (1, 1), (0, 2), (-1, -1), (-1, 0), (-1, 1)]

    for _ in range(N):
        paper.append(list(to_int()))
        temp_total = paper[-1][0]
        for j in range(M - 1):
            num = paper[-1][j]
            temp_total += paper[-1][j + 1]
            if max_num[0] < num:
                max_num[0] = num
            if max_two[0] < temp_total:
                max_two[0] = temp_total
            temp_total -= num

    for j in range(M):
        temp_total = paper[0][j]
        for i in range(N - 1):
            num = paper[i][j]
            temp_total += paper[i + 1][j]
            if max_num[1] < num:
                max_num[1] = num
            if max_two[1] < temp_total:
                max_two[1] = temp_total
            temp_total -= num

    # 가로 3, 4
    for i in range(N):
        total = sum(paper[i][:2])
        for j in range(M - 2):
            total += paper[i][j + 2]
            if max_total - total < max_num[0]:
                for di, dj in one_direct:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < M:
                        new_total = total + paper[ni][nj]
                        if new_total > max_total:
                            max_total = new_total
            total -= paper[i][j]

    # 세로 3, 4
    for j in range(M):
        total = paper[0][j] + paper[1][j]
        for i in range(N - 2):
            total += paper[i + 2][j]
            if max_total - total < max_num[1]:
                for dj, di in one_direct:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < M:
                        new_total = total + paper[ni][nj]
                        if new_total > max_total:
                            max_total = new_total
            total -= paper[i][j]
    # 가로 2
    for i in range(N):
        total = paper[i][0]
        for j in range(M - 1):
            total += paper[i][j + 1]
            if max_total - total < max_two[0]:
                for di, dj in two_direct:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N - 1 and 0 <= nj < M - 1:
                        new_total = total + sum(paper[ni][nj:nj + 2])
                        if new_total > max_total:
                            max_total = new_total
            total -= paper[i][j]
    # 세로 2
    for j in range(M):
        total = paper[0][j]
        for i in range(N - 1):
            total += paper[i + 1][j]
            if max_total - total < max_two[1]:
                for dj, di in two_direct:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N - 1 and 0 <= nj < M - 1:
                        new_total = total + paper[ni][nj] + paper[ni + 1][nj]
                        if new_total > max_total:
                            max_total = new_total
            total -= paper[i][j]

    return max_total

print(find_max_total())