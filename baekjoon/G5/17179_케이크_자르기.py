# 231027
# 31120 KB / 2420 ms
from sys import stdin

N, M, L = map(int, stdin.readline().split())
points = [int(stdin.readline()) for _ in range(M)]

for _ in range(N):
    target_cnt = int(stdin.readline())
    start, end = 1, L
    while start <= end:
        mid = (start + end) // 2
        before = cnt = 0
        for point in points:
            if point - before >= mid:
                before = point
                cnt += 1
        if L - before < mid:
            if cnt > target_cnt:
                start = mid + 1
            else:
                end = mid - 1
        elif cnt < target_cnt:
            end = mid - 1
        else:
            start = mid + 1

    print(end)



# 31120 KB / 920 ms
def binary_search():
    start, end = 1, L
    while start <= end:
        mid = (start + end) // 2
        before = cnt = 0
        for point in points:
            if point - before >= mid:
                before = point
                cnt += 1
        if L - before < mid:
            if cnt > target_cnt:
                start = mid + 1
            else:
                end = mid - 1
        elif cnt < target_cnt:
            end = mid - 1
        else:
            start = mid + 1

    return end

from sys import stdin

N, M, L = map(int, stdin.readline().split())
points = [int(stdin.readline()) for _ in range(M)]

for _ in range(N):
    target_cnt = int(stdin.readline())
    print(binary_search())


# 31120 KB / 924 ms
def binary_search(points, target_cnt, L):
    start, end = 1, L
    while start <= end:
        mid = (start + end) // 2
        before = cnt = 0

        for point in points:
            if point - before >= mid:
                before = point
                cnt += 1

        if L - before < mid:
            if cnt > target_cnt:
                start = mid + 1
            else:
                end = mid - 1
        elif cnt < target_cnt:
            end = mid - 1
        else:
            start = mid + 1

    return end


def find_max():
    from sys import stdin

    N, M, L = map(int, stdin.readline().split())
    points = [int(stdin.readline()) for _ in range(M)]

    for _ in range(N):
        target_cnt = int(stdin.readline())
        print(binary_search(points, target_cnt, L))

find_max()