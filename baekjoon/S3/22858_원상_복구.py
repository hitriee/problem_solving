#230411
# 2중 for문
to_int = lambda : map(int, input().split())
N, K = to_int()
after = list(to_int())
rule = list(to_int())
after.insert(0, 0)
rule.insert(0, 0)
before = [0] * (N+1)
for _ in range(K):
    for i in range(1, N+1):
        before[rule[i]] = after[i]
    after = before[:]
print(*before[1:])