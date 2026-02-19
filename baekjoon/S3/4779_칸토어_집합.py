# 260213
# 48096 KB / 72 ms
def main():
    while True:
        def change_arr(level, arr):
            if level == 1:
                return arr

            third = level // 3
            left = change_arr(third, arr[:third])

            return left + [' '] * third + left

        try:
            N = int(input())
            limit = 3**N
            result = change_arr(limit, ['-'] * limit)
            print(''.join(result))

        except Exception:
            break

main()




# 48096 KB / 56 ms
def main():
    from sys import stdin

    new_input = stdin.readline

    def change_arr(level, arr):
        if level == 1:
            return arr

        third = level // 3
        left = change_arr(third, arr[:third])

        return left + [' '] * third + left


    while True:

        try:
            N = int(new_input())
            limit = 3**N
            result = change_arr(limit, ['-'] * limit)
            print(''.join(result))

        except Exception:
            break

main()






# 48096 KB / 60 ms
def main():

    def change_arr(level, arr):
        if level == 1:
            return arr

        third = level // 3
        left = change_arr(third, arr[:third])

        return left + [' '] * third + left


    while True:

        try:
            N = int(input())
            limit = 3**N
            result = change_arr(limit, ['-'] * limit)
            print(''.join(result))

        except Exception:
            break

main()