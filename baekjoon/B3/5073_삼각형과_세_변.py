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

# 반복문 이용
while True:
    lines = sorted(map(int, input().split()))
    if lines[0] == 0:
        break
    elif sum(lines[:2]) <= lines[-1]:
        print('Invalid')
    else:
        lines.append(lines[0])
        cnt = 0
        for i in range(3):
            if lines[i] == lines[i+1]:
                cnt += 1
        if cnt == 3:
            print('Equilateral')
        elif cnt == 1:
            print('Isosceles')
        else:
            print('Scalene')


# 반복문 이용2
while True:
    lines = sorted(map(int, input().split()))
    if lines[0] == 0:
        break
    elif sum(lines[:2]) <= lines[-1]:
        print('Invalid')
    else:
        cnt = 0
        for i in range(2):
            if lines[i] == lines[i+1]:
                cnt += 1
        if cnt == 2:
            print('Equilateral')
        else:
            if lines[0] == lines[-1]:
                cnt += 1
            if cnt == 1:
                print('Isosceles')
            else:
                print('Scalene')