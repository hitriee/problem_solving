# 231108
# 176196 KB / 3460 ms
from sys import stdin
T = int(stdin.readline())
for _ in range(T):
    N = int(stdin.readline())
    index_list = list(map(int, stdin.readline().split()))
    max_val = index_list[-1]
    total_profit = cnt = buy_value = 0
    for i in range(N-2, -1, -1):
        now = index_list[i]
        if max_val <= now:
            total_profit += max(cnt * max_val - buy_value, 0)
            max_val = now
            cnt = buy_value = 0
        else:
            buy_value += now
            cnt += 1

    total_profit += max(cnt * max_val - buy_value, 0)

    print(total_profit)


# 176196 KB / 3448 ms
from sys import stdin
T = int(stdin.readline())
for _ in range(T):
    N = int(stdin.readline())
    index_list = list(map(int, stdin.readline().split()))
    max_val = index_list[-1]
    total_profit = cnt = buy_value = 0
    for i in range(N-2, -1, -1):
        now = index_list[i]
        if max_val <= now:
            total_profit += cnt * max_val - buy_value
            max_val = now
            cnt = buy_value = 0
        else:
            buy_value += now
            cnt += 1

    total_profit += cnt * max_val - buy_value

    print(total_profit)


# 176196 KB / 3448 ms
from sys import stdin
T = int(stdin.readline())
for _ in range(T):
    N = int(stdin.readline())
    index_list = list(map(int, stdin.readline().split()))
    max_val = index_list[-1]
    total_profit = cnt = 0
    for i in range(N-2, -1, -1):
        now = index_list[i]
        if max_val <= now:
            total_profit += cnt * max_val
            max_val, cnt = now, 0
        else:
            total_profit -= now
            cnt += 1

    total_profit += cnt * max_val

    print(total_profit)
