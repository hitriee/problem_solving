#230808
from sys import stdin
new_input = stdin.readline
N, M = map(int, new_input().split())
words = [new_input().rstrip() for _ in range(N)]
cnt = 0
words.sort()
for _ in range(M):
    word = new_input().rstrip()
    start, end = 0, N-1
    while start <= end:
        mid = (start + end)//2
        mid_word = words[mid]
        if word < mid_word:
            for i in range(len(word)):
                if word[i] != mid_word[i]:
                    if word[i] < mid_word[i]:
                        end = mid - 1
                    else:
                        start = mid + 1
                    break
            else:
                cnt += 1
                break
        elif word > mid_word:
            start = mid + 1
        else:
            cnt += 1
            break
print(cnt)


#
def count_prefix_word():
    from sys import stdin
    new_input = stdin.readline
    N, M = map(int, new_input().split())
    words = [new_input().rstrip() for _ in range(N)]
    cnt = 0
    words.sort()
    for _ in range(M):
        word = new_input().rstrip()
        start, end = 0, N - 1
        while start <= end:
            mid = (start + end) // 2
            mid_word = words[mid]
            if word < mid_word:
                for i in range(len(word)):
                    if word[i] != mid_word[i]:
                        if word[i] < mid_word[i]:
                            end = mid - 1
                        else:
                            start = mid + 1
                        break
                else:
                    cnt += 1
                    break
            elif word > mid_word:
                start = mid + 1
            else:
                cnt += 1
                break
    return cnt

print(count_prefix_word())


#
def need_increase(word, words, N):
    start, end = 0, N - 1
    while start <= end:
        mid = (start + end) // 2
        mid_word = words[mid]
        if word < mid_word:
            for i in range(len(word)):
                if word[i] != mid_word[i]:
                    if word[i] < mid_word[i]:
                        end = mid - 1
                    else:
                        start = mid + 1
                    break
            else:
                return True
        elif word > mid_word:
            start = mid + 1
        else:
            return True
    return False


def count_prefix_word():
    from sys import stdin
    new_input = stdin.readline
    N, M = map(int, new_input().split())
    words = [new_input().rstrip() for _ in range(N)]
    cnt = 0
    words.sort()

    for _ in range(M):
        word = new_input().rstrip()
        if need_increase(word, words, N):
            cnt += 1

    return cnt

print(count_prefix_word())


#
def count_prefix_word():
    from sys import stdin
    new_input = stdin.readline
    N, M = map(int, new_input().split())
    words = {}
    for _ in range(N):
        word = new_input().rstrip()
        first = word[0]
        if words.get(first):
            words[first].append(word)
        else:
            words[first] = [word]
    cnt = 0
    for key in words:
        words[key].sort()

    def binary_search():
        nonlocal cnt
        word = new_input().rstrip()
        first = word[0]
        if not words.get(first):
            return
        same_first = words[first]
        start, end = 0, len(same_first) - 1
        while start <= end:
            mid = (start + end) // 2
            mid_word = same_first[mid]
            if word < mid_word:
                for i in range(len(word)):
                    if word[i] != mid_word[i]:
                        if word[i] < mid_word[i]:
                            end = mid - 1
                        else:
                            start = mid + 1
                        break
                else:
                    cnt += 1
                    return
            elif word > mid_word:
                start = mid + 1
            else:
                cnt += 1
                return

    for _ in range(M):
        binary_search()

    return cnt


print(count_prefix_word())