#230915
from sys import stdin
N = int(stdin.readline())
to_do_list = []
for _ in range(N):
    duration, end = map(int, stdin.readline().split())
    to_do_list.append((end, duration))

to_do_list.sort(key=lambda to_do: (to_do[0], -to_do[1]))
answer = -1
ref = to_do_list[0][0] - to_do_list[0][1]

for start in range(ref, -1, -1):
    end = start + to_do_list[0][1]
    for i in range(1, N):
        new_end = end + to_do_list[i][1]
        if new_end <= to_do_list[i][0]:
            end = new_end
        else:
            break
    else:
        answer = start
        break

print(answer)


#
from sys import stdin
N = int(stdin.readline())
to_do_list = [list(map(int, stdin.readline().split())) for _ in range(N)]

to_do_list.sort(key=lambda to_do: (to_do[1], -to_do[0]))
answer = -1
ref = to_do_list[0][1] - to_do_list[0][0]

for start in range(ref, -1, -1):
    end = start + to_do_list[0][0]
    for i in range(1, N):
        new_end = end + to_do_list[i][0]
        if new_end <= to_do_list[i][1]:
            end = new_end
        else:
            break
    else:
        answer = start
        break

print(answer)

#
from sys import stdin
N = int(stdin.readline())
to_do_list = []
for _ in range(N):
    duration, end = map(int, stdin.readline().split())
    to_do_list.append((end, duration))

to_do_list.sort()
answer = -1
ref = to_do_list[0][0] - to_do_list[0][1]

for start in range(ref, -1, -1):
    end = start + to_do_list[0][1]
    for i in range(1, N):
        new_end = end + to_do_list[i][1]
        if new_end <= to_do_list[i][0]:
            end = new_end
        else:
            break
    else:
        answer = start
        break

print(answer)


#
def find_start_time():
    from sys import stdin

    N = int(stdin.readline())

    to_do_list = []
    for _ in range(N):
        duration, end = map(int, stdin.readline().split())
        to_do_list.append((end, duration))

    to_do_list.sort()

    ref = to_do_list[0][0] - to_do_list[0][1]

    for start in range(ref, -1, -1):
        end = start + to_do_list[0][1]

        for i in range(1, N):
            new_end = end + to_do_list[i][1]
            if new_end <= to_do_list[i][0]:
                end = new_end
            else:
                break

        else:
            return start

    return -1

print(find_start_time())


#
def find_start_time():
    from sys import stdin

    N = int(stdin.readline())

    to_do_list = []
    for _ in range(N):
        duration, end = map(int, stdin.readline().split())
        to_do_list.append((end, duration))

    to_do_list.sort()
    first_end, first_duration = to_do_list[0]
    ref = first_end - first_duration

    for start in range(ref, -1, -1):
        end = start + first_duration
        for i in range(1, N):
            next_end, next_duration = to_do_list[i]
            new_end = end + next_duration
            if new_end <= next_end:
                end = new_end
            else:
                break

        else:
            return start

    return -1

print(find_start_time())


#
def find_start_time():
    from sys import stdin

    N = int(stdin.readline())

    to_do_list = []
    for _ in range(N):
        duration, end = map(int, stdin.readline().split())
        to_do_list.append((end, duration))

    to_do_list.sort()
    first_duration = to_do_list[0][1]
    ref = to_do_list[0][0] - first_duration

    for start in range(ref, -1, -1):
        end = start + first_duration
        for i in range(1, N):
            new_end = end + to_do_list[i][1]
            if new_end <= to_do_list[i][0]:
                end = new_end
            else:
                break

        else:
            return start

    return -1

print(find_start_time())