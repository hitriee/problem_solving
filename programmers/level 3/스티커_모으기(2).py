#230717
def solution(sticker):
    length = len(sticker)
    if length <= 3:
        return max(sticker)

    cases = []
    for start, end, step in (0, length - 1, 1), (length-1, 0, -1), (1, length, 1):
        cases.append([[sticker[i], 0] for i in range(start, end, step)])

    max_value = 0
    for j in range(3):
        case = cases[j]
        case[1][1] = case[0][0]
        for i in range(2, length - 1):
            case[i][0] += max(case[i-1][1], *case[i-2])
            case[i][1] += max(case[i-1][0], *case[i-2])

        max_value = max(*case[-1], *case[-2], max_value)

    return max_value

'''
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.00ms, 10.4MB)
테스트 3 〉	통과 (0.03ms, 10.2MB)
테스트 4 〉	통과 (0.03ms, 10.1MB)
테스트 5 〉	통과 (0.03ms, 10.2MB)
테스트 6 〉	통과 (0.08ms, 10.2MB)
테스트 7 〉	통과 (5.59ms, 10.7MB)
테스트 8 〉	통과 (2.79ms, 10.5MB)
테스트 9 〉	통과 (3.09ms, 10.6MB)
테스트 10 〉	통과 (2.96ms, 10.5MB)
테스트 11 〉	통과 (2.85ms, 10.6MB)
테스트 12 〉	통과 (2.92ms, 10.5MB)
테스트 13 〉	통과 (5.66ms, 10.5MB)
테스트 14 〉	통과 (5.08ms, 10.6MB)
테스트 15 〉	통과 (3.63ms, 10.5MB)
테스트 16 〉	통과 (4.92ms, 10.5MB)
테스트 17 〉	통과 (4.74ms, 10.4MB)
테스트 18 〉	통과 (3.04ms, 10.6MB)
테스트 19 〉	통과 (2.84ms, 10.4MB)
테스트 20 〉	통과 (2.91ms, 10.6MB)
테스트 21 〉	통과 (2.82ms, 10.4MB)
테스트 22 〉	통과 (2.83ms, 10.4MB)
테스트 23 〉	통과 (3.01ms, 10.4MB)
테스트 24 〉	통과 (2.97ms, 10.4MB)
테스트 25 〉	통과 (4.45ms, 10.4MB)
테스트 26 〉	통과 (4.83ms, 10.5MB)
테스트 27 〉	통과 (5.55ms, 10.5MB)
테스트 28 〉	통과 (4.91ms, 10.5MB)
테스트 29 〉	통과 (2.80ms, 10.3MB)
테스트 30 〉	통과 (5.46ms, 10.4MB)
테스트 31 〉	통과 (5.59ms, 10.5MB)
테스트 32 〉	통과 (2.81ms, 10.5MB)
테스트 33 〉	통과 (0.00ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (296.47ms, 54.8MB)
테스트 2 〉	통과 (303.03ms, 54.7MB)
테스트 3 〉	통과 (296.56ms, 55MB)
테스트 4 〉	통과 (317.03ms, 54.8MB)
'''


solution([14, 6, 5, 11, 3, 9, 2, 10])
solution([1, 9, 2, 5, 8])
solution([9, 3, 2, 5, 8])


#
def solution(sticker):
    length = len(sticker)
    if length <= 3:
        return max(sticker)

    cases = []
    for start, end in (0, length - 1), (1, length):
        cases.append([[sticker[i], 0] for i in range(start, end)])

    max_value = 0
    for j in range(2):
        case = cases[j]
        case[1][1] = case[0][0]
        for i in range(2, length - 1):
            case[i][0] += max(case[i-1][1], *case[i-2])
            case[i][1] += max(case[i-1][0], *case[i-2])

        max_value = max(*case[-1], *case[-2], max_value)

    return max_value

'''
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.03ms, 10.2MB)
테스트 4 〉	통과 (0.04ms, 10.2MB)
테스트 5 〉	통과 (0.04ms, 10.2MB)
테스트 6 〉	통과 (0.05ms, 10.2MB)
테스트 7 〉	통과 (5.25ms, 10.4MB)
테스트 8 〉	통과 (1.99ms, 10.2MB)
테스트 9 〉	통과 (3.57ms, 10.3MB)
테스트 10 〉	통과 (1.99ms, 10.2MB)
테스트 11 〉	통과 (2.53ms, 10.2MB)
테스트 12 〉	통과 (2.81ms, 10.2MB)
테스트 13 〉	통과 (1.95ms, 10.3MB)
테스트 14 〉	통과 (1.98ms, 10.3MB)
테스트 15 〉	통과 (3.74ms, 10.2MB)
테스트 16 〉	통과 (3.77ms, 10.4MB)
테스트 17 〉	통과 (1.86ms, 10.4MB)
테스트 18 〉	통과 (1.89ms, 10.4MB)
테스트 19 〉	통과 (1.97ms, 10.3MB)
테스트 20 〉	통과 (3.53ms, 10.4MB)
테스트 21 〉	통과 (3.69ms, 10.4MB)
테스트 22 〉	통과 (3.71ms, 10.2MB)
테스트 23 〉	통과 (3.37ms, 10.4MB)
테스트 24 〉	통과 (2.89ms, 10.2MB)
테스트 25 〉	통과 (3.73ms, 10.2MB)
테스트 26 〉	통과 (2.64ms, 10.4MB)
테스트 27 〉	통과 (3.52ms, 10.3MB)
테스트 28 〉	통과 (2.10ms, 10.3MB)
테스트 29 〉	통과 (3.73ms, 10.2MB)
테스트 30 〉	통과 (3.37ms, 10.1MB)
테스트 31 〉	통과 (2.00ms, 10.4MB)
테스트 32 〉	통과 (1.85ms, 10.2MB)
테스트 33 〉	통과 (0.00ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (192.37ms, 40.2MB)
테스트 2 〉	통과 (213.76ms, 40.2MB)
테스트 3 〉	통과 (204.70ms, 40.2MB)
테스트 4 〉	통과 (217.39ms, 40.2MB)
'''


#
def solution(sticker):
    length = len(sticker)
    if length <= 3:
        return max(sticker)

    cases = []
    for start, end in (0, length - 1), (1, length):
        cases.append([[sticker[i], 0] for i in range(start, end)])

    max_value = 0
    for j in range(2):
        case = cases[j]
        case[1][1] = case[0][0]
        for i in range(2, length - 1):
            case[i][0] += max(case[i-1][1], *case[i-2])
            case[i][1] += max(case[i-1][0], *case[i-2])

        temp_max = max(*case[-1], *case[-2])
        if temp_max > max_value:
            max_value = temp_max

    return max_value

'''
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.3MB)
테스트 2 〉	통과 (0.00ms, 10.1MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.03ms, 10.3MB)
테스트 6 〉	통과 (0.05ms, 10.2MB)
테스트 7 〉	통과 (2.09ms, 10.3MB)
테스트 8 〉	통과 (1.85ms, 10.1MB)
테스트 9 〉	통과 (2.16ms, 10.1MB)
테스트 10 〉	통과 (2.86ms, 10.2MB)
테스트 11 〉	통과 (1.99ms, 10.3MB)
테스트 12 〉	통과 (3.45ms, 10.2MB)
테스트 13 〉	통과 (3.32ms, 10.3MB)
테스트 14 〉	통과 (2.06ms, 10.1MB)
테스트 15 〉	통과 (3.58ms, 10.3MB)
테스트 16 〉	통과 (1.90ms, 10.2MB)
테스트 17 〉	통과 (3.27ms, 10.2MB)
테스트 18 〉	통과 (2.25ms, 10.2MB)
테스트 19 〉	통과 (3.64ms, 10.1MB)
테스트 20 〉	통과 (3.21ms, 10.2MB)
테스트 21 〉	통과 (3.60ms, 10.4MB)
테스트 22 〉	통과 (3.53ms, 10.3MB)
테스트 23 〉	통과 (4.16ms, 10.2MB)
테스트 24 〉	통과 (1.98ms, 10.2MB)
테스트 25 〉	통과 (3.44ms, 10.4MB)
테스트 26 〉	통과 (1.98ms, 10.2MB)
테스트 27 〉	통과 (1.86ms, 10.2MB)
테스트 28 〉	통과 (1.96ms, 10.3MB)
테스트 29 〉	통과 (2.39ms, 10.3MB)
테스트 30 〉	통과 (3.80ms, 10.4MB)
테스트 31 〉	통과 (1.99ms, 10.2MB)
테스트 32 〉	통과 (2.01ms, 10.3MB)
테스트 33 〉	통과 (0.00ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (219.29ms, 40.1MB)
테스트 2 〉	통과 (202.95ms, 40.2MB)
테스트 3 〉	통과 (209.09ms, 40.2MB)
테스트 4 〉	통과 (204.48ms, 40.3MB)
'''

#
def solution(sticker):
    length = len(sticker)
    if length <= 3:
        return max(sticker)

    cases = []
    for start, end in (0, length - 1), (1, length):
        cases.append([[sticker[i], 0] for i in range(start, end)])

    max_value = 0
    for j in range(2):
        case = cases[j]
        case[1][1] = case[0][0]
        for i in range(2, length - 1):
            case[i][0] += max(case[i-1][1], *case[i-2])
            case[i][1] += max(case[i-1][0], *case[i-2])

        max_value = max(*case[-1], max_value)

    return max_value

'''
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.1MB)
테스트 2 〉	통과 (0.00ms, 10.1MB)
테스트 3 〉	통과 (0.04ms, 10.2MB)
테스트 4 〉	통과 (0.04ms, 10.2MB)
테스트 5 〉	통과 (0.04ms, 10.2MB)
테스트 6 〉	통과 (0.03ms, 10.1MB)
테스트 7 〉	통과 (2.54ms, 10.3MB)
테스트 8 〉	통과 (2.15ms, 10.2MB)
테스트 9 〉	통과 (3.35ms, 10.2MB)
테스트 10 〉	통과 (3.16ms, 10MB)
테스트 11 〉	통과 (3.51ms, 10.2MB)
테스트 12 〉	통과 (3.02ms, 10.3MB)
테스트 13 〉	통과 (4.26ms, 10.3MB)
테스트 14 〉	통과 (3.24ms, 10.4MB)
테스트 15 〉	통과 (2.66ms, 10.1MB)
테스트 16 〉	통과 (2.35ms, 10.2MB)
테스트 17 〉	통과 (3.35ms, 10.2MB)
테스트 18 〉	통과 (3.21ms, 10.1MB)
테스트 19 〉	통과 (2.68ms, 10.1MB)
테스트 20 〉	통과 (3.51ms, 10.3MB)
테스트 21 〉	통과 (1.84ms, 10.4MB)
테스트 22 〉	통과 (3.78ms, 10.2MB)
테스트 23 〉	통과 (2.50ms, 10.3MB)
테스트 24 〉	통과 (1.96ms, 10.2MB)
테스트 25 〉	통과 (3.48ms, 10.1MB)
테스트 26 〉	통과 (3.63ms, 10.3MB)
테스트 27 〉	통과 (3.58ms, 10.2MB)
테스트 28 〉	통과 (2.20ms, 10.4MB)
테스트 29 〉	통과 (2.24ms, 10.4MB)
테스트 30 〉	통과 (2.46ms, 10.2MB)
테스트 31 〉	통과 (2.21ms, 10.2MB)
테스트 32 〉	통과 (3.69ms, 10.4MB)
테스트 33 〉	통과 (0.00ms, 10.1MB)
효율성  테스트
테스트 1 〉	통과 (206.61ms, 40.1MB)
테스트 2 〉	통과 (214.94ms, 40.1MB)
테스트 3 〉	통과 (205.61ms, 40.2MB)
테스트 4 〉	통과 (198.08ms, 40.1MB)
'''