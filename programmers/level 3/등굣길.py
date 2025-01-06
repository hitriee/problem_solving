# 240502
# 250106
def solution(m, n, puddles):
    cases = [[0] * m for _ in range(n)]
    div_num = int(1e9)+7

    for x, y in puddles:
        cases[y-1][x-1] = -1

    for x in range(1, m):
        if cases[0][x] == -1:
            break
        cases[0][x] = 1

    for y in range(1, n):
        if cases[y][0] == -1:
            break
        cases[y][0] = 1


    for y in range(1, n):
        for x in range(1, m):
            if cases[y][x] != -1:
                for before in (cases[y-1][x], cases[y][x-1]):
                    if before != -1:
                        cases[y][x] = (cases[y][x] + before) % div_num

    return cases[-1][-1]

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.4MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	통과 (0.04ms, 10.4MB)
테스트 5 〉	통과 (0.07ms, 10.3MB)
테스트 6 〉	통과 (0.05ms, 10.2MB)
테스트 7 〉	통과 (0.06ms, 10.2MB)
테스트 8 〉	통과 (0.12ms, 10.2MB)
테스트 9 〉	통과 (0.08ms, 10MB)
테스트 10 〉	통과 (0.02ms, 10.3MB)

효율성  테스트
테스트 1 〉	통과 (3.48ms, 10.3MB)
테스트 2 〉	통과 (1.46ms, 10.3MB)
테스트 3 〉	통과 (2.02ms, 10.3MB)
테스트 4 〉	통과 (2.78ms, 10.2MB)
테스트 5 〉	통과 (2.16ms, 10.3MB)
테스트 6 〉	통과 (3.83ms, 10.2MB)
테스트 7 〉	통과 (2.01ms, 10.3MB)
테스트 8 〉	통과 (2.64ms, 10.3MB)
테스트 9 〉	통과 (3.09ms, 10.2MB)
테스트 10 〉	통과 (2.76ms, 10.2MB)
'''