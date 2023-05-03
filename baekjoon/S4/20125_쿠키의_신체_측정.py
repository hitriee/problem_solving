#230503
N = int(input())
board = [input() for _ in range(N)]
heart = []
body = []
def find_heart():
    for i in range(N):
        for j in range(N):
            if board[i][j] == '*':
                heart.extend((i+1, j))
                return
def find_arm(start, step):
    for j in range(start, heart[1], step):
        if board[heart[0]][j] == '*':
            body.append(abs(j - heart[1]))
            return
def find_lower_body(start, col):
    for i in range(start+1, N):
        if board[i][col] != '*':
            body.append(i-start-1)
            return i - 1
    body.append(N-start-1)

find_heart()
find_arm(0, 1)
find_arm(N-1, -1)
waist_end_point = find_lower_body(*heart)
find_lower_body(waist_end_point, heart[1]-1)
find_lower_body(waist_end_point, heart[1]+1)

print(heart[0]+1, heart[1]+1)
print(*body)


#
N = int(input())
board = [input() for _ in range(N)]
heart = []
body = []
def find_heart():
    for i in range(N):
        for j in range(N):
            if board[i][j] == '*':
                heart.extend((i+1, j))
                return
def find_arm(start, step):
    for j in range(start, heart[1], step):
        if board[heart[0]][j] == '*':
            body.append(abs(j - heart[1]))
            return
def find_lower_body(start, col):
    for i in range(start+1, N):
        if board[i][col] != '*':
            body.append(i-start-1)
            return i - 1
    body.append(N-start-1)

find_heart()
for start, step in (0, 1), (N-1, -1):
    find_arm(start, step)
waist_end_point = find_lower_body(*heart)
for num in (-1, 1):
    find_lower_body(waist_end_point, heart[1]+num)

print(heart[0]+1, heart[1]+1)
print(*body)