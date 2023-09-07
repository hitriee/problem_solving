#230907
N = int(input())
numbers = list(map(int, input().split()))
total = [0] * 21
total[numbers[0]] = 1

for i in range(1, N-1):
    next_total = [0] * 21
    number = numbers[i]
    for j in range(21):
        plus, minus, before = j+number, j-number, total[j]
        if minus >= 0:
            next_total[minus] += before
        if plus <= 20:
            next_total[plus] += before

    total = next_total[:]

print(total[numbers[-1]])



#
N = int(input())
numbers = list(map(int, input().split()))
total = [0] * 21
total[numbers[0]] = 1

for i in range(1, N-1):
    next_total = [0] * 21
    number = numbers[i]
    for j in range(21):
        plus, minus, before = j+number, j-number, total[j]
        if minus >= 0:
            next_total[minus] += before
        if plus <= 20:
            next_total[plus] += before

    for j in range(21):
        total[j] = next_total[j]

print(total[numbers[-1]])


#
def cnt_right_formula():
    N = int(input())
    numbers = list(map(int, input().split()))
    total = [0] * 21
    total[numbers[0]] = 1

    for i in range(1, N - 1):
        next_total = [0] * 21
        number = numbers[i]
        for j in range(21):
            plus, minus, before = j + number, j - number, total[j]
            if minus >= 0:
                next_total[minus] += before
            if plus <= 20:
                next_total[plus] += before

        for j in range(21):
            total[j] = next_total[j]

    return total[numbers[-1]]

print(cnt_right_formula())