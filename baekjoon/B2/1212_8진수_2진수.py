#230701
number = input()
if number == '0':
    print('0')
else:
    number = number.lstrip('0')
    length = len(number)
    converted_num = {}
    key = 0
    for i in range(2):
        for j in range(2):
            for k in range(2):
                converted_num[str(key)] = f'{i}{j}{k}'
                key += 1
    answer = []
    for i in range(length):
        answer.append(converted_num[number[i]])
    print(''.join(answer).lstrip('0'))


#
number = input()
if number == '0':
    print('0')
else:
    number = number.lstrip('0')
    length = len(number)
    converted_num = {}
    key = 0
    value = []
    for i in range(2):
        value.append(str(i))
        for j in range(2):
            value.append(str(j))
            for k in range(2):
                value.append(str(k))
                converted_num[str(key)] = ''.join(value)
                key += 1
                value.pop()
            value.pop()
        value.pop()
    answer = []
    for i in range(length):
        answer.append(converted_num[number[i]])
    print(''.join(answer).lstrip('0'))


#
def binary_num():
    number = input()
    if number == '0':
        return '0'

    number = number.lstrip('0')
    length = len(number)
    converted_num = {}
    key = 0
    for i in range(2):
        for j in range(2):
            for k in range(2):
                converted_num[str(key)] = f'{i}{j}{k}'
                key += 1
    answer = [converted_num[number[0]].lstrip('0')]
    for i in range(1, length):
        answer.append(converted_num[number[i]])
    return ''.join(answer)

print(binary_num())
