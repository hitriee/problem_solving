# 240319
def solution(info, edges):
    from collections import deque
    n = len(info)
    max_cnt = 0
    link_info = [set() for _ in range(n)]
    for parent, child in edges:
        link_info[parent].add(child)
    q = deque()
    q.append((0, 1, 0, set()))
    while q:
        now, s_cnt, w_cnt, candidate = q.popleft()
        if max_cnt < s_cnt:
            max_cnt = s_cnt
        new_candidate = candidate | link_info[now]
        for next in new_candidate:
            if info[next] == 0:
                q.append((next, s_cnt + 1, w_cnt, new_candidate - {next}))
            elif s_cnt > w_cnt + 1:
                q.append((next, s_cnt, w_cnt + 1, new_candidate - {next}))

    return max_cnt