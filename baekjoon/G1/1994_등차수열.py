# 250602
# 48108 KB / 2056 ms
def main():
    from sys import stdin

    def int_input():
        return int(stdin.readline())

    N = int_input()
    if N <= 2:
        return N

    def binary_search(target, end):
        start = 0
        while start <= end:
            mid = (start + end) // 2
            num = sorted_num[mid]
            if num > target:
                end = mid - 1
            elif num < target:
                start = mid + 1
            else:
                return mid

        return -1

    num_cnt = {}
    for _ in range(N):
        num = int_input()
        num_cnt[num] = num_cnt.get(num, 0) + 1

    sorted_num = sorted(num_cnt)
    max_len = max(2, *num_cnt.values())
    M = len(sorted_num)
    table = [[0] * i for i in range(M)]

    for large in range(M-1, 0, -1):
        num1 = sorted_num[large]
        for small in range(large-1, -1, -1):
            num2 = sorted_num[small]
            if table[large][small] == 0:
                table[large][small] = 2
                step = num2 - num1
                now_len, now_num = 2, num2 + step
                idx1, idx2 = small, binary_search(now_num, small-1)

                while idx2 >= 0:
                    now_len += 1
                    now_num += step
                    table[idx1][idx2] = now_len
                    idx1, idx2 = idx2, binary_search(now_num, idx2-1)

                if max_len < now_len:
                    max_len = now_len

    return max_len


print(main())



# 63840 KB / 2088 ms
def main():
    from sys import stdin

    def int_input():
        return int(stdin.readline())

    N = int_input()
    if N <= 2:
        return N

    def binary_search(target, end):
        start = 0
        while start <= end:
            mid = (start + end) // 2
            num = sorted_num[mid]
            if num > target:
                end = mid - 1
            elif num < target:
                start = mid + 1
            else:
                return mid

        return -1

    num_cnt = {}
    for _ in range(N):
        num = int_input()
        num_cnt[num] = num_cnt.get(num, 0) + 1

    sorted_num = sorted(num_cnt)
    max_len = max(2, *num_cnt.values())
    M = len(sorted_num)
    table = [[0] * M for _ in range(M)]

    for large in range(M-1, 0, -1):
        num1 = sorted_num[large]
        for small in range(large-1, -1, -1):
            num2 = sorted_num[small]
            if table[large][small] == 0:
                table[large][small] = 2
                step = num2 - num1
                now_len, now_num = 2, num2 + step
                idx1, idx2 = small, binary_search(now_num, small-1)

                while idx2 >= 0:
                    now_len += 1
                    now_num += step
                    table[idx1][idx2] = now_len
                    idx1, idx2 = idx2, binary_search(now_num, idx2-1)

                if max_len < now_len:
                    max_len = now_len

    return max_len


print(main())