# 260303
# 33700 KB / 56 ms
def main():
    N = int(input())
    str_arr = [input() for _ in range(2)]

    for j in (0, -1):
        if str_arr[0][j] != str_arr[1][j]:
            return 'NO'


    vowel_set = {'a', 'e', 'i', 'o', 'u'}
    consonants, vowels = [[], []], [[], []]

    for i in range(2):
        for alp in str_arr[i]:
            if alp in vowel_set:
                vowels[i].append(alp)
            else:
                consonants[i].append(alp)


    if ''.join(consonants[0]) != ''.join(consonants[1]):
        return 'NO'

    vowels[0].sort()
    vowels[1].sort()

    if ''.join(vowels[0]) != ''.join(vowels[1]):
        return 'NO'


    return 'YES'

print(main())








# 33700 KB / 52 ms
def main():
    N = int(input())
    str_arr = [input() for _ in range(2)]

    for j in (0, -1):
        if str_arr[0][j] != str_arr[1][j]:
            return 'NO'


    vowel_set = {'a', 'e', 'i', 'o', 'u'}
    consonants, vowels = [[], []], [[], []]

    for i in range(2):
        for alp in str_arr[i]:
            if alp in vowel_set:
                vowels[i].append(alp)
            else:
                consonants[i].append(alp)

    vowels[0].sort()
    vowels[1].sort()

    if ''.join(vowels[0]) != ''.join(vowels[1]):
        return 'NO'


    if ''.join(consonants[0]) != ''.join(consonants[1]):
        return 'NO'


    return 'YES'

print(main())






# 33700 KB / 52 ms
def main():
    _ = int(input())
    str_arr = [input() for _ in range(2)]

    for j in (0, -1):
        if str_arr[0][j] != str_arr[1][j]:
            return 'NO'


    vowel_set = {'a', 'e', 'i', 'o', 'u'}
    consonants, vowels = [[], []], [[], []]

    for i in range(2):
        for alp in str_arr[i]:
            if alp in vowel_set:
                vowels[i].append(alp)
            else:
                consonants[i].append(alp)

    vowels[0].sort()
    vowels[1].sort()

    if ''.join(vowels[0]) != ''.join(vowels[1]):
        return 'NO'


    if ''.join(consonants[0]) != ''.join(consonants[1]):
        return 'NO'


    return 'YES'

print(main())