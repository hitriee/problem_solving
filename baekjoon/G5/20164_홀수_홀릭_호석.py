# 241031
# 34220 KB / 64 ms
def main():
    from collections import deque
    N = input()
    if len(N) == 1:
        remain = int(N)%2
        return f'{remain} {remain}'

    odd_nums = set(str(i) for i in range(1, 10, 2))
    max_odd_cnt, min_odd_cnt = 0, 1e9

    for num in N:
        if num in odd_nums:
            max_odd_cnt += 1

    q = deque()
    q.append((max_odd_cnt, N))

    while q:
        odd_cnt, num = q.popleft()
        length = len(num)
        if length == 1:
            if max_odd_cnt < odd_cnt:
                max_odd_cnt = odd_cnt

            if min_odd_cnt > odd_cnt:
                min_odd_cnt = odd_cnt

        elif length <= 3:
            new_odd_cnt, new_num = odd_cnt, 0
            for element in num:
                new_num += int(element)
            new_num = str(new_num)

            for element in new_num:
                if element in odd_nums:
                    new_odd_cnt += 1

            q.append((new_odd_cnt, new_num))
        else:
            for i in range(1, length-1):
                num1 = int(num[:i])
                for j in range(i+1, length):
                    new_odd_cnt = odd_cnt
                    new_num = str(sum([num1, int(num[i:j]), int(num[j:])]))
                    for element in new_num:
                        if element in odd_nums:
                            new_odd_cnt += 1
                    q.append((new_odd_cnt, new_num))

    return f'{min_odd_cnt} {max_odd_cnt}'


print(main())


# 34096 KB / 68 ms
def main():
    from collections import deque
    N = input()
    if len(N) == 1:
        remain = int(N)%2
        return f'{remain} {remain}'

    odd_nums = set(str(i) for i in range(1, 10, 2))
    max_odd_cnt, min_odd_cnt = 0, 1e9

    for num in N:
        if num in odd_nums:
            max_odd_cnt += 1

    q = deque()
    q.append((max_odd_cnt, N))

    while q:
        odd_cnt, num = q.popleft()
        length = len(num)
        if length == 1:
            if max_odd_cnt < odd_cnt:
                max_odd_cnt = odd_cnt

            if min_odd_cnt > odd_cnt:
                min_odd_cnt = odd_cnt

        elif length <= 3:
            new_odd_cnt, new_num = odd_cnt, 0
            for element in num:
                new_num += int(element)
            new_num = str(new_num)

            for element in new_num:
                if element in odd_nums:
                    new_odd_cnt += 1

            q.append((new_odd_cnt, new_num))
        else:
            visited = set()
            for i in range(1, length-1):
                num1 = int(num[:i])
                for j in range(i+1, length):
                    new_odd_cnt = odd_cnt
                    nums = tuple(sorted((num1, int(num[i:j]), int(num[j:]))))
                    if nums not in visited:
                        new_num = str(sum(nums))
                        for element in new_num:
                            if element in odd_nums:
                                new_odd_cnt += 1
                        q.append((new_odd_cnt, new_num))

    return f'{min_odd_cnt} {max_odd_cnt}'

print(main())


# 34096 KB / 60 ms
def main():
    from collections import deque
    N = input()
    if len(N) == 1:
        remain = int(N)%2
        return f'{remain} {remain}'

    odd_nums = set(str(i) for i in range(1, 10, 2))
    max_odd_cnt, min_odd_cnt = 0, 1e9

    for num in N:
        if num in odd_nums:
            max_odd_cnt += 1

    q = deque()
    q.append((max_odd_cnt, N))

    while q:
        odd_cnt, num = q.popleft()
        length = len(num)
        if length == 1:
            if max_odd_cnt < odd_cnt:
                max_odd_cnt = odd_cnt

            if min_odd_cnt > odd_cnt:
                min_odd_cnt = odd_cnt

        elif length <= 3:
            new_odd_cnt, new_num = odd_cnt, 0
            for element in num:
                new_num += int(element)
            new_num = str(new_num)

            for element in new_num:
                if element in odd_nums:
                    new_odd_cnt += 1

            q.append((new_odd_cnt, new_num))
        else:
            visited = set()
            for i in range(1, length-1):
                num1 = int(num[:i])
                for j in range(i+1, length):
                    new_odd_cnt = odd_cnt
                    new_num = str(sum((num1, int(num[i:j]), int(num[j:]))))
                    if new_num not in visited:
                        for element in new_num:
                            if element in odd_nums:
                                new_odd_cnt += 1
                        q.append((new_odd_cnt, new_num))

    return f'{min_odd_cnt} {max_odd_cnt}'



print(main())
