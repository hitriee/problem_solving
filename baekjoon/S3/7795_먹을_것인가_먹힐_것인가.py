# 240130
# 34676 KB / 160 ms
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()

    i = j = cnt = 0
    while i < N:
        if j != M:
            if A[i] <= B[j]:
                cnt += j
                i += 1
            else:
                j += 1
        else:
            cnt += j
            i += 1

    print(cnt)


# 34670 KB / 164 ms
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()

    i = j = cnt = 0
    while i < N:
        if j == M or A[i] <= B[j]:
            cnt += j
            i += 1
        else:
            j += 1

    print(cnt)


# 34628 KB / 140 ms
def find_pair(N, M, A, B):
    A.sort()
    B.sort()

    i = j = cnt = 0
    while i < N:
        if j != M:
            if A[i] <= B[j]:
                cnt += j
                i += 1
            else:
                j += 1
        else:
            cnt += j
            i += 1

    return cnt

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(find_pair(N, M, A, B))
