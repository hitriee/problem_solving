# 260409
# 88736 KB / 660 ms
def main():
    N = int(input())

    def backtracking(level, result):
        if result in part_of:
            return

        part_of.add(result)

        if level == m:
            words.add(result)
            return

        for i in range(m):
            if not visited[i]:
                visited[i] = True
                new_result = result + word[i]
                backtracking(level+1, new_result)
                visited[i] = False

    for _ in range(N):
        words, part_of = set(), set()
        word = input()
        m = len(word)
        visited = [False] * m

        backtracking(0, '')
        print('\n'.join(sorted(words)))


main()



# 86176 KB / 552 ms
def main():
    N = int(input())

    def backtracking(level, result):
        if result in part_of:
            return

        part_of.add(result)

        if level == m:
            words.append(result)
            return

        for i in range(m):
            if not visited[i]:
                visited[i] = True
                new_result = result + word[i]
                backtracking(level+1, new_result)
                visited[i] = False

    for _ in range(N):
        words, part_of = [], set()
        word = sorted(input())
        m = len(word)
        visited = [False] * m

        backtracking(0, '')
        print('\n'.join(words))


main()




# 86176 KB / 556 ms
def main():
    N = int(input())
    visited = [False] * 20

    def backtracking(level, result):
        if result in part_of:
            return

        part_of.add(result)

        if level == m:
            words.append(result)
            return

        for i in range(m):
            if not visited[i]:
                visited[i] = True
                new_result = result + word[i]
                backtracking(level+1, new_result)
                visited[i] = False

    for _ in range(N):
        words, part_of = [], set()
        word = sorted(input())
        m = len(word)

        backtracking(0, '')
        print('\n'.join(words))


main()



# 86176 KB / 412 ms
def main():
    N = int(input())

    def backtracking(level, result):
        if result in part_of:
            return

        part_of.add(result)

        if level == m:
            words.append(result)
            return

        for alp in keys:
            if frequency[alp]:
                frequency[alp] -= 1
                new_result = result + alp
                backtracking(level+1, new_result)
                frequency[alp] += 1

    for _ in range(N):
        words, part_of = [], set()
        word = input()
        m = len(word)
        frequency = {}
        for alp in word:
            frequency[alp] = frequency.get(alp, 0) + 1

        keys = sorted(frequency)
        backtracking(0, '')
        print('\n'.join(words))


main()





# 43484 KB / 256 ms
def main():
    N = int(input())

    def dfs(level, result):
        if level == m:
            words.append(result)
            return

        for alp in keys:
            if frequency[alp]:
                frequency[alp] -= 1
                new_result = result + alp
                dfs(level+1, new_result)
                frequency[alp] += 1

    for _ in range(N):
        words, part_of = [], set()
        word = input()
        m = len(word)
        frequency = {}
        for alp in word:
            frequency[alp] = frequency.get(alp, 0) + 1

        keys = sorted(frequency)
        dfs(0, '')
        print('\n'.join(words))


main()






# 43484 KB / 252 ms
def main():
    N = int(input())

    def dfs(level, result):
        if level == m:
            words.append(result)
            return

        for alp in keys:
            if frequency[alp]:
                frequency[alp] -= 1
                dfs(level+1, result + alp)
                frequency[alp] += 1

    for _ in range(N):
        words = []
        word = input()
        m = len(word)
        frequency = {}
        for alp in word:
            frequency[alp] = frequency.get(alp, 0) + 1

        keys = sorted(frequency)
        dfs(0, '')
        print('\n'.join(words))


main()