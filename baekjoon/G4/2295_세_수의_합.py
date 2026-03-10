# 260202
# 260310
# 110740 KB / 496 ms (Pypy 3)
def main():
    from sys import stdin

    def int_input():
        return int(stdin.readline())

    N = int_input()
    num_arr = sorted(set(int_input() for _ in range(N)))
    M = len(num_arr)

    for i in range(M-1, 0, -1):
        total_num = num_arr[i]
        for j in range(i):
            target = total_num - num_arr[j]
            start, end = j, i-1
            while start <= end:
                sum_of_two = num_arr[start] + num_arr[end]
                if sum_of_two < target:
                    start += 1
                elif sum_of_two > target:
                    end -= 1
                else:
                    return total_num

    return num_arr[0]

print(main())







# 110576 KB / 496 ms (Pypy 3)
def main():
    from sys import stdin

    def int_input():
        return int(stdin.readline())

    N = int_input()
    num_arr = sorted(set(int_input() for _ in range(N)))
    M = len(num_arr)

    for i in range(M-1, 0, -1):
        total_num = num_arr[i]
        for j in range(i-1, -1, -1):
            target = total_num - num_arr[j]
            start, end = j, i-1
            while start <= end:
                sum_of_two = num_arr[start] + num_arr[end]
                if sum_of_two < target:
                    start += 1
                elif sum_of_two > target:
                    end -= 1
                else:
                    return total_num

    return num_arr[0]

print(main())








# 110576 KB / 496 ms (Pypy 3)
def main():
    from sys import stdin

    def int_input():
        return int(stdin.readline())

    N = int_input()
    num_arr = sorted([int_input() for _ in range(N)])

    for i in range(N-1, 0, -1):
        total_num = num_arr[i]
        for j in range(i-1, -1, -1):
            target = total_num - num_arr[j]
            start, end = j, i-1
            while start <= end:
                sum_of_two = num_arr[start] + num_arr[end]
                if sum_of_two < target:
                    start += 1
                elif sum_of_two > target:
                    end -= 1
                else:
                    return total_num

    return num_arr[0]

print(main())






# 110576 KB / 496 ms (Pypy 3)
def main():
    from sys import stdin

    def int_input():
        return int(stdin.readline())

    N = int_input()
    num_arr = [int_input() for _ in range(N)]
    num_arr.sort()

    for i in range(N-1, 0, -1):
        total_num = num_arr[i]
        for j in range(i-1, -1, -1):
            target = total_num - num_arr[j]
            start, end = j, i-1
            while start <= end:
                sum_of_two = num_arr[start] + num_arr[end]
                if sum_of_two < target:
                    start += 1
                elif sum_of_two > target:
                    end -= 1
                else:
                    return total_num

    return num_arr[0]

print(main())





# 19040 KB / 164 ms (Pypy 3)
# 67232 KB / 184 ms (Python 3)
def main():
    from sys import stdin

    def int_input():
        return int(stdin.readline())

    N = int_input()
    num_arr = [int_input() for _ in range(N)]

    two_of = set()
    for i in range(N):
        for j in range(i, N):
            two_of.add(num_arr[i] + num_arr[j])

    num_arr.sort()

    for i in range(N-1, 0, -1):
        total_num = num_arr[i]
        for j in range(i-1, -1, -1):
            if total_num - num_arr[j] in two_of:
                return total_num


    return num_arr[0]

print(main())