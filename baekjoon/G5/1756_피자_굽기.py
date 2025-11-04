# 251104
# 71588 KB / 716 ms
def main():
    D, N = map(int, input().split())
    diameters = list(map(int, input().split()))
    finished = list(map(int, input().split()))
    limit = D-1

    for i in range(D-1):
        diameter = diameters[i]
        if diameter < diameters[i+1]:
            diameters[i+1] = diameter

    for pizza in finished:
        start, end = 0, limit
        while start <= end:
            mid = (start + end) // 2
            if diameters[mid] >= pizza:
                start = mid + 1
            else:
                end = mid - 1

        if end < 0:
            return 0

        limit = end - 1

    return limit+2

print(main())