#230617
# 완전 탐색
N = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))
results = []
def calc(num1, num2, operator):
    if operator == 0:
        return num1+num2
    elif operator == 1:
        return num1-num2
    elif operator == 2:
        return num1*num2
    elif num1 * num2 > 0:
        return num1//num2
    else:
        return -((-num1)//num2)

def dfs(level, result):
    if level == N:
        results.append(result)
        return
    for i in range(4):
        if operators[i] > 0:
            operators[i] -= 1
            dfs(level+1, calc(result, numbers[level], i))
            operators[i] += 1

dfs(1, numbers[0])
print(max(results), min(results), sep='\n')


#
def return_answer():
    N = int(input())
    numbers = list(map(int, input().split()))
    operators = list(map(int, input().split()))
    results = []

    def calc(num1, num2, operator):
        if operator == 0:
            return num1+num2
        elif operator == 1:
            return num1-num2
        elif operator == 2:
            return num1*num2
        elif num1 * num2 > 0:
            return num1//num2
        else:
            return -((-num1)//num2)

    def dfs(level, result):
        if level == N:
            results.append(result)
            return
        for i in range(4):
            if operators[i] > 0:
                operators[i] -= 1
                dfs(level+1, calc(result, numbers[level], i))
                operators[i] += 1

    dfs(1, numbers[0])
    return f'{max(results)}\n{min(results)}'

print(return_answer())