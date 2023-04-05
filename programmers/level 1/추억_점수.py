#230405
# hash
def solution(name, yearning, photo):
    length = len(name)
    yearning_of = {name[i]: yearning[i] for i in range(length)}
    answer = []
    for each in photo:
        total_score = 0
        for person in each:
            if yearning_of.get(person):
                total_score += yearning_of[person]
        answer.append(total_score)
    return answer
'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.13ms, 10.4MB)
테스트 4 〉	통과 (0.06ms, 10.2MB)
테스트 5 〉	통과 (0.58ms, 10.5MB)
테스트 6 〉	통과 (0.64ms, 10.3MB)
테스트 7 〉	통과 (0.49ms, 10.3MB)
테스트 8 〉	통과 (1.02ms, 10.5MB)
테스트 9 〉	통과 (0.79ms, 10.5MB)
테스트 10 〉	통과 (1.19ms, 10.8MB)
테스트 11 〉	통과 (1.29ms, 10.9MB)
테스트 12 〉	통과 (0.86ms, 10.6MB)
테스트 13 〉	통과 (0.06ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)

'''