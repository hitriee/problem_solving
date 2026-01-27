# 260127
# 33192 KB / 776 ms
def main():
    N, K = map(int, input().split())
    amount_arr = list(map(int, input().split()))

    limit = N+1
    cnt_arr = [limit] * (K+1)
    cnt_arr[0] = 0

    for i in range(N):
        amount = amount_arr[i]
        for j in range(K, amount-1, -1):
            if cnt_arr[j-amount] != limit:
                cnt_arr[j] = min(cnt_arr[j-amount] + 1, cnt_arr[j])

    return -1 if cnt_arr[-1] == limit else cnt_arr[-1]

print(main())