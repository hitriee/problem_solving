# 250512
def solution(targets):
    N = len(targets)
    targets.sort(key=lambda target: (target[1], target[0]))
    i = cnt = 0

    while i < N:
        s, e = targets[i]
        j = i + 1
        while j < N:
            ns, ne = targets[j]
            if ns >= e:
                break
            j += 1

        cnt += 1

        i = j

    return cnt

'''
테스트 1 〉	통과 (0.01ms, 9.09MB)
테스트 2 〉	통과 (0.04ms, 9.23MB)
테스트 3 〉	통과 (0.04ms, 9.13MB)
테스트 4 〉	통과 (0.51ms, 9.53MB)
테스트 5 〉	통과 (6.48ms, 11.4MB)
테스트 6 〉	통과 (100.90ms, 31.4MB)
테스트 7 〉	통과 (779.59ms, 121MB)
테스트 8 〉	통과 (821.65ms, 121MB)
테스트 9 〉	통과 (712.49ms, 108MB)
테스트 10 〉	통과 (803.67ms, 98.5MB)
테스트 11 〉	통과 (0.00ms, 9.18MB)
'''


#
def solution(targets):
    N = len(targets)
    targets.sort(key=lambda target: (target[1], target[0]))
    i = cnt = 0

    while True:
        s, e = targets[i]
        cnt += 1
        j = i + 1
        while j < N:
            ns, ne = targets[j]
            if ns >= e:
                break
            j += 1
        else:
            break

        i = j

    return cnt
'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 9.13MB)
테스트 2 〉	통과 (0.02ms, 9.12MB)
테스트 3 〉	통과 (0.06ms, 9.26MB)
테스트 4 〉	통과 (0.53ms, 9.34MB)
테스트 5 〉	통과 (7.50ms, 11.5MB)
테스트 6 〉	통과 (171.26ms, 31.5MB)
테스트 7 〉	통과 (946.24ms, 121MB)
테스트 8 〉	통과 (914.58ms, 121MB)
테스트 9 〉	통과 (730.35ms, 108MB)
테스트 10 〉	통과 (971.26ms, 98.6MB)
테스트 11 〉	통과 (0.00ms, 9.15MB)
'''



def solution(targets):
    N = len(targets)
    targets.sort(key=lambda target: (target[1], target[0]))
    i = cnt = 0

    while i < N:
        cnt += 1
        s, e = targets[i]
        for j in range(i+1, N):
            ns, ne = targets[j]
            if ns >= e:
                i = j
                break
        else:
            break

    return cnt


'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 9.17MB)
테스트 2 〉	통과 (0.03ms, 9.15MB)
테스트 3 〉	통과 (0.05ms, 9.27MB)
테스트 4 〉	통과 (0.56ms, 9.43MB)
테스트 5 〉	통과 (6.90ms, 11.3MB)
테스트 6 〉	통과 (117.92ms, 31.6MB)
테스트 7 〉	통과 (824.72ms, 121MB)
테스트 8 〉	통과 (941.04ms, 121MB)
테스트 9 〉	통과 (846.72ms, 108MB)
테스트 10 〉	통과 (831.64ms, 98.6MB)
테스트 11 〉	통과 (0.00ms, 9.14MB)
'''


#
def solution(targets):
    N = len(targets)
    targets.sort(key=lambda target: (target[1], target[0]))
    i = cnt = 0

    while i < N:
        s, e = targets[i]
        cnt += 1
        j = i + 1
        while j < N:
            if targets[j][0] >= e:
                break
            j += 1

        i = j

    return cnt
'''
테스트 1 〉	통과 (0.01ms, 9.12MB)
테스트 2 〉	통과 (0.02ms, 9.08MB)
테스트 3 〉	통과 (0.04ms, 9.07MB)
테스트 4 〉	통과 (0.90ms, 9.56MB)
테스트 5 〉	통과 (6.56ms, 11.3MB)
테스트 6 〉	통과 (141.07ms, 31.5MB)
테스트 7 〉	통과 (762.49ms, 121MB)
테스트 8 〉	통과 (973.15ms, 121MB)
테스트 9 〉	통과 (629.15ms, 108MB)
테스트 10 〉	통과 (895.32ms, 98.5MB)
테스트 11 〉	통과 (0.00ms, 9.02MB)
'''