# 241217
# 32412 KB / 36 ms
name = input()
N = len(name)
alp_cnt = {chr(ord('A')+i):0 for i in range(26)}

for alp in name:
    alp_cnt[alp] += 1

pal_name = [''] * N
idx = 0
is_filled = False

for alp in alp_cnt:
    val = alp_cnt[alp]
    if val == 0:
        continue

    elif val % 2 == 1 and (N % 2 == 0 or is_filled):
        print('I\'m Sorry Hansoo')
        break

    for _ in range(val//2):
        pal_name[idx] = pal_name[N-1-idx] = alp
        idx += 1

    if val % 2 == 1:
        is_filled = True
        pal_name[N//2] = alp

else:
    print(''.join(pal_name))