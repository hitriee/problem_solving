#230404
# 구현, for
from sys import stdin
to_int = lambda: map(int, stdin.readline().split())
N, K = to_int()
score_list = list(to_int())
score_acc = [0] + score_list[:]
for i in range(2, N+1):
    score_acc[i] += score_acc[i-1]
for _ in range(K):
    start, end = to_int()
    total = score_acc[end] - score_acc[start-1]
    print(f'{total/(end-start+1) :.2f}')

# insert 사용
from sys import stdin
to_int = lambda: map(int, stdin.readline().split())
N, K = to_int()
score_list = list(to_int())
score_acc = score_list[:]
score_acc.insert(0, 0)
for i in range(2, N+1):
    score_acc[i] += score_acc[i-1]
for _ in range(K):
    start, end = to_int()
    total = score_acc[end] - score_acc[start-1]
    print(f'{total/(end-start+1) :.2f}')

# 함수화
def print_average():
    from sys import stdin
    to_int = lambda: map(int, stdin.readline().split())
    N, K = to_int()
    score_list = list(to_int())
    score_acc = score_list[:]
    score_acc.insert(0, 0)
    for i in range(2, N+1):
        score_acc[i] += score_acc[i-1]
    for _ in range(K):
        start, end = to_int()
        total = score_acc[end] - score_acc[start-1]
        print(f'{total/(end-start+1) :.2f}')
print_average()