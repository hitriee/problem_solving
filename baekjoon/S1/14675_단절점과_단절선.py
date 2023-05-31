#230531
from sys import stdin
from collections import defaultdict
new_input = stdin.readline

N = int(new_input())
link = defaultdict(list)
for _ in range(N-1):
    a, b = new_input().split()
    link[a].append(b)
    link[b].append(a)

q = int(new_input())
for _ in range(q):
    t, k = new_input().split()
    if t == '1':
        if len(link[k]) == 1:
            print('no')
        else:
            print('yes')
    else:
        print('yes')


#
from sys import stdin
from collections import defaultdict
new_input = stdin.readline

N = int(new_input())
link = defaultdict(list)
for _ in range(N-1):
    a, b = new_input().split()
    link[a].append(b)
    link[b].append(a)

q = int(new_input())
for _ in range(q):
    t, k = new_input().split()
    if t == '2' or len(link[k]) != 1:
        print('yes')
    else:
        print('no')


#
from sys import stdin
from collections import defaultdict
new_input = stdin.readline

N = int(new_input())
link = defaultdict(list)
for _ in range(N-1):
    a, b = new_input().split()
    link[a].append(b)
    link[b].append(a)

q = int(new_input())
for _ in range(q):
    t, k = new_input().split()
    if t == '2':
        print('yes')
    elif len(link[k]) == 1:
        print('no')
    else:
        print('yes')


#
def print_answer():
    from sys import stdin
    from collections import defaultdict
    new_input = stdin.readline

    N = int(new_input())
    link = defaultdict(list)
    for _ in range(N-1):
        a, b = new_input().split()
        link[a].append(b)
        link[b].append(a)

    def return_answer():
        t, k = new_input().split()
        if t == '2':
            return 'yes'
        elif len(link[k]) == 1:
            return 'no'
        return 'yes'

    q = int(new_input())
    for _ in range(q):
        print(return_answer())

print_answer()


#
def print_answer():
    from sys import stdin
    from collections import defaultdict
    new_input = stdin.readline

    N = int(new_input())
    link = defaultdict(list)
    for _ in range(N-1):
        a, b = new_input().split()
        link[a].append(b)
        link[b].append(a)

    def return_answer():
        t, k = new_input().split()
        if t == '1' and len(link[k]) == 1:
            return 'no'
        return 'yes'

    q = int(new_input())
    for _ in range(q):
        print(return_answer())

print_answer()

#
def print_answer():
    from sys import stdin
    new_input = stdin.readline

    N = int(new_input())
    link = {}
    for _ in range(N-1):
        a, b = new_input().split()
        if link.get(a):
            link[a].append(b)
        else:
            link[a] = [b]
        if link.get(b):
            link[b].append(a)
        else:
            link[b] = [a]

    def return_answer():
        t, k = new_input().split()
        if t == '2':
            return 'yes'
        elif len(link[k]) == 1:
            return 'no'
        return 'yes'

    q = int(new_input())
    for _ in range(q):
        print(return_answer())

print_answer()