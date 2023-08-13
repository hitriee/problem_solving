#230809
def solution(n, times):
    start, end = 0, min(times)*n
    while start <= end:
        mid = (start + end)//2
        def div(num):
            return mid//num

        total_people = sum(map(div, times))
        if total_people >= n:
            end = mid - 1
        else:
            start = mid + 1

    return start
'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.20ms, 10.2MB)
테스트 3 〉	통과 (4.91ms, 10.2MB)
테스트 4 〉	통과 (213.47ms, 13.9MB)
테스트 5 〉	통과 (587.21ms, 14.1MB)
테스트 6 〉	통과 (394.97ms, 14MB)
테스트 7 〉	통과 (517.82ms, 13.9MB)
테스트 8 〉	통과 (710.34ms, 14.3MB)
테스트 9 〉	통과 (0.03ms, 10.1MB)
'''

#
def solution(n, times):
    start, end = 0, min(times)*n
    while start <= end:
        mid = (start + end)//2
        total_people = 0
        for time in times:
            total_people += mid//time
        if total_people >= n:
            end = mid - 1
        else:
            start = mid + 1

    return start
'''
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.06ms, 10.2MB)
테스트 3 〉	통과 (3.86ms, 10.2MB)
테스트 4 〉	통과 (149.73ms, 14.2MB)
테스트 5 〉	통과 (462.93ms, 14.1MB)
테스트 6 〉	통과 (294.61ms, 14.1MB)
테스트 7 〉	통과 (406.94ms, 14.2MB)
테스트 8 〉	통과 (575.16ms, 14.3MB)
테스트 9 〉	통과 (0.02ms, 10.3MB)
'''

