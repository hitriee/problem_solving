#230413
# 정렬
# dict, list
from sys import stdin
to_int = lambda : map(int, stdin.readline().split())
while True:
    rank_of = {}
    N, M = to_int()
    if N == M == 0:
        break
    for _ in range(N):
        for number in to_int():
            if rank_of.get(number):
                rank_of[number] += 1
            else:
                rank_of[number] = 1
    items = sorted(rank_of.items(), key= lambda element: (-element[1], element[0]))
    max_val = items[0][1]
    second_val = 0
    second_prize = []
    for key, value in items:
        if second_val == 0:
            if value < max_val:
                second_val = value
                second_prize.append(key)
        elif second_val == value:
            second_prize.append(key)
        else:
            break
    print(*second_prize)


# 함수화
def find_second():
    rank_of = {}
    for _ in range(N):
        for number in to_int():
            if rank_of.get(number):
                rank_of[number] += 1
            else:
                rank_of[number] = 1
    items = sorted(rank_of.items(), key= lambda element: (-element[1], element[0]))
    max_val = items[0][1]
    second_val = 0
    second_prize = []
    for key, value in items:
        if second_val == 0:
            if value < max_val:
                second_val = value
                second_prize.append(key)
        elif second_val == value:
            second_prize.append(key)
        else:
            return second_prize
    return second_prize

from sys import stdin
to_int = lambda : map(int, stdin.readline().split())
while True:
    N, M = to_int()
    if N == M == 0:
        break
    print(*find_second())

# while문 내부만 함수화, 사람 번호 int로 변경 X
def find_second():
    rank_of = {}
    for _ in range(N):
        for number in new_input().split():
            if rank_of.get(number):
                rank_of[number] += 1
            else:
                rank_of[number] = 1
    items = sorted(rank_of.items(), key= lambda element: (-element[1], int(element[0])))
    max_val = items[0][1]
    second_val = 0
    second_prize = []
    for key, value in items:
        if second_val == 0:
            if value < max_val:
                second_val = value
                second_prize.append(key)
        elif second_val == value:
            second_prize.append(key)
        else:
            return ' '.join(second_prize)
    return ' '.join(second_prize)

from sys import stdin
new_input = stdin.readline
while True:
    N, M = map(int, new_input().split())
    if N == M == 0:
        break
    print(find_second())


# list에 추가 X, str
def find_second():
    rank_of = {}
    for _ in range(N):
        for number in new_input().split():
            if rank_of.get(number):
                rank_of[number] += 1
            else:
                rank_of[number] = 1
    items = sorted(rank_of.items(), key= lambda element: (-element[1], int(element[0])))
    max_val = items[0][1]
    second_val = 0
    second_prize = ''
    for key, value in items:
        if second_val == 0:
            if value < max_val:
                second_val = value
                second_prize += f'{key} '
        elif second_val == value:
            second_prize += f'{key} '
        else:
            return second_prize.rstrip()
    return second_prize.rstrip()

from sys import stdin
new_input = stdin.readline
while True:
    N, M = map(int, new_input().split())
    if N == M == 0:
        break
    print(find_second())

# 전체 함수화
def print_second():
    def find_second():
        rank_of = {}
        for _ in range(N):
            for number in new_input().split():
                if rank_of.get(number):
                    rank_of[number] += 1
                else:
                    rank_of[number] = 1
        items = sorted(rank_of.items(), key=lambda element: (-element[1], int(element[0])))
        max_val = items[0][1]
        second_val = 0
        second_prize = []
        for key, value in items:
            if second_val == 0:
                if value < max_val:
                    second_val = value
                    second_prize.append(key)
            elif second_val == value:
                second_prize.append(key)
            else:
                return ' '.join(second_prize)
        return ' '.join(second_prize)

    from sys import stdin
    new_input = stdin.readline
    while True:
        N, M = map(int, new_input().split())
        if N == M == 0:
            return
        print(find_second())


print_second()