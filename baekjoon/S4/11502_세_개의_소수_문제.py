# 230424
# 에라토스테네스의 체, 메모이제이션
def fill_set():
    global start
    prime_set.update(range(start, K))
    for num in range(2, K):
        if num in prime_set:
            multiple = num*2
            while multiple < K:
                if multiple in prime_set:
                    prime_set.remove(multiple)
                multiple += num
    start = K
def return_answer():
    for num1 in prime_set:
        for num2 in prime_set:
            num3 = K - (num1 + num2)
            if num3 in prime_set:
                return sorted([num1, num2, num3])
    return [0]

T = int(input())
prime_set = set()
start = 2
for _ in range(T):
    K = int(input())
    if K > start:
        fill_set()
    print(*return_answer())


# 함수 내부 변경
def fill_set():
    prime_set.update(range(start, K))
    for num in range(2, K):
        if num in prime_set:
            multiple = num*2
            while multiple < K:
                if multiple in prime_set:
                    prime_set.remove(multiple)
                multiple += num
def return_answer():
    for num1 in prime_set:
        for num2 in prime_set:
            num3 = K - (num1 + num2)
            if num3 in prime_set:
                return sorted([num1, num2, num3])
    return [0]

T = int(input())
prime_set = set()
start = 2
for _ in range(T):
    K = int(input())
    if K > start:
        fill_set()
        start = K
    print(*return_answer())


# 에라토스테네스의 체 범위 조절
def fill_set():
    prime_set.update(range(start, K))
    copied_set = set(prime_set)
    for num in copied_set:
        if num in prime_set:
            multiple = num*2
            while multiple < K:
                if multiple in prime_set:
                    prime_set.remove(multiple)
                multiple += num
def return_answer():
    for num1 in prime_set:
        for num2 in prime_set:
            num3 = K - (num1 + num2)
            if num3 in prime_set:
                return sorted([num1, num2, num3])
    return [0]

T = int(input())
prime_set = set()
start = 2
for _ in range(T):
    K = int(input())
    if K > start:
        fill_set()
        start = K
    print(*return_answer())


#
def print_three():
    def fill_set():
        prime_set.update(range(start, K))
        copied_set = set(prime_set)
        for num in copied_set:
            if num in prime_set:
                multiple = num * 2
                while multiple < K:
                    if multiple in prime_set:
                        prime_set.remove(multiple)
                    multiple += num

    def return_answer():
        for num1 in prime_set:
            for num2 in prime_set:
                num3 = K - (num1 + num2)
                if num3 in prime_set:
                    return sorted([num1, num2, num3])
        return [0]

    T = int(input())
    prime_set = set()
    start = 2
    for _ in range(T):
        K = int(input())
        if K > start:
            fill_set()
            start = K
        print(*return_answer())

print_three()


# 반복문 중간 break
def find_three():
    def fill_set():
        prime_set.update(range(start, K))
        copied_set = set(prime_set)
        for num in copied_set:
            if num in prime_set:
                multiple = num*2
                while multiple < K:
                    if multiple in prime_set:
                        prime_set.remove(multiple)
                    multiple += num

    def return_answer():
        for num1 in prime_set:
            for num2 in prime_set:
                num3 = K - (num1 + num2)
                if num3 <= 0:
                    break
                elif num3 in prime_set:
                    return sorted([num1, num2, num3])
        return [0]

    T = int(input())
    prime_set = set()
    start = 2
    for _ in range(T):
        K = int(input())
        if K > start:
            fill_set()
            start = K
        print(*return_answer())
find_three()


# num3 조건, sorted 조건 수정
def find_three():
    def fill_set():
        prime_set.update(range(start, K))
        copied_set = set(prime_set)
        for num in copied_set:
            if num in prime_set:
                multiple = num*2
                while multiple < K:
                    if multiple in prime_set:
                        prime_set.remove(multiple)
                    multiple += num

    def return_answer():
        for num1 in prime_set:
            for num2 in prime_set:
                num3 = K - (num1 + num2)
                if num3 <= 1:
                    break
                elif num3 in prime_set:
                    return [num1, num2, num3]
        return [0]

    T = int(input())
    prime_set = set()
    start = 2
    for _ in range(T):
        K = int(input())
        if K > start:
            fill_set()
            start = K
        print(*return_answer())
find_three()