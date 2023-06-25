#230625
def cnt_set():
    L = int(input())
    S = list(map(int, input().split()))
    S.sort()
    N = int(input())
    for i in range(L):
        if S[i] > N:
            start = S[i-1]+1 if i >= 1 else 1
            end = S[i]-1
            return (N - start + 1) * (end - N) + (N-start)
        elif S[i] == N:
            return 0

print(cnt_set())
