# 250606
# 33432 KB / 1708 ms
def main():
    str1 = input()
    str2 = input()
    max_len, n, m = 0, len(str1), len(str2)
    before = [0] * m
    after = [0] * m

    for j in range(m):
        if str1[0] == str2[j]:
            before[j] = max_len = 1

    for i in range(1, n):
        alp = str1[i]
        if alp == str2[0]:
            after[0] = 1

        for j in range(1, m):
            if alp == str2[j]:
                after[j] = before[j-1] + 1

        max_len = max(*after, max_len)
        before = after[:]
        after = [0] * m

    return max_len

print(main())




#
def main():
    str1 = input()
    str2 = input()
    max_len, n, m = 0, len(str1), len(str2)
    before = [0] * m
    after = [0] * m

    for j in range(m):
        if str1[0] == str2[j]:
            before[j] = max_len = 1

    for i in range(1, n):
        alp = str1[i]
        if alp == str2[0]:
            after[0] = 1

        for j in range(1, m):
            after[j] = before[j-1] + 1 if alp == str2[j] else 0

        max_len = max(*after, max_len)
        before = after[:]

    return max_len

print(main())




# 33432 KB / 2060 ms
def main():
    str1 = input()
    str2 = input()
    max_len, n, m = 0, len(str1), len(str2)
    before = [0] * (m+1)
    after = [0] * (m+1)

    for i in range(n):
        alp = str1[i]

        for j in range(1, m+1):
            after[j] = before[j-1] + 1 if alp == str2[j-1] else 0

        max_len = max(*after, max_len)
        before = after[:]

    return max_len

print(main())
