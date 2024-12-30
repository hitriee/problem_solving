# 241230
# 36264 KB / 180 ms
def main():
    T = int(input())
    cases = [0] * 100001
    cases[0] = cases[1] = 1
    cases[2] = cases[3] = 2
    for i in range(4, 6):
        cases[i] = cases[i-2] + cases[i-4]

    start_num = 6
    for _ in range(T):
        N = int(input())
        if cases[N]:
            print(cases[N])
        else:
            answer, div_num = 0, 1000000009
            for i in range(start_num, N+1):
                cases[i] = (cases[i-2] + cases[i-4] + cases[i-6])%div_num

            start_num = N
            print(cases[N])

main()


# 37288 KB / 108 ms
def main():
    T = int(input())
    arr = [int(input()) for _ in range(T)]

    limit = max(*arr, 5) + 1
    cases = [0] * limit
    cases[0] = cases[1] = 1
    cases[2] = cases[3] = 2
    div_num = 1000000009

    for i in range(4, 6):
        cases[i] = cases[i-2] + cases[i-4]


    for i in range(6, limit):
        cases[i] = (cases[i-2] + cases[i-4] + cases[i-6]) % div_num

    for num in arr:
        print(cases[num])

main()


# 37288 KB / 64 ms
def main():
    from sys import stdin

    def int_input():
        return int(stdin.readline())

    T = int_input()
    arr = [int_input() for _ in range(T)]

    limit = max(*arr, 5) + 1
    cases = [0] * limit
    cases[0] = cases[1] = 1
    cases[2] = cases[3] = 2
    div_num = 1000000009

    for i in range(4, 6):
        cases[i] = cases[i-2] + cases[i-4]


    for i in range(6, limit):
        cases[i] = (cases[i-2] + cases[i-4] + cases[i-6]) % div_num

    for num in arr:
        print(cases[num])

main()




# 37288 KB / 64 ms
def main():
    from sys import stdin

    def int_input():
        return int(stdin.readline())

    T = int_input()
    arr = [int_input() for _ in range(T)]

    limit = max(*arr, 5) + 1
    cases = [0] * limit
    cases[0] = cases[1] = 1
    cases[2] = cases[3] = 2
    div_num = 1000000009

    for i in range(4, 6):
        cases[i] = cases[i-2] + cases[i-4]


    for i in range(6, limit):
        cases[i] = (cases[i-2] + cases[i-4] + cases[i-6]) % div_num

    return '\n'.join(str(cases[num]) for num in arr)

print(main())