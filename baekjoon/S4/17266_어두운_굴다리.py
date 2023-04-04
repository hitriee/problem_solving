#230404
# 구현
# ceil, for
from math import ceil
N = int(input())
M = int(input())
lamp_position = list(map(int, input().split()))
min_height = max(lamp_position[0], N-lamp_position[-1])
for i in range(1, M):
    height = ceil((lamp_position[i] - lamp_position[i-1])/2)
    if height > min_height:
        min_height = height
print(min_height)

# 함수형
def find_min_height():
    from math import ceil
    N = int(input())
    M = int(input())
    lamp_position = list(map(int, input().split()))
    min_height = max(lamp_position[0], N-lamp_position[-1])
    for i in range(1, M):
        height = ceil((lamp_position[i] - lamp_position[i-1])/2)
        if height > min_height:
            min_height = height
    return min_height
print(find_min_height())

# readline
def find_min_height():
    from math import ceil
    from sys import stdin
    new_input = stdin.readline
    int_readline = lambda : int(new_input())
    N = int_readline()
    M = int_readline()
    lamp_position = list(map(int, new_input().split()))
    min_height = max(lamp_position[0], N-lamp_position[-1])
    for i in range(1, M):
        height = ceil((lamp_position[i] - lamp_position[i-1])/2)
        if height > min_height:
            min_height = height
    return min_height
print(find_min_height())

# map
def find_min_height():
    from math import ceil
    from sys import stdin
    new_input = stdin.readline
    int_readline = lambda : int(new_input())
    N = int_readline()
    M = int_readline()
    lamp_position = list(map(int, new_input().split()))
    min_height = max(lamp_position[0], N-lamp_position[-1])
    ceil_half_dif = lambda x, y: ceil((y-x)/2)
    max_heights = list(map(ceil_half_dif, lamp_position[:-1], lamp_position[1:]))
    if max_heights:
        return max(min_height, *max_heights)
    return min_height
print(find_min_height())
