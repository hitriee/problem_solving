# 231108
# 70840 KB / 5140 ms
from sys import stdin
T = int(stdin.readline())
for _ in range(T):
    N = int(stdin.readline())
    candidates = [list(map(int, stdin.readline().split())) for _ in range(N)]
    candidates.sort()
    cnt = 1
    limit = candidates[0][1]
    for i in range(1, N):
        if candidates[i][1] < limit:
            limit = candidates[i][1]
            cnt += 1
    print(cnt)


# 71348 KB / 4156
from sys import stdin
T = int(stdin.readline())
for _ in range(T):
    N = int(stdin.readline())
    candidates = [list(map(int, stdin.readline().split())) for _ in range(N)]
    candidates.sort(key=lambda candidate: candidate[0])
    cnt = 1
    limit = candidates[0][1]
    for i in range(1, N):
        if candidates[i][1] < limit:
            limit = candidates[i][1]
            cnt += 1
    print(cnt)


# 71348 KB / 3596 ms
def return_cnt(N, candidates):
    candidates.sort(key=lambda candidate: candidate[0])
    cnt = 1
    limit = candidates[0][1]
    for i in range(1, N):
        if candidates[i][1] < limit:
            limit = candidates[i][1]
            cnt += 1
    return cnt

from sys import stdin
T = int(stdin.readline())
for _ in range(T):
    N = int(stdin.readline())
    candidates = [list(map(int, stdin.readline().split())) for _ in range(N)]
    print(return_cnt(N, candidates))

# 70604 KB / 2552 ms
def return_cnt(N, candidates):
    interview_score = [0] * (N+1)
    for i in range(N):
        idx, score = candidates[i]
        interview_score[idx] = score
    cnt = 1
    limit = interview_score[1]
    for i in range(2, N+1):
        if interview_score[i] < limit:
            limit = interview_score[i]
            cnt += 1
    return cnt

from sys import stdin
T = int(stdin.readline())
for _ in range(T):
    N = int(stdin.readline())
    candidates = [list(map(int, stdin.readline().split())) for _ in range(N)]
    print(return_cnt(N, candidates))



# 35756 KB / 2084 ms
def return_cnt(N, interview_score):
    cnt = 1
    limit = interview_score[1]
    for i in range(2, N+1):
        if interview_score[i] < limit:
            limit = interview_score[i]
            cnt += 1
    return cnt

from sys import stdin
T = int(stdin.readline())
for _ in range(T):
    N = int(stdin.readline())
    interview_score = [0] * (N + 1)
    for _ in range(N):
        idx, score = map(int, stdin.readline().split())
        interview_score[idx] = score
    print(return_cnt(N, interview_score))


# 35756 KB / 2292 ms

from sys import stdin
T = int(stdin.readline())
for _ in range(T):
    N = int(stdin.readline())
    interview_score = [0] * (N + 1)

    for _ in range(N):
        idx, score = map(int, stdin.readline().split())
        interview_score[idx] = score

    cnt, limit = 1, interview_score[1]

    for i in range(2, N + 1):
        if interview_score[i] < limit:
            limit = interview_score[i]
            cnt += 1

    print(cnt)
