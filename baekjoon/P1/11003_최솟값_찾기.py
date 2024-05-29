# 240529
# 868896 KB / 6504 ms
from collections import deque
N, L = map(int, input().split())
arr = list(map(int, input().split()))
temp, D = deque(), []
for end_i in range(N):
    while temp and temp[-1][0] > arr[end_i]:
        temp.pop()

    temp.append((arr[end_i], end_i))
    if end_i-L == temp[0][1]:
        temp.popleft()

    D.append(temp[0][0])

print(*D)

# 870936 KB / 6508 ms
from collections import deque

N, L = map(int, input().split())
arr = list(map(int, input().split()))
temp, D = deque([(arr[0], 0)]), [arr[0]]

for end_i in range(1, N):
    while temp[-1][0] > arr[end_i]:
        temp.pop()
        if not temp:
            break
    else:
        if end_i - L == temp[0][1]:
            temp.popleft()

    temp.append((arr[end_i], end_i))

    D.append(temp[0][0])

print(*D)


# 871960 KB / 6448 ms
from collections import deque

N, L = map(int, input().split())
arr = list(map(int, input().split()))
temp, D = deque([(arr[0], 0)]), [arr[0]]

for end_i in range(1, N):
    end_val = arr[end_i]
    while temp[-1][0] > end_val:
        temp.pop()
        if not temp:
            break
    else:
        if end_i - L == temp[0][1]:
            temp.popleft()

    temp.append((end_val, end_i))

    D.append(temp[0][0])

print(*D)


# 869896 KB / 6656 ms
from collections import deque

N, L = map(int, input().split())
arr = list(map(int, input().split()))
sorted_num, D = deque(), []

for end_i in range(N):
    end_val = arr[end_i]
    while sorted_num and sorted_num[-1][0] > end_val:
        sorted_num.pop()

    sorted_num.append((end_val, end_i))
    if end_i-L == sorted_num[0][1]:
        sorted_num.popleft()

    D.append(sorted_num[0][0])

print(*D)



# 793708 KB / 5536 ms
def main():
    from collections import deque

    N, L = map(int, input().split())
    arr = list(map(int, input().split()))
    temp, D = deque([(arr[0], 0)]), [arr[0]]

    for end_i in range(1, N):
        end_val = arr[end_i]
        while temp[-1][0] > end_val:
            temp.pop()
            if not temp:
                break
        else:
            if end_i - L == temp[0][1]:
                temp.popleft()

        temp.append((end_val, end_i))

        D.append(temp[0][0])

    return D

print(*main())