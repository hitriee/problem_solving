# 240319
def find_last(end, arr):
    for i in range(end, -1, -1):
        if arr[i]:
            return i
    return -1


def solution(cap, n, deliveries, pickups):
    min_val = 0
    d_last = find_last(n - 1, deliveries)
    p_last = find_last(n - 1, pickups)

    while d_last >= 0 or p_last >= 0:
        now = cap
        min_val += (max(d_last, p_last) + 1) * 2
        # 택배 배송
        for i in range(d_last, -1, -1):
            delivery = deliveries[i]
            if delivery <= now:
                now -= delivery
                deliveries[i] = 0
            elif delivery > 0:
                deliveries[i] -= now
                d_last = i
                break
        else:
            d_last = -1

        now = cap

        # 상자 수거
        for i in range(p_last, -1, -1):
            pickup = pickups[i]
            if pickup <= now:
                now -= pickup
                pickups[i] = 0
            elif pickup > 0:
                pickups[i] -= now
                p_last = i
                break
        else:
            p_last = -1

    return min_val