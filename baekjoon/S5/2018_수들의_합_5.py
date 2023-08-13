#230813
from math import isqrt
N = int(input())
if N <= 2:
    print(1)
else:
    cnt = N%2 + 1
    root = isqrt(2*N) + 1
    total = sum(range(1, 4))
    for n in range(3, root):
        if (N-total)%n == 0:
            cnt += 1
        total += n+1
    print(cnt)


#
def find_cnt():
    from math import isqrt
    N = int(input())
    if N <= 2:
        return 1

    cnt = N % 2 + 1
    root = isqrt(2 * N) + 1
    total = sum(range(1, 4))
    for n in range(3, root):
        if (N - total) % n == 0:
            cnt += 1
        total += n + 1
    return cnt

print(find_cnt())
