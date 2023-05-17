#230517
# 자료 구조
N = int(input())
rand_num_list = [0] # 첫째 줄 => 인덱스, 둘째 줄 => 값
# second_line 뽑힌 숫자 set, temp_set 뽑힌 숫자를 인덱스로 했을 때 값
temp_set, second_line = set(), set()
for i in range(1, N+1):
    num = int(input())
    rand_num_list.append(num)
    second_line.add(num)
# 두 집합이 같아질 때까지 반복
while True:
    for num in second_line:
        if rand_num_list[num] in second_line:
            temp_set.add(rand_num_list[num])
    if second_line == temp_set:
        break
    second_line.clear()
    second_line.update(temp_set)
    temp_set.clear()

print(len(second_line), *sorted(second_line), sep='\n')



#
N = int(input())
rand_num_list = [0]
temp_set, second_line = set(), set()
for i in range(1, N+1):
    num = int(input())
    rand_num_list.append(num)
    second_line.add(num)

while True:
    for num in second_line:
        value = rand_num_list[num]
        if value in second_line:
            temp_set.add(value)
    if second_line == temp_set:
        break
    second_line.clear()
    second_line.update(temp_set)
    temp_set.clear()

print(len(second_line), *sorted(second_line), sep='\n')


#
from sys import stdin
def to_int(): return int(stdin.readline())
N = to_int()
rand_num_list = [0]
temp_set, second_line = set(), set()
for i in range(1, N+1):
    num = to_int()
    rand_num_list.append(num)
    second_line.add(num)

while True:
    for num in second_line:
        value = rand_num_list[num]
        if value in second_line:
            temp_set.add(value)
    if second_line == temp_set:
        break
    second_line.clear()
    second_line.update(temp_set)
    temp_set.clear()

print(len(second_line), *sorted(second_line), sep='\n')


#
def find_set():
    from sys import stdin

    def to_int(): return int(stdin.readline())

    N = to_int()
    rand_num_list = [0]
    temp_set, second_line = set(), set()
    for i in range(1, N+1):
        num = to_int()
        rand_num_list.append(num)
        second_line.add(num)

    while True:
        for num in second_line:
            value = rand_num_list[num]
            if value in second_line:
                temp_set.add(value)
        if second_line == temp_set:
            break
        second_line = set(temp_set)
        temp_set.clear()

    print(len(second_line), *sorted(second_line), sep='\n')

find_set()


#
def find_set():
    from sys import stdin

    def to_int(): return int(stdin.readline())

    N = to_int()
    rand_num_list = [0]
    temp_set, second_line = set(), set()
    for i in range(1, N+1):
        num = to_int()
        rand_num_list.append(num)
        second_line.add(num)

    while True:
        for num in second_line:
            value = rand_num_list[num]
            if value in second_line:
                temp_set.add(value)
        if second_line == temp_set:
            break
        second_line = set(temp_set)
        temp_set.clear()

    print(len(second_line))
    for num in sorted(second_line):
        print(num)

find_set()


#
def find_set():
    from sys import stdin

    def to_int(): return int(stdin.readline())

    N = to_int()
    rand_num_list = [0]
    temp_set, second_line = set(), set()
    for i in range(1, N+1):
        num = to_int()
        rand_num_list.append(num)
        second_line.add(num)

    while True:
        for num in second_line:
            value = rand_num_list[num]
            if value in second_line:
                temp_set.add(value)
        if len(second_line) == len(temp_set):
            break
        second_line = set(temp_set)
        temp_set.clear()

    print(len(second_line), *sorted(second_line), sep='\n')

find_set()




