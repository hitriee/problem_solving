#230624
T = int(input())
def find_gcd(num1, num2):
    while num1:
        num1, num2 = num2%num1, num1
    return num2

for _ in range(T):
    num_list = list(map(int, input().split()))
    N, num_list = num_list[0], num_list[1:]
    num_list.sort()
    total = 0
    for i in range(N-1):
        for j in range(i+1, N):
            total += find_gcd(num_list[i], num_list[j])
            # print(total)

    print(total)


#
from collections import deque
N = int(input())
def find_gcd(num1, num2):
    if num1 > num2:
        num1, num2 = num2, num1
    while num1:
        num1, num2 = num2%num1, num1
    return num2

for _ in range(N):
    num_list = deque(map(int, input().split()))
    N = num_list.popleft()
    total = 0
    for i in range(N-1):
        for j in range(i+1, N):
            total += find_gcd(num_list[i], num_list[j])

    print(total)


#
T = int(input())
def find_gcd(num1, num2):
    while num1:
        if num1 > num2:
            num1, num2 = num2, num1
        num1, num2 = num2%num1, num1
    return num2

for _ in range(T):
    num_list = list(map(int, input().split()))
    N, num_list = num_list[0], num_list[1:]
    total = 0
    for i in range(N-1):
        for j in range(i+1, N):
            total += find_gcd(num_list[i], num_list[j])

    print(total)


#
def print_total():
    T = int(input())

    def find_gcd(num1, num2):
        while num1:
            num1, num2 = num2 % num1, num1
        return num2

    for _ in range(T):
        num_list = list(map(int, input().split()))
        N, num_list = num_list[0], num_list[1:]
        num_list.sort()
        total = 0
        for i in range(N - 1):
            for j in range(i + 1, N):
                total += find_gcd(num_list[i], num_list[j])

        print(total)

print_total()
