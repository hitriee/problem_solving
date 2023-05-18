#230518
from sys import stdin
new_input = stdin.readline
N = int(new_input())
height_list = []
cnt = 0
for _ in range(N):
    position, height = map(int, new_input().split())
    while height_list and height_list[-1] > height:
        height_list.pop()
        cnt += 1
    if height and ((height_list and height_list[-1] < height) or not height_list):
        height_list.append(height)

print(cnt + len(height_list))


#
from sys import stdin
new_input = stdin.readline
N = int(new_input())
height_list = []
cnt = 0
for _ in range(N):
    position, height = map(int, new_input().split())
    while height_list and height_list[-1] > height:
        height_list.pop()
        cnt += 1
    if height and (not height_list or height_list[-1] < height):
        height_list.append(height)

print(cnt + len(height_list))


#
def min_building():
    from sys import stdin
    new_input = stdin.readline
    N = int(new_input())
    height_list = []
    cnt = 0
    for _ in range(N):
        position, height = map(int, new_input().split())
        while height_list and height_list[-1] > height:
            height_list.pop()
            cnt += 1
        if height and (not height_list or height_list[-1] < height):
            height_list.append(height)

    return cnt + len(height_list)
print(min_building())


#
def min_building():
    from sys import stdin
    new_input = stdin.readline
    N = int(new_input())
    height_list = []
    cnt = 0
    for _ in range(N):
        position, height = map(int, new_input().split())
        while height_list and height_list[-1] > height:
            height_list.pop()
            cnt += 1
        if height and ((height_list and height_list[-1] < height) or not height_list):
            height_list.append(height)

    return cnt + len(height_list)
print(min_building())


#
def min_building():
    from sys import stdin
    new_input = stdin.readline
    N = int(new_input())
    height_list = []
    cnt = 0
    for _ in range(N):
        height = new_input().rstrip().split()[1]
        height = int(height)
        while height_list and height_list[-1] > height:
            height_list.pop()
            cnt += 1
        if height and ((height_list and height_list[-1] < height) or not height_list):
            height_list.append(height)

    return cnt + len(height_list)
print(min_building())