#230622
#
N = int(input())
A = list(map(int, input().split()))
answer = [-1] * N
stack = [(A[0], 0)]
for i in range(1, N):
    number = A[i]
    while stack[-1][0] < number:
        j = stack.pop()[1]
        answer[j] = number
        if not stack:
            break
    stack.append((number, i))
print(*answer)

#
N = int(input())
A = list(map(int, input().split()))
answer = [-1] * N
stack = [(A[0], 0)]
for i in range(1, N):
    number = A[i]
    if stack[-1][0] < number:
        while stack:
            if stack[-1][0] < number:
                j = stack.pop()[1]
                answer[j] = number
            else:
                break
    stack.append((number, i))
print(*answer)


#
N = int(input())
A = list(map(int, input().split()))
answer = [-1] * N
stack = [0]
for i in range(1, N):
    number = A[i]
    if A[stack[-1]] < number:
        while stack:
            if A[stack[-1]] < number:
                j = stack.pop()
                answer[j] = number
            else:
                break
    stack.append(i)
print(*answer)


#
def print_nge_list():
    N = int(input())
    A = list(map(int, input().split()))
    answer = [-1] * N
    stack = [0]
    for i in range(1, N):
        number = A[i]
        if A[stack[-1]] < number:
            while stack:
                if A[stack[-1]] < number:
                    j = stack.pop()
                    answer[j] = number
                else:
                    break
        stack.append(i)
    print(*answer)

print_nge_list()


#
def print_nge_list():
    N = int(input())
    A = list(map(int, input().split()))
    answer = [-1] * N
    stack = [0]
    for i in range(1, N):
        number = A[i]
        if A[stack[-1]] < number:
            j = stack.pop()
            answer[j] = number
            while stack and A[stack[-1]] < number:
                j = stack.pop()
                answer[j] = number
        stack.append(i)
    print(*answer)

print_nge_list()


#
def return_nge_list():
    N = int(input())
    A = list(map(int, input().split()))
    answer = ['-1'] * N
    stack = [0]
    for i in range(1, N):
        number = A[i]
        if A[stack[-1]] < number:
            j = stack.pop()
            answer[j] = str(number)
            while stack and A[stack[-1]] < number:
                j = stack.pop()
                answer[j] = str(number)
        stack.append(i)
    return ' '.join(answer)

print(return_nge_list())