#230619
from heapq import heappush, heappop
from sys import stdin

def to_int():
    return int(stdin.readline())

N = to_int()
arr = []
for _ in range(N):
    number = to_int()
    if number:
        heappush(arr, (abs(number), number))
    elif arr:
        print(heappop(arr)[1])
    else:
        print(0)


#
def print_answer():
    from heapq import heappush, heappop
    from sys import stdin

    def to_int():
        return int(stdin.readline())

    N = to_int()
    arr = []
    for _ in range(N):
        number = to_int()
        if number:
            heappush(arr, (abs(number), number))
        elif arr:
            print(heappop(arr)[1])
        else:
            print(0)

print_answer()