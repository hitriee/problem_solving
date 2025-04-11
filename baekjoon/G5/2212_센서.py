# 250411
def main():
    N = int(input())
    K = int(input())
    sensor = sorted(map(int, input().split()))
    if K >= N:
        return 0

    dif_list = sorted([sensor[i+1] - sensor[i] for i in range(N-1)])[:N-K]

    return sum(dif_list)

print(main())