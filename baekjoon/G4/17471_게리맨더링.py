#230802
# 34976 KB / 68 ms
def main():
    from collections import deque

    def minus_one(num):
        return int(num) - 1

    N = int(input())
    population = list(map(int, input().split()))
    min_dif = total = sum(population)
    area = set(range(N))
    one = set()
    link_info = [list(map(minus_one, input().split()))[1:] for _ in range(N)]

    def is_possible(num_set):
        q = deque()
        q.append(num_set.pop())
        while q:
            now = q.popleft()
            next_set = num_set & set(link_info[now])
            q.extend(next_set)
            num_set -= next_set

        return not num_set

    def choose(level, now, cnt):
        nonlocal min_dif
        if level >= N-1:
            return

        for node in range(now+1, N):
            if node > now:
                one.add(node)
                choose(level+1, node, cnt+population[node])
                if is_possible(set(one)) and is_possible(area-one):
                    dif = abs(2*(cnt+population[node])-total)
                    if dif < min_dif:
                        min_dif = dif

                one.remove(node)

    choose(0, -1, 0)

    return min_dif if min_dif < total else -1

print(main())



# 34992 KB / 64 ms
def main():
    from collections import deque

    def minus_one(num):
        return int(num) - 1

    def is_possible(num_set):
        q = deque()
        q.append(num_set.pop())
        while q:
            now = q.popleft()
            next_set = num_set & set(link_info[now])
            q.extend(next_set)
            num_set -= next_set

        return not num_set

    def choose(level, now, cnt):
        nonlocal min_dif
        if level >= N-1:
            return

        for node in range(now+1, N):
            if node > now:
                one.add(node)
                choose(level+1, node, cnt+population[node])
                if is_possible(set(one)) and is_possible(area-one):
                    dif = abs(2*(cnt+population[node])-total)
                    if dif < min_dif:
                        min_dif = dif

                one.remove(node)

    N = int(input())
    population = list(map(int, input().split()))
    min_dif = total = sum(population)
    area = set(range(N))
    one = set()
    link_info = [list(map(minus_one, input().split()))[1:] for _ in range(N)]

    choose(0, -1, 0)

    return min_dif if min_dif < total else -1

print(main())



# 34992 KB / 68 ms
def main():
    from collections import deque

    def minus_one(num):
        return int(num) - 1

    def is_possible(num_set):
        q = deque()
        q.append(num_set.pop())
        while q:
            now = q.popleft()
            next_set = num_set & set(link_info[now])
            q.extend(next_set)
            num_set -= next_set

        return not num_set

    def choose(level, now, cnt):
        nonlocal min_dif
        if level >= N//2:
            return

        for node in range(now+1, N):
            if node > now:
                one.add(node)
                choose(level+1, node, cnt+population[node])
                if is_possible(set(one)) and is_possible(area-one):
                    dif = abs(2*(cnt+population[node])-total)
                    if dif < min_dif:
                        min_dif = dif

                one.remove(node)

    N = int(input())
    population = list(map(int, input().split()))
    min_dif = total = sum(population)
    area = set(range(N))
    one = set()
    link_info = [list(map(minus_one, input().split()))[1:] for _ in range(N)]

    choose(0, -1, 0)

    return min_dif if min_dif < total else -1

print(main())



# 34992 KB / 60 ms
def main():
    from collections import deque

    def minus_one(num):
        return int(num) - 1

    def is_possible(num_set):
        q = deque()
        q.append(num_set.pop())
        while q:
            now = q.popleft()
            next_set = num_set & set(link_info[now])
            q.extend(next_set)
            num_set -= next_set

        return not num_set

    def choose(level, now, cnt):
        nonlocal min_dif
        if level >= half:
            return

        for node in range(now+1, N):
            if node > now:
                one.add(node)
                new_cnt = cnt+population[node]
                choose(level+1, node, new_cnt)
                if is_possible(set(one)) and is_possible(area-one):
                    dif = abs(2*new_cnt-total)
                    if dif < min_dif:
                        min_dif = dif

                one.remove(node)

    N = int(input())
    population = list(map(int, input().split()))
    min_dif = total = sum(population)
    half = N//2
    area = set(range(N))
    one = set()
    link_info = [list(map(minus_one, input().split()))[1:] for _ in range(N)]

    choose(0, -1, 0)

    return min_dif if min_dif < total else -1

print(main())