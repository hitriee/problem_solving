# 240423
# 250922
# 251020
# 32412 KB / 2128 ms
def main():
    N, K = map(int, input().split())
    if N <= K:
        return 0
    cnt = 0
    while True:
        bin_num = bin(N+cnt)[2:]
        if bin_num.count('1') <= K:
            return cnt
        cnt += 1

print(main())


# 32412 KB / 36 ms
def main():
    N, K = map(int, input().split())
    if N <= K:
        return 0

    cnt = 0
    while True:
        bin_num = bin(N+cnt)[2:]
        if bin_num.count('1') <= K:
            return cnt

        m = len(bin_num)
        for i in range(m-1, -1, -1):
            if bin_num[i] == '1':
                cnt += 1 << (m-1-i)
                break

print(main())