#230425
# 구현
while True:
    a, b, c = sorted(map(int, input().split()))
    if a == 0:
        break
    elif a + b <= c:
        print('Invalid')
    elif a == b == c:
        print('Equilateral')
    elif a != b and b != c and c != a:
        print('Scalene')
    else:
        print('Isosceles')


# 함수화
def print_result():
    while True:
        a, b, c = sorted(map(int, input().split()))
        if a == 0:
            return
        elif a + b <= c:
            print('Invalid')
        elif a == b == c:
            print('Equilateral')
        elif a != b and b != c and c != a:
            print('Scalene')
        else:
            print('Isosceles')
print_result()


# 순서 변경
while True:
    a, b, c = sorted(map(int, input().split()))
    if a == 0:
        break
    elif a + b <= c:
        print('Invalid')
    elif a == b == c:
        print('Equilateral')
    elif a == b or b == c or c == a:
        print('Isosceles')
    else:
        print('Scalene')
