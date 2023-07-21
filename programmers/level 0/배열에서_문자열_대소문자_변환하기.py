#230721
def solution(strArr):
    answer = []
    for i in range(len(strArr)):
        old_str = strArr[i]
        new_str = ''
        if i%2:
            for alp in old_str:
                new_str += alp if alp.isupper() else alp.upper()

        else:
            for alp in old_str:
                new_str += alp if alp.islower() else alp.lower()

        answer.append(new_str)
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10MB)
테스트 2 〉	통과 (0.03ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 10.4MB)
테스트 5 〉	통과 (0.02ms, 9.9MB)
테스트 6 〉	통과 (0.02ms, 10.1MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.02ms, 10.1MB)
테스트 9 〉	통과 (0.02ms, 10.2MB)
테스트 10 〉	통과 (0.02ms, 10.1MB)
테스트 11 〉	통과 (0.02ms, 10.1MB)
'''