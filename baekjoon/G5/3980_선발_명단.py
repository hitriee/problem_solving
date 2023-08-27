#230827
C = int(input())
def find_max_score(level=0, score=0):
    global max_score
    if level == 11:
        if score > max_score:
            max_score = score
        return
    for i in range(11):
        if score_info[level][i] and not visited[i]:
            visited[i] = True
            find_max_score(level+1, score+score_info[level][i])
            visited[i] = False
for _ in range(C):
    score_info = [list(map(int, input().split())) for _ in range(11)]
    max_score = 0
    visited = [False] * 11
    find_max_score()
    print(max_score)


#
def decide_position():

    def find_max_score(level=0, score=0):
        nonlocal max_score
        if level == 11:
            if score > max_score:
                max_score = score
            return
        for i in range(11):
            if score_info[level][i] and not visited[i]:
                visited[i] = True
                find_max_score(level + 1, score + score_info[level][i])
                visited[i] = False

    C = int(input())
    for _ in range(C):
        score_info = [list(map(int, input().split())) for _ in range(11)]
        visited = [False] * 11
        max_score = 0
        find_max_score()
        print(max_score)

decide_position()

#
def decide_position():

    def find_max_score(level=0, score=0):
        nonlocal max_score
        if level == 11:
            if score > max_score:
                max_score = score
            return
        for i in range(11):
            if score_info[level][i] and not visited[i]:
                visited[i] = True
                find_max_score(level + 1, score + score_info[level][i])
                visited[i] = False

    C = int(input())
    visited = [False] * 11
    for _ in range(C):
        score_info = [list(map(int, input().split())) for _ in range(11)]
        max_score = 0
        find_max_score()
        print(max_score)

decide_position()