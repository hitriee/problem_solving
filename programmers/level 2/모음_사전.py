# 240319
def solution(target):
    cnt = answer = 0
    vowels = 'AEIOU'
    found = False

    def find_target(level, word):
        nonlocal found, answer, cnt
        if found or level == 6:
            return

        cnt += 1

        if word == target:
            found = True
            answer = cnt - 1
            return

        for vowel in vowels:
            find_target(level + 1, word + vowel)

    find_target(0, '')

    return answer


#
def solution(target):
    cnt = answer = -1
    vowels = 'AEIOU'
    found = False

    def find_target(level, word):
        nonlocal found, answer, cnt
        if found or level == 6:
            return

        cnt += 1

        if word == target:
            found = True
            answer = cnt
            return

        for vowel in vowels:
            find_target(level + 1, word + vowel)

    find_target(0, '')

    return answer