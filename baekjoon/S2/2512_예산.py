# 230808
# 250113
# 33432 KB / 40 ms
def main():
    N = int(input())
    deposit = list(map(int, input().split()))
    M = int(input())

    total = sum(deposit)
    deposit.sort()

    if total <= M:
        return deposit[-1]

    start, end = 1, deposit[-1]
    while start <= end:
        mid = (start + end)//2
        result = 0

        for i in range(N):
            each = deposit[i]
            if each <= mid:
                result += each
            else:
                result += mid * (N-i)
                break

        if result <= M:
            start = mid+1
        else:
            end = mid-1

    return end


print(main())



# 33432 KB / 44 ms
def binary_search(start, end, N, deposit, target):
    while start <= end:
        mid = (start + end) // 2
        result = 0

        for i in range(N):
            each = deposit[i]
            if each <= mid:
                result += each
            else:
                result += mid * (N - i)
                break

        if result <= target:
            start = mid + 1
        else:
            end = mid - 1

    return end

def main():
    N = int(input())
    deposit = list(map(int, input().split()))
    M = int(input())

    total = sum(deposit)
    deposit.sort()
    last = deposit[-1]

    if total <= M:
        return last

    return binary_search(1, last, N, deposit, M)


print(main())
