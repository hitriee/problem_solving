#230612
from sys import stdin
new_input = stdin.readline

N = int(new_input())
numbers = [0]
numbers.extend(map(int, new_input().split()))

table = [[0]*(i+1) for i in range(N+1)]
# 홀수
for mid in range(1, N+1):
    table[mid][mid] = 1
    start, end = mid-1, mid+1
    while start >= 1 and end <= N:
        if numbers[end] == numbers[start]:
            table[end][start] = 1
            end += 1
            start -= 1
        else:
            break

# 짝수
for mid in range(1, N):
    start, end = mid, mid+1
    while start >= 1 and end <= N:
        if numbers[end] == numbers[start]:
            table[end][start] = 1
            end += 1
            start -= 1
        else:
            break

M = int(new_input())
for _ in range(M):
    S, E = map(int, new_input().split())
    print(table[E][S])



#
from sys import stdin
new_input = stdin.readline

N = int(new_input())
numbers = [0]
numbers.extend(map(int, new_input().split()))

table = [[0]*(i+1) for i in range(N+1)]

def check_palindrome(limit, plus):
    for mid in range(1, limit):
        start, end = mid, mid + plus
        while start >= 1 and end <= N:
            if numbers[end] == numbers[start]:
                table[end][start] = 1
                end += 1
                start -= 1
            else:
                break


check_palindrome(N+1, 0)
check_palindrome(N, 1)

M = int(new_input())
for _ in range(M):
    S, E = map(int, new_input().split())
    print(table[E][S])


#
def print_answer():
    from sys import stdin
    new_input = stdin.readline

    N = int(new_input())
    numbers = [0]
    numbers.extend(map(int, new_input().split()))

    table = [[0]*(i+1) for i in range(N+1)]

    def check_palindrome(limit, plus):
        for mid in range(1, limit):
            start, end = mid, mid + plus
            while start >= 1 and end <= N:
                if numbers[end] == numbers[start]:
                    table[end][start] = 1
                    end += 1
                    start -= 1
                else:
                    break


    check_palindrome(N+1, 0)
    check_palindrome(N, 1)

    M = int(new_input())
    for _ in range(M):
        S, E = map(int, new_input().split())
        print(table[E][S])

print_answer()