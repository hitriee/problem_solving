#230408
N = int(input())
bomb_position = set()
for i in range(N):
    admin_map = input()
    for j in range(N):
        if admin_map[j] == '*':
            bomb_position.add((i, j))
user_map = [list(map(str, input())) for _ in range(N)]
direct = []
for di in range(-1, 2):
    for dj in range(-1, 2):
        direct.append((di, dj))
direct.remove((0, 0))
show_bomb = False
for i in range(N):
    for j in range(N):
        if user_map[i][j] == 'x':
            if (i, j) not in bomb_position:
                cnt = 0
                for di, dj in direct:
                    ni, nj = i+di, j+dj
                    if 0 <= ni < N and 0 <= nj < N and (ni, nj) in bomb_position:
                        cnt += 1
                user_map[i][j] = str(cnt)
            elif not show_bomb:
                show_bomb = True
if show_bomb:
    for i, j in bomb_position:
        user_map[i][j] = '*'
for i in range(N):
    print(''.join(user_map[i]))