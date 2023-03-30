#230330
# 리스트에 담아 주기
# T = int(input())
# for _ in range(T):
#     words = input().split()
#     for i in range(len(words)):
#         words[i] = words[i][::-1]
#     print(' '.join(words))

# 함수형
def return_words():
    words = input().split()
    for i in range(len(words)):
        words[i] = words[i][::-1]
    return ' '.join(words)

T = int(input())
for _ in range(T):
    print(return_words())


# 리스트 X
def return_sentence():
    new_sentence = ''
    words = input().split()
    for i in range(len(words)):
        new_sentence += words[i][::-1]
        new_sentence += ' '
    return new_sentence.rstrip()

T = int(input())
for _ in range(T):
    print(return_sentence())

# readline
def return_words():
    words = new_input().split()
    for i in range(len(words)):
        words[i] = words[i][::-1]
    return ' '.join(words)

from sys import stdin
new_input = stdin.readline
T = int(new_input())
for _ in range(T):
    print(return_words())

# 함수 안에서만 사용
def return_words():
    from sys import stdin
    new_input = stdin.readline
    words = new_input().split()
    for i in range(len(words)):
        words[i] = words[i][::-1]
    return ' '.join(words)

T = int(input())
for _ in range(T):
    print(return_words())


# 전체 함수
def print_words():
    def return_words():
        from sys import stdin
        new_input = stdin.readline
        words = new_input().split()
        for i in range(len(words)):
            words[i] = words[i][::-1]
        return ' '.join(words)

    T = int(input())
    for _ in range(T):
        print(return_words())
print_words()

# 순서 변경
from sys import stdin
new_input = stdin.readline
T = int(new_input())

def return_words():
    words = new_input().split()
    for i in range(len(words)):
        words[i] = words[i][::-1]
    return ' '.join(words)

for _ in range(T):
    print(return_words())

# map
def return_words():
    words = list(map(reverse_word, new_input().split()))
    return ' '.join(words)

from sys import stdin
new_input = stdin.readline
T = int(new_input())
reverse_word = lambda word: word[::-1]
for _ in range(T):
    print(return_words())