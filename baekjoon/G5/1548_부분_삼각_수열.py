# 230921
N = int(input())
if N < 3:
    print(N)
else:
    B = list(map(int, input().split()))
    B.sort()
    max_length = 2

    for i in range(N):
        for j in range(i+1, N):
            k = j+1
            length = 2
            min_sum = B[i]+B[j]
            while k < N:
                if min_sum <= B[k]:
                    break
                length += 1
                k += 1
            if length > max_length:
                max_length = length

    print(max_length)


#
def find_max_length():
    N = int(input())
    if N < 3:
        return N

    B = list(map(int, input().split()))
    B.sort()
    max_length = 2

    for i in range(N):
        for j in range(i + 1, N):
            k = j + 1
            length = 2
            min_sum = B[i] + B[j]
            while k < N:
                if min_sum <= B[k]:
                    break
                length += 1
                k += 1
            if length > max_length:
                max_length = length

    return max_length

print(find_max_length())


#
def find_max_length():
    N = int(input())
    if N < 3:
        return N

    B = list(map(int, input().split()))
    B.sort()
    max_length = 2

    for i in range(N):
        for j in range(i + 1, N):
            length = 2
            min_sum = B[i] + B[j]
            for k in range(j+1, N):
                if min_sum <= B[k]:
                    break
                length += 1
            if length > max_length:
                max_length = length

    return max_length

print(find_max_length())


#
def find_max_length():
    N = int(input())
    if N < 3:
        return N

    B = list(map(int, input().split()))
    B.sort()
    max_length = 2

    for i in range(N-2):
        for j in range(i + 1, N-1):
            length = 2
            min_sum = B[i] + B[j]
            for k in range(j+1, N):
                if min_sum <= B[k]:
                    break
                length += 1
            if length > max_length:
                max_length = length

    return max_length

print(find_max_length())


#
def find_max_length():
    N = int(input())
    if N < 3:
        return N

    B = list(map(int, input().split()))
    B.sort()
    max_length = 2

    for i in range(N):
        for j in range(i + 1, N):
            if N-j+1 <= max_length:
                break
            length = 2
            min_sum = B[i] + B[j]
            for k in range(j+1, N):
                if min_sum <= B[k]:
                    break
                length += 1
            if length > max_length:
                max_length = length

    return max_length

print(find_max_length())