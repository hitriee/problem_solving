#230522
original = input()
bomb = input()
limit = len(bomb)
stack = []
for element in original:
    stack.append(element)
    if len(stack) >= limit:
        for i in range(-1, -limit-1, -1):
            if stack[i] != bomb[i]:
                break
        else:
            for _ in range(limit):
                stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')



#
original = input()
bomb = input()
limit = len(bomb)
stack = []
length = 0
for element in original:
    stack.append(element)
    length += 1
    if length >= limit:
        for i in range(-1, -limit-1, -1):
            if stack[i] != bomb[i]:
                break
        else:
            for _ in range(limit):
                stack.pop()
            length -= limit

if stack:
    print(''.join(stack))
else:
    print('FRULA')


#
def bomb_string():
    original = input()
    bomb = input()
    limit = len(bomb)
    stack = []
    for element in original:
        stack.append(element)
        if len(stack) >= limit:
            for i in range(-1, -limit-1, -1):
                if stack[i] != bomb[i]:
                    break
            else:
                for _ in range(limit):
                    stack.pop()

    return ''.join(stack) if stack else 'FRULA'

print(bomb_string())


#
def bomb_string():
    original = input()
    bomb = input()
    stack = []
    for element in original:
        stack.append(element)
        if len(stack) >= len(bomb):
            for i in range(-1, -len(bomb) - 1, -1):
                if stack[i] != bomb[i]:
                    break
            else:
                for _ in range(len(bomb)):
                    stack.pop()

    return ''.join(stack) if stack else 'FRULA'


print(bomb_string())


#
def bomb_string():
    original = input()
    bomb = input()
    limit = len(bomb)
    stack = []
    def bomb_one_string():
        for i in range(-1, -limit - 1, -1):
            if stack[i] != bomb[i]:
                return
        for _ in range(limit):
            stack.pop()

    for element in original:
        stack.append(element)
        if len(stack) >= limit:
            bomb_one_string()

    return ''.join(stack) if stack else 'FRULA'

print(bomb_string())


#
def bomb_string():
    original = input()
    bomb = input()
    stack = []
    for element in original:
        stack.append(element)

        if element == bomb[-1] and len(stack) >= len(bomb):
            for i in range(-1, -len(bomb) - 1, -1):
                if stack[i] != bomb[i]:
                    break
            else:
                for _ in range(len(bomb)):
                    stack.pop()

    return ''.join(stack) if stack else 'FRULA'

print(bomb_string())


#
def bomb_string():
    original = input()
    bomb = input()
    limit = len(bomb)
    stack = []
    for element in original:
        stack.append(element)

        if element == bomb[-1] and len(stack) >= limit:
            for i in range(-2, -limit - 1, -1):
                if stack[i] != bomb[i]:
                    break
            else:
                for _ in range(limit):
                    stack.pop()

    return ''.join(stack) if stack else 'FRULA'

print(bomb_string())