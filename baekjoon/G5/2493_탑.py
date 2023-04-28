#230428
# 스택
N = int(input())
height_list = list(map(int, input().split()))
receiver_list = [0] * N
stack = [(N-1, height_list[-1])]
for i in range(N-2, -1, -1):
    height = height_list[i]
    while stack:
        if stack[-1][1] < height:
            receiver_list[stack[-1][0]] = i+1
            stack.pop()
        else:
            break
    stack.append((i, height))
print(*receiver_list)



# receiver_list 제거
N = int(input())
height_list = list(map(int, input().split()))
stack = [(N-1, height_list[-1])]
height_list[-1] = 0
for i in range(N-2, -1, -1):
    height = height_list[i]
    height_list[i] = 0
    while stack:
        if stack[-1][1] < height:
            height_list[stack[-1][0]] = i+1
            stack.pop()
        else:
            break
    stack.append((i, height))
print(*height_list)


# stack 내 값 저장
N = int(input())
height_list = list(map(int, input().split()))
receiver_list = [0] * N
stack = [(N-1, height_list[-1])]
for i in range(N-2, -1, -1):
    height = height_list[i]
    while stack:
        pre_i, before = stack[-1]
        if before < height:
            receiver_list[pre_i] = i+1
            stack.pop()
        else:
            break
    stack.append((i, height))
print(*receiver_list)


# 함수화
def find_receiver():
    receiver_list = [0] * N
    stack = [(N-1, height_list[-1])]
    for i in range(N-2, -1, -1):
        height = height_list[i]
        while stack:
            if stack[-1][1] < height:
                receiver_list[stack[-1][0]] = i+1
                stack.pop()
            else:
                break
        stack.append((i, height))
    return receiver_list

N = int(input())
height_list = list(map(int, input().split()))
print(*find_receiver())


# join
def find_receiver():
    receiver_list = ['0'] * N
    stack = [(N-1, height_list[-1])]
    for i in range(N-2, -1, -1):
        height = height_list[i]
        while stack:
            if stack[-1][1] < height:
                receiver_list[stack[-1][0]] = str(i+1)
                stack.pop()
            else:
                break
        stack.append((i, height))
    return ' '.join(receiver_list)

N = int(input())
height_list = list(map(int, input().split()))
print(find_receiver())


# str(i+1) 저장
def find_receiver():
    receiver_list = ['0'] * N
    stack = [(N-1, height_list[-1])]
    for i in range(N-2, -1, -1):
        height = height_list[i]
        str_i = str(i+1)
        while stack:
            if stack[-1][1] < height:
                receiver_list[stack[-1][0]] = str_i
                stack.pop()
            else:
                break
        stack.append((i, height))
    return ' '.join(receiver_list)

N = int(input())
height_list = list(map(int, input().split()))
print(find_receiver())


# break 제거
def find_receiver():
    receiver_list = ['0'] * N
    stack = [(N-1, height_list[-1])]
    for i in range(N-2, -1, -1):
        height = height_list[i]
        while stack and stack[-1][1] < height:
            receiver_list[stack[-1][0]] = str(i+1)
            stack.pop()
        stack.append((i, height))
    return ' '.join(receiver_list)

N = int(input())
height_list = list(map(int, input().split()))
print(find_receiver())