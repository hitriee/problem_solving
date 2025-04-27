# 250425
# 32412 KB / 36 ms
def main():
    N = int(input())
    values = list(map(int, input().split()))
    if N == 1:
        return sum(values) - max(values)

    # 반대편 = 5-i
    overall = set(range(6))
    around = []

    for i in range(6):
        around.append(overall - {i, 5-i})

    # 1개 = (N-2)*(N-2) + (N-1) * (N-2) * 4
    min_value1 = min(values)
    # 맞닿은 2개 = (N-2)*4 + (N-1)*4
    # 맞닿은 3개 = 4
    min_value2, min_value3 = 100, 150
    for i in range(5):
        val1 = values[i]
        for j in around[i]:
            val2 = values[j]
            total = val1 + val2
            min_value2 = min(min_value2, total)
            for k in around[i] & around[j]:
                min_value3 = min(min_value3, total+values[k])

    min_value1 *= (N-2)*(N-2) + (N-1) * (N-2) * 4
    min_value2 *= (N-2)*4 + (N-1)*4
    min_value3 *= 4


    return min_value1 + min_value2 + min_value3

print(main())





# 32412 KB / 40 ms
def main():
    N = int(input())
    values = list(map(int, input().split()))
    if N == 1:
        return sum(values) - max(values)

    # 반대편 = 5-i
    overall = set(range(6))
    around = [overall - {i, 5-i} for i in range(6)]

    min_value1 = min(values)
    min_value2, min_value3 = 100, 150

    for i in range(5):
        val1 = values[i]
        for j in around[i]:
            val2 = values[j]
            total = val1 + val2
            min_value2 = min(min_value2, total)
            for k in around[i] & around[j]:
                min_value3 = min(min_value3, total+values[k])

    # 1개 = (N-2)*(N-2) + (N-1) * (N-2) * 4 = 4 * (N-2) * (2*N-3)
    # 맞닿은 2개 = (N-2)*4 + (N-1)*4 = 4 * (2*N-3)
    # 맞닿은 3개 = 4

    min_value1 *= (5*N - 6) * (N-2)
    min_value2 *= 8 * N - 12
    min_value3 *= 4

    return min_value1 + min_value2 + min_value3

print(main())