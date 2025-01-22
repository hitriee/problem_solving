# 250121
# 33432 KB / 104 ms
def main():
    n, k = map(int, input().split())
    coins = [int(input()) for _ in range(n)]
    coins.sort()
    cases = [0] * (k+1)

    for coin in coins:
        if coin <= k:
            cases[coin] += 1
            for total in range(coin+1, k+1):
                cases[total] += cases[total-coin]
        else:
            break

    return cases[-1]

print(main())



# 33432 KB / 104 ms
def main():
    n, k = map(int, input().split())
    coins = [int(input()) for _ in range(n)]
    cases = [0] * (k+1)

    for coin in coins:
        if coin <= k:
            cases[coin] += 1
            for total in range(coin+1, k+1):
                cases[total] += cases[total-coin]

    return cases[-1]

print(main())



# 33432 KB / 104 ms
def main():
    from sys import stdin

    new_input = stdin.readline
    n, k = map(int, new_input().split())
    coins = [int(new_input()) for _ in range(n)]
    cases = [0] * (k+1)

    for coin in coins:
        if coin <= k:
            cases[coin] += 1
            for total in range(coin+1, k+1):
                cases[total] += cases[total-coin]

    return cases[-1]

print(main())
