#230502
T = int(input())
for _ in range(T):
    W = input()
    K = int(input())
    position = {}
    length = len(W)
    min_length = length + 1
    max_length = -1
    for i in range(length):
        alp = W[i]
        if position.get(alp):
            position[alp].append(i)
        else:
            position[alp] = [i]
    for value in position.values():
        value_len = len(value)
        if value_len >= K:
            for i in range(value_len - K + 1):
                dif = value[i + K - 1] - value[i] + 1
                if min_length > dif:
                    min_length = dif
                if max_length < dif:
                    max_length = dif
    if min_length == length + 1:
        print(-1)
    else:
        print(min_length, max_length)


#
T = int(input())
for _ in range(T):
    W = input()
    K = int(input())
    position = {}
    length = min_length = len(W)
    max_length = -1
    for i in range(length):
        alp = W[i]
        if position.get(alp):
            position[alp].append(i)
        else:
            position[alp] = [i]
    for value in position.values():
        value_len = len(value)
        if value_len >= K:
            for i in range(value_len - K + 1):
                dif = value[i + K - 1] - value[i] + 1
                if min_length > dif:
                    min_length = dif
                if max_length < dif:
                    max_length = dif
    if max_length == -1:
        print(-1)
    else:
        print(min_length, max_length)



#
from sys import stdin
new_input = stdin.readline
T = int(new_input())
for _ in range(T):
    W = new_input()
    K = int(new_input())
    position = {}
    length = min_length = len(W)
    max_length = -1
    for i in range(length):
        alp = W[i]
        if position.get(alp):
            position[alp].append(i)
        else:
            position[alp] = [i]
    for value in position.values():
        value_len = len(value)
        if value_len >= K:
            for i in range(value_len - K + 1):
                dif = value[i + K - 1] - value[i] + 1
                if min_length > dif:
                    min_length = dif
                if max_length < dif:
                    max_length = dif
    if max_length == -1:
        print(-1)
    else:
        print(min_length, max_length)

#
def find_length():
    W = new_input()
    K = int(new_input())
    position = {}
    length = min_length = len(W)
    max_length = -1

    for i in range(length):
        alp = W[i]
        if position.get(alp):
            position[alp].append(i)
        else:
            position[alp] = [i]

    for value in position.values():
        value_len = len(value)
        if value_len >= K:
            for i in range(value_len - K + 1):
                dif = value[i + K - 1] - value[i] + 1
                if min_length > dif:
                    min_length = dif
                if max_length < dif:
                    max_length = dif

    if max_length == -1:
        return -1
    return f'{min_length} {max_length}'

from sys import stdin
new_input = stdin.readline
T = int(new_input())
for _ in range(T):
    print(find_length())


#
def find_length():
    W = new_input()
    K = int(new_input())
    position = {}
    length = min_length = len(W)
    max_length = -1

    for i in range(length):
        alp = W[i]
        if position.get(alp):
            position[alp].append(i)
        else:
            position[alp] = [i]

    for value in position.values():
        value_len_dif = len(value) - K
        if value_len_dif >= 0:
            for i in range(value_len_dif + 1):
                dif = value[i + K - 1] - value[i] + 1
                if min_length > dif:
                    min_length = dif
                if max_length < dif:
                    max_length = dif

    if max_length == -1:
        return -1
    return f'{min_length} {max_length}'

from sys import stdin
new_input = stdin.readline
T = int(new_input())
for _ in range(T):
    print(find_length())


#
def find_length():
    from collections import defaultdict
    W = new_input()
    K = int(new_input())
    position = defaultdict(list)
    length = min_length = len(W)
    max_length = -1

    for i in range(length):
        position[W[i]].append(i)

    for value in position.values():
        value_len_dif = len(value) - K
        if value_len_dif >= 0:
            for i in range(value_len_dif + 1):
                dif = value[i + K - 1] - value[i] + 1
                if min_length > dif:
                    min_length = dif
                if max_length < dif:
                    max_length = dif

    if max_length == -1:
        return -1
    return f'{min_length} {max_length}'

from sys import stdin
new_input = stdin.readline
T = int(new_input())
for _ in range(T):
    print(find_length())


#
def print_length():
    def fill_position():
        for i in range(length):
            alp = W[i]
            if position.get(alp):
                position[alp].append(i)
            else:
                position[alp] = [i]
    def find_length():
        min_length, max_length = length, -1
        for value in position.values():
            value_len = len(value)
            if value_len >= K:
                for i in range(value_len - K + 1):
                    dif = value[i + K - 1] - value[i] + 1
                    if min_length > dif:
                        min_length = dif
                    if max_length < dif:
                        max_length = dif

        if max_length == -1:
            return -1
        return f'{min_length} {max_length}'

    from sys import stdin
    new_input = stdin.readline
    T = int(new_input())
    for _ in range(T):
        W = new_input()
        K = int(new_input())
        position = {}
        length = len(W)
        fill_position()
        print(find_length())

print_length()


#
def find_length():
    W = new_input()
    K = int(new_input())
    position = {}
    length = min_length = len(W)
    max_length = -1

    for i in range(length):
        alp = W[i]
        if position.get(alp):
            position[alp].append(i)
        else:
            position[alp] = [i]

    for key in position:
        value = position[key]
        value_len = len(value)
        if value_len >= K:
            for i in range(value_len - K + 1):
                dif = value[i + K - 1] - value[i] + 1
                if min_length > dif:
                    min_length = dif
                if max_length < dif:
                    max_length = dif

    if max_length == -1:
        return -1
    return f'{min_length} {max_length}'


from sys import stdin

new_input = stdin.readline
T = int(new_input())
for _ in range(T):
    print(find_length())