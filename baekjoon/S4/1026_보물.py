#230422
# 그리디
N = int(input())
A = sorted(map(int, input().split()), reverse=True)
B = sorted(map(int, input().split()))
min_total = 0
for i in range(N):
    min_total += A[i] * B[i]
print(min_total)


#
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort(reverse=True)
min_total = 0
for i in range(N):
    min_total += A[i] * B[i]
print(min_total)


#
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()
min_total = 0
for i in range(N):
    min_total += A[i] * B[N-1-i]
print(min_total)


#
def treasure():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    min_total = 0
    for i in range(N):
        min_total += A[i] * B[N-1-i]
    return min_total
print(treasure())