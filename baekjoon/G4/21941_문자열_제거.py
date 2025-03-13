# 250313
# 32412 KB / 216 ms
def main():
    S = list(input())
    M = int(input())
    N = len(S)
    score_dict = {}
    # 인덱스 : 지울 문자열의 끝 인덱스+1, 값 : 최대 점수
    before = [0] * (N+1)
    after = [0] * (N+1)

    for _ in range(M):
        a, score = input().split()
        score_dict[a] = int(score)

    for start_i in range(N):
        after[start_i+1] = before[start_i+1]
        substring = ''
        for end_i in range(start_i, N):
            substring += S[end_i]
            # 지울 수 있는 문자열이면 그 점수와 이전 점수 + 1 비교
            if score_dict.get(substring):
                after[end_i+1] = max(before[end_i+1], before[start_i] + score_dict[substring])
            else:
                after[end_i+1] = max(after[end_i]+1, before[end_i+1])
        # print(after)
        before = after[:]
        after = [0] * (N+1)

    return before[-1]

print(main())




# 32412 KB / 216 ms
def main():
    from sys import stdin

    new_input = stdin.readline
    S = new_input().rstrip()
    M = int(new_input())
    N = len(S)
    score_dict = {}
    before = [0] * (N+1)
    after = [0] * (N+1)

    for _ in range(M):
        a, score = new_input().split()
        score_dict[a] = int(score)

    for start_i in range(N):
        substring = ''
        for end_i in range(start_i, N):
            substring += S[end_i]
            if score_dict.get(substring):
                after[end_i+1] = max(before[end_i+1], before[start_i] + score_dict[substring])
            else:
                after[end_i+1] = max(after[end_i]+1, before[end_i+1])

        before = after[:]
        after = [0] * (N+1)

    return before[-1]

print(main())