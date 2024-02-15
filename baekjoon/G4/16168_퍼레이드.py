# 240215
# 31120 KB / 44 ms
from sys import stdin

def to_int():
    return map(int, stdin.readline().split())

V, E = to_int()
limit = V+1
cnt = [0] * limit
top_of = [i for i in range(limit)]

def find(a):
    if top_of[a] == a:
        return a

    root_a = find(top_of[a])
    top_of[a] = root_a

    return root_a

def union(a, b):
    root_a, root_b = find(a), find(b)
    if root_a != root_b:
        min_root = min(root_a, root_b)
        top_of[a] = top_of[b] = min_root

for _ in range(E):
    a, b = to_int()
    cnt[a] += 1
    cnt[b] += 1
    union(a, b)

odd_cnt = 0
for i in range(1, limit):
    if find(i) != 1:
        print('NO')
        break
    if cnt[i]%2:
        odd_cnt += 1
else:
    if odd_cnt == 0 or odd_cnt == 2:
        print('YES')
    else:
        print('NO')