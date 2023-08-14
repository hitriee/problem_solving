#230814
from sys import stdin
new_input = stdin.readline
N = int(new_input())
alp_to_i = {}
i_to_alp = [''] * 52
large, small = ord('A'), ord('a')

for i in range(26):
    large_i, small_i = chr(large+i), chr(small+i)
    alp_to_i[large_i] = i
    alp_to_i[small_i] = i+26
    i_to_alp[i] = large_i
    i_to_alp[i+26] = small_i

check = [[False] * 52 for _ in range(52)]

cnt = 0
for _ in range(N):
    left, right = new_input().rstrip().split(' => ')
    left_i, right_i = alp_to_i[left], alp_to_i[right]
    if not check[left_i][right_i]:
        check[left_i][right_i] = True

for k in range(52):
    for i in range(52):
        if k != i:
            for j in range(52):
                if check[i][k] and check[k][j]:
                    check[i][j] = True

proof = []
for i in range(52):
    for j in range(52):
        if i != j and check[i][j]:
            cnt += 1
            proof.append(f'{i_to_alp[i]} => {i_to_alp[j]}')
print(cnt, *proof, sep='\n')
