#230819
from sys import stdin
from heapq import heappush, heappop
new_input = stdin.readline
N = int(new_input())
board, min_score, max_score = [], [], []
row = list(map(int, new_input().split()))
for j in range(3):
    heappush(min_score, (row[j], j))
    heappush(max_score, (-row[j], j))

for _ in range(N-1):
    row = list(map(int, new_input().split()))
    new_min_score, new_max_score = row[:], row[:]

    min_num, min_index = heappop(min_score)
    max_num, max_index = heappop(max_score)
    if min_index == 1:
        for j in range(3):
            new_min_score[j] += min_num
    elif min_index == 0:
        for j in range(3):
            new_min_score[j] += min_num if j < 2 else min_score[0][0]
    else:
        for j in range(3):
            new_min_score[j] += min_num if j > 0 else min_score[0][0]

    if max_index == 1:
        for j in range(3):
            new_max_score[j] -= max_num
    elif max_index == 0:
        for j in range(3):
            new_max_score[j] -= max_num if j < 2 else max_score[0][0]
    else:
        for j in range(3):
            new_max_score[j] -= max_num if j> 0 else max_score[0][0]

    min_score.clear()
    max_score.clear()

    for j in range(3):
        heappush(min_score, (new_min_score[j], j))
        heappush(max_score, (-new_max_score[j], j))

print(-max_score[0][0], min_score[0][0])


#
def find_min_max():
    from sys import stdin
    from heapq import heappush, heappop
    new_input = stdin.readline
    N = int(new_input())
    board, min_score, max_score = [], [], []
    row = list(map(int, new_input().split()))
    for j in range(3):
        heappush(min_score, (row[j], j))
        heappush(max_score, (-row[j], j))

    for _ in range(N - 1):
        row = list(map(int, new_input().split()))
        new_min_score, new_max_score = row[:], row[:]

        min_num, min_index = heappop(min_score)
        max_num, max_index = heappop(max_score)
        if min_index == 1:
            for j in range(3):
                new_min_score[j] += min_num
        elif min_index == 0:
            for j in range(3):
                new_min_score[j] += min_num if j < 2 else min_score[0][0]
        else:
            for j in range(3):
                new_min_score[j] += min_num if j > 0 else min_score[0][0]

        if max_index == 1:
            for j in range(3):
                new_max_score[j] -= max_num
        elif max_index == 0:
            for j in range(3):
                new_max_score[j] -= max_num if j < 2 else max_score[0][0]
        else:
            for j in range(3):
                new_max_score[j] -= max_num if j > 0 else max_score[0][0]

        min_score.clear()
        max_score.clear()

        for j in range(3):
            heappush(min_score, (new_min_score[j], j))
            heappush(max_score, (-new_max_score[j], j))

    return f'{-max_score[0][0]} {min_score[0][0]}'

print(find_min_max())


#
def find_new_score(index, arr, first, second):
    if index == 1:
        for j in range(3):
            arr[j] += first
    elif index == 0:
        for j in range(2):
            arr[j] += first
        arr[2] += second
    else:
        arr[0] += second
        for j in range(1, 3):
            arr[j] += first

def find_min_max():
    from sys import stdin
    from heapq import heappush, heappop
    new_input = stdin.readline
    N = int(new_input())
    min_score, max_score = [], []
    row = list(map(int, new_input().split()))
    for j in range(3):
        heappush(min_score, (row[j], j))
        heappush(max_score, (-row[j], j))

    for _ in range(N - 1):
        row = list(map(int, new_input().split()))
        new_min_score, new_max_score = row[:], row[:]

        min_num, min_index = heappop(min_score)
        max_num, max_index = heappop(max_score)

        find_new_score(min_index, new_min_score, min_num, min_score[0][0])
        find_new_score(max_index, new_max_score, -max_num, -max_score[0][0])

        min_score.clear()
        max_score.clear()

        for j in range(3):
            heappush(min_score, (new_min_score[j], j))
            heappush(max_score, (-new_max_score[j], j))

    return f'{-max_score[0][0]} {min_score[0][0]}'

print(find_min_max())


#
def find_new_score(index, arr, first, second):
    if index == 1:
        for j in range(3):
            arr[j] += first
    elif index == 0:
        for j in range(2):
            arr[j] += first
        arr[2] += second
    else:
        arr[0] += second
        for j in range(1, 3):
            arr[j] += first

def find_min_max():
    from sys import stdin
    from heapq import heappush, heappop
    new_input = stdin.readline
    N = int(new_input())
    min_score, max_score = [], []
    row = list(map(int, new_input().split()))
    for j in range(3):
        heappush(min_score, (row[j], j))
        heappush(max_score, (-row[j], j))

    for _ in range(N - 1):
        new_min_score = list(map(int, new_input().split()))
        new_max_score = new_min_score[:]

        min_num, min_index = heappop(min_score)
        max_num, max_index = heappop(max_score)

        find_new_score(min_index, new_min_score, min_num, min_score[0][0])
        find_new_score(max_index, new_max_score, -max_num, -max_score[0][0])

        min_score.clear()
        max_score.clear()

        for j in range(3):
            heappush(min_score, (new_min_score[j], j))
            heappush(max_score, (-new_max_score[j], j))

    return f'{-max_score[0][0]} {min_score[0][0]}'

print(find_min_max())
