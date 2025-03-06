# 250306
# 33432 KB / 48 ms
def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        coins = list(map(int, input().split()))
        M = int(input())
        value = [0] * (M+1)
        value[0] = 1

        for coin in coins:
            for i in range(coin, M+1):
                value[i] += value[i-coin]

        print(value[-1])

main()




# 33432 KB / 48 ms
def main():
    T = int(input())
    for _ in range(T):
        _ = input()
        coins = list(map(int, input().split()))
        M = int(input())
        value = [0] * (M+1)
        value[0] = 1

        for coin in coins:
            for i in range(coin, M+1):
                value[i] += value[i-coin]

        print(value[-1])

main()