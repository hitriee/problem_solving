#230614
T = int(input())
cases = [1] * 10001
before_max_num = 1
for _ in range(T):
    n = int(input())
    if before_max_num <= n-1:
        for i in range(before_max_num, n):
            not_one = (i+1)//3 if (i+1)%3 != 1 else (i+1)//3-1
            cases[i+1] = cases[i] + not_one//2 + 1
    print(cases[n])
    if before_max_num < n:
        before_max_num = n


#
T = int(input())
before_max_num = 1
num_arr = [int(input()) for _ in range(T)]
cases = [1] * (max(num_arr)+1)
for n in num_arr:
    if before_max_num <= n-1:
        for i in range(before_max_num, n):
            not_one = (i+1)//3 if (i+1)%3 != 1 else (i+1)//3-1
            cases[i+1] = cases[i] + not_one//2 + 1
    print(cases[n])
    if before_max_num < n:
        before_max_num = n


#
from sys import stdin

def to_int(): return int(stdin.readline())

T = to_int()
before_max_num = 1
num_arr = [to_int() for _ in range(T)]
cases = [1] * (max(num_arr)+1)
for n in num_arr:
    if before_max_num <= n-1:
        for i in range(before_max_num, n):
            not_one = (i+1)//3 if (i+1)%3 != 1 else (i+1)//3-1
            cases[i+1] = cases[i] + not_one//2 + 1
    print(cases[n])
    if before_max_num < n:
        before_max_num = n



#
def find_cases():
    from sys import stdin

    def to_int(): return int(stdin.readline())

    T = to_int()
    before_max_num = 1
    num_arr = [to_int() for _ in range(T)]
    cases = [1] * (max(num_arr) + 1)
    for n in num_arr:
        if before_max_num <= n - 1:
            for i in range(before_max_num, n):
                not_one = (i + 1) // 3 if (i + 1) % 3 != 1 else (i + 1) // 3 - 1
                cases[i + 1] = cases[i] + not_one // 2 + 1
        print(cases[n])
        if before_max_num < n:
            before_max_num = n

find_cases()


#
def find_cases():
    from sys import stdin

    def to_int(): return int(stdin.readline())
    def fill_cases():
        if before_max_num <= n - 1:
            for i in range(before_max_num, n):
                not_one = (i + 1) // 3 if (i + 1) % 3 != 1 else (i + 1) // 3 - 1
                cases[i + 1] = cases[i] + not_one // 2 + 1
        return cases[n]

    T = to_int()
    before_max_num = 1
    num_arr = [to_int() for _ in range(T)]
    cases = [1] * (max(num_arr) + 1)
    for n in num_arr:
        print(fill_cases())
        if before_max_num < n:
            before_max_num = n

find_cases()


#
def find_cases():
    from sys import stdin

    def to_int(): return int(stdin.readline())
    def fill_cases():
        if before_max_num <= n:
            for i in range(before_max_num, n+1):
                not_one = i // 3 if i % 3 != 1 else i // 3 - 1
                cases[i] = cases[i-1] + not_one // 2 + 1
        return cases[n]

    T = to_int()
    before_max_num = 1
    num_arr = [to_int() for _ in range(T)]
    cases = [1] * (max(num_arr) + 1)
    for n in num_arr:
        print(fill_cases())
        if before_max_num < n+1:
            before_max_num = n+1

find_cases()