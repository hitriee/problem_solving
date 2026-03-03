# 260303
# 35508 KB / 40 ms
def main():
    from heapq import heapify, heappop

    def minus(num):
        return -int(num)

    B, C, D = map(int, input().split())
    burgers = list(map(minus, input().split()))
    side_menus = list(map(minus, input().split()))
    drink_menus = list(map(minus, input().split()))
    N = min(B, C, D)
    heapify(burgers)
    heapify(side_menus)
    heapify(drink_menus)

    total_before = 0
    total_after = 0
    for _ in range(N):
        set_cost = heappop(side_menus) + heappop(burgers) + heappop(drink_menus)
        total_before -= set_cost
        total_after -= set_cost * 0.9

    remain = sum(side_menus) + sum(burgers) + sum(drink_menus)
    total_before -= remain
    total_after -= remain

    return f'{total_before}\n{int(total_after)}'

print(main())







# 32412 KB / 36 ms
def main():

    B, C, D = map(int, input().split())
    burgers = list(map(int, input().split()))
    side_menus = list(map(int, input().split()))
    drink_menus = list(map(int, input().split()))

    N = min(B, C, D)
    burgers.sort()
    side_menus.sort()
    drink_menus.sort()

    total_before = 0
    total_after = 0
    for _ in range(N):
        set_cost = side_menus.pop() + burgers.pop() + drink_menus.pop()
        total_before += set_cost
        total_after += set_cost * 0.9

    remain = sum(side_menus) + sum(burgers) + sum(drink_menus)
    total_before += remain
    total_after += remain

    return f'{total_before}\n{int(total_after)}'

print(main())