# 250121
# 33432 KB / 52 ms
def main():
    T = int(input())
    for _ in range(T):
        _ = int(input())
        coins = list(map(int, input().split()))
        M = int(input())

        cases = [0] * (M+1)
        for coin in coins:
            if coin <= M:
                cases[coin] += 1
                for total in range(coin+1, M+1):
                    cases[total] += cases[total-coin]
            else:
                break

        print(cases[-1])

main()


# 33432 KB / 52 ms
def main():

    def calc_case():
        _ = int(input())
        coins = list(map(int, input().split()))
        M = int(input())

        cases = [0] * (M + 1)
        for coin in coins:
            if coin <= M:
                cases[coin] += 1
                for total in range(coin + 1, M + 1):
                    cases[total] += cases[total - coin]
            else:
                break

        return cases[-1]


    T = int(input())
    for _ in range(T):
        print(calc_case())

main()