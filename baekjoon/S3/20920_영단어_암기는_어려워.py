#230505
from sys import stdin
def new_input(): return stdin.readline().rstrip()
N, M = map(int, new_input().split())
# 단어별 빈도수 계산
word_to_freq = {}
for _ in range(N):
    word = new_input()
    if len(word) >= M:
        if word_to_freq.get(word):
            word_to_freq[word] += 1
        else:
            word_to_freq[word] = 1

# 빈도수별 길이, 단어
freq_to_len_word = {}
for key in sorted(word_to_freq):
    freq = word_to_freq[key]
    if freq_to_len_word.get(freq):
        freq_to_len_word[freq].append((len(key), key))
    else:
        freq_to_len_word[freq] = [(len(key), key)]

for freq in sorted(freq_to_len_word, reverse=True):
    freq_to_len_word[freq].sort(key=lambda info: -info[0])
    for info in freq_to_len_word[freq]:
        print(info[-1])

#
def print_words():
    from sys import stdin
    def new_input(): return stdin.readline().rstrip()
    N, M = map(int, new_input().split())
    # 단어별 빈도수 계산
    word_to_freq = {}
    # 빈도수별 길이, 단어
    freq_to_len_word = {}

    for _ in range(N):
        word = new_input()
        if len(word) >= M:
            if word_to_freq.get(word):
                word_to_freq[word] += 1
            else:
                word_to_freq[word] = 1

    for key in sorted(word_to_freq):
        freq = word_to_freq[key]
        if freq_to_len_word.get(freq):
            freq_to_len_word[freq].append((len(key), key))
        else:
            freq_to_len_word[freq] = [(len(key), key)]

    for freq in sorted(freq_to_len_word, reverse=True):
        freq_to_len_word[freq].sort(key=lambda info: -info[0])
        for info in freq_to_len_word[freq]:
            print(info[-1])
print_words()


#
def print_words():
    from sys import stdin
    def new_input(): return stdin.readline().rstrip()
    N, M = map(int, new_input().split())
    # 단어별 빈도수 계산
    word_to_freq = {}
    # 빈도수별 길이, 단어
    freq_to_len_word = {}

    for _ in range(N):
        word = new_input()
        length = len(word)
        if length >= M:
            if word_to_freq.get(word):
                word_to_freq[word][0] += 1
            else:
                word_to_freq[word] = [1, length]

    for key in sorted(word_to_freq):
        freq, length = word_to_freq[key]
        if freq_to_len_word.get(freq):
            freq_to_len_word[freq].append((length, key))
        else:
            freq_to_len_word[freq] = [(length, key)]

    for freq in sorted(freq_to_len_word, reverse=True):
        freq_to_len_word[freq].sort(key=lambda info: -info[0])
        for info in freq_to_len_word[freq]:
            print(info[-1])
print_words()

#
def print_words():
    from sys import stdin
    def new_input(): return stdin.readline().rstrip()
    N, M = map(int, new_input().split())
    # 단어별 빈도수 계산
    word_to_freq = {}
    # 빈도수별 길이, 단어
    freq_to_len_word = {}

    for _ in range(N):
        word = new_input()
        if len(word) >= M:
            if word_to_freq.get(word):
                word_to_freq[word] += 1
            else:
                word_to_freq[word] = 1

    for key in sorted(word_to_freq):
        freq = word_to_freq[key]
        if freq_to_len_word.get(freq):
            freq_to_len_word[freq].append((len(key), key))
        else:
            freq_to_len_word[freq] = [(len(key), key)]

    for freq in sorted(freq_to_len_word, reverse=True):
        for info in sorted(freq_to_len_word[freq], key=lambda info: -info[0]):
            print(info[-1])
print_words()


#
def print_words():
    from sys import stdin
    def new_input(): return stdin.readline().rstrip()
    N, M = map(int, new_input().split())
    # 단어별 빈도수 계산
    word_to_freq = {}
    # 빈도수별 길이, 단어
    freq_to_len_word = {}

    for _ in range(N):
        word = new_input()
        if len(word) >= M:
            if word_to_freq.get(word):
                word_to_freq[word] += 1
            else:
                word_to_freq[word] = 1

    for key in word_to_freq:
        freq = word_to_freq[key]
        if freq_to_len_word.get(freq):
            freq_to_len_word[freq].append((len(key), key))
        else:
            freq_to_len_word[freq] = [(len(key), key)]

    for freq in sorted(freq_to_len_word, reverse=True):
        freq_to_len_word[freq].sort(key=lambda info: (-info[0], info[1]))
        for info in freq_to_len_word[freq]:
            print(info[-1])
print_words()


#
def print_words():
    from sys import stdin
    def new_input():
        return stdin.readline().rstrip()

    N, M = map(int, new_input().split())
    # 단어별 빈도수 계산
    word_to_freq = {}
    # 빈도수별 길이, 단어
    freq_to_len_word = {}

    def fill_dict():
        for _ in range(N):
            word = new_input()
            if len(word) >= M:
                if word_to_freq.get(word):
                    word_to_freq[word] += 1
                else:
                    word_to_freq[word] = 1

        for key in sorted(word_to_freq):
            freq = word_to_freq[key]
            if freq_to_len_word.get(freq):
                freq_to_len_word[freq].append((len(key), key))
            else:
                freq_to_len_word[freq] = [(len(key), key)]

    fill_dict()
    for freq in sorted(freq_to_len_word, reverse=True):
        freq_to_len_word[freq].sort(key=lambda info: -info[0])
        for info in freq_to_len_word[freq]:
            print(info[-1])

print_words()


#
def print_words():
    from sys import stdin
    def new_input():
        return stdin.readline().rstrip()

    N, M = map(int, new_input().split())
    # 단어: [빈도수, 길이, 단어]
    word_to_freq = {}

    def fill_dict():
        for _ in range(N):
            word = new_input()
            length = len(word)
            if length >= M:
                if word_to_freq.get(word):
                    word_to_freq[word][0] += 1
                else:
                    word_to_freq[word] = [1, length, word]

    fill_dict()
    values = list(word_to_freq.values())
    values.sort(key= lambda value: (-value[0], -value[1], value[2]))
    for value in values:
        print(value[-1])

print_words()


#
def print_words():
    from sys import stdin
    def new_input():
        return stdin.readline().rstrip()

    N, M = map(int, new_input().split())
    # 단어별 빈도수 계산
    word_to_freq = {}
    # 빈도수별 길이, 단어
    freq_to_len_word = {}

    for _ in range(N):
        word = new_input()
        if len(word) >= M:
            if word_to_freq.get(word):
                word_to_freq[word] += 1
            else:
                word_to_freq[word] = 1
    keys = sorted(word_to_freq)
    for key in keys:
        freq = word_to_freq[key]
        if freq_to_len_word.get(freq):
            freq_to_len_word[freq].append((len(key), key))
        else:
            freq_to_len_word[freq] = [(len(key), key)]

    keys = sorted(freq_to_len_word, reverse=True)
    for freq in keys:
        freq_to_len_word[freq].sort(key=lambda info: -info[0])
        for info in freq_to_len_word[freq]:
            print(info[-1])

print_words()