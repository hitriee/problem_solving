# 241022
# 250404
# 138096 KB / 4780 ms
def main():
    from heapq import heappush, heappop, heapify

    T = int(input())
    for _ in range(T):
        K = int(input())
        pages = list(map(int, input().split()))
        total = 0
        heapify(pages)
        for _ in range(K-1):
            page1 = heappop(pages)
            page2 = heappop(pages)
            duration = page1+page2
            heappush(pages, duration)
            total += duration

        print(total)

main()




# 138080 KB / 5244 ms
def main():
    from sys import stdin
    from heapq import heappush, heappop, heapify

    new_input = stdin.readline
    T = int(new_input())
    for _ in range(T):
        K = int(new_input())
        pages = list(map(int, new_input().split()))
        total = 0
        heapify(pages)
        for _ in range(K-1):
            page1 = heappop(pages)
            page2 = heappop(pages)
            duration = page1+page2
            heappush(pages, duration)
            total += duration

        print(total)

main()




# 138096 KB / 4772 ms
def main():
    from heapq import heappush, heappop, heapify

    T = int(input())
    for _ in range(T):
        K = int(input())
        pages = list(map(int, input().split()))
        total = 0
        heapify(pages)
        combined = []
        for _ in range(K-1):
            duration = 0
            for _ in range(2):
                if not combined:
                    duration += heappop(pages)
                elif not pages:
                    duration += heappop(combined)
                elif combined[0] <= pages[0]:
                    duration += heappop(combined)
                else:
                    duration += heappop(pages)

            heappush(combined, duration)
            total += duration

        print(total)

main()