# 250131
# 57628 KB / 212 ms
def main():
    str1 = input()
    str2 = input()
    len1, len2 = len(str1), len(str2)
    arr = [[0] * (len2+1) for _ in range(len1+1)]

    for i in range(len1):
        for j in range(len2):
            if str1[i] == str2[j]:
                arr[i+1][j+1] = arr[i][j] + 1
            else:
                arr[i+1][j+1] = max(arr[i][j+1], arr[i+1][j])

    len3 = arr[-1][-1]
    print(len3)

    if len3:
        lcs = ''
        i, j = len1, len2
        while i > 0 and j > 0:
            length = arr[i][j]
            if length != max(arr[i - 1][j], arr[i][j - 1]):
                lcs += str1[i - 1]
                i -= 1
                j -= 1
            elif length == arr[i - 1][j]:
                i -= 1
            else:
                j -= 1

        print(lcs[::-1])

main()



# 57628 KB / 208 ms
def main():
    str1 = input()
    str2 = input()
    len1, len2 = len(str1), len(str2)
    arr = [[0] * (len2+1) for _ in range(len1+1)]

    for i in range(len1):
        for j in range(len2):
            if str1[i] == str2[j]:
                arr[i+1][j+1] = arr[i][j] + 1
            else:
                arr[i+1][j+1] = max(arr[i][j+1], arr[i+1][j])

    len3 = arr[-1][-1]
    if len3 == 0:
        return 0


    lcs = ''
    i, j = len1, len2
    while i > 0 and j > 0:
        length = arr[i][j]
        if length != max(arr[i - 1][j], arr[i][j - 1]):
            lcs += str1[i - 1]
            i -= 1
            j -= 1
        elif length == arr[i - 1][j]:
            i -= 1
        else:
            j -= 1

    return f'{len3}\n{lcs[::-1]}'

print(main())




# 56604 KB / 212 ms
def main():
    str1 = input()
    str2 = input()
    len1, len2 = len(str1), len(str2)
    arr = [[0] * (len2+1) for _ in range(len1+1)]

    for i in range(len1):
        for j in range(len2):
            arr[i+1][j+1] = arr[i][j] + 1 if str1[i] == str2[j] else max(arr[i][j+1], arr[i+1][j])

    len3 = arr[-1][-1]
    if len3 == 0:
        return 0


    lcs = ''
    i, j = len1, len2
    while i > 0 and j > 0:
        length = arr[i][j]
        if length != max(arr[i - 1][j], arr[i][j - 1]):
            lcs += str1[i - 1]
            i -= 1
            j -= 1
        elif length == arr[i - 1][j]:
            i -= 1
        else:
            j -= 1

    return f'{len3}\n{lcs[::-1]}'

print(main())




# 57628 KB / 216 ms
def main():
    def calc_lcs_len():
        for i in range(len1):
            for j in range(len2):
                arr[i+1][j+1] = arr[i][j] + 1 if str1[i] == str2[j] else max(arr[i][j+1], arr[i+1][j])

        return arr[-1][-1]

    def find_lcs():
        result = ''
        i, j = len1, len2
        while i > 0 and j > 0:
            length = arr[i][j]
            if length != max(arr[i - 1][j], arr[i][j - 1]):
                result += str1[i - 1]
                i -= 1
                j -= 1
            elif length == arr[i - 1][j]:
                i -= 1
            else:
                j -= 1
        return result


    str1 = input()
    str2 = input()
    len1, len2 = len(str1), len(str2)
    arr = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    len3 = calc_lcs_len()
    if len3 == 0:
        return 0

    lcs = find_lcs()[::-1]

    return f'{len3}\n{lcs}'

print(main())