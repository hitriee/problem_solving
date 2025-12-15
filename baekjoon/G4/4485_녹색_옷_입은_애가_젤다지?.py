#230714
# 251215
# 35508 KB / 92 ms
def main():
    from heapq import heappush, heappop
    from sys import stdin

    tc = 1
    new_input = stdin.readline
    delta_arr = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    answer, heap = [], []

    while True:
        N = int(new_input())
        if N == 0:
            return '\n'.join(answer)

        def in_range(idx):
            return 0 <= idx < N

        limit = int(1e6)
        arr = [list(map(int, new_input().split())) for _ in range(N)]
        min_lost = [[limit] * N for _ in range(N)]

        heappush(heap, (arr[0][0], 0, 0))
        min_lost[0][0] = arr[0][0]

        while heap:
            lost, y, x = heappop(heap)
            if min_lost[y][x] < lost:
                continue

            for dy, dx in delta_arr:
                ny, nx = y+dy, x+dx
                if in_range(ny) and in_range(nx):
                    new_lost = lost + arr[ny][nx]
                    if min_lost[ny][nx] <= new_lost:
                        continue
                    min_lost[ny][nx] = new_lost
                    heappush(heap, (new_lost, ny, nx))

        answer.append(f'Problem {tc}: {min_lost[-1][-1]}')
        tc += 1


print(main())




# 35508 KB / 100 ms
def main():
    from heapq import heappush, heappop
    from sys import stdin

    tc = 1
    new_input = stdin.readline
    delta_arr = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    heap = []

    while True:
        N = int(new_input())
        if N == 0:
            return

        def in_range(idx):
            return 0 <= idx < N

        limit = int(1e6)
        arr = [list(map(int, new_input().split())) for _ in range(N)]
        min_lost = [[limit] * N for _ in range(N)]

        heappush(heap, (arr[0][0], 0, 0))
        min_lost[0][0] = arr[0][0]

        while heap:
            lost, y, x = heappop(heap)
            if min_lost[y][x] < lost:
                continue

            for dy, dx in delta_arr:
                ny, nx = y+dy, x+dx
                if in_range(ny) and in_range(nx):
                    new_lost = lost + arr[ny][nx]
                    if min_lost[ny][nx] <= new_lost:
                        continue
                    min_lost[ny][nx] = new_lost
                    heappush(heap, (new_lost, ny, nx))

        print(f'Problem {tc}: {min_lost[-1][-1]}')
        tc += 1


main()
