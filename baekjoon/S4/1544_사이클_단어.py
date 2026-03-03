# 260303
# 32412 KB / 44 ms
def main():
    N = int(input())
    cnt = 0
    word_dict = {}

    def is_new_one():
        if word_dict.get(n):
            for before in word_dict[n]:
                for i in range(n):
                    if before[i] == word[0]:
                        i = (i+1)%n
                        j = 1%n
                        while j != 0:
                            if before[i] != word[j]:
                                break

                            i = (i + 1) % n
                            j = (j + 1) % n
                        else:
                            return False

            word_dict[n].add(word)
            return True

        word_dict[n] = {word}
        return True

    for _ in range(N):
        word = input()
        n = len(word)
        if is_new_one():
            cnt += 1

    return cnt

print(main())








# 32412 KB / 44 ms
def main():
    N = int(input())
    cnt = 0
    word_dict = {}

    def is_new_one():
        if word_dict.get(n):
            for before in word_dict[n]:
                for i in range(n):
                    if before[i] == word[0]:
                        i = (i+1)%n
                        j = 1%n
                        while j != 0:
                            if before[i] != word[j]:
                                break

                            i = (i + 1) % n
                            j = (j + 1) % n
                        else:
                            return False

            word_dict[n].append(word)
            return True

        word_dict[n] = [word]
        return True

    for _ in range(N):
        word = input()
        n = len(word)
        if is_new_one():
            cnt += 1

    return cnt

print(main())






# 32412 KB / 44 ms
def main():
    N = int(input())
    cnt = 0
    word_dict = {}

    def is_new_one(word):
        n = len(word)

        if word_dict.get(n):
            for before in word_dict[n]:
                for i in range(n):
                    if before[i] == word[0]:
                        i = (i+1)%n
                        j = 1%n
                        while j != 0:
                            if before[i] != word[j]:
                                break

                            i = (i + 1) % n
                            j = (j + 1) % n
                        else:
                            return False

            word_dict[n].append(word)
            return True

        word_dict[n] = [word]
        return True

    for _ in range(N):
        if is_new_one(input()):
            cnt += 1

    return cnt

print(main())






# 32412 KB / 40 ms
def main():
    def is_new_one(word):
        n = len(word)

        if word_dict.get(n):
            for before in word_dict[n]:
                for i in range(n):
                    if before[i] == word[0]:
                        i = (i+1)%n
                        j = 1%n
                        while j != 0:
                            if before[i] != word[j]:
                                break

                            i = (i + 1) % n
                            j = (j + 1) % n
                        else:
                            return False

            word_dict[n].append(word)
            return True

        word_dict[n] = [word]
        return True



    N = int(input())
    cnt = 0
    word_dict = {}

    for _ in range(N):
        if is_new_one(input()):
            cnt += 1

    return cnt

print(main())