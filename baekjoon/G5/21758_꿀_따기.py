# 250408
# 42660 KB / 92 ms
def main():
    N = int(input())
    amount = list(map(int, input().split()))
    acc = amount[:]
    max_total = 0

    for i in range(1, N):
        acc[i] += acc[i-1]


    for i in (0, N-1, N//2, N//2+1):
        if i == 0:
            total = acc[-2]
            for k in range(1, N-1):
                new_total = total - amount[k] + acc[k-1]
                if new_total > max_total:
                    max_total = new_total

        elif i == N-1:
            total = acc[-1] - acc[0]
            for k in range(1, N-1):
                new_total = total - amount[k] + acc[-1] - acc[k]
                if new_total > max_total:
                    max_total = new_total

        else:
            total = acc[i] - acc[0] + acc[-2] - acc[i-1]
            if total > max_total:
                max_total = total

        if total > max_total:
            max_total = total

    return max_total

print(main())
