#230727
from collections import deque
n = int(input())
if n <= 1:
    print(n)
else:
    q = deque([0, 1])
    for _ in range(n-1):
        next_num = sum(q)%1000000007
        q.popleft()
        q.append(next_num)
    print(q[-1])

#
def fibonacci_num():
    from collections import deque
    n = int(input())
    if n <= 1:
        return n
    q = deque([0, 1])
    for _ in range(n - 1):
        next_num = sum(q) % 1000000007
        q.popleft()
        q.append(next_num)
    return q[-1]

print(fibonacci_num())


#
def fibonacci_num():
    from collections import deque
    n = int(input())
    if n <= 1:
        return n
    q = deque([0, 1])
    next_num = 1
    for _ in range(n - 2):
        before = q.popleft()
        q.append(next_num)
        next_num = (2*next_num - before)%1000000007
    return next_num

print(fibonacci_num())
