#230607
N = int(input())
colors = [list(map(int, input().split())) for _ in range(N)]
target = list(map(int, input().split()))
min_dif = 255*3

def sum_avg(a, b, cnt):
    total = 0
    for j in range(3):
        total += abs(a[j] - b[j]//cnt)
    return total

def dfs(level, now, start):
    global min_dif
    if level == 7:
        return
    for j in range(start, N):
        dr, dg, db = colors[j]
        r, g, b = now
        new_now = [r+dr, g+dg, b+db]
        dfs(level+1, new_now, j+1)
        dif = sum_avg(target, new_now, level+1)
        if dif < min_dif:
            min_dif = dif

for i in range(N):
    dfs(1, colors[i], i+1)

print(min_dif)
