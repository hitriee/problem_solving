# 231124
# 31120 KB / 40 ms
from sys import stdin
def to_int():
    return int(stdin.readline())

N = to_int()
step = [to_int() for _ in range(N)]
if N <= 2:
    print(sum(step))
else:
    step_point = [[0]*2 for _ in range(N)]
    step_point[-1][0] = step[-1]
    step_point[-2][1] = step[-1]+step[-2]
    for i in range(N-3, -1, -1):
        step_point[i][0] = max(max(step_point[i+2]) + step[i], step_point[i][0])
        if step_point[i+1][0]:
            step_point[i][1] = max(step_point[i+1][0]+step[i], step_point[i][1])

    print(max(*step_point[0], *step_point[1]))


#
def hop_step():
    from sys import stdin
    def to_int():
        return int(stdin.readline())

    N = to_int()
    step = [to_int() for _ in range(N)]
    if N <= 2:
        return sum(step)

    step_point = [[0] * 2 for _ in range(N)]
    step_point[-1][0] = step[-1]
    step_point[-2][1] = step[-1] + step[-2]
    for i in range(N - 3, -1, -1):
        step_point[i][0] = max(max(step_point[i + 2]) + step[i], step_point[i][0])
        if step_point[i + 1][0]:
            step_point[i][1] = max(step_point[i + 1][0] + step[i], step_point[i][1])

    return max(*step_point[0], *step_point[1])

print(hop_step())