# 260312
# 37820 KB / 64 ms
def main():
    def int_input():
        return map(int, input().split())

    N, K = int_input()
    arr = list(int_input())
    if K == 1:
        return sum(arr)

    acc = [0] + arr[:]
    for i in range(2, N+1):
        acc[i] += acc[i-1]

    start, end = 0, acc[-1]
    while start <= end:
        mid = (start + end) // 2
        cnt = left = 0
        s = 1

        while True:
            target = mid + left
            e = N
            while s <= e:
                m = (s + e) // 2
                if target < acc[m]:
                    e = m - 1
                elif target > acc[m]:
                    s = m + 1
                else:
                    s = m
                    break

            if s > N:
                break
            cnt += 1
            left = acc[s]

        if cnt >= K:
            start = mid + 1
        else:
            end = mid - 1

    return end

print(main())