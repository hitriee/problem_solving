#230526
from math import factorial
N, M, K = map(int, input().split())
if K:
    cnt = 1
    for num in (K-1, N*M-K):
        quot, remain = divmod(num, M)
        cnt *= factorial(quot+remain)//(factorial(quot) * factorial(remain))
    print(cnt)
else:
    print(factorial(N+M-2)//(factorial(N-1) * factorial(M-1)))


#
N, M, K = map(int, input().split())

def multiple(start, end):
    final = 1
    for i in range(start, end+1):
        final *= i
    return final

if K:
    cnt = 1
    for num in (K-1, N*M-K):
        min_val, max_val = sorted(divmod(num, M))
        cnt *= multiple(max_val+1, min_val+max_val)//multiple(1, min_val)
    print(cnt)
else:
    min_val, max_val = sorted([N, M])
    print(multiple(max_val, min_val + max_val-2)//multiple(1, min_val-1))


#
def cnt_path():
    N, M, K = map(int, input().split())

    def multiple(start, end):
        final = 1
        for i in range(start, end+1):
            final *= i
        return final

    if K:
        cnt = 1
        for num in (K-1, N*M-K):
            min_val, max_val = sorted(divmod(num, M))
            cnt *= multiple(max_val+1, min_val+max_val)//multiple(1, min_val)
        return cnt

    return multiple(N, N + M-2)//multiple(1, M-1)

print(cnt_path())


# 함수화
def cnt_path():
    from math import factorial
    N, M, K = map(int, input().split())
    if K:
        cnt = 1
        for num in (K-1, N*M-K):
            quot, remain = divmod(num, M)
            cnt *= factorial(quot+remain)//(factorial(quot) * factorial(remain))
        return cnt

    return factorial(N+M-2)//(factorial(N-1) * factorial(M-1))

print(cnt_path())


