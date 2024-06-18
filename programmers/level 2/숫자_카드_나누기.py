# 240618
def find_gcd(num1, num2):
    while num1:
        num1, num2 = num2 % num1, num1
    return num2


def solution(arrayA, arrayB):
    length = len(arrayA)
    if set(arrayA) & set(arrayB):
        return 0
    if length == 1:
        return max(*arrayA, *arrayB)

    arrayA.sort()
    arrayB.sort()
    gcd1 = find_gcd(*arrayA[:2])

    for i in range(2, length):
        gcd1 = find_gcd(gcd1, arrayA[i])

    gcd2 = find_gcd(*arrayB[:2])

    for i in range(2, length):
        gcd2 = find_gcd(gcd2, arrayB[i])

    if gcd1 == gcd2:
        return 0

    gcd = 0
    for i in range(length):
        if arrayB[i] % gcd1 == 0:
            break
    else:
        gcd = gcd1

    for i in range(length):
        if arrayA[i] % gcd2 == 0:
            break
    else:
        gcd = max(gcd, gcd2)

    return gcd