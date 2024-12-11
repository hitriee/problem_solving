# 241211
def solution(m, n, board):
    board = [list(board[i]) for i in range(m)]
    cnt = 0
    while True:
        removed = set()
        for i in range(m-1):
            for j in range(n-1):
                block = board[i][j]
                if block == '':
                    continue

                temp = [(i, j)]
                for di, dj in (1, 0), (1, 1), (0, 1):
                    ni, nj = i+di, j+dj
                    if board[ni][nj] != block:
                        break
                    temp.append((ni, nj))
                else:
                    removed.update(temp)

        if not removed:
            return cnt

        cnt += len(removed)
        for i, j in removed:
            board[i][j] = ''

        new_board = [[''] * n for _ in range(m)]
        for j in range(n):
            idx = m-1
            for i in range(m-1, -1, -1):
                if board[i][j] != '':
                    new_board[idx][j] = board[i][j]
                    idx -= 1

            for i in range(m):
                board[i][j] = new_board[i][j]



'''
테스트 1 〉	통과 (0.05ms, 10.3MB)
테스트 2 〉	통과 (0.07ms, 10.4MB)
테스트 3 〉	통과 (0.01ms, 10.4MB)
테스트 4 〉	통과 (1.16ms, 10.3MB)
테스트 5 〉	통과 (75.29ms, 10.4MB)
테스트 6 〉	통과 (5.43ms, 10.3MB)
테스트 7 〉	통과 (0.66ms, 10.4MB)
테스트 8 〉	통과 (1.17ms, 10.3MB)
테스트 9 〉	통과 (0.08ms, 10.3MB)
테스트 10 〉	통과 (0.53ms, 10.2MB)
테스트 11 〉	통과 (1.58ms, 10.3MB)
'''