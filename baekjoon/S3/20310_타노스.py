#230507
# 그리디
# list, join
S = input()
length = len(S)
zero = S.count('0')
one = length - zero
half_zero, half_one = zero//2, one//2
S = list(map(str, S))
for i in range(length-1, -1, -1):
    if half_zero == 0:
        break
    elif S[i] == '0':
        S[i] = ''
        half_zero -= 1
for i in range(length):
    if half_one == 0:
        break
    elif S[i] == '1':
        S[i] = ''
        half_one -= 1
print(''.join(S))


# 함수화
def remove_element(half, start, end, step, target):
    for i in range(start, end, step):
        if half == 0:
            return
        elif S[i] == target:
            S[i] = ''
            half -= 1

S = list(map(str, input()))
length = len(S)
zero = S.count('0')
one = length - zero
remove_element(zero//2, length-1, -1, -1, '0')
remove_element(one//2, 0, length, 1, '1')
print(''.join(S))
