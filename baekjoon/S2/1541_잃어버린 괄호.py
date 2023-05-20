#230520
# 그리디
equation = input()
splited = []
result = []
mark_set = {'+', '-'}
end = len(equation)
for i in range(len(equation)-2, -1, -1):
    element = equation[i]
    if element in mark_set:
        splited.append(int(equation[i+1:end]))
        end = i
        if element == '-':
            result.append(sum(splited))
            splited.clear()
splited.append(int(equation[:end]))
print(sum(splited) - sum(result))


#
def calc():
    equation = input()
    splited, result = [], []

    mark_set = {'+', '-'}
    end = len(equation)
    for i in range(len(equation)-2, -1, -1):
        element = equation[i]
        if element in mark_set:
            splited.append(int(equation[i+1:end]))
            end = i
            if element == '-':
                result.append(sum(splited))
                splited.clear()
    splited.append(int(equation[:end]))
    return sum(splited) - sum(result)

print(calc())



