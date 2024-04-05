# 240405
def solution(p):
    n = len(p)

    def change_answer(length, target):
        if target == '':
            return ''

        open_cnt = close_cnt = 0
        for i in range(length):
            bracket = target[i]
            if bracket == '(':
                open_cnt += 1
            else:
                close_cnt += 1

            # u 찾음
            if open_cnt == close_cnt:
                u, v = target[:i + 1], target[i + 1:]
                # 올바른 문자열
                if bracket == ')':
                    # u + 새 u
                    return u + change_answer(length - i, v)
                else:
                    new_val = f'({change_answer(length - i, v)})'

                    for j in range(1, i):
                        if u[j] == ')':
                            new_val += '('
                        else:
                            new_val += ')'

                    return new_val

    return change_answer(n, p)
'''
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.4MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.02ms, 10.3MB)
테스트 8 〉	통과 (0.01ms, 10.1MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.01ms, 10.3MB)
테스트 11 〉	통과 (0.02ms, 10.3MB)
테스트 12 〉	통과 (0.04ms, 10.4MB)
테스트 13 〉	통과 (0.03ms, 10.1MB)
테스트 14 〉	통과 (0.04ms, 10.1MB)
테스트 15 〉	통과 (0.06ms, 10.1MB)
테스트 16 〉	통과 (0.14ms, 10.2MB)
테스트 17 〉	통과 (0.10ms, 10.2MB)
테스트 18 〉	통과 (0.14ms, 10.2MB)
테스트 19 〉	통과 (0.26ms, 10.2MB)
테스트 20 〉	통과 (0.19ms, 10.2MB)
테스트 21 〉	통과 (0.33ms, 10.3MB)
테스트 22 〉	통과 (0.19ms, 10.2MB)
테스트 23 〉	통과 (0.16ms, 10.3MB)
테스트 24 〉	통과 (0.06ms, 10.3MB)
테스트 25 〉	통과 (0.09ms, 10.2MB)
'''


#
def change_answer(length, target):
    if target == '':
        return ''

    open_cnt = close_cnt = 0
    for i in range(length):
        bracket = target[i]
        if bracket == '(':
            open_cnt += 1
        else:
            close_cnt += 1

        # u 찾음
        if open_cnt == close_cnt:
            u, v = target[:i + 1], target[i + 1:]
            # 올바른 문자열
            if bracket == ')':
                # u + 새 u
                return u + change_answer(length - i, v)
            else:
                new_val = f'({change_answer(length - i, v)})'

                for j in range(1, i):
                    if u[j] == ')':
                        new_val += '('
                    else:
                        new_val += ')'

                return new_val


def solution(p):
    return change_answer(len(p), p)

'''
테스트 1 〉	통과 (0.03ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.1MB)
테스트 7 〉	통과 (0.01ms, 10.3MB)
테스트 8 〉	통과 (0.01ms, 10.4MB)
테스트 9 〉	통과 (0.01ms, 10.4MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.03ms, 10.1MB)
테스트 12 〉	통과 (0.03ms, 10.2MB)
테스트 13 〉	통과 (0.03ms, 10.4MB)
테스트 14 〉	통과 (0.05ms, 10.1MB)
테스트 15 〉	통과 (0.08ms, 10.4MB)
테스트 16 〉	통과 (0.13ms, 10.2MB)
테스트 17 〉	통과 (0.10ms, 10.2MB)
테스트 18 〉	통과 (0.14ms, 10.3MB)
테스트 19 〉	통과 (0.26ms, 10.2MB)
테스트 20 〉	통과 (0.33ms, 10.2MB)
테스트 21 〉	통과 (0.36ms, 10.3MB)
테스트 22 〉	통과 (0.10ms, 10.2MB)
테스트 23 〉	통과 (0.29ms, 10.2MB)
테스트 24 〉	통과 (0.06ms, 10.4MB)
테스트 25 〉	통과 (0.09ms, 10.2MB)
'''



#
def solution(p):
    def change_answer(length, target):
        if target == '':
            return ''

        open_cnt = close_cnt = 0
        for i in range(length):
            bracket = target[i]
            if bracket == '(':
                open_cnt += 1
            else:
                close_cnt += 1

            # u 찾음
            if open_cnt == close_cnt:
                u, v = target[:i + 1], target[i + 1:]
                new_u = change_answer(length - i, v)
                # 올바른 문자열
                if bracket == ')':
                    # u + 새 u
                    return u + new_u
                else:
                    new_val = f'({new_u})'

                    for j in range(1, i):
                        if u[j] == ')':
                            new_val += '('
                        else:
                            new_val += ')'

                    return new_val

    return change_answer(len(p), p)

'''
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 10MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.4MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.02ms, 10.1MB)
테스트 12 〉	통과 (0.05ms, 10.2MB)
테스트 13 〉	통과 (0.03ms, 10.2MB)
테스트 14 〉	통과 (0.05ms, 10.2MB)
테스트 15 〉	통과 (0.07ms, 10.2MB)
테스트 16 〉	통과 (0.23ms, 10.3MB)
테스트 17 〉	통과 (0.10ms, 10.2MB)
테스트 18 〉	통과 (0.26ms, 10.2MB)
테스트 19 〉	통과 (0.51ms, 10.3MB)
테스트 20 〉	통과 (0.20ms, 10.3MB)
테스트 21 〉	통과 (0.34ms, 10.3MB)
테스트 22 〉	통과 (0.10ms, 10.1MB)
테스트 23 〉	통과 (0.31ms, 10.2MB)
테스트 24 〉	통과 (0.06ms, 10.3MB)
테스트 25 〉	통과 (0.10ms, 10.2MB)
'''



#
def solution(p):
    def convert(bracket):
        return ')' if bracket == '(' else '('

    def change_answer(length, target):
        if target == '':
            return ''

        open_cnt = close_cnt = 0
        for i in range(length):
            bracket = target[i]
            if bracket == '(':
                open_cnt += 1
            else:
                close_cnt += 1

            # u 찾음
            if open_cnt == close_cnt:
                u, v = target[:i + 1], target[i + 1:]
                new_u = change_answer(length - i, v)
                # 올바른 문자열
                if bracket == ')':
                    return u + new_u

                return f'({new_u})' + ''.join(map(convert, u[1:i]))

    return change_answer(len(p), p)
'''
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.02ms, 10.1MB)
테스트 8 〉	통과 (0.01ms, 10.3MB)
테스트 9 〉	통과 (0.01ms, 10MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.03ms, 10.2MB)
테스트 12 〉	통과 (0.04ms, 10.2MB)
테스트 13 〉	통과 (0.04ms, 10.2MB)
테스트 14 〉	통과 (0.09ms, 10.2MB)
테스트 15 〉	통과 (0.07ms, 10.2MB)
테스트 16 〉	통과 (0.14ms, 10.3MB)
테스트 17 〉	통과 (0.16ms, 10.2MB)
테스트 18 〉	통과 (0.16ms, 10.2MB)
테스트 19 〉	통과 (0.51ms, 10.2MB)
테스트 20 〉	통과 (0.21ms, 10.3MB)
테스트 21 〉	통과 (0.20ms, 10.1MB)
테스트 22 〉	통과 (0.12ms, 10.3MB)
테스트 23 〉	통과 (0.18ms, 10.3MB)
테스트 24 〉	통과 (0.06ms, 10.3MB)
테스트 25 〉	통과 (0.10ms, 10.2MB)
'''