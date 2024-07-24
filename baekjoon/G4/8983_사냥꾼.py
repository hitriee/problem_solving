#240724
# 48640 KB / 432 ms
def main():
    from sys import stdin

    def int_input():
        return map(int, stdin.readline().split())

    def can_capture(dif_x, dif_y):
        return dif_x + dif_y <= L

    def binary_search(x, y):
        if y > L:
            return 0

        start, end = 0, M - 1
        while start <= end:
            mid = (start + end) // 2
            new_x = arr[mid]
            if new_x < x:
                start = mid + 1
            elif new_x > x:
                end = mid - 1
            else:
                return 1
        else:
            if start < M and can_capture(arr[start] - x, y):
                return 1
            elif end >= 0 and can_capture(x - arr[end], y):
                return 1
            else:
                return 0

    M, N, L = int_input()
    arr = sorted(int_input())
    cnt = 0
    animals = [tuple(int_input()) for _ in range(N)]

    for x, y in animals:
        cnt += binary_search(x, y)

    return cnt

print(main())



# 48632 KB / 412 ms
def main():
    from sys import stdin

    def int_input():
        return map(int, stdin.readline().split())

    def can_capture(dif_x, dif_y):
        return dif_x + dif_y <= L

    def binary_search(x, y):
        if y > L:
            return 0

        start, end = 0, M - 1
        while start <= end:
            mid = (start + end) // 2
            new_x = arr[mid]
            if new_x < x:
                start = mid + 1
            elif new_x > x:
                end = mid - 1
            else:
                return 1

        if start < M and can_capture(arr[start] - x, y):
            return 1
        elif end >= 0 and can_capture(x - arr[end], y):
            return 1
        else:
            return 0

    M, N, L = int_input()
    arr = sorted(int_input())
    animals = [tuple(int_input()) for _ in range(N)]
    cnt = 0

    for animal in animals:
        cnt += binary_search(*animal)

    return cnt

print(main())