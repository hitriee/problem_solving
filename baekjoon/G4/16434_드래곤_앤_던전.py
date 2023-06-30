#230630
from sys import stdin
from math import ceil

def to_int(): return map(int, stdin.readline().split())

N, attack = to_int()
max_hp = hp = 1
for _ in range(N):
    t, a, h = to_int()
    if t == 1:
        hp += (ceil(h/attack) - 1) * a
    else:
        attack += a
        if hp > max_hp:
            max_hp = hp
        hp = max(1, hp - h)

print(max(max_hp, hp))


#
from sys import stdin
from math import ceil

def to_int(): return map(int, stdin.readline().split())

N, attack = to_int()
max_hp = hp = 1
for _ in range(N):
    t, a, h = to_int()
    if t == 1:
        hp += (ceil(h/attack) - 1) * a
        if hp > max_hp:
            max_hp = hp
    else:
        attack += a
        if hp > max_hp:
            max_hp = hp
        hp = max(1, hp - h)

print(max_hp)


#
def return_max_hp():
    from sys import stdin
    from math import ceil

    def to_int():
        return map(int, stdin.readline().split())

    N, attack = to_int()
    max_hp = hp = 1
    for _ in range(N):
        t, a, h = to_int()
        if t == 1:
            hp += (ceil(h / attack) - 1) * a
        else:
            attack += a
            if hp > max_hp:
                max_hp = hp
            hp = max(1, hp - h)

    return max(max_hp, hp)

print(return_max_hp())


#
def return_max_hp():
    from sys import stdin

    def to_int():
        return map(int, stdin.readline().split())

    N, attack = to_int()
    max_hp = hp = 1
    for _ in range(N):
        t, a, h = to_int()
        if t == 1:
            quot = h//attack
            hp += (quot if h%attack else quot - 1) * a
        else:
            attack += a
            if hp > max_hp:
                max_hp = hp
            hp = max(1, hp - h)

    return max(max_hp, hp)

print(return_max_hp())
