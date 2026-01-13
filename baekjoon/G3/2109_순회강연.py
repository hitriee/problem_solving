#230926


# 250113
# 36532 KB / 1692 ms
def main():
    from sys import stdin
    from heapq import heappush, heappop

    new_input = stdin.readline
    N = int(new_input())
    heap = []
    for _ in range(N):
        p, d = map(int, new_input().split())
        heappush(heap, (-p, d))

    total = [0] * 10001

    while heap:
        income, limit = heappop(heap)
        if total[limit] == 0:
            total[limit] = -income
        else:
            for i in range(limit-1, 0, -1):
                if total[i] == 0:
                    total[i] = -income
                    break
    return sum(total)

print(main())




# 36532 KB / 68 ms
def main():
    from sys import stdin
    from heapq import heappush, heappop

    new_input = stdin.readline
    N = int(new_input())
    heap = []
    for _ in range(N):
        p, d = map(int, new_input().split())
        heappush(heap, (-p, d))

    total = 0
    i_list = list(range(1, 10001))

    while heap:
        income, limit = heappop(heap)
        start, end = 0, len(i_list) - 1

        while start <= end:
            mid = (start + end) // 2
            mid_i = i_list[mid]
            if mid_i < limit:
                start = mid + 1
            elif mid_i > limit:
                end = mid - 1
            else:
                total -= income
                i_list.pop(mid)
                break

        else:
            if end >= 0:
                total -= income
                i_list.pop(end)

    return total

print(main())