#230826
from sys import stdin
new_input = stdin.readline
N = int(new_input())
robot = {}
rank = {}

def find_group(num):
    if not robot.get(num):
        rank[num] = 1
        robot[num] = num
        return num
    elif robot[num] == num:
        return num
    result = find_group(robot[num])
    robot[num] = result
    return result

def union_group(num1, num2):
    group1, group2 = find_group(int(num1)), find_group(int(num2))
    if group1 == group2:
        return
    if rank[group1] >= rank[group2]:
        rank[group1] += rank[group2]
        robot[group2] = group1
    else:
        rank[group2] += rank[group1]
        robot[group1] = group2

for _ in range(N):
    command = new_input().split()
    if command[0] == 'I':
        union_group(*command[1:])
    else:
        num = int(command[1])
        if robot.get(num):
            group = find_group(num)
            print(rank[group])
        else:
            print(1)


#
def find_group(num, robot, depth):
    if not robot.get(num):
        depth[num] = 1
        robot[num] = num
        return num
    elif robot[num] == num:
        return num
    result = find_group(robot[num], robot, depth)
    robot[num] = result
    return result

def union_group(num1, num2, robot, depth):
    group1, group2 = find_group(int(num1), robot, depth), find_group(int(num2), robot, depth)
    if group1 == group2:
        return
    if depth[group1] >= depth[group2]:
        depth[group1] += depth[group2]
        robot[group2] = group1
    else:
        depth[group2] += depth[group1]
        robot[group1] = group2

def practice_command():
    from sys import stdin
    new_input = stdin.readline
    N = int(new_input())
    robot, depth = {}, {}

    for _ in range(N):
        command = new_input().split()
        if command[0] == 'I':
            union_group(*command[1:], robot, depth)
        else:
            num = int(command[1])
            if robot.get(num):
                group = find_group(num, robot, depth)
                print(depth[group])
            else:
                print(1)

practice_command()


#
def find_group(num, robot):
    if robot[num] < 0:
        return num
    result = find_group(robot[num], robot)
    robot[num] = result
    return result

def union_group(num1, num2, robot):
    group1, group2 = find_group(int(num1), robot), find_group(int(num2), robot)
    if group1 == group2:
        return
    if robot[group1] <= robot[group2]:
        robot[group1] += robot[group2]
        robot[group2] = group1
    else:
        robot[group2] += robot[group1]
        robot[group1] = group2

def practice_command():
    from sys import stdin
    new_input = stdin.readline
    N = int(new_input())
    robot = [-1] * (int(1e6)+1)

    for _ in range(N):
        command = new_input().split()
        if command[0] == 'I':
            union_group(*command[1:], robot)
        else:
            num = int(command[1])
            group = find_group(num, robot)
            print(-robot[group])


practice_command()


#
def find_group(num, robot):
    if robot[num] == num:
        return num
    result = find_group(robot[num], robot)
    robot[num] = result
    return result

def union_group(num1, num2, robot, depth):
    group1, group2 = find_group(int(num1), robot), find_group(int(num2), robot)
    if group1 == group2:
        return
    if depth[group1] >= depth[group2]:
        depth[group1] += depth[group2]
        robot[group2] = group1
    else:
        depth[group2] += depth[group1]
        robot[group1] = group2

def practice_command():
    from sys import stdin
    new_input = stdin.readline
    N = int(new_input())
    limit = int(1e6)+1
    robot, depth = list(range(limit)), [1] * limit

    for _ in range(N):
        command = new_input().split()
        if command[0] == 'I':
            union_group(*command[1:], robot, depth)
        else:
            num = int(command[1])
            group = find_group(num, robot)
            print(depth[group])


practice_command()