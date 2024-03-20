# 240320
# 31120 KB / 44 ms
n = int(input())
if n == 1:
    print(1)
else:
    b_before, before = 0, 1
    for _ in range(1, n):
        b_before, before = before, before + b_before
    print(before)