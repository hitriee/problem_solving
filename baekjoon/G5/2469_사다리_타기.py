# 250123
# 33432 KB / 40 ms
def main():
    from sys import stdin

    new_input = stdin.readline
    k = int(new_input())
    n = int(new_input())
    initial = ''.join([chr(ord('A')+i) for i in range(k)])
    result = new_input().rstrip()
    board = []
    answer, idx = '', 0

    for i in range(n):
        row = new_input().rstrip()
        if row[0] == '?':
            idx = i
        board.append(list(row))

    top, bottom = [''] * k, [''] * k
    for j in range(k):
        col = j
        for row in range(idx):
            if col < k-1 and board[row][col] == '-':
                col += 1
            elif col > 0 and board[row][col-1] == '-':
                col -= 1
        top[col] = initial[j]

    for j in range(k):
        col = j
        for row in range(n-1, idx, -1):
            if col < k-1 and board[row][col] == '-':
                col += 1
            elif col > 0 and board[row][col-1] == '-':
                col -= 1
        bottom[col] = result[j]

    i = 0
    while i < k-1:
        if top[i] == bottom[i]:
            answer += '*'
            i += 1
        elif top[i] == bottom[i+1] and bottom[i] == top[i+1]:
            answer += '-*'
            i += 2
        else:
            return 'x'*(k-1)
    if i == k:
        return answer[:-1]

    return answer

print(main())