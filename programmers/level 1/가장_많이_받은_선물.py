# 240403
def solution(friends, gifts):
    n, m = len(friends), len(gifts)
    friend_to_i = {friends[i]: i for i in range(n)}
    detail = [[0] * n for _ in range(n)]
    gift_index, cnt_list = [0] * n, [0] * n

    for i in range(m):
        a, b = map(lambda x: friend_to_i[x], gifts[i].split())
        detail[a][b] += 1
        gift_index[a] += 1
        gift_index[b] -= 1

    for i in range(n):
        for j in range(i + 1, n):
            give_cnt, receive_cnt = detail[i][j], detail[j][i]
            if give_cnt > receive_cnt:
                cnt_list[i] += 1
            elif give_cnt < receive_cnt:
                cnt_list[j] += 1
            else:
                i_index, j_index = gift_index[i], gift_index[j]
                if i_index > j_index:
                    cnt_list[i] += 1
                elif i_index < j_index:
                    cnt_list[j] += 1

    return max(cnt_list)