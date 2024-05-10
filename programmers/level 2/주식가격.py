# 240510
def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []

    for i in range(n):
        price = prices[i]
        while stack and stack[-1][0] > price:
            _, j = stack.pop()
            answer[j] = i - j
            if not stack:
                break
        stack.append((price, i))

    for i in range(len(stack)):
        _, j = stack[i]
        answer[j] = n - 1 - j

    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.05ms, 10.2MB)
테스트 3 〉	통과 (0.44ms, 10.3MB)
테스트 4 〉	통과 (0.38ms, 10.2MB)
테스트 5 〉	통과 (0.31ms, 10.1MB)
테스트 6 〉	통과 (0.03ms, 10.1MB)
테스트 7 〉	통과 (0.37ms, 10.2MB)
테스트 8 〉	통과 (0.24ms, 10.4MB)
테스트 9 〉	통과 (0.03ms, 10.1MB)
테스트 10 〉	통과 (0.61ms, 10.4MB)
효율성  테스트
테스트 1 〉	통과 (25.90ms, 18.7MB)
테스트 2 〉	통과 (19.23ms, 17.5MB)
테스트 3 〉	통과 (28.84ms, 19.4MB)
테스트 4 〉	통과 (22.10ms, 18.2MB)
테스트 5 〉	통과 (15.80ms, 16.8MB)
'''


#
def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []

    for i in range(n):
        price = prices[i]
        while stack and stack[-1][0] > price:
            j = stack.pop()[1]
            answer[j] = i - j

        stack.append((price, i))

    for i in range(len(stack)):
        j = stack[i][1]
        answer[j] = n - 1 - j

    return answer


'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.04ms, 10.2MB)
테스트 3 〉	통과 (0.24ms, 10.3MB)
테스트 4 〉	통과 (0.56ms, 10.4MB)
테스트 5 〉	통과 (0.55ms, 10.2MB)
테스트 6 〉	통과 (0.03ms, 10.3MB)
테스트 7 〉	통과 (0.33ms, 10.2MB)
테스트 8 〉	통과 (0.21ms, 10.1MB)
테스트 9 〉	통과 (0.02ms, 10.3MB)
테스트 10 〉	통과 (0.33ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (25.80ms, 18.8MB)
테스트 2 〉	통과 (19.81ms, 17.2MB)
테스트 3 〉	통과 (28.74ms, 19.2MB)
테스트 4 〉	통과 (22.73ms, 18.1MB)
테스트 5 〉	통과 (15.76ms, 16.7MB)
'''