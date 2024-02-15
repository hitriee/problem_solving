# 240214
# 32432 KB / 10312 ms
N = int(input())
values = list(map(int, input().split()))
cnt_values = {}

for value in values:
    if cnt_values.get(value):
        cnt_values[value] += 1
    else:
        cnt_values[value] = 1

keys = sorted(cnt_values)
length = len(keys)
cnt = 0

for i in range(length):
    value1 = keys[i]
    if cnt_values[value1] >= 2:
        target = -2*value1
        if value1 == 0:
            if cnt_values[0] >= 3:
                cnt += (cnt_values[0] * (cnt_values[0] - 1) * (cnt_values[0] - 2)) // 6
        elif cnt_values.get(target):
            cnt += (cnt_values[target] * (cnt_values[value1] * (cnt_values[value1] - 1))) // 2

    for j in range(i+1, length):
        value2 = keys[j]
        target = -(value1 + value2)
        if cnt_values.get(target):
            if target > value2:
                cnt += (cnt_values[target] * cnt_values[value1] * cnt_values[value2])

print(cnt)