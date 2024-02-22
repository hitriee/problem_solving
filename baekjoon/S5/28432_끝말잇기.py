# 240222
N = int(input())
found = False
last = first = ''
word_set = set()
for _ in range(N):
    word = input()
    word_set.add(word)
    if word == '?':
        found = True
    elif not found:
        last = word[-1]
    elif first == '':
        first = word[0]

M = int(input())
if first == last == '':
    print(input())
elif first == '':
    for _ in range(M):
        word = input()
        if word[0] == last and word not in word_set:
            print(word)
            break
elif last == '':
    for _ in range(M):
        word = input()
        if word[-1] == first and word not in word_set:
            print(word)
            break
else:
    for _ in range(M):
        word = input()
        if word[0] == last and word[-1] == first and word not in word_set:
            print(word)
            break