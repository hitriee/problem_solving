#230523
from collections import deque
N = int(input())
num_list = input().split()
length = len(set(num_list))
if length == N:
    print(N*(N+1)//2)
elif length == 1:
    print(N)
else:
    cnt = 0
    visited = set()
    path = deque()
    for i in range(N):
        num = num_list[i]
        if num in visited:
            length = len(visited)
            while True:
                cnt += length
                new_num = path.popleft()
                visited.remove(new_num)
                if num in visited:
                    length -= 1
                else:
                    visited.add(num)
                    path.append(num)
                    break
        else:
            visited.add(num)
            path.append(num)
    length = len(visited)
    cnt += (length * (length+1)) //2
    print(cnt)

#
def find_cases():
    from collections import deque
    N = int(input())
    num_list = input().split()
    length = len(set(num_list))

    if length == N:
        return N * (N + 1) // 2
    elif length == 1:
        return N

    cnt = 0
    visited = set()
    path = deque()
    for i in range(N):
        num = num_list[i]
        if num in visited:
            length = len(visited)
            while True:
                cnt += length
                new_num = path.popleft()
                visited.remove(new_num)
                if num in visited:
                    length -= 1
                else:
                    visited.add(num)
                    path.append(num)
                    break
        else:
            visited.add(num)
            path.append(num)

    length = len(visited)
    cnt += (length * (length + 1)) // 2

    return cnt


print(find_cases())


#
def find_cases():
    from collections import deque
    N = int(input())
    num_list = input().split()
    length = len(set(num_list))

    if length == N:
        return N*(N+1)//2
    elif length == 1:
        return N

    cnt = length = 0
    visited = set()
    path = deque()
    for i in range(N):
        num = num_list[i]
        if num in visited:
            while True:
                cnt += length
                new_num = path.popleft()
                visited.remove(new_num)
                length -= 1
                if num not in visited:
                    visited.add(num)
                    path.append(num)
                    length += 1
                    break
        else:
            visited.add(num)
            path.append(num)
            length += 1

    cnt += (length * (length+1)) //2

    return cnt
print(find_cases())

