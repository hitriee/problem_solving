# 260206
# 34368 KB / 228 ms
def main():
    candidate = input()
    pw = input()
    limit = 900528
    N, M = len(candidate), len(pw)
    alp_to_num = {}

    for i in range(N):
        alp_to_num[candidate[i]] = i+1

    # 한 글자일 경우 첫
    # 두 글자일 경우 N*첫 + 둘
    # 세 글자일 경우 N*N*첫 + N*둘 + 셋

    multiple, total = 1, 0
    for i in range(M-1, -1, -1):
        total = (total + multiple * alp_to_num[pw[i]]) % limit
        multiple = (multiple * N) % limit

    return total

print(main())