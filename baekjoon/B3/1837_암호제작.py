#230629
P, K = map(int, input().split())
num_set = set()
start = 2
for i in range(2, min(K, P//2+1)):
    if P%i == 0:
        num_set.update(range(start, i+1))
        for j in range(start, i//2+1):
            num = j * 2
            while num < i:
                if num in num_set:
                    num_set.remove(num)
                num += j
        if i in num_set:
            print(f'BAD {i}')
            break
        start = i//2+1
else:
    print('GOOD')


#
def is_good_num():
    P, K = map(int, input().split())
    num_set = set()
    start = 2
    for i in range(2, min(K, P // 2 + 1)):
        if P % i == 0:
            num_set.update(range(start, i + 1))
            for j in range(start, i // 2 + 1):
                num = j * 2
                while num < i:
                    if num in num_set:
                        num_set.remove(num)
                    num += j
            if i in num_set:
                return f'BAD {i}'
            start = i // 2 + 1

    return 'GOOD'

print(is_good_num())


#
def is_good_num():
    P, K = map(int, input().split())
    if P%2 == 0:
        return f'BAD {2}' if K > 2 else 'GOOD'

    num_set = set()
    start = 3
    for i in range(3, min(K, P // 2 + 1), 2):
        if P % i == 0:
            num_set.update(range(start, i + 1))
            for j in range(start, i // 2 + 1):
                num = j * 2
                while num < i:
                    if num in num_set:
                        num_set.remove(num)
                    num += j
            if i in num_set:
                return f'BAD {i}'
            start = i // 2 + 1

    return 'GOOD'

print(is_good_num())


#
def is_good_num():
    from math import isqrt
    P, K = map(int, input().split())
    if P%2 == 0:
        return f'BAD {2}' if K > 2 else 'GOOD'

    num_set = set()
    start = 3
    for i in range(3, min(K, isqrt(P) + 1), 2):
        if P % i == 0:
            num_set.update(range(start, i + 1))
            root = isqrt(i)
            for j in range(start, root + 1):
                num = j * 2
                while num < i:
                    if num in num_set:
                        num_set.remove(num)
                    num += j
            if i in num_set:
                return f'BAD {i}'
            start = root

    return 'GOOD'

print(is_good_num())


#
def is_good_num():
    from math import isqrt
    P, K = map(int, input().split())
    if P%2 == 0:
        return f'BAD {2}' if K > 2 else 'GOOD'

    num_set = set(range(3, min(K, isqrt(P) + 1), 2))
    start = 3
    for i in range(3, min(K, isqrt(P) + 1), 2):
        if P % i == 0:
            root = isqrt(i)
            for j in range(start, root + 1):
                num = j * 2
                while num < i:
                    if num in num_set:
                        num_set.remove(num)
                    num += j
            if i in num_set:
                return f'BAD {i}'
            start = root

    return 'GOOD'

print(is_good_num())