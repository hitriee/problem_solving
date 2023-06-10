#230610
S = input()
length = len(S)
possible = {'pi', 'ka', 'chu'}
i = 0
while i < length:
    word = S[i:i+2]
    if word in possible:
        i += 2
    elif i + 2 < length and word + S[i+2] in possible:
        i += 3
    else:
        print('NO')
        break
else:
    print('YES')


#
def can_pronounce():
    S = input()
    length = len(S)
    possible = {'pi', 'ka', 'chu'}
    i = 0
    while i < length:
        word = S[i:i + 2]
        if word in possible:
            i += 2
        elif i + 2 < length and word + S[i + 2] in possible:
            i += 3
        else:
            return 'NO'
    return 'YES'

print(can_pronounce())
