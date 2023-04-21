#230421
# 투 포인터
to_int = lambda : map(int, input().split())
N, M = to_int()
A = list(to_int())
B = list(to_int())
a_i = b_i = 0
result = []
while a_i < N and b_i < M:
    if A[a_i] < B[b_i]:
        result.append(A[a_i])
        a_i += 1
    else:
        result.append(B[b_i])
        b_i += 1
if a_i < N:
    result.extend(A[a_i:])
else:
    result.extend(B[b_i:])
print(*result)


# 정렬
to_int = lambda : map(int, input().split())
N, M = to_int()
result = list(to_int()) + list(to_int())
result.sort()
print(*result)


# 함수화
def return_result():
    to_int = lambda : map(int, input().split())
    N, M = to_int()
    A = list(to_int())
    B = list(to_int())
    a_i = b_i = 0
    result = []
    while a_i < N and b_i < M:
        if A[a_i] < B[b_i]:
            result.append(A[a_i])
            a_i += 1
        else:
            result.append(B[b_i])
            b_i += 1
    if a_i < N:
        result.extend(A[a_i:])
    else:
        result.extend(B[b_i:])
    return result
print(*return_result())


# 함수화
def return_result():
    to_int = lambda : map(int, input().split())
    N, M = to_int()
    result = list(to_int()) + list(to_int())
    result.sort()
    return result
print(*return_result())


# if문 삭제
def return_result():
    to_int = lambda : map(int, input().split())
    N, M = to_int()
    A = list(to_int())
    B = list(to_int())
    a_i = b_i = 0
    result = []
    while a_i < N and b_i < M:
        if A[a_i] < B[b_i]:
            result.append(A[a_i])
            a_i += 1
        else:
            result.append(B[b_i])
            b_i += 1
    result.extend(A[a_i:])
    result.extend(B[b_i:])
    return result
print(*return_result())
