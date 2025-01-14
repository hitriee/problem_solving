# 250119
# 32412 KB / 64 ms
def main():
    N = int(input())
    min_cost = list(map(int, input().split()))
    for target in range(1, N):
        for num in range(target//2+1):
            min_cost[target] = min(min_cost[target], min_cost[num] + min_cost[target-num-1])
    return min_cost[-1]

print(main())


# 32412 KB / 60 ms
def main():
    N = int(input())
    min_cost = list(map(int, input().split()))
    for target in range(1, N):
        for num in range(target//2+1):
            other = min_cost[num] + min_cost[target-num-1]
            if min_cost[target] > other:
                min_cost[target] = other

    return min_cost[-1]

print(main())

