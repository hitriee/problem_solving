# 241216
# 33432 KB / 44 ms
def main():
    N = input()
    M = len(N)
    if M == 1:
        return 1 if N != '0' else 0

    if N[0] == '0':
        return 0
    # 1자리 숫자일 때, 2자리 숫자일 때
    cases = [[0] * 2 for _ in range(M+1)]
    cases[0][0] = 1

    for i in range(1, M+1):
        if N[i-1] != '0':
            cases[i][0] = sum(cases[i-1]) % 1000000
        else:
            cases[i-1][0] = 0

        if '10' <= N[i-2:i] <= '26':
            cases[i][1] = sum(cases[i-2]) % 1000000

    return sum(cases[-1]) % 1000000


print(main())