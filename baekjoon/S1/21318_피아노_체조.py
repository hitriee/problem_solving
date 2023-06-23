#230623
#
from sys import stdin

def to_int(): return int(stdin.readline())
def to_map_int(): return map(int, stdin.readline().split())

N = to_int()
difficulty = [0]
difficulty.extend(list(to_map_int()))
Q = to_int()
mistake = [0] * N
for i in range(1, N):
    if difficulty[i] > difficulty[i+1]:
        mistake[i] = mistake[i-1] + 1
    else:
        mistake[i] = mistake[i-1]
for _ in range(Q):
    x, y = to_map_int()
    print(mistake[y-1] - mistake[x-1])

#
from sys import stdin

def to_int(): return int(stdin.readline())
def to_map_int(): return map(int, stdin.readline().split())

N = to_int()
difficulty = [0]
difficulty.extend(list(to_map_int()))
Q = to_int()

mistake = [0] * (N+1)
for i in range(1, N):
    if difficulty[i] > difficulty[i+1]:
        mistake[i+1] = mistake[i] + 1
    else:
        mistake[i+1] = mistake[i]
for _ in range(Q):
    x, y = to_map_int()
    print(mistake[y] - mistake[x])



#
def print_difficulty():
    from sys import stdin

    def to_int(): return int(stdin.readline())
    def to_map_int(): return map(int, stdin.readline().split())

    N = to_int()
    difficulty = [0]
    difficulty.extend(list(to_map_int()))
    Q = to_int()

    mistake = [0] * (N+1)
    for i in range(1, N):
        if difficulty[i] > difficulty[i+1]:
            mistake[i+1] = mistake[i] + 1
        else:
            mistake[i+1] = mistake[i]

    for _ in range(Q):
        x, y = to_map_int()
        print(mistake[y] - mistake[x])

print_difficulty()


#
def print_difficulty():
    from sys import stdin

    def to_int(): return int(stdin.readline())
    def to_map_int(): return map(int, stdin.readline().split())

    N = to_int()
    difficulty = [0]
    difficulty.extend(list(to_map_int()))
    Q = to_int()

    mistake = [0] * (N+1)
    for i in range(1, N):
        mistake[i+1] = mistake[i]
        if difficulty[i] > difficulty[i+1]:
            mistake[i+1] += 1

    for _ in range(Q):
        x, y = to_map_int()
        print(mistake[y] - mistake[x])

print_difficulty()