# 230913
from sys import stdin
from heapq import heappush, heappop
N = int(stdin.readline())
sorted_problem_list, reversed_problem_list = [], []
problem_difficulty = [0] * (int(1e5)+1)
# 0이면 존재 X, 존재하면 난이도
def minus_int(num):
    return -int(num)

for _ in range(N):
    num, difficulty = map(int, stdin.readline().split())
    heappush(sorted_problem_list, (difficulty, num))
    heappush(reversed_problem_list, (-difficulty, -num))
    problem_difficulty[num] = difficulty

M = int(stdin.readline())
for _ in range(M):
    command = stdin.readline().split()
    if command[0] == 'add':
        num, difficulty = map(int, command[1:])
        problem_difficulty[num] = difficulty
        heappush(sorted_problem_list, (difficulty, num))
        heappush(reversed_problem_list, (-difficulty, -num))
    elif command[0] == 'solved':
        problem_difficulty[int(command[1])] = 0
    elif command[1] == '1':
        while True:
            difficulty, num = map(minus_int, reversed_problem_list[0])
            if problem_difficulty[num] == difficulty:
                print(num)
                break
            else:
                heappop(reversed_problem_list)
    else:
        while True:
            difficulty, num = sorted_problem_list[0]
            if problem_difficulty[num] == difficulty:
                print(num)
                break
            else:
                heappop(sorted_problem_list)

#
from sys import stdin
from heapq import heappush, heappop
N = int(stdin.readline())
sorted_problem_list, reversed_problem_list = [], []
problem_difficulty = [0] * (int(1e5)+1)
# 0이면 존재 X, 존재하면 난이도
def minus_int(num):
    return -num

for _ in range(N):
    num, difficulty = map(int, stdin.readline().split())
    problem_difficulty[num] = difficulty
    heappush(sorted_problem_list, (difficulty, num))
    heappush(reversed_problem_list, (-difficulty, -num))

M = int(stdin.readline())
for _ in range(M):
    command = stdin.readline().split()
    if command[0] == 'add':
        num, difficulty = map(int, command[1:])
        problem_difficulty[num] = difficulty
        heappush(sorted_problem_list, (difficulty, num))
        heappush(reversed_problem_list, (-difficulty, -num))
    elif command[0] == 'solved':
        problem_difficulty[int(command[1])] = 0
    elif command[1] == '1':
        while True:
            difficulty, num = map(minus_int, reversed_problem_list[0])
            if problem_difficulty[num] == difficulty:
                print(num)
                break
            else:
                heappop(reversed_problem_list)
    else:
        while True:
            difficulty, num = sorted_problem_list[0]
            if problem_difficulty[num] == difficulty:
                print(num)
                break
            else:
                heappop(sorted_problem_list)

#
def minus_int(num):
    return -num

def recommend_problems():
    from sys import stdin
    from heapq import heappush, heappop

    N = int(stdin.readline())
    sorted_problem_list, reversed_problem_list = [], []
    problem_difficulty = [0] * (int(1e5) + 1)

    for _ in range(N):
        num, difficulty = map(int, stdin.readline().split())
        problem_difficulty[num] = difficulty
        heappush(sorted_problem_list, (difficulty, num))
        heappush(reversed_problem_list, (-difficulty, -num))

    M = int(stdin.readline())

    for _ in range(M):
        command = stdin.readline().split()

        if command[0] == 'add':
            num, difficulty = map(int, command[1:])
            problem_difficulty[num] = difficulty
            heappush(sorted_problem_list, (difficulty, num))
            heappush(reversed_problem_list, (-difficulty, -num))

        elif command[0] == 'solved':
            problem_difficulty[int(command[1])] = 0

        elif command[1] == '1':
            while True:
                difficulty, num = map(minus_int, reversed_problem_list[0])
                if problem_difficulty[num] == difficulty:
                    print(num)
                    break
                else:
                    heappop(reversed_problem_list)

        else:
            while True:
                difficulty, num = sorted_problem_list[0]
                if problem_difficulty[num] == difficulty:
                    print(num)
                    break
                else:
                    heappop(sorted_problem_list)

recommend_problems()