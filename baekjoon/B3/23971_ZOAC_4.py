#230425
# 그리디
from math import ceil
H, W, N, M = map(int, input().split())
cnt = ceil(H/(N+1)) * ceil(W/(M+1))
print(cnt)

# ceil X
H, W, N, M = map(int, input().split())
cnt = (H//(N+1) + int(H%(N+1) != 0)) * (W//(M+1)+ int(W%(M+1) != 0))
print(cnt)

# if else
H, W, N, M = map(int, input().split())
row_people = H//(N+1)
if H%(N+1):
    row_people += 1
col_people = W//(M+1)
if W%(M+1):
    col_people += 1
cnt = row_people * col_people
print(cnt)


# 함수화
def max_people():
    H, W, N, M = map(int, input().split())
    row_people = H//(N+1)
    if H%(N+1):
        row_people += 1
    col_people = W//(M+1)
    if W%(M+1):
        col_people += 1
    cnt = row_people * col_people
    return cnt
print(max_people())