# 240425
def solution(board, h, w):
    answer = 0
    n, m = len(board), len(board[0])
    ref = board[h][w]
    for dh, dw in (-1, 0), (1, 0), (0, -1), (0, 1):
        nh, nw = h+dh, w+dw
        if 0 <= nh < n and 0 <= nw < m and ref == board[nh][nw]:
            answer += 1
    return answer