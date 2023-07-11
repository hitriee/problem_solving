#230711
def solution(s):
    min_len = length = len(s) # 길이
    if length == 1: # 길이가 1일 경우 => 압축할 필요 없음
        return length
    half = length//2 # 길이의 절반 => 자를 문자 길이의 최댓값 (절반을 넘어서면 앞 길이 > 뒤 길이 => 압축 X)
    if s[:half] == s[half:half*2]:
        return length - half + 1
    for step in range(half-1, 0, -1): # 문자열 자를 길이
        answer = length # 자른 문자 길이에 따른 압축 문자열 길이
        cnt = 1 # 반복되는 문자열 개수
        before = s[:step] # 비교할 문자열
        for i in range(step, length, step):
            if before == s[i:i+step]: # 비교할 문자열과 현재 문자열이 같으면 cnt 증가
                cnt += 1
            else:
                if cnt > 1: # 문자열이 2개 이상 존재하면 (문자열 개수-1)*문자열 길이 빼주고 cnt의 길이만큼 더해줌
                    answer -= (step * (cnt-1) - len(str(cnt)))
                before = s[i:i + step] # 비교할 문자열과 현재 문자열이 다르면 before 갱신, cnt 초기화
                cnt = 1

        if cnt > 1: # for문에서 else문에 들어가지 않을 경우 고려 (마지막 문자열과 비교 문자열이 같은 채 for문 종료)
            answer -= (step * (cnt - 1) - len(str(cnt)))
        if min_len > answer: # min_len과 answer 비교
            min_len = answer
    return min_len


print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))

'''
테스트 1 〉	통과 (0.00ms, 9.97MB)
테스트 2 〉	통과 (0.27ms, 10.2MB)
테스트 3 〉	통과 (0.23ms, 10.2MB)
테스트 4 〉	통과 (0.04ms, 10MB)
테스트 5 〉	통과 (0.00ms, 10.2MB)
테스트 6 〉	통과 (0.05ms, 10.4MB)
테스트 7 〉	통과 (0.51ms, 10.1MB)
테스트 8 〉	통과 (0.31ms, 10MB)
테스트 9 〉	통과 (0.01ms, 9.98MB)
테스트 10 〉	통과 (1.93ms, 10MB)
테스트 11 〉	통과 (0.07ms, 10MB)
테스트 12 〉	통과 (0.00ms, 10.2MB)
테스트 13 〉	통과 (0.12ms, 10.3MB)
테스트 14 〉	통과 (0.45ms, 10.2MB)
테스트 15 〉	통과 (0.08ms, 10.1MB)
테스트 16 〉	통과 (0.01ms, 10.3MB)
테스트 17 〉	통과 (0.84ms, 10MB)
테스트 18 〉	통과 (1.56ms, 10.1MB)
테스트 19 〉	통과 (1.64ms, 10.1MB)
테스트 20 〉	통과 (1.81ms, 10.2MB)
테스트 21 〉	통과 (3.54ms, 10.2MB)
테스트 22 〉	통과 (3.60ms, 10.2MB)
테스트 23 〉	통과 (2.01ms, 10.1MB)
테스트 24 〉	통과 (1.65ms, 10.2MB)
테스트 25 〉	통과 (0.00ms, 10.2MB)
테스트 26 〉	통과 (1.77ms, 10.3MB)
테스트 27 〉	통과 (1.90ms, 10.1MB)
테스트 28 〉	통과 (0.01ms, 10.2MB)
'''
