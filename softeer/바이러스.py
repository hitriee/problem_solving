#230428
K, P, N = map(int, input().split())
div_num = 1000000007
square = (P * P)%div_num
answer = K
for _ in range(N//2):
    answer = (answer*square)%div_num
if N % 2:
    answer = (answer*P)%div_num
print(answer)