#230830
N, B = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

def multiple_matrix(left_matrix, right_matrix):
    answer_matrix = [right_matrix[i][:] for i in range(N)]
    for i in range(N):
        for j in range(N):
            answer = 0
            for k in range(N):
                answer += left_matrix[i][k] * right_matrix[k][j]
            answer_matrix[i][j] = answer%1000
    return answer_matrix

def exponential_matrix(answer_matrix, cnt):
    if cnt == 1:
        for i in range(N):
            for j in range(N):
                answer_matrix[i][j] %= 1000
        return answer_matrix
    result = exponential_matrix(answer_matrix, cnt//2)
    new_matrix = multiple_matrix(result, result)
    if cnt%2:
        new_matrix = multiple_matrix(new_matrix, matrix)
    return new_matrix

answer_matrix = exponential_matrix(matrix, B)

for i in range(N):
    print(*answer_matrix[i])


#
def multiple_matrix(left_matrix, right_matrix, N):
    answer_matrix = [right_matrix[i][:] for i in range(N)]

    for i in range(N):
        for j in range(N):
            answer = 0
            for k in range(N):
                answer += left_matrix[i][k] * right_matrix[k][j]
            answer_matrix[i][j] = answer % 1000

    return answer_matrix


def exponential_matrix(answer_matrix, cnt, matrix, N):
    if cnt == 1:
        for i in range(N):
            for j in range(N):
                answer_matrix[i][j] %= 1000
        return answer_matrix

    result = exponential_matrix(answer_matrix, cnt // 2, matrix, N)
    new_matrix = multiple_matrix(result, result, N)

    if cnt % 2:
        new_matrix = multiple_matrix(new_matrix, matrix, N)

    return new_matrix


def calc_new_matrix():
    N, B = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    answer_matrix = exponential_matrix(matrix, B, matrix, N)

    for i in range(N):
        print(*answer_matrix[i])


calc_new_matrix()



#
def multiple_matrix(left_matrix, right_matrix, N):
    answer_matrix = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                answer_matrix[i][j] += left_matrix[i][k] * right_matrix[k][j]
            answer_matrix[i][j] %= 1000

    return answer_matrix

def exponential_matrix(answer_matrix, cnt, matrix, N):
    if cnt == 1:
        for i in range(N):
            for j in range(N):
                answer_matrix[i][j] %= 1000
        return answer_matrix

    result = exponential_matrix(answer_matrix, cnt // 2, matrix, N)
    new_matrix = multiple_matrix(result, result, N)

    if cnt % 2:
        new_matrix = multiple_matrix(new_matrix, matrix, N)

    return new_matrix


def calc_new_matrix():
    N, B = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    answer_matrix = exponential_matrix(matrix, B, matrix, N)

    for i in range(N):
        print(*answer_matrix[i])

calc_new_matrix()


#
N, B = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

def multiple_matrix(left_matrix, right_matrix):
    answer_matrix = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                answer_matrix[i][j] += left_matrix[i][k] * right_matrix[k][j]
            answer_matrix[i][j] %= 1000
    return answer_matrix

def exponential_matrix(answer_matrix, cnt):
    if cnt == 1:
        return answer_matrix

    result = exponential_matrix(answer_matrix, cnt//2)
    new_matrix = multiple_matrix(result, result)

    if cnt%2:
        new_matrix = multiple_matrix(new_matrix, matrix)
    return new_matrix


for i in range(N):
    for j in range(N):
        matrix[i][j] %= 1000

answer_matrix = exponential_matrix(matrix, B)

for i in range(N):
    print(*answer_matrix[i])


#
def multiple_matrix(left_matrix, right_matrix, N):
    answer_matrix = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                answer_matrix[i][j] += left_matrix[i][k] * right_matrix[k][j]
            answer_matrix[i][j] %= 1000

    return answer_matrix

def exponential_matrix(answer_matrix, cnt, matrix, N):
    if cnt == 1:
        return answer_matrix

    result = exponential_matrix(answer_matrix, cnt // 2, matrix, N)
    new_matrix = multiple_matrix(result, result, N)

    if cnt % 2:
        new_matrix = multiple_matrix(new_matrix, matrix, N)

    return new_matrix


def calc_new_matrix():
    N, B = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            matrix[i][j] %= 1000

    answer_matrix = exponential_matrix(matrix, B, matrix, N)

    for i in range(N):
        print(*answer_matrix[i])

calc_new_matrix()


#
def multiple_matrix(left_matrix, right_matrix, N):
    answer_matrix = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                answer_matrix[i][j] += left_matrix[i][k] * right_matrix[k][j]
            answer_matrix[i][j] %= 1000

    return answer_matrix


def exponential_matrix(answer_matrix, cnt, matrix, N):
    if cnt == 1:
        return answer_matrix

    result = exponential_matrix(answer_matrix, cnt // 2, matrix, N)
    new_matrix = multiple_matrix(result, result, N)

    if cnt % 2:
        new_matrix = multiple_matrix(new_matrix, matrix, N)

    return new_matrix

def div_1000(num):
    return int(num)%1000


def calc_new_matrix():
    N, B = map(int, input().split())
    matrix = [list(map(div_1000, input().split())) for _ in range(N)]

    answer_matrix = exponential_matrix(matrix, B, matrix, N)

    for i in range(N):
        print(*answer_matrix[i])


calc_new_matrix()
