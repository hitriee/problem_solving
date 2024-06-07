# 240607
# 56592 KB / 1140 ms
from sys import stdin

def to_int():
    return int(stdin.readline())

while True:
    N = to_int()
    if N == 0:
        break
    acc = [0]
    max_total = -1000
    for _ in range(N):
        profit = to_int()
        acc.append(acc[-1] + profit)
        if profit > max_total:
            max_total = profit

    max_total = max(*acc[1:], max_total)
    stack = [acc[1]]
    for i in range(2, N+1):
        profit = acc[i]
        while stack[-1] > profit:
            stack.pop()
            if not stack:
                break
        else:
            dif = profit - stack[0]
            if dif > max_total:
                max_total = dif
        stack.append(profit)

    print(max_total)



# 70452 KB / 1100 ms
from sys import stdin

def to_int():
    return int(stdin.readline())

while True:
    N = to_int()
    if N == 0:
        break
    acc = [0]
    profits = [to_int() for _ in range(N)]
    max_total = -1000
    for i in range(N):
        acc.append(acc[-1] + profits[i])

    max_total = max(*acc[1:], *profits)
    stack = [acc[1]]
    for i in range(2, N+1):
        profit = acc[i]
        while stack[-1] > profit:
            stack.pop()
            if not stack:
                break
        else:
            dif = profit - stack[0]
            if dif > max_total:
                max_total = dif
        stack.append(profit)

    print(max_total)
