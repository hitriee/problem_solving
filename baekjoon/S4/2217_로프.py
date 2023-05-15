#230515
# 그리디
from sys import stdin
def to_int(): return int(stdin.readline())
N = to_int()
max_weight_list = [to_int() for _ in range(N)]
max_weight_list.sort()
candidates = []
for i in range(N):
    candidates.append(max_weight_list[i] * (N-i))
print(max(candidates))


#
def find_max_weight():
    from sys import stdin
    def to_int(): return int(stdin.readline())

    N = to_int()
    max_weight_list = [to_int() for _ in range(N)]
    max_weight_list.sort()
    candidates = [max_weight_list[i] * (N - i) for i in range(N)]
    return max(candidates)

print(find_max_weight())