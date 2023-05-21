#230521
from sys import stdin
new_input = stdin.readline
N = int(new_input())
info = {}
for _ in range(N):
    L, H = map(int, new_input().split())
    info[L] = H

keys = sorted(info.keys())
left, right = [keys[0]], [keys[-1]]
for i in range(1, N):
    if info[left[-1]] < info[keys[i]]:
        left.append(keys[i])
    if info[right[-1]] < info[keys[N-1-i]]:
        right.append(keys[N-1-i])

min_area = 0
for i in range(len(left)-1):
    min_area += (left[i+1] - left[i]) * info[left[i]]
for i in range(len(right)-1):
    min_area += (right[i] - right[i+1]) * info[right[i]]
min_area += (right[-1] - left[-1] + 1) * info[left[-1]]
print(min_area)


#
from sys import stdin
new_input = stdin.readline
N = int(new_input())
info = {}
for _ in range(N):
    L, H = map(int, new_input().split())
    info[L] = H

keys = sorted(info.keys())
left, right = [keys[0]], [keys[-1]]
left_key, right_key = left[0], right[0]
for i in range(1, N):
    if info[left_key] < info[keys[i]]:
        left.append(keys[i])
        left_key = keys[i]
    if info[right_key] < info[keys[N-1-i]]:
        right.append(keys[N-1-i])
        right_key = keys[N-1-i]

min_area = 0
for i in range(len(left)-1):
    min_area += (left[i+1] - left[i]) * info[left[i]]
for i in range(len(right)-1):
    min_area += (right[i] - right[i+1]) * info[right[i]]
min_area += (right[-1] - left[-1] + 1) * info[left[-1]]
print(min_area)


#
def calc_roof_area():
    from sys import stdin
    new_input = stdin.readline
    N = int(new_input())
    info = {}
    for _ in range(N):
        L, H = map(int, new_input().split())
        info[L] = H

    keys = sorted(info.keys())
    left, right = [keys[0]], [keys[-1]]
    left_key, right_key = left[0], right[0]
    for i in range(1, N):
        if info[left_key] < info[keys[i]]:
            left.append(keys[i])
            left_key = keys[i]
        if info[right_key] < info[keys[N-1-i]]:
            right.append(keys[N-1-i])
            right_key = keys[N-1-i]

    min_area = 0
    for i in range(len(left)-1):
        min_area += (left[i+1] - left[i]) * info[left[i]]
    for i in range(len(right)-1):
        min_area += (right[i] - right[i+1]) * info[right[i]]
    min_area += (right[-1] - left[-1] + 1) * info[left[-1]]
    return min_area
print(calc_roof_area())


#
from sys import stdin
new_input = stdin.readline
N = int(new_input())
info = {}
for _ in range(N):
    L, H = map(int, new_input().split())
    info[L] = H

keys = sorted(info.keys())
increased_keys = [[keys[0]], [keys[-1]]]
before_key = [increased_keys[0][0], increased_keys[1][0]]
for i in range(1, N):
    index = [i, N-i-1]
    for j in range(2):
        key = keys[index[j]]
        if info[before_key[j]] < info[key]:
            increased_keys[j].append(key)
            before_key[j] = key
min_area = 0
for i in range(2):
    heights = increased_keys[i]
    for j in range(len(heights) - 1):
        min_area += abs(heights[j+1] - heights[j]) * info[heights[j]]

last = [increased_keys[i].pop() for i in range(2)]
min_area += (last[1] - last[0] + 1) * info[last[0]]
print(min_area)
