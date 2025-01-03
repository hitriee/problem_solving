# 250103
# 32412 KB / 36 ms
def main():
    # 4 7 / 44 47 74 77
    # 444 447 474 477 744 747 774 777

    K = int(input())
    if K == 1:
        return '4'
    if K == 2:
        return '7'
    k, plus = 0, 2


    while True:
        if k + plus >= K:
            num = ''
            while plus > 1:
                plus //= 2
                if k + plus >= K:
                    num += '4'
                else:
                    num += '7'
                    k += plus

            return num

        k += plus
        plus *= 2

print(main())


# 32412 KB / 36 ms
def main():
    K = int(input())

    def find_num(level, plus):
        num = ''
        while plus > 1:
            plus //= 2
            if level + plus >= K:
                num += '4'
            else:
                num += '7'
                level += plus

        return num

    def acc_level(level, plus):
        if level + plus >= K:
            return find_num(level, plus)

        return acc_level(level+plus, plus*2)

    return acc_level(0, 2)

print(main())


# 32412 KB / 32 ms
def main():

    K = int(input())
    k, plus = 0, 2

    while True:
        if k + plus >= K:
            num = ''
            while plus > 1:
                plus //= 2
                if k + plus >= K:
                    num += '4'
                else:
                    num += '7'
                    k += plus

            return num

        k += plus
        plus *= 2

print(main())