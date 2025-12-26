# 251222
# 32412 KB / 96 ms
def main():
    from sys import stdin

    new_input = stdin.readline
    limit = int(1e9)
    result = []

    def perform(command):
        length = len(stack)
        if command[:3] == 'NUM':
            stack.append(int(command[4:]))
            return

        if length == 0:
            return 'ERROR'

        last = stack[-1]
        if command == 'POP':
            stack.pop()
            return
        elif command == 'INV':
            stack[-1] = -last
            return
        elif command == 'DUP':
            stack.append(last)
            return

        if length == 1:
            return 'ERROR'

        pre_last = stack[-2]
        if command == 'SWP':
            stack[-1], stack[-2] = pre_last, last
            return

        for _ in range(2):
            stack.pop()

        if command == 'ADD':
            answer = pre_last + last
            if abs(answer) <= limit:
                stack.append(answer)
                return
            else:
                return 'ERROR'
        elif command == 'SUB':
            answer = pre_last - last
            if abs(answer) <= limit:
                stack.append(answer)
                return
            else:
                return 'ERROR'
        elif command == 'MUL':
            answer = pre_last * last
            if abs(answer) <= limit:
                stack.append(answer)
                return
            else:
                return 'ERROR'

        if last == 0:
            return 'ERROR'

        if command == 'DIV':
            is_minus = pre_last * last < 0
            answer = abs(pre_last) // abs(last)
        else:
            is_minus = pre_last < 0
            answer = abs(pre_last) % abs(last)

        stack.append(-answer if is_minus else answer)

    while True:
        program = []
        while True:
            val = new_input().rstrip()
            if val == 'QUIT':
                return '\n\n'.join(result)

            if val == 'END':
                break

            program.append(val)

        N = int(new_input())
        part_of = []
        for _ in range(N):
            stack = [int(new_input())]
            for command in program:
                if perform(command):
                    part_of.append('ERROR')
                    break
            else:
                part_of.append(str(stack[-1]) if len(stack) == 1 else 'ERROR')
        new_input()
        result.append('\n'.join(part_of))

print(main())




# 32412 KB / 116 ms
def main():
    from sys import stdin

    new_input = stdin.readline
    limit = int(1e9)
    result = []

    def perform(command):
        length = len(stack)
        if command[:3] == 'NUM':
            return [int(command[4:])]

        if length == 0:
            return 'ERROR'

        last = stack[-1]
        if command == 'POP':
            stack.pop()
            return []
        elif command == 'INV':
            stack.pop()
            return [-last]
        elif command == 'DUP':
            return [last]

        if length == 1:
            return 'ERROR'

        pre_last = stack[-2]
        for _ in range(2):
            stack.pop()

        if command == 'SWP':
            return [last, pre_last]

        if command == 'ADD':
            answer = pre_last + last
            return [answer] if abs(answer) <= limit else 'ERROR'

        elif command == 'SUB':
            answer = pre_last - last
            return [answer] if abs(answer) <= limit else 'ERROR'
        elif command == 'MUL':
            answer = pre_last * last
            return [answer] if abs(answer) <= limit else 'ERROR'

        if last == 0:
            return 'ERROR'

        if command == 'DIV':
            is_minus = pre_last * last < 0
            answer = abs(pre_last) // abs(last)
        else:
            is_minus = pre_last < 0
            answer = abs(pre_last) % abs(last)

        return [-answer if is_minus else answer]

    while True:
        program = []
        while True:
            val = new_input().rstrip()
            if val == 'QUIT':
                return '\n\n'.join(result)

            if val == 'END':
                break

            program.append(val)

        N = int(new_input())
        part_of = []
        for _ in range(N):
            stack = [int(new_input())]
            for command in program:
                answer = perform(command)
                if answer == 'ERROR':
                    part_of.append('ERROR')
                    break
                else:
                    stack.extend(answer)
            else:
                part_of.append(str(stack[-1]) if len(stack) == 1 else 'ERROR')
        new_input()
        result.append('\n'.join(part_of))


print(main())