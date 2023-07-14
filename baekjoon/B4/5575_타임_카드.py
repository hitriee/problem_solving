#230714
for _ in range(3):
    h1, m1, s1, h2, m2, s2 = map(int, input().split())
    answer = [h2-h1, m2-m1, s2-s1]
    for i in range(2, 0, -1):
        if answer[i] < 0:
            answer[i] += 60
            answer[i-1] -= 1
    print(*answer)