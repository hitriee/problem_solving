#230828
from sys import stdin

for _ in range(3):
    N = int(stdin.readline())
    check = {0}
    total = 0
    for _ in range(N):
        type, cnt = map(int, stdin.readline().split())
        each_total = type*cnt
        new_check = set(check)
        total += each_total
        for i in check:
            for j in range(type, each_total+1, type):
                new_check.add(i+j)
        check = set(new_check)

    if total%2:
        print(0)
    else:
        print(1 if total//2 in check else 0)


#
from sys import stdin

for _ in range(3):
    N = int(stdin.readline())
    limit = int(1e5) + 1
    check = [False] * limit
    check[0] = True
    total = 0
    for _ in range(N):
        type, cnt = map(int, stdin.readline().split())
        each_total = type*cnt
        new_check = list(check)
        total += each_total
        for i in range(limit):
            if check[i]:
                for j in range(type, each_total+1, type):
                    key = i+j
                    new_check[key] = True
        check = list(new_check)

    if total%2:
        print(0)
    else:
        print(1 if check[total//2] else 0)


#
from sys import stdin

for _ in range(3):
    N = int(stdin.readline())
    limit = int(1e5) + 1
    check = [False] * limit
    check[0] = True
    total, new_limit = 0, 1
    for _ in range(N):
        type, cnt = map(int, stdin.readline().split())
        each_total = type*cnt
        new_check = list(check)
        total += each_total
        for i in range(new_limit):
            if check[i]:
                for j in range(type, each_total+1, type):
                    key = i+j
                    new_check[key] = True
        new_limit += each_total
        check = list(new_check)

    if total%2:
        print(0)
    else:
        print(1 if check[total//2] else 0)


#
def return_result():
    from sys import stdin
    N = int(stdin.readline())
    limit = int(1e5) + 1
    check = [False] * limit
    check[0] = True
    total = 0
    for _ in range(N):
        type, cnt = map(int, stdin.readline().split())
        each_total = type*cnt
        new_check = list(check)
        total += each_total
        for i in range(limit):
            if check[i]:
                for j in range(type, each_total+1, type):
                    key = i+j
                    new_check[key] = True
        check = list(new_check)

    if total%2:
        return 0

    return 1 if check[total//2] else 0

for _ in range(3):
    print(return_result())
