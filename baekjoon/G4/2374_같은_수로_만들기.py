# 231129
# 31120 KB / 40 ms
from sys import stdin
def to_int():
    return int(stdin.readline())

N = to_int()
stack = [to_int()]
add_cnt = 0

for _ in range(N-1):
    num = to_int()
    while num > stack[-1]:
        last = stack.pop()
        if stack:
            add_cnt += (min(stack[-1], num) - last)
        else:
            add_cnt += (num - last)
            break

    stack.append(num)

for i in range(len(stack)-1):
    add_cnt += stack[i] - stack[i+1]

print(add_cnt)


# 31120 KB / 40 ms
from sys import stdin
def to_int():
    return int(stdin.readline())

N = to_int()
stack = [to_int()]
add_cnt = 0

for _ in range(N-1):
    num = to_int()
    if num > stack[-1]:
        while True:
            last = stack.pop()
            if stack and num > stack[-1]:
                add_cnt += (stack[-1] - last)
            else:
                add_cnt += (num - last)
                break

    stack.append(num)

for i in range(len(stack)-1):
    add_cnt += stack[i] - stack[i+1]

print(add_cnt)