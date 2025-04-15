# 250414
# 45016 KB / 328 ms
def main():
    from heapq import heappush, heappop

    N = int(input())
    target = list(map(int, input().split()))
    total = sum(target)
    if total % 3:
        return 'NO'

    def find_tree():
        while min_heap:
            min_val = heappop(min_heap)
            if cnt[min_val]:
                break

        while max_heap:
            max_val = -heappop(max_heap)
            if cnt[max_val]:
                break

        return (min_val, max_val)

    limit = 10001
    cnt = [0] * limit
    max_heap, min_heap = [], []
    for height in target:
        cnt[height] += 1
        heappush(max_heap, -height)
        heappush(min_heap, height)


    start, end = heappop(min_heap), -heappop(max_heap)
    while start < end:
        cnt[start] -= 1
        cnt[end] -= 1
        min_val = min(start, end//2)
        for val in (end - 2*min_val, start - min_val):
            if val:
                cnt[val] += 1
                heappush(min_heap, val)
                heappush(max_heap, -val)

        start, end = find_tree()
        # print(start, end)


    if start == 0:
        return 'YES'
    elif start == 1:
        return 'NO'

    return 'YES'

print(main())




# 44940 KB / 324 ms
def main():
    from heapq import heappush, heappop

    _ = int(input())
    target = list(map(int, input().split()))
    total = sum(target)
    if total % 3:
        return 'NO'

    def find_tree():
        while min_heap:
            min_val = heappop(min_heap)
            if cnt[min_val]:
                break

        while max_heap:
            max_val = -heappop(max_heap)
            if cnt[max_val]:
                break

        return (min_val, max_val)

    limit = 10001
    cnt = [0] * limit
    max_heap, min_heap = [], []
    for height in target:
        cnt[height] += 1
        heappush(max_heap, -height)
        heappush(min_heap, height)


    start, end = heappop(min_heap), -heappop(max_heap)
    while start < end:
        cnt[start] -= 1
        cnt[end] -= 1
        min_val = min(start, end//2)
        for val in (end - 2*min_val, start - min_val):
            if val:
                cnt[val] += 1
                heappush(min_heap, val)
                heappush(max_heap, -val)

        start, end = find_tree()


    if start == 1:
        return 'NO'

    return 'YES'




# 45032 KB / 328 ms
def main():
    from heapq import heappush, heappop

    _ = int(input())
    target = list(map(int, input().split()))
    total = sum(target)
    if total % 3:
        return 'NO'

    def find_tree():
        while min_heap:
            min_val = heappop(min_heap)
            if cnt[min_val]:
                break

        while max_heap:
            max_val = -heappop(max_heap)
            if cnt[max_val]:
                break

        return (min_val, max_val)

    limit = 10001
    cnt = [0] * limit
    max_heap, min_heap = [], []
    for height in target:
        cnt[height] += 1
        heappush(max_heap, -height)
        heappush(min_heap, height)


    start, end = heappop(min_heap), -heappop(max_heap)
    while start < end:
        cnt[start] -= 1
        cnt[end] -= 1
        min_val = min(start, end//2)
        for val in (end - 2*min_val, start - min_val):
            if val:
                cnt[val] += 1
                heappush(min_heap, val)
                heappush(max_heap, -val)

        start, end = find_tree()


    return 'YES' if start != 1 else 'NO'

print(main())




# 45032 KB / 340 ms
def main():
    from heapq import heappush, heappop

    _ = int(input())
    target = list(map(int, input().split()))
    total = sum(target)
    if total % 3:
        return 'NO'

    def find_tree():
        while min_heap:
            min_val = heappop(min_heap)
            if cnt[min_val]:
                break

        while max_heap:
            max_val = -heappop(max_heap)
            if cnt[max_val]:
                break

        return (min_val, max_val)

    cnt = [0] * 10001
    max_heap, min_heap = [], []
    for height in target:
        cnt[height] += 1
        heappush(max_heap, -height)
        heappush(min_heap, height)


    start, end = heappop(min_heap), -heappop(max_heap)
    while start < end:
        cnt[start] -= 1
        cnt[end] -= 1
        min_val = min(start, end//2)
        for val in (end - 2*min_val, start - min_val):
            if val:
                cnt[val] += 1
                heappush(min_heap, val)
                heappush(max_heap, -val)

        start, end = find_tree()


    return 'YES' if start != 1 else 'NO'

print(main())



#
def main():
    from heapq import heappush, heappop

    _ = int(input())
    target = list(map(int, input().split()))
    total = sum(target)
    if total % 3:
        return 'NO'

    def find_tree():
        while min_heap:
            min_val = heappop(min_heap)
            if cnt[min_val]:
                break

        while max_heap:
            max_val = -heappop(max_heap)
            if cnt[max_val]:
                break

        return (min_val, max_val)

    limit = 10001
    cnt = [0] * limit
    max_heap, min_heap = [], []
    for height in target:
        cnt[height] += 1
        heappush(max_heap, -height)
        heappush(min_heap, height)


    start, end = heappop(min_heap), -heappop(max_heap)
    while start < end:
        cnt[start] -= 1
        cnt[end] -= 1
        min_val = min(start, end//2)
        for val in (end - 2*min_val, start - min_val):
            if val:
                cnt[val] += 1
                heappush(min_heap, val)
                heappush(max_heap, -val)

        start, end = find_tree()


    if start == 1:
        return 'NO'

    return 'YES'

print(main())