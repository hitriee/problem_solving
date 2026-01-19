# 260119
# 55128 KB / 248 ms
def main():
    from sys import stdin

    def int_input():
        return map(int, stdin.readline().split())

    N, D = int_input()
    gift_list = [tuple(int_input()) for _ in range(N)]
    gift_list.sort(key=lambda gift: (gift[0], -gift[1]))

    start = end = total = max_total = 0
    while start < N:
        price, value = gift_list[start]
        limit = price + D

        while end < N:
            if gift_list[end][0] < limit:
                total += gift_list[end][1]
                end += 1
            else:
                break

        if max_total < total:
            max_total = total

        total -= value
        start += 1
        if end < start:
            end = start


    return max_total

print(main())






# 46936 KB / 196 ms
def main():
    from sys import stdin

    def int_input():
        return map(int, stdin.readline().split())

    N, D = int_input()
    gift_list = [tuple(int_input()) for _ in range(N)]
    gift_list.sort(key=lambda gift: gift[0])

    start = end = total = max_total = 0
    while start < N:
        price, value = gift_list[start]
        limit = price + D

        while end < N:
            if gift_list[end][0] < limit:
                total += gift_list[end][1]
                end += 1
            else:
                break

        if max_total < total:
            max_total = total

        total -= value
        start += 1
        if end < start:
            end = start


    return max_total

print(main())





# 46936 KB / 184 ms
def main():
    from sys import stdin

    def int_input():
        return map(int, stdin.readline().split())

    N, D = int_input()
    gift_list = [tuple(int_input()) for _ in range(N)]
    gift_list.sort(key=lambda gift: gift[0])

    end = total = max_total = 0
    for start in range(N):
        price, value = gift_list[start]
        limit = price + D

        if end < start:
            end = start

        while end < N:
            if gift_list[end][0] < limit:
                total += gift_list[end][1]
                end += 1
            else:
                break

        if max_total < total:
            max_total = total

        total -= value


    return max_total

print(main())