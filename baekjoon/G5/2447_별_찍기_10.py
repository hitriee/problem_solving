# 231129
# 260210
# 78116 KB / 116 ms
def main():
    N = int(input())
    base = [['*'] * 3, ['*', ' ', '*'], ['*'] * 3]

    def make_star(level):
        if level == 3:
            return base

        new_arr = [[' '] * level for _ in range(level)]
        quot = level // 3
        before = make_star(quot)
        for idx in range(9):
            if idx != 4:
                for i in range(quot):
                    new_arr[i+(idx//3)*quot][(idx%3)*quot:(idx%3+1)*quot] = before[i]


        return new_arr


    result = make_star(N)
    new_arr = [''.join(result[i]) for i in range(N)]

    return '\n'.join(new_arr)

print(main())



# 78116 KB / 116 ms
def main():
    N = int(input())
    base = [['*'] * 3, ['*', ' ', '*'], ['*'] * 3]

    def make_star(level):
        if level == 3:
            return base

        new_arr = [[' '] * level for _ in range(level)]
        quot = level // 3
        before = make_star(quot)
        for idx in range(9):
            if idx != 4:
                row, col = divmod(idx, 3)
                for i in range(quot):
                    new_arr[i+row*quot][col*quot:(col+1)*quot] = before[i]


        return new_arr


    result = make_star(N)
    new_arr = [''.join(result[i]) for i in range(N)]

    return '\n'.join(new_arr)

print(main())




# 41760 KB / 52 ms
def main():
    N = int(input())
    base = ['***', '* *', '***']

    def make_star(level):
        if level == 3:
            return base

        new_arr = [''] * level
        quot = level // 3
        before = make_star(quot)
        for idx in range(9):
            if idx != 4:
                for i in range(quot):
                    new_arr[(idx//3) * quot + i] += before[i]
            else:
                for i in range(quot):
                    new_arr[(idx//3) * quot + i] += ' ' * quot



        return new_arr


    result = make_star(N)

    return '\n'.join(result)

print(main())



# 41760 KB / 44 ms
def main():
    N = int(input())
    base = ['***', '* *', '***']

    def make_star(level):
        if level == 3:
            return base

        new_arr = [''] * level
        quot = level // 3
        before = make_star(quot)
        for idx in range(9):
            if idx != 4:
                for i in range(quot):
                    new_arr[(idx//3) * quot + i] += before[i]
            else:
                empty = ' ' * quot
                for i in range(quot):
                    new_arr[(idx//3) * quot + i] += empty

        return new_arr


    result = make_star(N)

    return '\n'.join(result)

print(main())




# 41760 KB / 48 ms
def main():
    N = int(input())
    base = ['***', '* *', '***']

    def make_star(level):
        if level == 3:
            return base

        new_arr = [''] * level
        quot = level // 3
        before = make_star(quot)
        for idx in range(9):
            if idx != 4:
                for i in range(quot):
                    new_arr[(idx//3) * quot + i] += before[i]
            else:
                empty = ' ' * quot
                for i in range(quot):
                    new_arr[(idx//3) * quot + i] += empty

        return new_arr


    return '\n'.join(make_star(N))

print(main())




# 41760 KB / 48 ms
def main():
    N = int(input())
    base = ['***', '* *', '***']

    def make_star(level):
        if level == 3:
            return base

        new_arr = [''] * level
        quot = level // 3
        before = make_star(quot)
        for idx in range(9):
            j = (idx//3) * quot
            if idx != 4:
                for i in range(quot):
                    new_arr[j + i] += before[i]
            else:
                empty = ' ' * quot
                for i in range(quot):
                    new_arr[j + i] += empty

        return new_arr


    result = make_star(N)

    return '\n'.join(result)

print(main())