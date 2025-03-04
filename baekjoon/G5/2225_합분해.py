# 250304
# 32412 KB / 456 ms
def main():
    N, K = map(int, input().split())
    before, after = [1] * (N+1), [0] * (N+1)
    div_num = int(1e9)
    for _ in range(K-1):
        for i in range(N+1):
            for j in range(N+1-i):
                after[i+j] = (after[i+j] + before[i]) % div_num
        before = after[:]
        after = [0] * (N+1)
    return before[-1]

print(main())



# 32412 KB / 392 ms
def main():
    N, K = map(int, input().split())
    before, after = [1] * (N+1), [0] * (N+1)
    div_num = int(1e9)
    for _ in range(K-1):
        for i in range(N+1):
            for j in range(i, N+1):
                after[j] = (after[j] + before[i]) % div_num
        before = after[:]
        after = [0] * (N+1)
    return before[-1]

print(main())



# 32412 KB / 44 ms
def main():
    N, K = map(int, input().split())
    if K == 1:
        return 1

    before = list(range(1, N+2))
    div_num = int(1e9)
    for _ in range(K-2):
        for i in range(1, N+1):
            before[i] = (before[i] + before[i-1]) % div_num

    return before[-1]

print(main())


# 32412 KB / 40 ms
def main():
    N, K = map(int, input().split())
    before = [1] * (N+1)
    div_num = int(1e9)
    for _ in range(K - 1):
        for i in range(1, N + 1):
            before[i] = (before[i] + before[i - 1]) % div_num

    return before[-1]


print(main())




# 32412 KB / 44 ms
def main():
    N, K = map(int, input().split())
    if K == 1:
        return 1

    cnt = [1] * (N+1)
    div_num = int(1e9)
    for _ in range(K - 2):
        for i in range(1, N + 1):
            cnt[i] = (cnt[i] + cnt[i - 1]) % div_num

    return sum(cnt) % div_num


print(main())