# 240320
# 31120 KB / 44 ms
N = int(input())
schedules = [tuple(map(int, input().split())) for _ in range(N)]
dp = [0] * (N+1)
max_revenue = 0

for i in range(N):
    if max_revenue < dp[i]:
        max_revenue = dp[i]

    next_i = i+schedules[i][0]
    if next_i <= N:
        new_revenue = max_revenue + schedules[i][1]
        if dp[next_i] < new_revenue:
            dp[next_i] = new_revenue

print(max(dp))


