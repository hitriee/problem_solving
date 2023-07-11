#230711
from sys import stdin
from math import isqrt
while True:
    num = int(stdin.readline())
    if num == 0:
        break
    if num == 1:
        print(1)
    else:
        prime_num = set(range(num+2, 2*num+1, 2) if num%2 == 1 else range(num+1, 2*num+1, 2))
        for i in range(3, isqrt(2*num)+1, 2):
            multiple_num = i*3
            while multiple_num < 2*num+1:
                if multiple_num in prime_num:
                    prime_num.remove(multiple_num)
                multiple_num += 2*i
        print(len(prime_num))


#
from sys import stdin
from math import isqrt
while True:
    num = int(stdin.readline())
    if num == 0:
        break
    if num == 1:
        print(1)
    else:
        limit = 2*num
        prime_num = set(range(num+2, limit, 2) if num%2 == 1 else range(num+1, limit, 2))
        for i in range(3, isqrt(limit)+1, 2):
            multiple_num = i*3
            while multiple_num < 2*num+1:
                if multiple_num in prime_num:
                    prime_num.remove(multiple_num)
                multiple_num += 2*i
        print(len(prime_num))


#
def print_cnt():
    from sys import stdin
    from math import isqrt
    while True:
        num = int(stdin.readline())
        if num == 0:
            break
        if num == 1:
            print(1)
        else:
            limit = 2 * num
            prime_num = set(range(num + 2, limit, 2) if num % 2 == 1 else range(num + 1, limit, 2))
            for i in range(3, isqrt(limit) + 1, 2):
                multiple_num = i * 3
                while multiple_num < 2 * num + 1:
                    if multiple_num in prime_num:
                        prime_num.remove(multiple_num)
                    multiple_num += 2 * i
            print(len(prime_num))

print_cnt()


#
def print_cnt():
    from sys import stdin
    from math import isqrt
    prime_num = {2}
    before = 2
    while True:
        num = int(stdin.readline())
        if num == 0:
            break
        if num == 1:
            print(1)
        else:
            limit = 2 * num
            if limit > before:
                prime_num.update(range(before+1, limit+1, 2))
                before = limit
                for i in range(3, isqrt(limit)+1):
                    multiple_num = i * 3
                    while multiple_num <= limit:
                        if multiple_num in prime_num:
                            prime_num.remove(multiple_num)
                        multiple_num += 2 * i
            cnt = 0
            for i in range(num+2 if num%2 else num+1, limit+1, 2):
                if i in prime_num:
                    cnt += 1
            print(cnt)

print_cnt()