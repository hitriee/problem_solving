# 241213
def solution(sequence):
    acc = [[0], [0]]
    minus_i = 0

    for num in sequence:
        acc[minus_i].append(acc[minus_i][-1] - num)
        acc[1-minus_i].append(acc[1-minus_i][-1] + num)
        minus_i ^= 1

    max1, max2 = max(acc[0]), max(acc[1])
    min1, min2 = min(acc[0]), min(acc[1])

    answer = max(max1 - min1, max2 - min2)
    return answer