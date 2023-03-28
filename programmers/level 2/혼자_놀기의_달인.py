#230327
# heap + visited + if-else
def solution(cards):
    from heapq import heappush, heappop
    # 상자 그룹에 속한 상자의 수 (점수)를 구하는 함수
    def find_score():
        # 인덱스와 상자 번호를 맞춰주기 위해 맨 앞에 0 추가
        cards.insert(0, 0)
        length = len(cards)
        # 이미 연 상자인지 구별하기 위한 배열
        visited = [False] * length
        # 다음에 열 상자 번호 갱신하면서, 이미 연 상자인지 확인
        for i in range(1, length):
            box = i
            length = 0
            while not visited[box]:
                visited[box] = True
                box = cards[box]
                length += 1
            # 최대힙을 만들기 위해 -length를 추가
            if length:
                heappush(score_list, -length)

    answer = 1
    score_list = []
    find_score()
    # 찾은 상자 그룹이 1개면 0점
    if len(score_list) < 2:
        return 0
    # 찾은 점수 중 큰 점수를 answer에 곱하기
    for _ in range(2):
        answer *= heappop(score_list)
    return answer
'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.02ms, 9.98MB)
테스트 3 〉	통과 (0.03ms, 10.1MB)
테스트 4 〉	통과 (0.02ms, 10.4MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.02ms, 10.4MB)
테스트 7 〉	통과 (0.02ms, 10.4MB)
테스트 8 〉	통과 (0.03ms, 10.2MB)
테스트 9 〉	통과 (0.04ms, 10.2MB)
테스트 10 〉	통과 (0.04ms, 10.3MB)
'''


# heapq + visited + try-except
def solution(cards):
    from heapq import heappush, heappop
    # 상자 그룹에 속한 상자의 수 (점수)를 구하는 함수
    def find_score():
        # 인덱스와 상자 번호를 맞춰주기 위해 맨 앞에 0 추가
        cards.insert(0, 0)
        length = len(cards)
        # 이미 연 상자인지 구별하기 위한 배열
        visited = [False] * length
        # 다음에 열 상자 번호 갱신하면서, 이미 연 상자인지 확인
        for i in range(1, length):
            box = i
            length = 0
            while not visited[box]:
                visited[box] = True
                box = cards[box]
                length += 1
            # 최대힙을 만들기 위해 -length를 추가
            if length:
                heappush(score_list, -length)

    answer = 1
    score_list = []
    find_score()
    # 찾은 상자 그룹이 1개면 0점, 찾은 점수 중 큰 점수를 answer에 곱하기
    try:
        for _ in range(2):
            answer *= heappop(score_list)
        return answer
    except IndexError:
        return 0
'''
정확성  테스트
테스트 1 〉	통과 (0.05ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.05ms, 10.3MB)
테스트 4 〉	통과 (0.05ms, 10.2MB)
테스트 5 〉	통과 (0.05ms, 10.1MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.03ms, 10.2MB)
테스트 9 〉	통과 (0.02ms, 10.2MB)
테스트 10 〉	통과 (0.03ms, 10.4MB)
'''

# for + visited + if-else
def solution(cards):
    # 상자 그룹에 속한 상자의 수 (점수)를 구하는 함수
    def find_score():
        # 인덱스와 상자 번호를 맞춰주기 위해 맨 앞에 0 추가
        cards.insert(0, 0)
        length = len(cards)
        # 이미 연 상자인지 구별하기 위한 배열
        visited = [False] * length
        # 다음에 열 상자 번호 갱신하면서, 이미 연 상자인지 확인
        for i in range(1, length):
            box = i
            length = 0
            while not visited[box]:
                visited[box] = True
                box = cards[box]
                length += 1
            if length:
                score_list.append(length)

    score_list = []
    find_score()
    length = len(score_list)
    # 찾은 상자 그룹이 1개면 0점
    if length < 2:
        return 0
    # 찾은 점수 중 큰 점수 두 개를 answer에 곱하기
    max_val = second_max_val = 0
    for i in range(length):
        score = score_list[i]
        # 가장 큰 값, 두 번째 큰 값 갱신
        if max_val <= score:
            second_max_val = max_val
            max_val = score
        # 두 번째 큰 값 갱신
        elif second_max_val < score:
            second_max_val = score
    return max_val * second_max_val
'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.4MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.4MB)
테스트 7 〉	통과 (0.04ms, 10.1MB)
테스트 8 〉	통과 (0.03ms, 10.2MB)
테스트 9 〉	통과 (0.02ms, 10.2MB)
테스트 10 〉	통과 (0.02ms, 10.3MB)
'''

# sort + visited + if-else
def solution(cards):
    # 상자 그룹에 속한 상자의 수 (점수)를 구하는 함수
    def find_score():
        # 인덱스와 상자 번호를 맞춰주기 위해 맨 앞에 0 추가
        cards.insert(0, 0)
        length = len(cards)
        # 이미 연 상자인지 구별하기 위한 배열
        visited = [False] * length
        # 다음에 열 상자 번호 갱신하면서, 이미 연 상자인지 확인
        for i in range(1, length):
            box = i
            length = 0
            while not visited[box]:
                visited[box] = True
                box = cards[box]
                length += 1
            if length:
                score_list.append(length)

    score_list = []
    find_score()
    length = len(score_list)
    # 찾은 상자 그룹이 1개면 0점
    if length < 2:
        return 0
    # 찾은 점수 중 큰 점수 두 개를 answer에 곱하기
    score_list.sort()
    return score_list[-1] * score_list[-2]
'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.4MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	통과 (0.03ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.02ms, 10.3MB)
테스트 9 〉	통과 (0.03ms, 10.3MB)
테스트 10 〉	통과 (0.02ms, 10.1MB)
'''