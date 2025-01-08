# 250108
# 32412 KB / 112 ms
def main():
    from sys import stdin

    new_input = stdin.readline
    N = int(new_input())
    max_cnt = min_grade = 0
    check_list = [0] * 6
    for _ in range(N):
        a, b = map(int, new_input().split())
        check_list[a] += 1
        if a != b:
            check_list[b] += 1
        for grade in range(1, 6):
            if grade != a and grade != b:
                cnt = check_list[grade]
                if cnt > max_cnt:
                    max_cnt, min_grade = cnt, grade
                elif cnt == max_cnt and grade < min_grade:
                    min_grade = grade
                check_list[grade] = 0

    for i in range(1, 6):
        cnt = check_list[i]
        if cnt > max_cnt:
            max_cnt, min_grade = cnt, i
        elif cnt == max_cnt and i < min_grade:
            min_grade = i

    return f'{max_cnt} {min_grade}'

print(main())


# 32412 KB / 108 ms
def main():
    from sys import stdin

    new_input = stdin.readline
    N = int(new_input())
    max_cnt = min_grade = 0
    check_list = [0] * 6
    for _ in range(N):
        a, b = map(int, new_input().split())
        check_list[a] += 1
        if a != b:
            check_list[b] += 1
        for grade in range(1, 6):
            if grade != a and grade != b:
                cnt = check_list[grade]
                if cnt:
                    if cnt > max_cnt:
                        max_cnt, min_grade = cnt, grade
                    elif cnt == max_cnt and grade < min_grade:
                        min_grade = grade
                    check_list[grade] = 0

    for i in range(1, 6):
        cnt = check_list[i]
        if cnt > max_cnt:
            max_cnt, min_grade = cnt, i
        elif cnt == max_cnt and i < min_grade:
            min_grade = i

    return f'{max_cnt} {min_grade}'

print(main())


# 32412 KB / 116 ms
def main():
    from sys import stdin

    new_input = stdin.readline
    N = int(new_input())
    max_cnt = min_grade = 0
    check_list = [0] * 6
    for _ in range(N):
        grades = set(map(int, new_input().split()))
        for grade in range(1, 6):
            if grade in grades:
                check_list[grade] += 1
            else:
                cnt = check_list[grade]
                if cnt:
                    if cnt > max_cnt:
                        max_cnt, min_grade = cnt, grade
                    elif cnt == max_cnt and grade < min_grade:
                        min_grade = grade
                    check_list[grade] = 0

    for i in grades:
        cnt = check_list[i]
        if cnt > max_cnt:
            max_cnt, min_grade = cnt, i
        elif cnt == max_cnt and i < min_grade:
            min_grade = i

    return f'{max_cnt} {min_grade}'

print(main())