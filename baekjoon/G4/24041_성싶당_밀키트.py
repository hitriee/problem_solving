# 260311
# 211392 KB / 1544 ms (Pypy3)
# 87784 KB / 3116 ms (Python3)
def main():
    from sys import stdin

    def int_input():
        return map(int, stdin.readline().split())

    N, G, K = int_input()
    arr = [list(int_input()) for _ in range(N)]

    arr.sort(key=lambda x: (x[1], x[0], x[2]))

    start, end = 0, int(2e9)
    while start <= end:
        mid = (start + end) // 2
        left, right = 0, N-1

        while left <= right:
            middle = (left + right) // 2
            l = arr[middle][1]
            if l >= mid:
                right = middle - 1
            else:
                left = middle + 1

        total = 0
        minus = []
        for i in range(left):
            s, l, o = arr[i]
            result = s * (mid - l)
            if o == 1:
                minus.append(result)
            else:
                total += result

        for i in range(left, N):
            s, _, o = arr[i]
            if o == 1:
                minus.append(s)
            else:
                total += s

        minus.sort(reverse=True)
        total += sum(minus[K:])

        if total > G:
            end = mid - 1
        elif total < G:
            start = mid + 1
        else:
            return mid

    return end

print(main())




# 87784 KB / 3696 ms
def main():
    from sys import stdin

    def int_input():
        return map(int, stdin.readline().split())

    N, G, K = int_input()
    arr = [list(int_input()) for _ in range(N)]

    arr.sort(key=lambda x: (x[1], x[0], x[2]))

    start, end = 0, int(2e9)
    while start <= end:
        mid = (start + end) // 2

        total = 0
        minus = []
        for i in range(N):
            s, l, o = arr[i]
            result = s * max(1, mid - l)
            if o == 1:
                minus.append(result)
            else:
                total += result

        minus.sort(reverse=True)
        total += sum(minus[K:])

        if total > G:
            end = mid - 1
        elif total < G:
            start = mid + 1
        else:
            return mid

    return end

print(main())




#
def main():
    from sys import stdin

    def int_input():
        return map(int, stdin.readline().split())

    N, G, K = int_input()
    important, remain = [], []
    for _ in range(N):
        s, l, o = int_input()
        if o == 0:
            important.append((l, s))
        else:
            remain.append((l, s))

    M = len(important)
    important.sort()
    remain.sort()


    start, end = 0, int(2e9)
    while start <= end:
        mid = (start + end) // 2
        left, right = 0, M-1

        while left <= right:
            middle = (left + right) // 2
            l = important[middle][0]
            if l >= mid:
                right = middle - 1
            else:
                left = middle + 1

        total = 0
        minus = []
        for i in range(left):
            l, s = important[i]
            result = s * (mid - l)
            total += result

        for i in range(left, M):
            s = important[i][1]
            total += s

        left, right = 0, M - N- 1
        while left <= right:
            middle = (left + right) // 2
            l = remain[middle][0]
            if l >= mid:
                right = middle - 1
            else:
                left = middle + 1

        for i in range(left):
            l, s = remain[i]
            result = s * (mid - l)
            minus.append(result)

        for i in range(left, M):
            s = important[i][1]
            minus.append(s)


        minus.sort(reverse=True)
        total += sum(minus[K:])

        if total > G:
            end = mid - 1
        elif total < G:
            start = mid + 1
        else:
            return mid

    return end

print(main())