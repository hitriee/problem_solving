# 250207
# 32412 KB / 32 ms
def main():
    # 123 -> 3
    # 33(562(71(9))) -> 19
    # [1, 3, '(', 6]
    # [
    # 3(567979)*3

    S = input()
    N = len(S)
    stack = []
    length = i = 0
    while i < N:
        element = S[i]
        if element == ')':
            if length:
                stack.append(length)
                length = 0

            multiple = 0
            while True:
                val = stack.pop()
                if val == '(':
                    break
                multiple += int(val)
            multiple *= int(stack.pop())
            if not stack:
                stack.append(multiple)
            else:
                stack[-1] += multiple

        elif i < N-1 and S[i+1] == '(':
            stack.extend([length, int(element), '('])
            length = 0
            i += 1
        else:
            length += 1
        i += 1


    return sum(stack) + length if stack else length

print(main())




# 32412 KB / 44 ms
def main():
    S = input()
    N = len(S)
    stack = []
    length = i = 0
    while i < N:
        element = S[i]
        if element == ')':
            if length:
                stack.append(length)
                length = 0

            multiple = 0
            while True:
                val = stack.pop()
                if val == '(':
                    break
                multiple += val
            multiple *= stack.pop()
            if not stack:
                stack.append(multiple)
            else:
                stack[-1] += multiple

        elif i < N - 1 and S[i + 1] == '(':
            stack.extend([length, int(element), '('])
            length = 0
            i += 1
        else:
            length += 1
        i += 1

    return sum(stack) + length if stack else length


print(main())