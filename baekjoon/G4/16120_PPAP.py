# 250206
# 39856 KB / 288 ms
def main():
    input_str = input()
    N = len(input_str)
    stack = list(input_str[:3])
    reversed_substring = 'APP'
    for i in range(3, N):
        alp = input_str[i]
        if alp == 'P':
            if len(stack) >= 3:
                for j in range(3):
                    if stack[-1-j] != reversed_substring[j]:
                        break
                else:
                    for _ in range(3):
                        stack.pop()
        stack.append(alp)

    while len(stack) > 1:
        alp = stack[-1]
        if alp != 'P' or len(stack) < 4:
            return 'NP'

        for j in range(1, 4):
            if stack[-1 - j] != reversed_substring[j-1]:
                return 'NP'
        else:
            for _ in range(4):
                stack.pop()

    return 'PPAP' if stack[-1] == 'P' else 'NP'

print(main())



# 39856 KB / 324 ms
def main():
    def is_ppap():
        for j in range(1, 4):
            if stack[-1 - j] != target[j-1]:
                return False

        for _ in range(3):
            stack.pop()

        return True

    input_str = input()
    N = len(input_str)
    stack = list(input_str[:3])
    target = 'APP'
    for i in range(3, N):
        alp = input_str[i]
        stack.append(alp)
        if alp == 'P':
            if len(stack) >= 4:
                is_ppap()


    while len(stack) > 1:
        alp = stack[-1]
        if alp != 'P' or len(stack) < 4:
            return 'NP'

        if not is_ppap():
            return 'NP'

    return 'PPAP' if stack[-1] == 'P' else 'NP'

print(main())
