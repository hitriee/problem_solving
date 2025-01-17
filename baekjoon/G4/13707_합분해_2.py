# 230908
# 250117
# 33432 KB / 4020 ms
def main():
    N, K = map(int, input().split())
    before, after = [0] * (N+1), [0] * (N+1)
    div_num = int(1e9)

    for j in range(N+1):
        before[j] = 1

    for _ in range(1, K):
        for target in range(N+1):
            after[target] = before[target]

        before[0], after[0] = after[0], 0
        for target in range(1, N+1):
            before[target] = (before[target-1] + after[target]) % div_num

    return before[-1]

print(main())


# 250117
# 32412 KB / 3228 ms
def main():
    N, K = map(int, input().split())
    cnt = [1] * (N+1)
    div_num = int(1e9)

    for _ in range(K-1):
        for target in range(1, N+1):
            cnt[target] = (cnt[target] + cnt[target-1]) % div_num

    return cnt[-1]

print(main())
