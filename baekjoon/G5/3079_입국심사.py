# 240920
# 34972 KB / 616 ms
def main():
    from sys import stdin
    new_input = stdin.readline

    N, M = map(int, new_input().split())
    arr = [int(new_input()) for _ in range(N)]

    start, end = 0, M * arr[0]
    while start <= end:
        mid = (start + end)//2
        leftover = M
        for i in range(N):
            leftover -= mid // arr[i]
        if leftover <= 0:
            end = mid - 1
        else:
            start = mid + 1

    return start


print(main())


# 35364 KB / 720 ms
def main():
    from sys import stdin
    new_input = stdin.readline

    N, M = map(int, new_input().split())
    arr = [int(new_input()) for _ in range(N)]
    arr.sort()

    start, end = 0, M * arr[0]
    while start <= end:
        mid = (start + end)//2
        leftover = M
        for i in range(N):
            leftover -= mid // arr[i]
        if leftover <= 0:
            end = mid - 1
        else:
            start = mid + 1

    return start


print(main())



# 41876 KB / 1252 ms
def main():
    from sys import stdin
    new_input = stdin.readline

    N, M = map(int, new_input().split())
    duration = {}
    for _ in range(N):
        key = int(new_input())
        duration[key] = duration.get(key, 0) + 1
    
    sorted_keys = sorted(duration)

    start, end = 0, M * sorted_keys[0]
    while start <= end:
        mid = (start + end)//2
        leftover = M
        for key in sorted_keys:
            leftover -= (mid // key) * duration[key]
        
        if leftover <= 0:
            end = mid - 1
        else:
            start = mid + 1

    return start


print(main())


# 34972 KB / 488 ms
def main():
    from sys import stdin
    new_input = stdin.readline

    N, M = map(int, new_input().split())
    arr = [int(new_input()) for _ in range(N)]

    start, end = 0, M * arr[0]
    while start <= end:
        mid = (start + end)//2
        leftover = M
        for i in range(N):
            leftover -= mid // arr[i]
            if leftover <= 0:
                end = mid - 1
                break
        else:
            start = mid + 1

    return start


print(main())


# 35364 KB / 564 ms
def main():
    from sys import stdin
    new_input = stdin.readline

    N, M = map(int, new_input().split())
    arr = [int(new_input()) for _ in range(N)]
    arr.sort()

    start, end = 0, M * arr[0]
    while start <= end:
        mid = (start + end)//2
        leftover = M
        for i in range(N):
            leftover -= mid // arr[i]
            if leftover <= 0:
                end = mid - 1
                break
        else:
            start = mid + 1

    return start


print(main())



# 34972 KB / 488 ms
def binary_search(start, end, N, M, arr):
    while start <= end:
        mid, leftover = (start + end)//2, M

        for i in range(N):
            leftover -= mid // arr[i]
            if leftover <= 0:
                end = mid - 1
                break
        else:
            start = mid + 1

    return start


def main():
    from sys import stdin
    new_input = stdin.readline

    N, M = map(int, new_input().split())
    arr = [int(new_input()) for _ in range(N)]

    return binary_search(0, M * arr[0], N, M, arr)

print(main())



# 34972 KB / 504 ms
def binary_search(start, end, N, M, arr):
    while start <= end:
        mid = (start + end) // 2
        cnt = 0

        for i in range(N):
            cnt += mid // arr[i]
            if cnt >= M:
                end = mid - 1
                break
        else:
            start = mid + 1

    return start


def main():
    from sys import stdin
    new_input = stdin.readline

    N, M = map(int, new_input().split())
    arr = [int(new_input()) for _ in range(N)]

    return binary_search(0, M * arr[0], N, M, arr)

print(main())


# 34972 KB / 492 ms
def main():
    from sys import stdin
    new_input = stdin.readline

    N, M = map(int, new_input().split())
    arr = [int(new_input()) for _ in range(N)]

    start, end = 0, M * min(arr)
    while start <= end:
        mid = (start + end)//2
        leftover = M
        for i in range(N):
            leftover -= mid // arr[i]
            if leftover <= 0:
                end = mid - 1
                break
        else:
            start = mid + 1

    return start


print(main())
