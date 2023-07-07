#230707
N, M = map(int, input().split())
knew = list(map(int, input().split()))
if knew[0] == 0:
    print(M)
else:
    knew_person = set(knew[1:])
    need_truth = set()
    length = 0
    party = [set(list(map(int, input().split()))[1:]) for _ in range(M)]
    while length != len(knew_person):
        length = len(knew_person)
        for i in range(M):
            if party[i] & knew_person:
                need_truth.add(i)
                knew_person.update(party[i])
    print(M-len(need_truth))


#
def cnt_possible():
    N, M = map(int, input().split())
    knew = list(map(int, input().split()))
    if knew[0] == 0:
        return M

    knew_person = set(knew[1:])
    need_truth = set()
    length = 0
    party = [set(list(map(int, input().split()))[1:]) for _ in range(M)]

    while length != len(knew_person):
        length = len(knew_person)
        for i in range(M):
            if party[i] & knew_person:
                need_truth.add(i)
                knew_person.update(party[i])

    return M-len(need_truth)

print(cnt_possible())


#
def cnt_possible():
    N, M = map(int, input().split())
    knew = list(map(int, input().split()))
    if knew[0] == 0:
        return M

    knew_person = set(knew[1:])
    need_truth = set()
    length = 0
    party = [set(list(map(int, input().split()))[1:]) for _ in range(M)]

    while length != len(knew_person):
        length = len(knew_person)
        for i in range(M):
            if i not in need_truth and party[i] & knew_person:
                need_truth.add(i)
                knew_person.update(party[i])

    return M-len(need_truth)

print(cnt_possible())


#
def cnt_possible():
    N, M = map(int, input().split())
    knew_person = set(map(int, input().split()[1:]))
    if len(knew_person) == 0:
        return M

    need_truth = set()
    length = 0
    party = [set(map(int, input().split()[1:])) for _ in range(M)]

    while length != len(knew_person):
        length = len(knew_person)
        for i in range(M):
            if i not in need_truth and party[i] & knew_person:
                need_truth.add(i)
                knew_person.update(party[i])

    return M-len(need_truth)

print(cnt_possible())


#
def cnt_possible():
    N, M = map(int, input().split())
    knew_person = set(map(int, input().split()[1:]))
    if len(knew_person) == 0:
        return M

    need_truth = set()
    changed = False
    party = [set(map(int, input().split()[1:])) for _ in range(M)]

    while True:
        for i in range(M):
            if i not in need_truth and party[i] & knew_person:
                need_truth.add(i)
                knew_person.update(party[i])
                if not changed:
                    changed = True

        if not changed:
            return M-len(need_truth)

        changed = False

print(cnt_possible())


#
def cnt_possible():
    from sys import stdin

    def to_int_set():
        return set(map(int, stdin.readline().split()[1:]))

    N, M = map(int, stdin.readline().split())
    knew_person = to_int_set()
    if len(knew_person) == 0:
        return M

    need_truth = set()
    changed = False
    party = [to_int_set() for _ in range(M)]

    while True:
        for i in range(M):
            if i not in need_truth and party[i] & knew_person:
                need_truth.add(i)
                knew_person.update(party[i])
                if not changed:
                    changed = True

        if not changed:
            return M-len(need_truth)

        changed = False

print(cnt_possible())


#
def cnt_possible():
    from sys import stdin

    def to_int_set():
        return set(map(int, stdin.readline().split()[1:]))

    N, M = map(int, input().split())
    knew_person = to_int_set()
    if len(knew_person) == 0:
        return M

    need_truth = set()
    changed = False
    party = [to_int_set() for _ in range(M)]

    while True:
        for i in range(M):
            if i not in need_truth and party[i] & knew_person:
                need_truth.add(i)
                knew_person.update(party[i])
                if not changed:
                    changed = True

        if not changed:
            return M-len(need_truth)

        changed = False

print(cnt_possible())