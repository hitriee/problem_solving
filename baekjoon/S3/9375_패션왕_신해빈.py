# 230527
# 231212
# 31120 KB / 40 ms
from sys import stdin

new_input = stdin.readline
T = int(new_input())
for _ in range(T):
    clothes = {}
    cnt = 1
    N = int(new_input())
    for _ in range(N):
        kind = new_input().split()[1]
        if clothes.get(kind):
            clothes[kind] += 1
        else:
            clothes[kind] = 2

    for value in clothes.values():
        cnt *= value

    print(cnt - 1)

