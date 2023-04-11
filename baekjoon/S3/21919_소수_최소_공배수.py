#230411
# isqrt, for, set
from math import isqrt
N = int(input())
num_arr = list(map(int, input().split()))
prime_num = set()
for num in num_arr:
    end = isqrt(num) + 1
    for div in range(2, end):
        if num%div == 0:
            break
    else:
        prime_num.add(num)
if prime_num:
    lcm = 1
    for num in prime_num:
        lcm *= num
    print(lcm)
else:
    print(-1)


# for-else에서 else 삭제
N = int(input())
num_arr = list(map(int, input().split()))
prime_num = set()
for num in num_arr:
    for div in range(2, num + 1):
        if num//div < div:
            prime_num.add(num)
            break
        if num%div == 0:
            break
if prime_num:
    lcm = 1
    for num in prime_num:
        lcm *= num
    print(lcm)
else:
    print(-1)

# 함수화
def return_lcm():
    from math import isqrt
    N = int(input())
    num_arr = list(map(int, input().split()))
    prime_num = set()
    for num in num_arr:
        end = isqrt(num) + 1
        for div in range(2, end):
            if num%div == 0:
                break
        else:
            prime_num.add(num)
    if prime_num:
        lcm = 1
        for num in prime_num:
            lcm *= num
        return lcm
    return -1
print(return_lcm())


# 함수화2
def return_lcm():
    def add_prime():
        for num in num_arr:
            end = isqrt(num) + 1
            for div in range(2, end):
                if num%div == 0:
                    break
            else:
                prime_num.add(num)

    from math import isqrt
    N = int(input())
    num_arr = list(map(int, input().split()))
    prime_num = set()
    add_prime()
    if prime_num:
        lcm = 1
        for num in prime_num:
            lcm *= num
        return lcm
    return -1
print(return_lcm())


# 함수화3
def return_lcm():
    def add_prime():
        end = isqrt(num) + 1
        for div in range(2, end):
            if num%div == 0:
                return
        prime_num.add(num)

    from math import isqrt
    N = int(input())
    num_arr = list(map(int, input().split()))
    prime_num = set()
    for num in num_arr:
        add_prime()
    if prime_num:
        lcm = 1
        for num in prime_num:
            lcm *= num
        return lcm
    return -1
print(return_lcm())

# lcm 바로 구하기
def return_lcm():
    def calc_lcm():
        lcm = 1
        for num in num_arr:
            end = isqrt(num) + 1
            for div in range(2, end):
                if num%div == 0:
                    break
            else:
                lcm *= num
        return lcm

    from math import isqrt
    N = int(input())
    num_arr = set(map(int, input().split()))
    lcm = calc_lcm()
    return lcm if lcm != 1 else -1
print(return_lcm())


# isqrt 제거
def return_lcm():
    def calc_lcm():
        from math import isqrt
        lcm = 1
        for num in num_arr:
            end = isqrt(num) + 1
            for div in range(2, end):
                if num%div == 0:
                    break
            else:
                lcm *= num
        return lcm

    N = int(input())
    num_arr = set(map(int, input().split()))
    lcm = calc_lcm()
    return lcm if lcm != 1 else -1
print(return_lcm())
