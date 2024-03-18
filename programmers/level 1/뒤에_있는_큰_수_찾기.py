# 240318
def solution(numbers):
    n = len(numbers)
    answer = [-1] * n

    stack = [(0, numbers[0])]
    for i in range(1, n):
        number = numbers[i]
        if stack:
            while stack[-1][-1] < number:
                idx, _ = stack.pop()
                answer[idx] = number
                if not stack:
                    break
        stack.append((i, number))

    return answer

'''
테스트 1 〉	통과 (0.01ms, 10MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.05ms, 10.2MB)
테스트 5 〉	통과 (0.31ms, 10.1MB)
테스트 6 〉	통과 (3.15ms, 11.3MB)
테스트 7 〉	통과 (3.29ms, 11.4MB)
테스트 8 〉	통과 (15.61ms, 17MB)
테스트 9 〉	통과 (17.42ms, 17.1MB)
테스트 10 〉	통과 (37.39ms, 19.6MB)
테스트 11 〉	통과 (30.66ms, 19.6MB)
테스트 12 〉	통과 (67.38ms, 25.5MB)
테스트 13 〉	통과 (63.95ms, 25.4MB)
테스트 14 〉	통과 (152.93ms, 43.3MB)
테스트 15 〉	통과 (338.36ms, 75.4MB)
테스트 16 〉	통과 (364.63ms, 75.5MB)
테스트 17 〉	통과 (327.58ms, 75.4MB)
테스트 18 〉	통과 (322.47ms, 75.5MB)
테스트 19 〉	통과 (331.50ms, 75.5MB)
테스트 20 〉	통과 (434.43ms, 136MB)
테스트 21 〉	통과 (336.07ms, 173MB)
테스트 22 〉	통과 (319.85ms, 70.9MB)
테스트 23 〉	통과 (326.16ms, 173MB)
'''