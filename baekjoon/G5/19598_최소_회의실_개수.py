# 250409
# 59844 KB / 372 ms
def main():
    from sys import stdin
    from heapq import heappush, heappop

    new_input = stdin.readline
    N = int(new_input())
    info = [list(map(int, new_input().split())) for _ in range(N)]
    info.sort()

    cnt = 1
    heap = [(info[0][1], 0)]

    for i in range(1, N):
        start, end = info[i]
        if heap[0][0] <= start:
            idx = heappop(heap)[1]
            heappush(heap, (end, idx))
        else:
            heappush(heap, (end, cnt))
            cnt += 1

    return cnt

print(main())