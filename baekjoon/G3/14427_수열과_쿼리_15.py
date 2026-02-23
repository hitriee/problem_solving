# 260219
# 55016 KB / 228 ms
def main():
    from sys import stdin
    from heapq import heappush, heappop

    new_input = stdin.readline
    N = int(new_input())
    arr = list(map(int, new_input().split()))
    M = int(new_input())
    heap = []

    for i in range(N):
        heappush(heap, (arr[i], i+1))

    for _ in range(M):
        num, *args = map(int, new_input().split())
        if num == 1:
            idx, val = args
            arr[idx-1] = val
            if idx == heap[0][1]:
                heappop(heap)

            heappush(heap, (val, idx))

        else:
            while heap:
                val, idx = heap[0]
                if val == arr[idx-1]:
                    break
                heappop(heap)

            print(heap[0][1])


main()








# 55016 KB / 292 ms
def main():
    from sys import stdin
    from heapq import heappush, heappop

    new_input = stdin.readline
    N = int(new_input())
    arr = list(map(int, new_input().split()))
    M = int(new_input())
    heap = []

    for i in range(N):
        heappush(heap, (arr[i], i+1))

    for _ in range(M):
        num, *args = map(int, new_input().split())
        if num == 1:
            idx, val = args
            arr[idx-1] = val
            heappush(heap, (val, idx))

        else:
            while heap:
                val, idx = heap[0]
                if val == arr[idx-1]:
                    break
                heappop(heap)

            print(heap[0][1])


main()