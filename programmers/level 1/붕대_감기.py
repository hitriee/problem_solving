# 240313
def calc_min(bandage, now, health, dif):
    after = now + dif * bandage[1]
    if dif >= bandage[0]:
        after += (dif // bandage[0]) * bandage[2]

    return min(after, health)


def solution(bandage, health, attacks):
    n = len(attacks)
    now, before_time = health - attacks[0][1], attacks[0][0]
    for i in range(1, n):
        if now <= 0:
            return -1
        time, power = attacks[i]
        now = calc_min(bandage, now, health, time - before_time - 1) - power
        before_time = time

    return now if now > 0 else -1