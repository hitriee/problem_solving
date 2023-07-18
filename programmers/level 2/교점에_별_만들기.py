#230718
def solution(line):
    from math import isclose
    answer = set()
    length = len(line)
    for i in range(length-1):
        a, b, e = line[i]
        for j in range(i+1, length):
            c, d, f = line[j]
            if a*d != b*c:
                bottom = a*d - b*c
                x, y = (b*f - e*d)/bottom, (e*c - a*f)/bottom
                int_x, int_y = int(x), int(y)
                if isclose(x, int_x, abs_tol=1e-9) and isclose(y, int_y, abs_tol=1e-9):
                    answer.add((int_x, int_y))

    if len(answer) == 1:
        return ['*']

    x_list, y_list = [], []
    for x, y in answer:
        x_list.append(x)
        y_list.append(y)

    min_x = min(x_list)
    dif_x = max(x_list) - min_x + 1
    max_y = max(y_list)
    dif_y = max_y - min(y_list) + 1

    min_rectangle = [['.']*dif_x for _ in range(dif_y)]
    for x, y in answer:
        min_rectangle[-(y-max_y)][x-min_x] = '*'
    for i in range(dif_y):
        min_rectangle[i] = ''.join(min_rectangle[i])

    return min_rectangle

solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]])
solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]])
solution([[1, -1, 0], [2, -1, 0]])
solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]])
'''
정확성  테스트
테스트 1 〉	통과 (0.14ms, 10.3MB)
테스트 2 〉	통과 (3.98ms, 12.2MB)
테스트 3 〉	통과 (0.10ms, 10.3MB)
테스트 4 〉	통과 (8.07ms, 14MB)
테스트 5 〉	통과 (2.09ms, 11.4MB)
테스트 6 〉	통과 (0.67ms, 10.4MB)
테스트 7 〉	통과 (3.26ms, 11.9MB)
테스트 8 〉	통과 (0.06ms, 10.3MB)
테스트 9 〉	통과 (214.53ms, 10.7MB)
테스트 10 〉	통과 (238.38ms, 10.4MB)
테스트 11 〉	통과 (262.34ms, 10.5MB)
테스트 12 〉	통과 (326.55ms, 10.5MB)
테스트 13 〉	통과 (351.95ms, 10.9MB)
테스트 14 〉	통과 (298.39ms, 11.1MB)
테스트 15 〉	통과 (279.33ms, 10.4MB)
테스트 16 〉	통과 (242.02ms, 10.4MB)
테스트 17 〉	통과 (322.48ms, 11MB)
테스트 18 〉	통과 (276.04ms, 11.2MB)
테스트 19 〉	통과 (270.46ms, 10.4MB)
테스트 20 〉	통과 (213.83ms, 10.4MB)
테스트 21 〉	통과 (216.63ms, 11.7MB)
테스트 22 〉	통과 (0.08ms, 10.4MB)
테스트 23 〉	통과 (0.08ms, 10.3MB)
테스트 24 〉	통과 (0.02ms, 10.3MB)
테스트 25 〉	통과 (0.06ms, 10.2MB)
테스트 26 〉	통과 (0.18ms, 10.3MB)
테스트 27 〉	통과 (0.01ms, 10.2MB)
테스트 28 〉	통과 (0.03ms, 10.3MB)
테스트 29 〉	통과 (0.01ms, 10.3MB)
'''

#
def solution(line):
    from math import isclose
    answer = set()
    length = len(line)
    for i in range(length-1):
        a, b, e = line[i]
        for j in range(i+1, length):
            c, d, f = line[j]
            if a*d != b*c:
                bottom = a*d - b*c
                x, y = (b*f - e*d)/bottom, (e*c - a*f)/bottom
                int_x, int_y = int(x), int(y)
                if isclose(x, int_x, abs_tol=1e-9) and isclose(y, int_y, abs_tol=1e-9):
                    answer.add((int_x, int_y))

    if len(answer) == 1:
        return ['*']

    x_list, y_list = [], []
    for x, y in answer:
        x_list.append(x)
        y_list.append(y)

    min_x = min(x_list)
    dif_x = max(x_list) - min_x + 1
    max_y = max(y_list)
    dif_y = max_y - min(y_list) + 1

    def convert_x_y(dot):
        x, y = dot
        return (x-min_x , -(y-max_y))

    answer = set(map(convert_x_y, answer))

    min_rectangle = []
    for i in range(dif_y):
        min_rectangle.append(''.join(['*' if (j, i) in answer else '.' for j in range(dif_x)]))

    return min_rectangle

'''
정확성  테스트
테스트 1 〉	통과 (0.33ms, 10.3MB)
테스트 2 〉	통과 (19.44ms, 10.7MB)
테스트 3 〉	통과 (0.10ms, 10.3MB)
테스트 4 〉	통과 (41.98ms, 11.6MB)
테스트 5 〉	통과 (11.44ms, 10.7MB)
테스트 6 〉	통과 (3.32ms, 10.3MB)
테스트 7 〉	통과 (18.23ms, 10.7MB)
테스트 8 〉	통과 (0.15ms, 10.5MB)
테스트 9 〉	통과 (254.15ms, 10.5MB)
테스트 10 〉	통과 (318.31ms, 10.5MB)
테스트 11 〉	통과 (305.79ms, 10.5MB)
테스트 12 〉	통과 (342.17ms, 10.5MB)
테스트 13 〉	통과 (354.86ms, 10.5MB)
테스트 14 〉	통과 (323.48ms, 10.8MB)
테스트 15 〉	통과 (278.20ms, 10.3MB)
테스트 16 〉	통과 (262.48ms, 10.4MB)
테스트 17 〉	통과 (350.38ms, 10.6MB)
테스트 18 〉	통과 (308.77ms, 10.6MB)
테스트 19 〉	통과 (356.91ms, 10.5MB)
테스트 20 〉	통과 (246.03ms, 10.4MB)
테스트 21 〉	통과 (356.37ms, 10.8MB)
테스트 22 〉	통과 (0.10ms, 10.4MB)
테스트 23 〉	통과 (0.08ms, 10.4MB)
테스트 24 〉	통과 (0.04ms, 10.3MB)
테스트 25 〉	통과 (0.13ms, 10.4MB)
테스트 26 〉	통과 (0.16ms, 10.4MB)
테스트 27 〉	통과 (0.01ms, 10.3MB)
테스트 28 〉	통과 (0.04ms, 10.2MB)
테스트 29 〉	통과 (0.02ms, 10.2MB)
'''