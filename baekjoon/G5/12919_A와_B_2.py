#230427
# 틀림
# S = input()
# T = input()
# initial_length = len(S)
# final_length = len(T)
# cases = set()
# cases.add(S)
# patterns = set(T[j:j+initial_length+1] for j in range(final_length - initial_length))
# for i in range(initial_length+1, final_length+1):
#     new_cases = set()
#     print(patterns)
#     while cases:
#         target = cases.pop()
#         new1, new2 = target + 'A', 'B' + target[::-1]
#         if new1 in patterns:
#             new_cases.add(new1)
#         if new2 in patterns:
#             new_cases.add(new2)
#     # print(new_cases)
#     if new_cases:
#         cases = set(new_cases)
#         patterns.clear()
#         for j in range(final_length - i):
#             patterns.add(T[j:j + i + 1])
#     else:
#         print(0)
#         break
# else:
#     print(1)



#230609
# bfs
from collections import deque
S = input()
T = input()

len_s, len_t = len(S), len(T)
pattern = set()

for length in range(len_s, len_t+1):
    for i in range(len_t - length + 1):
        pattern.add(T[i:i+length])

q = deque()
q.append((S, len_s))
while q:
    word, length = q.popleft()
    if word == T:
        print(1)
        break
    elif length < len_t:
        for new_word in (word+'A', (word+'B')[::-1]):
            if new_word in pattern or new_word[::-1] in pattern:
                q.append((new_word, length+1))
else:
    print(0)



#
def is_possible():
    S = input()
    T = input()
    len_s, len_t = len(S), len(T)
    pattern = set()

    for length in range(len_s, len_t + 1):
        for i in range(len_t - length + 1):
            pattern.add(T[i:i + length])

    def bfs(initial_value: tuple, word_limit: int, target: str):
        from collections import deque
        q = deque()
        q.append(initial_value)
        while q:
            word, length = q.popleft()
            if word == target:
                return 1
            elif length < word_limit:
                for new_word in (word + 'A', (word + 'B')[::-1]):
                    if new_word in pattern or new_word[::-1] in pattern:
                        q.append((new_word, length + 1))
        return 0

    return bfs((S, len_s), len_t, T)

print(is_possible())

#
def is_possible():
    S = input()
    T = input()
    len_s, len_t = len(S), len(T)
    pattern = set()

    for length in range(len_s, len_t + 1):
        for i in range(len_t - length + 1):
            pattern.add(T[i:i + length])

    def bfs():
        from collections import deque
        q = deque()
        q.append((S, len_s))
        while q:
            word, length = q.popleft()
            if word == T:
                return 1
            elif length < len_t:
                for new_word in (word + 'A', (word + 'B')[::-1]):
                    if new_word in pattern or new_word[::-1] in pattern:
                        q.append((new_word, length + 1))
        return 0

    return bfs()

print(is_possible())


#
S = input()
T = input()

len_s, len_t = len(S), len(T)
pattern = set()

for length in range(len_s, len_t+1):
    for i in range(len_t - length + 1):
        pattern.add(T[i:i+length])

answer = 0

def find_word(level, word):
    global answer
    if answer == 1:
        return
    if level == len_t:
        if word == T:
            answer = 1
        return

    for new_word in (word + 'A', (word + 'B')[::-1]):
        if new_word in pattern or new_word[::-1] in pattern:
            find_word(level+1, new_word)

find_word(len_s, S)
print(answer)


#
def is_possible():
    S = input()
    T = input()

    len_s, len_t = len(S), len(T)
    pattern = set()

    for length in range(len_s, len_t+1):
        for i in range(len_t - length + 1):
            pattern.add(T[i:i+length])

    answer = 0

    def find_word(level, word):
        nonlocal answer
        if answer == 1:
            return
        if level == len_t:
            if word == T:
                answer = 1
            return

        for new_word in (word + 'A', (word + 'B')[::-1]):
            if new_word in pattern or new_word[::-1] in pattern:
                find_word(level+1, new_word)

    find_word(len_s, S)

    return answer

print(is_possible())


#
def is_possible():
    S = input()
    T = input()

    len_s, len_t = len(S), len(T)
    pattern = {}

    for length in range(len_s, len_t+1):
        pattern[length] = set()
        for i in range(len_t - length + 1):
            pattern[length].add(T[i:i+length])

    answer = 0

    def find_word(level, word):
        nonlocal answer
        if answer == 1:
            return
        if level == len_t:
            if word == T:
                answer = 1
            return

        each_pattern = pattern[level+1]
        for new_word in (word + 'A', (word + 'B')[::-1]):
            if new_word in each_pattern or new_word[::-1] in each_pattern:
                find_word(level+1, new_word)

    find_word(len_s, S)

    return answer

print(is_possible())


#
S = input()
T = input()

len_s, len_t = len(S), len(T)
pattern = {}

for length in range(len_s, len_t+1):
    pattern[length] = set()
    for i in range(len_t - length + 1):
        pattern[length].add(T[i:i+length])

answer = 0


def find_word(level, word):
    global answer
    if answer == 1:
        return
    if level == len_t:
        if word == T:
            answer = 1
        return

    each_pattern = pattern[level+1]
    for new_word in (word + 'A', (word + 'B')[::-1]):
        if new_word in each_pattern or new_word[::-1] in each_pattern:
            find_word(level+1, new_word)


find_word(len_s, S)

print(answer)


#
def is_possible():
    S = input()
    T = input()

    len_s, len_t = len(S), len(T)
    pattern = {}

    for length in range(len_s, len_t+1):
        pattern[length] = set()
        for i in range(len_t - length + 1):
            word = T[i:i+length]
            if word not in pattern[length]:
                pattern[length].add(word)

    answer = 0

    def find_word(level, word):
        nonlocal answer
        if answer == 1:
            return
        if level == len_t:
            if word == T:
                answer = 1
            return

        each_pattern = pattern[level+1]
        for new_word in (word + 'A', (word + 'B')[::-1]):
            if new_word in each_pattern or new_word[::-1] in each_pattern:
                find_word(level+1, new_word)

    find_word(len_s, S)

    return answer

print(is_possible())