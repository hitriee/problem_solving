# 260430
# 1631.52 ms / 254 MB
def solution(money):
    n = len(money)
    dp1 = [[0] * 2 for _ in range(n)]
    dp2 = [[0] * 2 for _ in range(n)]
    dp1[0][1] = money[0]
    dp2[1][1] = money[1]

    for i in range(1, n):
        dp1[i][1] = dp1[i-1][0] + money[i]
        dp1[i][0] = max(dp1[i-1])

    total1, total2 = dp1[-1]
    if total1 >= total2:
        return total1

    for i in range(2, n):
        dp2[i][1] = dp2[i - 1][0] + money[i]
        dp2[i][0] = max(dp2[i - 1])

    return max(*dp2[-1], *dp1[-2])





# 1521.23 ms / 254 MB
def solution(money):
    n = len(money)
    dp1 = [[0] * 2 for _ in range(n)]
    dp2 = [[0] * 2 for _ in range(n)]
    dp1[0][1] = dp1[1][0] = money[0]
    dp1[1][1] = dp2[1][1] = money[1]

    for i in range(2, n):
        dp1[i][1] = dp1[i-1][0] + money[i]
        dp1[i][0] = max(dp1[i-1])
        dp2[i][1] = dp2[i - 1][0] + money[i]
        dp2[i][0] = max(dp2[i - 1])

    total1, total2 = dp1[-1]
    if total1 >= total2:
        return total1

    return max(*dp2[-1], *dp1[-2])


# 1577.50 ms / 254 MB
def solution(money):
    n = len(money)
    dp1 = [[0] * 2 for _ in range(n)]
    dp2 = [[0] * 2 for _ in range(n)]
    dp1[0][1] = dp1[1][0] = money[0]
    dp1[1][1] = dp2[1][1] = money[1]

    for i in range(2, n):
        dp1[i][1] = dp1[i-1][0] + money[i]
        dp1[i][0] = max(dp1[i-1])
        dp2[i][1] = dp2[i - 1][0] + money[i]
        dp2[i][0] = max(dp2[i - 1])

    return max(*dp2[-1], *dp1[-2])



# print(solution([1, 2, 3, 1]))
# print(solution([1, 2, 3, 4]))
# print(solution([1, 1, 1, 1]))
# print(solution([5, 1, 1, 4]))
# print(solution([5, 3, 1, 3, 4]))
print(solution([5, 3, 1, 3, 1, 4]))