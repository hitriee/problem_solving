#230721
def solution(my_string):
    answer = [0] * 52
    ref_lower = ord('a')
    ref_upper = ord('A')
    alp_to_index = {}

    for i in range(26):
        alp_to_index[chr(ref_lower+i)] = i + 26
        alp_to_index[chr(ref_upper+i)] = i

    for alp in my_string:
        answer[alp_to_index[alp]] += 1

    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10.2MB)
테스트 6 〉	통과 (0.02ms, 10MB)
테스트 7 〉	통과 (0.04ms, 10.3MB)
테스트 8 〉	통과 (0.02ms, 10.1MB)
테스트 9 〉	통과 (0.03ms, 10.1MB)
테스트 10 〉	통과 (0.07ms, 10.2MB)
테스트 11 〉	통과 (0.06ms, 10.3MB)
테스트 12 〉	통과 (0.06ms, 10.2MB)
테스트 13 〉	통과 (0.08ms, 10MB)
테스트 14 〉	통과 (0.08ms, 10.2MB)
테스트 15 〉	통과 (0.09ms, 10.2MB)
테스트 16 〉	통과 (0.09ms, 10.1MB)
테스트 17 〉	통과 (0.09ms, 10.2MB)
테스트 18 〉	통과 (0.10ms, 10.2MB)
테스트 19 〉	통과 (0.01ms, 10.2MB)
테스트 20 〉	통과 (0.02ms, 10.2MB)
'''