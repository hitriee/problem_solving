#231016
# 41540 KB / 404 ms
from sys import stdin

cursor_left = list(stdin.readline().rstrip())
cursor_right = []
N = int(stdin.readline())

for _ in range(N):
    command = stdin.readline().rstrip()
    if command.startswith('L'):
        if cursor_left:
            cursor_right.append(cursor_left.pop())
    elif command.startswith('D'):
        if cursor_right:
            cursor_left.append(cursor_right.pop())
    elif command.startswith('B'):
        if cursor_left:
            cursor_left.pop()
    else:
        cursor_left.append(command[2:])

print(''.join(cursor_left+cursor_right[::-1]))


# 41540 KB / 304 ms
def return_str():
    from sys import stdin

    cursor_left = list(stdin.readline().rstrip())
    cursor_right = []
    N = int(stdin.readline())

    for _ in range(N):
        command = stdin.readline().rstrip()
        if command.startswith('L'):
            if cursor_left:
                cursor_right.append(cursor_left.pop())
        elif command.startswith('D'):
            if cursor_right:
                cursor_left.append(cursor_right.pop())
        elif command.startswith('B'):
            if cursor_left:
                cursor_left.pop()
        else:
            cursor_left.append(command[2:])

    return ''.join(cursor_left + cursor_right[::-1])

print(return_str())