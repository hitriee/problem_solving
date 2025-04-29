# 250429
def solution(players, m, k):
    from collections import deque

    q = deque()
    total_cnt = cnt = 0

    for i in range(24):
        player = players[i]
        if player >= m * (cnt + 1):
            new_cnt = player // m
            q.append((i + k - 1, new_cnt - cnt))
            total_cnt += new_cnt - cnt
            cnt = new_cnt

        if q and q[0][0] == i:
            cnt -= q.popleft()[1]

    return total_cnt