# 240501
def solution(topping):
    n, answer = len(topping), 0
    topping_of_right, has_topping_left = [0] * 10001, [False] * 10001
    for each in topping:
        topping_of_right[each] += 1

    left_kind, right_kind = 0, len(set(topping))

    for i in range(n - 1):
        each = topping[i]
        topping_of_right[each] -= 1
        if topping_of_right[each] == 0:
            right_kind -= 1

        if not has_topping_left[each]:
            left_kind += 1
            has_topping_left[each] = True

        if right_kind < left_kind:
            break
        elif right_kind == left_kind:
            answer += 1

    return answer

'''
테스트 1 〉	통과 (1.80ms, 10.6MB)
테스트 2 〉	통과 (28.24ms, 14.5MB)
테스트 3 〉	통과 (35.90ms, 10.9MB)
테스트 4 〉	통과 (52.12ms, 11MB)
테스트 5 〉	통과 (285.25ms, 18.7MB)
테스트 6 〉	통과 (218.79ms, 51.3MB)
테스트 7 〉	통과 (186.37ms, 51.2MB)
테스트 8 〉	통과 (242.37ms, 51.4MB)
테스트 9 〉	통과 (78.62ms, 50.4MB)
테스트 10 〉	통과 (76.34ms, 50.6MB)
테스트 11 〉	통과 (9.74ms, 11MB)
테스트 12 〉	통과 (2.47ms, 11.2MB)
테스트 13 〉	통과 (255.06ms, 50.4MB)
테스트 14 〉	통과 (297.11ms, 50.6MB)
테스트 15 〉	통과 (290.38ms, 50.5MB)
테스트 16 〉	통과 (282.41ms, 50.6MB)
테스트 17 〉	통과 (240.05ms, 50.6MB)
테스트 18 〉	통과 (244.53ms, 51.4MB)
테스트 19 〉	통과 (144.28ms, 51.3MB)
테스트 20 〉	통과 (120.92ms, 51.3MB)
'''



#
def solution(topping):
    n, answer = len(topping), 0
    topping_of_right, has_topping_on_left = [0] * 10001, [False] * 10001
    for each in topping:
        topping_of_right[each] += 1

    left_kind, right_kind = 0, len(set(topping))

    for i in range(n - 1):
        each = topping[i]
        topping_of_right[each] -= 1
        if topping_of_right[each] == 0:
            right_kind -= 1

        if not has_topping_on_left[each]:
            left_kind += 1
            has_topping_on_left[each] = True

        if right_kind == left_kind:
            answer += 1

    return answer

'''
테스트 1 〉	통과 (2.50ms, 10.3MB)
테스트 2 〉	통과 (24.34ms, 14.4MB)
테스트 3 〉	통과 (26.76ms, 10.9MB)
테스트 4 〉	통과 (26.82ms, 11MB)
테스트 5 〉	통과 (234.65ms, 18.7MB)
테스트 6 〉	통과 (318.03ms, 51.4MB)
테스트 7 〉	통과 (313.97ms, 51.4MB)
테스트 8 〉	통과 (314.46ms, 51.2MB)
테스트 9 〉	통과 (291.33ms, 50.7MB)
테스트 10 〉	통과 (251.84ms, 50.5MB)
테스트 11 〉	통과 (36.67ms, 10.8MB)
테스트 12 〉	통과 (4.83ms, 11.1MB)
테스트 13 〉	통과 (279.32ms, 50.5MB)
테스트 14 〉	통과 (339.54ms, 50.4MB)
테스트 15 〉	통과 (374.64ms, 50.6MB)
테스트 16 〉	통과 (293.02ms, 50.5MB)
테스트 17 〉	통과 (322.29ms, 50.6MB)
테스트 18 〉	통과 (318.37ms, 51.2MB)
테스트 19 〉	통과 (305.80ms, 51.3MB)
테스트 20 〉	통과 (301.49ms, 51.3MB)
'''


#
def solution(topping):
    n, answer = len(topping), 0
    topping_of_right, has_topping_on_left = [0] * 10001, [False] * 10001
    for each in topping:
        topping_of_right[each] += 1

    left_kind = right_kind = 0

    for i in range(10001):
        if topping_of_right[i]:
            right_kind += 1

    for i in range(n - 1):
        each = topping[i]
        topping_of_right[each] -= 1
        if topping_of_right[each] == 0:
            right_kind -= 1

        if not has_topping_on_left[each]:
            left_kind += 1
            has_topping_on_left[each] = True

        if right_kind < left_kind:
            break
        elif right_kind == left_kind:
            answer += 1

    return answer

'''
테스트 1 〉	통과 (3.51ms, 10.4MB)
테스트 2 〉	통과 (15.54ms, 13.8MB)
테스트 3 〉	통과 (35.05ms, 11MB)
테스트 4 〉	통과 (49.18ms, 11.1MB)
테스트 5 〉	통과 (249.80ms, 18.6MB)
테스트 6 〉	통과 (176.16ms, 51.2MB)
테스트 7 〉	통과 (173.00ms, 51.4MB)
테스트 8 〉	통과 (252.62ms, 51.3MB)
테스트 9 〉	통과 (61.88ms, 50.5MB)
테스트 10 〉	통과 (59.57ms, 50.6MB)
테스트 11 〉	통과 (10.68ms, 11.1MB)
테스트 12 〉	통과 (4.94ms, 10.4MB)
테스트 13 〉	통과 (267.55ms, 50.6MB)
테스트 14 〉	통과 (296.89ms, 50.5MB)
테스트 15 〉	통과 (281.11ms, 50.6MB)
테스트 16 〉	통과 (245.74ms, 50.5MB)
테스트 17 〉	통과 (186.43ms, 50.5MB)
테스트 18 〉	통과 (192.57ms, 51.3MB)
테스트 19 〉	통과 (128.21ms, 51.1MB)
테스트 20 〉	통과 (100.62ms, 51.3MB)
'''


#
def solution(topping):
    n, answer = len(topping), 0
    topping_of_right, has_topping_on_left = [0] * 10001, set()
    for each in topping:
        topping_of_right[each] += 1

    left_kind = right_kind = 0

    for i in range(10001):
        if topping_of_right[i]:
            right_kind += 1

    for i in range(n - 1):
        each = topping[i]
        topping_of_right[each] -= 1
        if topping_of_right[each] == 0:
            right_kind -= 1

        if each not in has_topping_on_left:
            left_kind += 1
            has_topping_on_left.add(each)

        if right_kind < left_kind:
            break
        elif right_kind == left_kind:
            answer += 1

    return answer

'''
정확성  테스트
테스트 1 〉	통과 (3.54ms, 10.4MB)
테스트 2 〉	통과 (19.86ms, 14.3MB)
테스트 3 〉	통과 (29.14ms, 10.9MB)
테스트 4 〉	통과 (29.25ms, 10.9MB)
테스트 5 〉	통과 (278.70ms, 18.7MB)
테스트 6 〉	통과 (282.15ms, 51.2MB)
테스트 7 〉	통과 (301.57ms, 51.3MB)
테스트 8 〉	통과 (311.17ms, 51.2MB)
테스트 9 〉	통과 (70.13ms, 50.5MB)
테스트 10 〉	통과 (78.63ms, 50.6MB)
테스트 11 〉	통과 (13.27ms, 10.9MB)
테스트 12 〉	통과 (5.86ms, 11.1MB)
테스트 13 〉	통과 (362.73ms, 50.4MB)
테스트 14 〉	통과 (325.73ms, 50.5MB)
테스트 15 〉	통과 (344.75ms, 50.6MB)
테스트 16 〉	통과 (241.62ms, 50.5MB)
테스트 17 〉	통과 (195.24ms, 50.5MB)
테스트 18 〉	통과 (251.96ms, 51.4MB)
테스트 19 〉	통과 (165.58ms, 51.3MB)
테스트 20 〉	통과 (122.69ms, 51.4MB)
'''