# 250312
# 250916
# 33192 KB / 2208 ms
def main():
    from sys import stdin

    def int_input():
        return map(int, stdin.readline().split())


    D, P = int_input()
    max_c = [0] * (D+1)

    for _ in range(P):
        L, C = int_input()
        if L <= D and max_c[L] < C:
            max_c[L] = C

        for i in range(D, L, -1):
            new_c = min(max_c[i-L], C)
            if max_c[i] < new_c:
                max_c[i] = new_c

    return max_c[-1]


print(main())