# 250326
# 34952 KB / 60 ms
def main():
    from collections import deque

    def calc(num1, num2, operator):
        if operator == '+':
            return num1+num2
        elif operator == '-':
            return num1-num2
        return num1 * num2

    N = int(input())
    formula = input()
    q = deque()
    q.append((int(formula[0]), 1))
    max_val = -2**31

    while q:
        num, idx = q.popleft()
        if idx == N:
            if max_val < num:
                max_val = num
            continue

        operator = formula[idx]
        next_num = int(formula[idx+1])
        idx += 2

        new_num = calc(num, next_num, operator)
        q.append((new_num, idx))
        if idx < N:
            new_num1 = calc(next_num, int(formula[idx+1]), formula[idx])
            new_num2 = calc(num, new_num1, operator)
            q.append((new_num2, idx+2))

    return max_val

print(main())






# 34952 KB / 60 ms
def main():
    def calc(num1, num2, operator):
        if operator == '+':
            return num1+num2
        elif operator == '-':
            return num1-num2
        return num1 * num2


    def bfs():
        from collections import deque

        q = deque()
        q.append((int(formula[0]), 1))
        max_val = -2 ** 31

        while q:
            num, idx = q.popleft()
            if idx == N:
                if max_val < num:
                    max_val = num
                continue

            operator = formula[idx]
            next_num = int(formula[idx+1])
            idx += 2

            new_num = calc(num, next_num, operator)
            q.append((new_num, idx))
            if idx < N:
                new_num1 = calc(next_num, int(formula[idx+1]), formula[idx])
                new_num2 = calc(num, new_num1, operator)
                q.append((new_num2, idx+2))

        return max_val



    N = int(input())
    formula = input()
    return bfs()

print(main())