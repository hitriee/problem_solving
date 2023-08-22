#230822
N = int(input())
alp_weight = {}
alp_to_num = {}
words = []
max_len = 0
for _ in range(N):
    word = input()
    length = len(word)
    if max_len < length:
        max_len = length
    words.append(word.rjust(8, ' '))
cnt = 9
for i in range(8-max_len, 8):
    weight = 10**(8-i)
    for j in range(N):
        alp = words[j][i]
        if alp != ' ':
            if alp_weight.get(alp):
                alp_weight[alp] += weight
            else:
                alp_weight[alp] = weight
items = list(alp_weight.items())
items.sort(key=lambda item: -item[1])

for item in items:
    alp_to_num[item[0]] = str(cnt)
    cnt -= 1

total = 0
for i in range(N):
    word = words[i].lstrip()
    num = ''
    for alp in word:
        num += alp_to_num[alp]
    total += int(num)

print(total)



#
def find_max():
    N = int(input())
    alp_weight, alp_to_num = {}, {}
    words = []
    max_len = 0
    for _ in range(N):
        word = input()
        length = len(word)
        if max_len < length:
            max_len = length
        words.append(word.rjust(8, ' '))

    cnt = 9
    for i in range(8-max_len, 8):
        weight = 10**(8-i)
        for j in range(N):
            alp = words[j][i]
            if alp != ' ':
                if alp_weight.get(alp):
                    alp_weight[alp] += weight
                else:
                    alp_weight[alp] = weight
    items = list(alp_weight.items())
    items.sort(key=lambda item: -item[1])

    for item in items:
        alp_to_num[item[0]] = str(cnt)
        cnt -= 1

    total = 0
    for i in range(N):
        word = words[i].lstrip()
        num = ''
        for alp in word:
            num += alp_to_num[alp]
        total += int(num)

    return total

print(find_max())


#
def find_max():
    N = int(input())
    alp_weight, alp_to_num = {}, {}
    words = []
    max_len = 0
    for _ in range(N):
        word = input()
        length = len(word)
        if max_len < length:
            max_len = length
        words.append(word.rjust(8, ' '))

    words.sort(reverse=True)

    cnt = 9
    for i in range(8-max_len, 8):
        weight = 10**(8-i)
        for j in range(N):
            alp = words[j][i]
            if alp == ' ':
                break
            if alp_weight.get(alp):
                alp_weight[alp] += weight
            else:
                alp_weight[alp] = weight
    items = list(alp_weight.items())
    items.sort(key=lambda item: -item[1])

    for item in items:
        alp_to_num[item[0]] = str(cnt)
        cnt -= 1

    total = 0
    for i in range(N):
        word = words[i].lstrip()
        num = ''
        for alp in word:
            num += alp_to_num[alp]
        total += int(num)

    return total

print(find_max())


#
def find_max():
    N = int(input())
    alp_weight, alp_to_num = {}, {}
    words = []
    max_len = 0
    for _ in range(N):
        word = input()
        length = len(word)
        if max_len < length:
            max_len = length
        words.append(word.rjust(8, ' '))

    words.sort(reverse=True)

    cnt = 9
    weight = 10 ** max_len
    for i in range(8 - max_len, 8):
        for j in range(N):
            alp = words[j][i]
            if alp == ' ':
                break
            if alp_weight.get(alp):
                alp_weight[alp] += weight
            else:
                alp_weight[alp] = weight
        weight //= 10
    items = list(alp_weight.items())
    items.sort(key=lambda item: -item[1])

    for item in items:
        alp_to_num[item[0]] = str(cnt)
        cnt -= 1

    total = 0
    for i in range(N):
        word = words[i].lstrip()
        num = ''
        for alp in word:
            num += alp_to_num[alp]
        total += int(num)

    return total


print(find_max())


#
def find_max():
    N = int(input())
    alp_weight, alp_to_num = {}, {}
    words = []
    max_len = 0

    # 길이를 8로 맞춰주기
    for _ in range(N):
        word = input()
        length = len(word)
        if max_len < length:
            max_len = length
        words.append(word.rjust(8, ' '))

    weight = 10 ** max_len
    for i in range(8 - max_len, 8):
        for j in range(N):
            alp = words[j][i]
            if alp != ' ':
                if alp_weight.get(alp):
                    alp_weight[alp] += weight
                else:
                    alp_weight[alp] = weight
        weight //= 10

    cnt = 9
    items = list(alp_weight.items())
    items.sort(key=lambda item: -item[1])
    for item in items:
        alp_to_num[item[0]] = str(cnt)
        cnt -= 1

    total = 0
    for i in range(N):
        word = words[i].lstrip()
        num = ''
        for alp in word:
            num += alp_to_num[alp]
        total += int(num)

    return total


print(find_max())