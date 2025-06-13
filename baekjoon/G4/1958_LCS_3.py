# 250611
# 40560 KB / 1292 ms
def main():
    str1 = input()
    str2 = input()
    str3 = input()
    N, M, L = len(str1), len(str2), len(str3)
    lcs_len = [[[0] * (L + 1) for _ in range(M + 1)] for _ in range(N+1)]

    for i in range(N):
        for j in range(M):
            for k in range(L):
                if str1[i] == str2[j] == str3[k]:
                    lcs_len[i+1][j+1][k+1] = lcs_len[i][j][k] + 1
                else:
                    temp = []
                    for di in range(2):
                        ni = i+di
                        for dj in range(2):
                            nj = j+dj
                            for dk in range(2):
                                nk = k+dk
                                temp.append(lcs_len[ni][nj][nk])

                    lcs_len[i+1][j+1][k+1] = max(temp)

    return lcs_len[-1][-1][-1]

print(main())
