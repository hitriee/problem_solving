#230524
#230528
from sys import stdin
from collections import deque
def to_int(): return int(stdin.readline())

N = to_int()
amount = [to_int() for _ in range(N)]
if N < 3:
    print(sum(amount))
else:
    cases = deque()
    cases.append([0]*2)
    cases.append([amount[0]] * 2)
    max_val = deque([0, amount[0]])
    for i in range(1, N):
        case = [max_val[0] + amount[i], cases[-1][0] + amount[i]]
        cases.append(case)
        max_val.append(max(*case, *max_val))
        cases.popleft()
        max_val.popleft()
    # print(cases)
    print(max(*cases[-1], *cases[-2]))


#
from sys import stdin
from collections import deque
def to_int(): return int(stdin.readline())

N = to_int()
amount = [to_int() for _ in range(N)]
if N < 3:
    print(sum(amount))
else:
    cases = deque()
    cases.append([amount[0]] * 2)
    max_val = deque([0, amount[0]])
    for i in range(1, N):
        case = [max_val[0] + amount[i], cases[-1][0] + amount[i]]
        cases.append(case)
        max_val.append(max(*case, *max_val))
        cases.popleft()
        max_val.popleft()
    print(max(*cases[0], *max_val))


#
from sys import stdin
from collections import deque
def to_int(): return int(stdin.readline())

N = to_int()
amount = [to_int() for _ in range(N)]
if N < 3:
    print(sum(amount))
else:
    cases = deque()
    cases.append([amount[0]] * 2)
    max_val = deque([0, amount[0]])
    for i in range(1, N):
        case = [max_val[-2] + amount[i], cases[-1][0] + amount[i]]
        cases.append(case)
        max_val.append(max(*case, *max_val))
    print(max(*cases[-1], *max_val))


#
def find_max():
    from sys import stdin
    from collections import deque
    def to_int(): return int(stdin.readline())

    N = to_int()
    amount = [to_int() for _ in range(N)]

    if N < 3:
        return sum(amount)

    before = [amount[0]] * 2
    max_val = deque([0, amount[0]])

    for i in range(1, N):
        case = [max_val[0] + amount[i], before[0] + amount[i]]
        before = case[:]
        max_val.append(max(*case, *max_val))
        max_val.popleft()

    return max(*case, *max_val)

print(find_max())


#
def find_max():
    from sys import stdin
    from collections import deque

    def to_int():
        return int(stdin.readline())

    N = to_int()
    amount = [to_int() for _ in range(N)]

    if N < 3:
        return sum(amount)

    cases = deque() # i-1 일 때, 연속으로 마시지 않은 경우 최댓값, 연속으로 마셨을 경우 최댓값
    cases.append([amount[0]] * 2)
    max_val = deque([0, amount[0]]) # i-2까지의 최댓값, i-1까지의 최댓값

    for i in range(1, N):
        # 연속으로 마시지 않은 경우 => i-2까지의 최댓값 + 현재 포도주 양
        # 연속으로 마신 경우 => i-1일 때 연속으로 마시지 않은 경우 최댓값 + 현재 포도주 양
        case = [max_val[0] + amount[i], cases[-1][0] + amount[i]]
        cases.append(case)
        # i-1일 때의 최댓값 갱신
        max_val.append(max(*case, *max_val))
        cases.popleft()
        max_val.popleft()

    return max(*cases[0], *max_val)


print(find_max())



