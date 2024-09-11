# 240910
# 70676 KB / 312 ms
from sys import stdin

new_input = stdin.readline
N = int(new_input())
M = int(new_input())
room_state = [0] * (N+1)
for _ in range(M):
    x, y = map(int, new_input().split())
    room_state[x] += 1
    room_state[y] -= 1

for i in range(1, N+1):
    room_state[i] += room_state[i-1]

cnt = 0
for i in range(N):
    if room_state[i] <= 0:
        cnt += 1

print(cnt)



# 70676 KB / 292 ms
from sys import stdin

new_input = stdin.readline
N = int(new_input())
M = int(new_input())
room_state = [0] * (N+1)
for _ in range(M):
    x, y = map(int, new_input().split())
    room_state[x] += 1
    room_state[y] -= 1

cnt = 1
for i in range(1, N):
    room_state[i] += room_state[i-1]
    if room_state[i] <= 0:
        cnt += 1

print(cnt)



# 38932 KB / 60 ms
from sys import stdin

new_input = stdin.readline
N = int(new_input())
M = int(new_input())
room_state = [0] * (N+1)
if M:
    orders = [tuple(map(int, new_input().split())) for _ in range(M)]
    orders.sort()
    start, end = orders[0]
    cnt = start
    for i in range(1, M):
        x, y = orders[i]
        if x > end:
            cnt += x - end
            start, end = x, y
        elif y > end:
            end = y

    print(cnt + N - end)
else:
    print(N)




# 31120 KB / 36 ms
def cnt_room():
    from sys import stdin
    
    new_input = stdin.readline
    N = int(new_input())
    M = int(new_input())
    
    if M == 0:
        return N
    
    orders = [tuple(map(int, new_input().split())) for _ in range(M)]
    orders.sort()
    start, end = orders[0]
    cnt = start
    for i in range(1, M):
        x, y = orders[i]
        if x > end:
            cnt += x - end
            start, end = x, y
        elif y > end:
            end = y

    return cnt + N - end
        
print(cnt_room())

