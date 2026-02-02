# 260130
# 33464 KB / 780 ms
def main():
    N, M, K = map(int, input().split())

    cnt = [[0] * (K+1) for _ in range(M+1)]

    for _ in range(N):
        burger, fry = map(int, input().split())
        temp = [cnt[i][:] for i in range(M+1)]

        for i in range(M-burger+1):
            for j in range(K-fry+1):
                new_val = cnt[i+burger][j+fry]+1
                if temp[i][j] < new_val:
                    temp[i][j] = new_val

        cnt = [temp[i][:] for i in range(M + 1)]

    return cnt[0][0]

print(main())