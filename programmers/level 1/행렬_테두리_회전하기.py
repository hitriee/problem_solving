# 240404
def minus_one(x):
    return x - 1


def solution(rows, columns, queries):
    answer = []
    arr = [[0] * columns for _ in range(rows)]
    for i in range(rows * columns):
        arr[i // columns][i % columns] = i + 1

    for query in queries:
        y1, x1, y2, x2 = map(minus_one, query)

        temp = []
        for j in range(x1, x2):
            temp.append(arr[y1][j])

        for i in range(y1, y2):
            temp.append(arr[i][x2])

        for j in range(x2, x1, -1):
            temp.append(arr[y2][j])

        for i in range(y2, y1, -1):
            temp.append(arr[i][x1])

        # 변경
        idx = 0
        for j in range(x1 + 1, x2):
            arr[y1][j] = temp[idx]
            idx += 1

        for i in range(y1, y2):
            arr[i][x2] = temp[idx]
            idx += 1

        for j in range(x2, x1, -1):
            arr[y2][j] = temp[idx]
            idx += 1

        for i in range(y2, y1, -1):
            arr[i][x1] = temp[idx]
            idx += 1

        arr[y1][x1] = temp[-1]
        answer.append(min(temp))

    return answer