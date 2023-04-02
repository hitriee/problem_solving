#230402
# 그리디 - 뒤에서부터 비교
N = int(input())
score = [int(input()) for _ in range(N)]
cnt = 0
for i in range(N-2, -1, -1):
    if score[i+1] <= score[i]:
        cnt += score[i] - score[i+1] + 1
        score[i] = score[i+1] - 1
print(cnt)


# before와 배열 값 비교
N = int(input())
score = [int(input()) for _ in range(N)]
cnt = 0
before = score[N-1]
for i in range(N-2, -1, -1):
    if before <= score[i]:
        cnt += score[i] - before + 1
        before -= 1
    else:
        before = score[i]

print(cnt)

# before + 함수화
def cnt_decrease():
    N = int(input())
    score = [int(input()) for _ in range(N)]
    cnt = 0
    before = score[N-1]
    for i in range(N-2, -1, -1):
        if before <= score[i]:
            cnt += score[i] - before + 1
            before -= 1
        else:
            before = score[i]
    return cnt

print(cnt_decrease())

# input 대신 stdin.readline 사용 + 람다 함수
def cnt_decrease():
    from sys import stdin
    to_int = lambda : int(stdin.readline())
    N = to_int()
    score = [to_int() for _ in range(N)]
    cnt = 0
    before = score[N-1]
    for i in range(N-2, -1, -1):
        if before <= score[i]:
            cnt += score[i] - before + 1
            before -= 1
        else:
            before = score[i]
    return cnt

print(cnt_decrease())

# 함수화 X
from sys import stdin
to_int = lambda : int(stdin.readline())
N = to_int()
score = [to_int() for _ in range(N)]
cnt = 0
before = score[N-1]
for i in range(N-2, -1, -1):
    if before <= score[i]:
        cnt += score[i] - before + 1
        before -= 1
    else:
        before = score[i]
print(cnt)