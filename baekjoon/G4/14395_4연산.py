# 240424
# 34052 KB, 68 ms
from collections import deque
s, t = map(int, input().split())
if s == t:
    print(0)
else:
    limit = int(1e9) + 1
    visited = set()
    q = deque()
    visited.add(s)
    for num, calc in (s*s, '*'), (2*s, '+'), (1, '/'):
        if num < limit and num not in visited:
            visited.add(num)
            q.append((num, calc))

    while q:
        num, result = q.popleft()
        if num == t:
            print(result)
            break
        else:
            for new_num, calc in (num * num, '*'), (2 * num, '+'):
                if new_num < limit and new_num not in visited:
                    visited.add(new_num)
                    q.append((new_num, result+calc))

    else:
        print(-1)


# 34176 KB, 68 ms
from collections import deque
s, t = map(int, input().split())
if s == t:
    print(0)
else:
    limit = max(s, t) + 1
    visited = set()
    q = deque()
    visited.add(s)
    for num, calc in (s*s, '*'), (2*s, '+'), (1, '/'):
        if num < limit and num not in visited:
            visited.add(num)
            q.append((num, calc))

    while q:
        num, result = q.popleft()
        if num == t:
            print(result)
            break
        else:
            for new_num, calc in (num * num, '*'), (2 * num, '+'):
                if new_num < limit and new_num not in visited:
                    visited.add(new_num)
                    q.append((new_num, result+calc))

    else:
        print(-1)

# 34044 KB, 64 ms
from collections import deque
s, t = map(int, input().split())
if s == t:
    print(0)
else:
    limit = t + 1
    visited = set()
    q = deque()
    visited.add(s)
    for num, calc in (s*s, '*'), (2*s, '+'), (1, '/'):
        if num < limit and num not in visited:
            visited.add(num)
            q.append((num, calc))

    while q:
        num, result = q.popleft()
        if num == t:
            print(result)
            break
        else:
            for new_num, calc in (num * num, '*'), (2 * num, '+'):
                if new_num < limit and new_num not in visited:
                    visited.add(new_num)
                    q.append((new_num, result+calc))

    else:
        print(-1)


# 34184 KB, 76 ms
def return_result(s, t):
    from collections import deque
    if s == t:
        return 0

    limit = t + 1
    visited, q = set(), deque()
    visited.add(s)
    for num, calc in (s * s, '*'), (2 * s, '+'), (1, '/'):
        if num < limit and num not in visited:
            visited.add(num)
            q.append((num, calc))

    while q:
        num, result = q.popleft()
        if num == t:
            return result

        for new_num, calc in (num * num, '*'), (2 * num, '+'):
            if new_num < limit and new_num not in visited:
                visited.add(new_num)
                q.append((new_num, result + calc))

    return -1

print(return_result(*map(int, input().split())))