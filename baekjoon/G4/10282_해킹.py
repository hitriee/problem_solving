#230720
from sys import stdin
from heapq import heappush, heappop
from collections import defaultdict
def to_int():
    return map(int, stdin.readline().split())

T = int(input())
for _ in range(T):
    n, d, c = to_int()
    time_list = [-1] * (n+1)
    link = defaultdict(list)
    for _ in range(d):
        a, b, s = to_int()
        link[b].append((s, a))
    process = [(0, c)]
    time_list[c] = 0
    cnt = 1

    while process:
        time, computer = heappop(process)
        for new_time, other in link[computer]:
            final_time = time+new_time
            if time_list[other] == -1:
                cnt += 1
                time_list[other] = final_time
                heappush(process, (final_time, other))
            elif time_list[other] > final_time:
                time_list[other] = final_time
                heappush(process, (final_time, other))
    print(cnt, max(time_list))


#
from sys import stdin
from heapq import heappush, heappop
def to_int():
    return map(int, stdin.readline().split())

T = int(input())
for _ in range(T):
    n, d, c = to_int()
    time_list = [-1] * (n+1)
    link = {}
    for _ in range(d):
        a, b, s = to_int()
        if link.get(b):
            link[b].append((s, a))
        else:
            link[b] = [(s, a)]
    process = [(0, c)]
    time_list[c] = 0
    cnt = 1

    while process:
        time, computer = heappop(process)
        if link.get(computer):
            for new_time, other in link[computer]:
                final_time = time+new_time
                if time_list[other] == -1:
                    cnt += 1
                    time_list[other] = final_time
                    heappush(process, (final_time, other))
                elif time_list[other] > final_time:
                    time_list[other] = final_time
                    heappush(process, (final_time, other))
    print(cnt, max(time_list))


#
def after_hacked():
    from heapq import heappush, heappop
    from sys import stdin

    def to_int():
        return map(int, stdin.readline().split())

    n, d, c = to_int()
    time_list = [-1] * (n + 1)
    link = {}
    for _ in range(d):
        a, b, s = to_int()
        if link.get(b):
            link[b].append((s, a))
        else:
            link[b] = [(s, a)]
    process = [(0, c)]
    time_list[c] = 0
    cnt = 1

    while process:
        time, computer = heappop(process)
        if link.get(computer):
            for new_time, other in link[computer]:
                final_time = time + new_time
                if time_list[other] == -1:
                    cnt += 1
                    time_list[other] = final_time
                    heappush(process, (final_time, other))
                elif time_list[other] > final_time:
                    time_list[other] = final_time
                    heappush(process, (final_time, other))
    return f'{cnt} {max(time_list)}'

T = int(input())
for _ in range(T):
    print(after_hacked())


#
from sys import stdin

def to_int():
    return map(int, stdin.readline().split())

def after_hacked():
    from heapq import heappush, heappop

    n, d, c = to_int()
    time_list = [-1] * (n + 1)
    link = {}
    for _ in range(d):
        a, b, s = to_int()
        if link.get(b):
            link[b].append((s, a))
        else:
            link[b] = [(s, a)]
    process = [(0, c)]
    time_list[c] = 0
    cnt = 1

    while process:
        time, computer = heappop(process)
        if link.get(computer):
            for new_time, other in link[computer]:
                final_time = time + new_time
                if time_list[other] == -1:
                    cnt += 1
                    time_list[other] = final_time
                    heappush(process, (final_time, other))
                elif time_list[other] > final_time:
                    time_list[other] = final_time
                    heappush(process, (final_time, other))
    return f'{cnt} {max(time_list)}'

T = int(input())
for _ in range(T):
    print(after_hacked())


#
def after_hacked():
    from heapq import heappush, heappop
    from sys import stdin

    def to_int():
        return map(int, stdin.readline().split())

    n, d, c = to_int()
    limit = 2e7
    time_list = [limit] * (n + 1)
    link = {}
    for _ in range(d):
        a, b, s = to_int()
        if link.get(b):
            link[b].append((s, a))
        else:
            link[b] = [(s, a)]
    process = [(0, c)]
    max_time = time_list[c] = 0
    cnt = 1

    while process:
        time, computer = heappop(process)
        if link.get(computer):
            for new_time, other in link[computer]:
                final_time = time + new_time
                if time_list[other] > final_time:
                    if time_list[other] == limit:
                        cnt += 1
                    time_list[other] = final_time
                    heappush(process, (final_time, other))

    for i in range(1, n+1):
        time = time_list[i]
        if time != limit and max_time < time:
            max_time = time

    return f'{cnt} {max_time}'

T = int(input())
for _ in range(T):
    print(after_hacked())


#
def after_hacked():
    from heapq import heappush, heappop
    from sys import stdin

    def to_int():
        return map(int, stdin.readline().split())

    n, d, c = to_int()
    limit = 2e7
    time_list = [limit] * (n + 1)
    link = {}
    for _ in range(d):
        a, b, s = to_int()
        if link.get(b):
            link[b].append((s, a))
        else:
            link[b] = [(s, a)]
    process = [(0, c)]
    cnt = max_time = time_list[c] = 0

    while process:
        time, computer = heappop(process)
        if link.get(computer):
            for new_time, other in link[computer]:
                final_time = time + new_time
                if time_list[other] > final_time:
                    time_list[other] = final_time
                    heappush(process, (final_time, other))

    for i in range(1, n + 1):
        time = time_list[i]
        if time != limit:
            if max_time < time:
                max_time = time
            cnt += 1

    return f'{cnt} {max_time}'


T = int(input())
for _ in range(T):
    print(after_hacked())


#
def after_hacked():
    from heapq import heappush, heappop
    from sys import stdin

    def to_int():
        return map(int, stdin.readline().split())

    n, d, c = to_int()
    time_list = [-1] * (n + 1)
    link = {}
    for _ in range(d):
        a, b, s = to_int()
        if link.get(b):
            link[b].append((s, a))
        else:
            link[b] = [(s, a)]
    process = [(0, c)]
    cnt = max_time = time_list[c] = 0

    while process:
        time, computer = heappop(process)
        if link.get(computer):
            for new_time, other in link[computer]:
                final_time = time + new_time
                if time_list[other] == -1 or time_list[other] > final_time:
                    time_list[other] = final_time
                    heappush(process, (final_time, other))

    for i in range(1, n+1):
        time = time_list[i]
        if time != -1:
            if max_time < time:
                max_time = time
            cnt += 1

    return f'{cnt} {max(time_list)}'


T = int(input())
for _ in range(T):
    print(after_hacked())



#
def after_hacked():
    from heapq import heappush, heappop
    from sys import stdin

    def to_int():
        return map(int, stdin.readline().split())

    n, d, c = to_int()
    limit = n * 1000 + 1
    time_list = [limit] * (n + 1)
    link = {}
    for _ in range(d):
        a, b, s = to_int()
        if link.get(b):
            link[b].append((s, a))
        else:
            link[b] = [(s, a)]
    process = [(0, c)]
    cnt = max_time = time_list[c] = 0

    while process:
        time, computer = heappop(process)
        if link.get(computer):
            for new_time, other in link[computer]:
                final_time = time + new_time
                if time_list[other] > final_time:
                    time_list[other] = final_time
                    heappush(process, (final_time, other))

    for i in range(1, n + 1):
        time = time_list[i]
        if time != limit:
            if max_time < time:
                max_time = time
            cnt += 1

    return f'{cnt} {max_time}'


T = int(input())
for _ in range(T):
    print(after_hacked())


#
def after_hacked():
    from heapq import heappush, heappop
    from sys import stdin

    def to_int():
        return map(int, stdin.readline().split())

    n, d, c = to_int()
    limit = 2e7
    time_list = [limit] * (n + 1)
    link = {}
    for _ in range(d):
        a, b, s = to_int()
        if link.get(b):
            heappush(link[b], (s, a))
        else:
            link[b] = [(s, a)]
    process = [(0, c)]
    cnt = max_time = time_list[c] = 0

    while process:
        time, computer = heappop(process)
        if link.get(computer):
            while link[computer]:
                new_time, other = heappop(link[computer])
                final_time = time + new_time
                if time_list[other] > final_time:
                    time_list[other] = final_time
                    heappush(process, (final_time, other))

    for i in range(1, n + 1):
        time = time_list[i]
        if time != limit:
            if max_time < time:
                max_time = time
            cnt += 1

    return f'{cnt} {max_time}'


T = int(input())
for _ in range(T):
    print(after_hacked())


#
def after_hacked():
    from heapq import heappush, heappop
    from sys import stdin

    def to_int():
        return map(int, stdin.readline().split())

    n, d, c = to_int()
    limit = 2e7
    time_list = [limit] * (n + 1)
    link = {}
    for _ in range(d):
        a, b, s = to_int()
        if link.get(b):
            link[b].append((s, a))
        else:
            link[b] = [(s, a)]
    process = [(0, c)]
    cnt = max_time = time_list[c] = 0

    while process:
        time, computer = heappop(process)
        if link.get(computer):
            for new_time, other in link[computer]:
                final_time = time + new_time
                if time_list[other] > final_time:
                    time_list[other] = final_time
                    heappush(process, (final_time, other))

    for i in range(1, n + 1):
        time = time_list[i]
        if time != limit:
            if max_time < time:
                max_time = time
            cnt += 1

    return f'{cnt} {max_time}'

def print_result():
    T = int(input())
    for _ in range(T):
        print(after_hacked())

print_result()
