#230618
from sys import stdin
from math import ceil

def to_int(): return map(int, stdin.readline().split())

N, L = to_int()
info = [list(to_int()) for _ in range(N)]
info.sort()
final_end = cnt = 0
for start, end in info:
    if final_end < end:
        max_val = max(start, final_end)
        quot = ceil((end - max_val)/L)
        final_end = max_val + L * quot
        cnt += quot
print(cnt)



#
def cnt_min():
    from sys import stdin
    from math import ceil

    def to_int():
        return map(int, stdin.readline().split())

    N, L = to_int()
    info = [list(to_int()) for _ in range(N)]
    info.sort()
    final_end = cnt = 0
    for start, end in info:
        if final_end < end:
            max_val = max(start, final_end)
            quot = ceil((end - max_val) / L)
            final_end = max_val + L * quot
            cnt += quot
    return cnt

print(cnt_min())