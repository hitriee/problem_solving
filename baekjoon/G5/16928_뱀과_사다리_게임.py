#230621
from collections import deque
def to_int(): return map(int, input().split())
N, M = to_int()
move_to = list(range(101))

for _ in range(N+M):
    start, end = to_int()
    move_to[start] = end

q = deque()
q.append((1, 0))
visited = [False] * 101
while True:
    now, cnt = q.popleft()
    if now == 100:
        print(cnt)
        break
    cnt += 1
    for new in range(now+1, now+7):
        if new <= 100 and not visited[new]:
            visited[new] = True
            q.append((move_to[new], cnt))


#
from collections import deque
def to_int(): return map(int, input().split())
N, M = to_int()
move_to = list(range(101))

for _ in range(N+M):
    start, end = to_int()
    move_to[start] = end

q = deque()
q.append((1, 0))
visited = [False] * 101
while True:
    now, cnt = q.popleft()
    if now == 100:
        print(cnt)
        break
    cnt += 1
    for new in range(now+1, now+7):
        if new <= 100:
            result = move_to[new]
            if not visited[result]:
                visited[result] = True
                if new != result:
                    visited[new] = True
                q.append((result, cnt))


#
def return_cnt():
    def to_int():
        return map(int, input().split())

    N, M = to_int()
    move_to = list(range(101))

    for _ in range(N + M):
        start, end = to_int()
        move_to[start] = end

    def calc_cnt():
        from collections import deque
        q = deque()
        q.append((1, 0))
        visited = [False] * 101
        while True:
            now, cnt = q.popleft()
            if now == 100:
                return cnt
            cnt += 1
            for new in range(now + 1, now + 7):
                if new <= 100 and not visited[new]:
                    visited[new] = True
                    q.append((move_to[new], cnt))

    return calc_cnt()

print(return_cnt())



#
def return_cnt():
    def to_int():
        return map(int, input().split())

    N, M = to_int()
    move_to = list(range(101))

    for _ in range(N + M):
        start, end = to_int()
        move_to[start] = end

    def calc_cnt():
        from collections import deque
        q = deque()
        q.append((1, 0))
        visited = [False] * 101
        while True:
            now, cnt = q.popleft()
            if now == 100:
                return cnt
            cnt += 1
            for new in range(now + 1, min(now+7, 101)):
                if not visited[new]:
                    visited[new] = True
                    q.append((move_to[new], cnt))

    return calc_cnt()

print(return_cnt())


#
def return_cnt():
    def to_int():
        return map(int, input().split())

    N, M = to_int()
    move_to = list(range(101))

    for _ in range(N + M):
        start, end = to_int()
        move_to[start] = end

    def calc_cnt():
        from collections import deque
        q = deque()
        q.append((1, 0))
        visited = [False] * 101
        while True:
            now, cnt = q.popleft()
            if now == 100:
                return cnt
            cnt += 1
            limit = min(now+7, 101)
            for new in range(now + 1, limit):
                if not visited[new]:
                    visited[new] = True
                    q.append((move_to[new], cnt))

    return calc_cnt()

print(return_cnt())


#
def return_cnt():

    def to_int():
        return map(int, input().split())

    N, M = to_int()
    move_to = list(range(101))

    for _ in range(N + M):
        start, end = to_int()
        move_to[start] = end

    def calc_cnt():
        from collections import deque
        q = deque()
        q.append((1, 0))
        visited = [False] * 101
        while True:
            now, cnt = q.popleft()
            if now == 100:
                return cnt
            cnt += 1
            for new in range(now + 1, now + 7):
                if new <= 100:
                    result = move_to[new]
                    if not visited[result]:
                        visited[result] = True
                        if new != result:
                            visited[new] = True
                        q.append((result, cnt))

    return calc_cnt()

print(return_cnt())



#
def return_cnt():

    def to_int():
        return map(int, input().split())

    N, M = to_int()
    move_to = list(range(101))

    for _ in range(N + M):
        start, end = to_int()
        move_to[start] = end

    def calc_cnt():
        from collections import deque
        q = deque()
        q.append((1, 0))
        visited = [False] * 101

        while True:
            now, cnt = q.popleft()
            if now == 100:
                return cnt
            cnt += 1
            for new in range(now + 1, min(101, now+7)):
                result = move_to[new]
                if not visited[result]:
                    visited[result] = True
                    if new != result:
                        visited[new] = True
                    q.append((result, cnt))

    return calc_cnt()

print(return_cnt())


#
def return_cnt():

    def to_int():
        return map(int, input().split())

    N, M = to_int()
    move_to = list(range(100))

    for _ in range(N + M):
        start, end = to_int()
        move_to[start] = end

    def calc_cnt():
        from collections import deque
        q = deque()
        q.append((1, 0))
        visited = [False] * 100
        while True:
            now, cnt = q.popleft()
            cnt += 1
            for new in range(now + 1, now + 7):
                if new < 100:
                    result = move_to[new]
                    if not visited[result]:
                        visited[result] = True
                        if new != result:
                            visited[new] = True
                        q.append((result, cnt))
                elif new == 100:
                    return cnt

    return calc_cnt()

print(return_cnt())


#
def return_cnt():
    def to_int():
        return map(int, input().split())

    N, M = to_int()
    move_to = {}

    for _ in range(N + M):
        start, end = to_int()
        move_to[start] = end

    def calc_cnt():
        from collections import deque
        q = deque()
        q.append((1, 0))
        visited = [False] * 101
        while True:
            now, cnt = q.popleft()
            if now == 100:
                return cnt
            cnt += 1
            for new in range(now + 1, now + 7):
                if new <= 100 and not visited[new]:
                    visited[new] = True
                    q.append((move_to[new] if move_to.get(new) else new, cnt))

    return calc_cnt()


print(return_cnt())



#
def return_cnt():
    def to_int():
        return map(int, input().split())

    N, M = to_int()
    move_to = {}

    for _ in range(N + M):
        start, end = to_int()
        move_to[start] = end

    def calc_cnt():
        from collections import deque
        q = deque()
        q.append((1, 0))
        visited = [False] * 101
        while True:
            now, cnt = q.popleft()
            if now == 100:
                return cnt
            cnt += 1
            for new in range(now + 1, now + 7):
                if new <= 100 and not visited[new]:
                    visited[new] = True
                    if move_to.get(new):
                        result = move_to[new]
                        if not visited[result]:
                            visited[result] = True
                            q.append((result, cnt))
                    else:
                        q.append((new, cnt))

    return calc_cnt()


print(return_cnt())


#
def return_cnt():
    def to_int():
        return map(int, input().split())

    N, M = to_int()
    move_to = list(range(101))

    for _ in range(N + M):
        start, end = to_int()
        move_to[start] = end

    def calc_cnt():
        from collections import deque
        q = deque()
        q.append((1, 0))
        visited = [False] * 101
        while True:
            now, cnt = q.popleft()
            if now == 100:
                return cnt
            cnt += 1
            for new in range(now + 1, now + 7):
                if new <= 100:
                    result = move_to[new]
                    if not visited[result]:
                        visited[result] = visited[new] = True
                        q.append((result, cnt))

    return calc_cnt()


print(return_cnt())


#
def return_cnt():
    def to_int():
        return map(int, input().split())

    N, M = to_int()
    move_to = list(range(101))

    for _ in range(N + M):
        start, end = to_int()
        move_to[start] = end

    def calc_cnt():
        from collections import deque
        q = deque()
        q.append((1, 0))
        visited = [False] * 101
        while True:
            now, cnt = q.popleft()
            if now == 100:
                return cnt
            cnt += 1
            for new in range(now + 1, now + 7):
                if new <= 100:
                    result = move_to[new]
                    if not visited[result]:
                        visited[result] = True
                        q.append((result, cnt))

    return calc_cnt()


print(return_cnt())


#
def return_cnt():
    from sys import stdin

    def to_int():
        return map(int, stdin.readline().split())

    N, M = to_int()
    move_to = list(range(101))

    for _ in range(N + M):
        start, end = to_int()
        move_to[start] = end

    def calc_cnt():
        from collections import deque
        q = deque()
        q.append((1, 0))
        visited = [False] * 101
        while True:
            now, cnt = q.popleft()
            if now == 100:
                return cnt
            cnt += 1
            for new in range(now + 1, now + 7):
                if new <= 100:
                    result = move_to[new]
                    if not visited[result]:
                        visited[result] = True
                        if new != result:
                            visited[new] = True
                        q.append((result, cnt))

    return calc_cnt()


print(return_cnt())