#230611
T = int(input())

def return_square_sum(a, b):
    return a*a + b*b

for _ in  range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if x1 == x2 and y1 == y2:
        if r1 != r2:
            print(0)
        elif r1 == 0:
            print(1)
        else:
            print(-1)
    else:
        total_distance = return_square_sum(x1-x2, y1-y2)
        plus_distance = return_square_sum(r1+r2, 0)
        minus_distance = return_square_sum(r1-r2, 0)
        if total_distance == plus_distance:
            print(1)
        elif total_distance > plus_distance:
            print(0)
        elif r1 == 0 or r2 == 0:
            print(0)
        elif minus_distance == total_distance:
            print(1)
        elif minus_distance > total_distance:
            print(0)
        else:
            print(2)


#
T = int(input())

def return_square_sum(a, b):
    return a*a + b*b

def return_answer():
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if x1 == x2 and y1 == y2:
        if r1 != r2:
            return 0
        elif r1 == 0:
            return 1
        return -1

    total_distance = return_square_sum(x1 - x2, y1 - y2)
    plus_distance = return_square_sum(r1 + r2, 0)
    minus_distance = return_square_sum(r1 - r2, 0)

    if total_distance == plus_distance:
        return 1
    elif total_distance > plus_distance:
        return 0
    elif r1 == 0 or r2 == 0:
        return 0
    elif minus_distance == total_distance:
        return 1
    elif minus_distance > total_distance:
        return 0
    else:
        return 2

for _ in  range(T):
    print(return_answer())



#
def main():
    from sys import stdin
    new_input = stdin.readline
    T = int(new_input())

    def return_square_sum(a, b):
        return a * a + b * b

    def return_answer():
        x1, y1, r1, x2, y2, r2 = map(int, new_input().split())
        if x1 == x2 and y1 == y2:
            if r1 != r2:
                return 0
            elif r1 == 0:
                return 1
            return -1

        total_distance = return_square_sum(x1 - x2, y1 - y2)
        plus_distance = return_square_sum(r1 + r2, 0)
        minus_distance = return_square_sum(r1 - r2, 0)

        if total_distance == plus_distance:
            return 1
        elif total_distance > plus_distance:
            return 0
        elif r1 == 0 or r2 == 0:
            return 0
        elif minus_distance == total_distance:
            return 1
        elif minus_distance > total_distance:
            return 0
        else:
            return 2

    for _ in range(T):
        print(return_answer())

main()