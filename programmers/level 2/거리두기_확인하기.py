# 240930
def gap(y1,x1,y2,x2):
    return abs(y1 - y2) + abs(x1 - x2)

def solution(places):
    # 행 길이 = 대기실 개수 = 5
    # 열 길이 = 대기실 세로 길이 = 5
    # P 응시자, O 빈 테이블, X 파티션
  
    def find_people():
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    people.append((i, j))
                    
    def is_correct():
        limit = len(people)
        for i in range(limit):
            y1, x1 = people[i]
            for j in range(i+1, limit):
                y2, x2 = people[j]
                if gap(y1, x1, y2, x2) > 2:
                    continue
                
                if y1 == y2:
                    if place[y1][min(x1, x2)+1] != 'X':
                        return 0
                elif x1 == x2:
                    if place[min(y1, y2)+1][x1] != 'X':
                        return 0
                elif place[y1][x2] != 'X' or place[y2][x1] != 'X':
                    return 0
                
        return 1
                    
    
    answer = []
    # 강의실별로 탐색
    for place in places:
        # 응시자 위치 찾기
        people = []
        find_people()
        
        # 응시자 거리 탐색
        answer.append(is_correct())
        
        
    return answer



'''
정확성  테스트
테스트 1 〉	통과 (0.13ms, 10.3MB)
테스트 2 〉	통과 (0.04ms, 10.4MB)
테스트 3 〉	통과 (0.05ms, 10.4MB)
테스트 4 〉	통과 (0.06ms, 10.3MB)
테스트 5 〉	통과 (0.05ms, 10.2MB)
테스트 6 〉	통과 (0.03ms, 10.3MB)
테스트 7 〉	통과 (0.05ms, 10.1MB)
테스트 8 〉	통과 (0.06ms, 10.3MB)
테스트 9 〉	통과 (0.04ms, 10.2MB)
테스트 10 〉	통과 (0.03ms, 10.3MB)
테스트 11 〉	통과 (0.04ms, 10.2MB)
테스트 12 〉	통과 (0.06ms, 10.4MB)
테스트 13 〉	통과 (0.03ms, 10.3MB)
테스트 14 〉	통과 (0.03ms, 10.3MB)
테스트 15 〉	통과 (0.04ms, 10.2MB)
테스트 16 〉	통과 (0.03ms, 10.3MB)
테스트 17 〉	통과 (0.03ms, 10.2MB)
테스트 18 〉	통과 (0.03ms, 10.2MB)
테스트 19 〉	통과 (0.03ms, 10.2MB)
테스트 20 〉	통과 (0.05ms, 10.3MB)
테스트 21 〉	통과 (0.04ms, 10.2MB)
테스트 22 〉	통과 (0.04ms, 10.2MB)
테스트 23 〉	통과 (0.02ms, 10.2MB)
테스트 24 〉	통과 (0.04ms, 10.2MB)
테스트 25 〉	통과 (0.04ms, 10.4MB)
테스트 26 〉	통과 (0.02ms, 10.4MB)
테스트 27 〉	통과 (0.06ms, 10.3MB)
테스트 28 〉	통과 (0.05ms, 10.3MB)
테스트 29 〉	통과 (0.03ms, 10.1MB)
테스트 30 〉	통과 (0.03ms, 10.4MB)
테스트 31 〉	통과 (0.03ms, 10.4MB)
'''


#
def gap(y1,x1,y2,x2):
    return abs(y1 - y2) + abs(x1 - x2)

def solution(places):
    # 행 길이 = 대기실 개수 = 5
    # 열 길이 = 대기실 세로 길이 = 5
    # P 응시자, O 빈 테이블, X 파티션
  
    def find_people():
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    people.append((i, j))
                    
    def is_correct():
        limit = len(people)
        for i in range(limit):
            y1, x1 = people[i]
            for j in range(i+1, limit):
                y2, x2 = people[j]
                distance = gap(y1, x1, y2, x2)
                if distance > 2:
                    continue
                
                if distance == 1:
                    return 0
                
                if y1 == y2:
                    if place[y1][min(x1, x2)+1] != 'X':
                        return 0
                elif x1 == x2:
                    if place[min(y1, y2)+1][x1] != 'X':
                        return 0
                elif place[y1][x2] != 'X' or place[y2][x1] != 'X':
                    return 0
                
        return 1
                    
                    
    answer = []
    # 강의실별로 탐색
    for place in places:
        # 응시자 위치 찾기
        people = []
        find_people()
        
        # 응시자 거리 탐색
        answer.append(is_correct())
        
        
    return answer



'''
테스트 1 〉	통과 (0.07ms, 10.3MB)
테스트 2 〉	통과 (0.06ms, 10.4MB)
테스트 3 〉	통과 (0.03ms, 10.2MB)
테스트 4 〉	통과 (0.04ms, 10.4MB)
테스트 5 〉	통과 (0.03ms, 10.3MB)
테스트 6 〉	통과 (0.03ms, 10.1MB)
테스트 7 〉	통과 (0.03ms, 10.2MB)
테스트 8 〉	통과 (0.04ms, 10.3MB)
테스트 9 〉	통과 (0.04ms, 10.3MB)
테스트 10 〉	통과 (0.05ms, 10.3MB)
테스트 11 〉	통과 (0.03ms, 10.4MB)
테스트 12 〉	통과 (0.03ms, 10.3MB)
테스트 13 〉	통과 (0.03ms, 10.2MB)
테스트 14 〉	통과 (0.03ms, 10.3MB)
테스트 15 〉	통과 (0.03ms, 10.2MB)
테스트 16 〉	통과 (0.03ms, 10.4MB)
테스트 17 〉	통과 (0.04ms, 10.3MB)
테스트 18 〉	통과 (0.03ms, 10.4MB)
테스트 19 〉	통과 (0.03ms, 10.3MB)
테스트 20 〉	통과 (0.04ms, 10.4MB)
테스트 21 〉	통과 (0.04ms, 10.3MB)
테스트 22 〉	통과 (0.05ms, 10.3MB)
테스트 23 〉	통과 (0.04ms, 10.3MB)
테스트 24 〉	통과 (0.03ms, 10.3MB)
테스트 25 〉	통과 (0.02ms, 10.3MB)
테스트 26 〉	통과 (0.04ms, 10.2MB)
테스트 27 〉	통과 (0.03ms, 10.2MB)
테스트 28 〉	통과 (0.03ms, 10.2MB)
테스트 29 〉	통과 (0.03ms, 10.3MB)
테스트 30 〉	통과 (0.03ms, 10.3MB)
테스트 31 〉	통과 (0.03ms, 10.3MB)
'''
