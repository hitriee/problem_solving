#230817
from sys import stdin
new_input = stdin.readline
N, K = map(int, new_input().split())
students = [len(new_input().rstrip()) for _ in range(N)]
check = {}
for i in range(K):
    student = students[i]
    if check.get(student):
        check[student] += 1
    else:
        check[student] = 1
cnt = 0
for i in range(N-K):
    student = students[i]
    end_student = students[i+K]
    if check.get(end_student):
        check[end_student] += 1
    else:
        check[end_student] = 1
    cnt += check[student] - 1
    check[student] -= 1
for i in range(N-K, N-1):
    student = students[i]
    cnt += check[student] - 1
    check[student] -= 1
print(cnt)


#
def cnt_good_friends():
    from sys import stdin
    new_input = stdin.readline
    N, K = map(int, new_input().split())
    students = [len(new_input().rstrip()) for _ in range(N)]
    check = {}
    cnt = 0

    for i in range(K):
        student = students[i]
        if check.get(student):
            check[student] += 1
        else:
            check[student] = 1

    for i in range(N - K):
        student = students[i]
        end_student = students[i + K]
        if check.get(end_student):
            check[end_student] += 1
        else:
            check[end_student] = 1
        cnt += check[student] - 1
        check[student] -= 1

    for i in range(N - K, N - 1):
        student = students[i]
        cnt += check[student] - 1
        check[student] -= 1
    return cnt

print(cnt_good_friends())


#
def cnt_good_friends():
    from sys import stdin
    new_input = stdin.readline
    N, K = map(int, new_input().split())
    students = [len(new_input().rstrip()) for _ in range(N)]
    check = {i:0 for i in range(2, 21)}
    cnt = 0

    for i in range(K):
        student = students[i]
        check[student] += 1

    for i in range(N - K):
        student = students[i]
        end_student = students[i + K]
        check[end_student] += 1
        cnt += check[student] - 1
        check[student] -= 1

    for i in range(N - K, N - 1):
        student = students[i]
        cnt += check[student] - 1
        check[student] -= 1
    return cnt

print(cnt_good_friends())


#
def cnt_good_friends():
    from sys import stdin
    new_input = stdin.readline
    N, K = map(int, new_input().split())
    students = [len(new_input().rstrip()) for _ in range(N)]
    check = [0] * 21
    cnt = 0

    for i in range(1, K):
        student = students[i]
        check[student] += 1

    for i in range(N - K):
        student = students[i]
        end_student = students[i + K]
        check[end_student] += 1
        cnt += check[student]
        check[students[i+1]] -= 1

    for i in range(N - K, N - 1):
        student = students[i]
        cnt += check[student]
        check[students[i+1]] -= 1

    return cnt

print(cnt_good_friends())


#
def cnt_good_friends():
    from sys import stdin
    new_input = stdin.readline
    N, K = map(int, new_input().split())
    students = [len(new_input().rstrip()) for _ in range(N)]
    check = [0] * 21
    cnt = 0

    for i in range(1, K):
        check[students[i]] += 1

    for i in range(N - K):
        check[students[i + K]] += 1
        cnt += check[students[i]]
        check[students[i + 1]] -= 1

    for i in range(N - K, N - 1):
        cnt += check[students[i]]
        check[students[i + 1]] -= 1

    return cnt


print(cnt_good_friends())


#
def cnt_good_friends():
    from sys import stdin
    new_input = stdin.readline
    N, K = map(int, new_input().split())
    students = [len(new_input().rstrip()) for _ in range(N)]
    students.extend([0] * (K-1))
    check = [0] * 21
    cnt = 0

    for i in range(1, K):
        check[students[i]] += 1

    for i in range(N - 1):
        check[students[i + K]] += 1
        cnt += check[students[i]]
        check[students[i + 1]] -= 1

    return cnt


print(cnt_good_friends())