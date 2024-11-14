# 241114
# 33240 KB / 36 ms
def main():
    from math import isqrt

    N = int(input())

    def is_prime_num(num):
        if num == 1:
            return False
        if num == 2:
            return True
        if num%2 == 0:
            return False

        limit = isqrt(num)+1
        for j in range(3, limit, 2):
            if num % j == 0:
                return False
        return True

    def make_num(level, num):
        if level > 0 and not is_prime_num(int(num)):
            return
        if level == N:
            print(num)
            return

        for i in range(1, 10):
            make_num(level+1, num+str(i))

    make_num(0, '')


main()



# 33240 KB / 36 ms
def main():
    from math import isqrt

    N = int(input())

    def is_prime_num(num):
        if num == 1:
            return False
        if num == 2:
            return True
        if num%2 == 0:
            return False

        limit = isqrt(num)+1
        for j in range(3, limit, 2):
            if num % j == 0:
                return False
        return True

    def make_num(level, num):
        if not is_prime_num(int(num)):
            return

        if level == N:
            print(num)
            return

        for i in range(1, 10):
            make_num(level+1, num+str(i))

    for i in ['2', '3', '5', '7']:
        make_num(1, i)


main()




# 33240 KB / 36 ms
def main():
    from math import isqrt

    N = int(input())

    def is_prime_num(num):
        if num%2 == 0:
            return False

        limit = isqrt(num)+1
        for j in range(3, limit, 2):
            if num % j == 0:
                return False
        return True

    def make_num(level, num):
        if level > 1 and not is_prime_num(int(num)):
            return

        if level == N:
            print(num)
            return

        for i in range(1, 10):
            make_num(level+1, num+str(i))

    for i in ['2', '3', '5', '7']:
        make_num(1, i)


main()
