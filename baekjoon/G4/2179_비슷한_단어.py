#230525
from sys import stdin
new_input = stdin.readline
N = int(new_input())
word_dict = {}
answer_words = []
for _ in range(2):
    word = new_input().rstrip()
    answer_words.append(word)
    first = word[0]
    if word_dict.get(first):
        word_dict[first].append(word)
    else:
        word_dict[first] = [word]

for _ in range(N-2):
    word = new_input().rstrip()
    first = word[0]
    if word_dict.get(first):
        word_dict[first].append(word)
    else:
        word_dict[first] = [word]

max_length = 0
words = list(word_dict.keys())
for alp in words:
    same_prefix = word_dict[alp]
    length = len(same_prefix)
    if length >= 2:
        for i in range(length-1):
            word1 = same_prefix[i]
            length1 = len(word1)
            if length1 > max_length:
                for j in range(i+1, length):
                    word2 = same_prefix[j]
                    length2 = len(word2)
                    if length2 > max_length:
                        min_length = min(length1, length2)
                        for k in range(min_length):
                            if word1[k] != word2[k]:
                                if k > max_length:
                                    max_length = k
                                    answer_words = [word1, word2]
                                break
                        else:
                            if min_length > max_length:
                                max_length = min_length
                                answer_words = [word1, word2]

print('\n'.join(answer_words))


#
from sys import stdin
new_input = stdin.readline
N = int(new_input())
word_dict = {}
answer_words = []
for _ in range(2):
    word = new_input().rstrip()
    answer_words.append(word)
    first = word[0]
    if word_dict.get(first):
        word_dict[first].append(word)
    else:
        word_dict[first] = [word]

for _ in range(N-2):
    word = new_input().rstrip()
    first = word[0]
    if word_dict.get(first):
        word_dict[first].append(word)
    else:
        word_dict[first] = [word]

max_length = 0
words = list(word_dict.keys())
for alp in words:
    same_prefix = word_dict[alp]
    length = len(same_prefix)
    if length >= 2:
        for i in range(length-1):
            word1 = same_prefix[i]
            length1 = len(word1)
            if length1 > max_length:
                for j in range(i+1, length):
                    word2 = same_prefix[j]
                    length2 = len(word2)
                    if length2 > max_length:
                        min_length = min(length1, length2)
                        for k in range(min_length):
                            if word1[k] != word2[k]:
                                if k > max_length:
                                    max_length = k
                                    answer_words = [word1, word2]
                                break
                        else:
                            if min_length > max_length:
                                max_length = min_length
                                answer_words = [word1, word2]

                        if max_length == length1:
                            break

print('\n'.join(answer_words))


#
def find_similar():
    from sys import stdin
    new_input = stdin.readline
    N = int(new_input())
    word_dict = {}
    answer_words = []
    for _ in range(2):
        word = new_input().rstrip()
        answer_words.append(word)
        first = word[0]
        if word_dict.get(first):
            word_dict[first].append(word)
        else:
            word_dict[first] = [word]

    for _ in range(N-2):
        word = new_input().rstrip()
        first = word[0]
        if word_dict.get(first):
            word_dict[first].append(word)
        else:
            word_dict[first] = [word]

    max_length = 0
    words = list(word_dict.keys())
    for alp in words:
        same_prefix = word_dict[alp]
        length = len(same_prefix)
        if length >= 2:
            for i in range(length-1):
                word1 = same_prefix[i]
                length1 = len(word1)
                if length1 > max_length:
                    for j in range(i+1, length):
                        word2 = same_prefix[j]
                        length2 = len(word2)
                        if length2 > max_length:
                            min_length = min(length1, length2)
                            for k in range(min_length):
                                if word1[k] != word2[k]:
                                    if k > max_length:
                                        max_length = k
                                        answer_words = [word1, word2]
                                    break
                            else:
                                if min_length > max_length:
                                    max_length = min_length
                                    answer_words = [word1, word2]

                            if max_length == length1:
                                break

    return '\n'.join(answer_words)

print(find_similar())


#
def find_similar():
    from sys import stdin
    new_input = stdin.readline

    N = int(new_input())
    word_dict, answer_words = {}, []

    # word_dict 채우기, 초기값 설정
    for _ in range(2):
        word = new_input().rstrip()
        answer_words.append(word)
        first = word[0]
        if word_dict.get(first):
            word_dict[first].append(word)
        else:
            word_dict[first] = [word]

    # word_dict 채우기
    for _ in range(N-2):
        word = new_input().rstrip()
        first = word[0]
        if word_dict.get(first):
            word_dict[first].append(word)
        else:
            word_dict[first] = [word]

    # answer_words 갱신
    def find_answer_words():
        nonlocal answer_words
        max_length = 0
        words = list(word_dict.keys())
        for alp in words:
            same_prefix = word_dict[alp]
            length = len(same_prefix)
            if length >= 2:
                for i in range(length-1):
                    word1 = same_prefix[i]
                    length1 = len(word1)
                    if length1 > max_length:
                        for j in range(i+1, length):
                            word2 = same_prefix[j]
                            length2 = len(word2)
                            if length2 > max_length:
                                min_length = min(length1, length2)
                                for k in range(min_length):
                                    if word1[k] != word2[k]:
                                        if k > max_length:
                                            max_length = k
                                            answer_words = [word1, word2]
                                        break
                                else:
                                    if min_length > max_length:
                                        max_length = min_length
                                        answer_words = [word1, word2]

                                if max_length == length1:
                                    break
    find_answer_words()

    return '\n'.join(answer_words)

print(find_similar())



def find_similar():
    from sys import stdin
    new_input = stdin.readline

    N = int(new_input())
    word_dict, answer_words = {}, []

    # word_dict 채우기, 초기값 설정
    for _ in range(2):
        word = new_input().rstrip()
        answer_words.append(word)
        first = word[0]
        if word_dict.get(first):
            word_dict[first].append(word)
        else:
            word_dict[first] = [word]

    # word_dict 채우기
    for _ in range(N-2):
        word = new_input().rstrip()
        first = word[0]
        if word_dict.get(first):
            word_dict[first].append(word)
        else:
            word_dict[first] = [word]

    # answer_words 갱신
    def find_answer_words():
        nonlocal answer_words
        max_length = 0
        for alp in word_dict:
            same_prefix = word_dict[alp]
            length = len(same_prefix)
            if length >= 2:
                for i in range(length-1):
                    word1 = same_prefix[i]
                    length1 = len(word1)
                    if length1 > max_length:
                        for j in range(i+1, length):
                            word2 = same_prefix[j]
                            length2 = len(word2)
                            if length2 > max_length:
                                min_length = min(length1, length2)
                                for k in range(min_length):
                                    if word1[k] != word2[k]:
                                        if k > max_length:
                                            max_length = k
                                            answer_words = [word1, word2]
                                        break
                                else:
                                    max_length = min_length
                                    answer_words = [word1, word2]

    find_answer_words()

    return '\n'.join(answer_words)

print(find_similar())


#
def find_similar():
    from sys import stdin
    new_input = stdin.readline

    N = int(new_input())
    word_dict, answer_words = {}, []

    # word_dict 채우기, 초기값 설정
    for _ in range(2):
        word = new_input().rstrip()
        answer_words.append(word)
        first = word[0]
        if word_dict.get(first):
            word_dict[first].append(word)
        else:
            word_dict[first] = [word]

    # word_dict 채우기
    for _ in range(N-2):
        word = new_input().rstrip()
        first = word[0]
        if word_dict.get(first):
            word_dict[first].append(word)
        else:
            word_dict[first] = [word]

    # answer_words 갱신
    def find_answer_words():
        nonlocal answer_words
        max_length = 0
        for alp in word_dict:
            same_prefix = word_dict[alp]
            length = len(same_prefix)
            if length >= 2:
                for i in range(length-1):
                    word1 = same_prefix[i]
                    length1 = len(word1)
                    if length1 > max_length:
                        for j in range(i+1, length):
                            word2 = same_prefix[j]
                            length2 = len(word2)
                            if length2 > max_length:
                                min_length = min(length1, length2)
                                for k in range(1, min_length):
                                    if word1[k] != word2[k]:
                                        if k > max_length:
                                            max_length = k
                                            answer_words = [word1, word2]
                                        break
                                else:
                                    max_length = min_length
                                    answer_words = [word1, word2]

    find_answer_words()

    return '\n'.join(answer_words)

print(find_similar())


#
def find_similar():
    from sys import stdin
    new_input = stdin.readline

    N = int(new_input())
    word_dict, answer_words = {}, []
    def fill_word_dict():
        first = word[0]
        if word_dict.get(first):
            word_dict[first].append(word)
        else:
            word_dict[first] = [word]

    # word_dict 채우기, 초기값 설정
    for _ in range(2):
        word = new_input().rstrip()
        answer_words.append(word)
        fill_word_dict()

    # word_dict 채우기
    for _ in range(N-2):
        word = new_input().rstrip()
        fill_word_dict()

    # answer_words 갱신
    def find_answer_words():
        nonlocal answer_words
        max_length = 0
        for alp in word_dict:
            same_prefix = word_dict[alp]
            length = len(same_prefix)
            if length >= 2:
                for i in range(length-1):
                    word1 = same_prefix[i]
                    length1 = len(word1)
                    if length1 > max_length:
                        for j in range(i+1, length):
                            word2 = same_prefix[j]
                            length2 = len(word2)
                            if length2 > max_length:
                                min_length = min(length1, length2)
                                for k in range(1, min_length):
                                    if word1[k] != word2[k]:
                                        if k > max_length:
                                            max_length = k
                                            answer_words = [word1, word2]
                                        break
                                else:
                                    max_length = min_length
                                    answer_words = [word1, word2]

    find_answer_words()

    return '\n'.join(answer_words)

print(find_similar())