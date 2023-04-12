#230412
# 그리디
N = int(input())
colors = input()
start = end = 0
present_color = colors[start]
for i in range(N-1, 0, -1):
    if colors[i] == present_color:
        end = i
        break
cnt = 2 if end < N-1 else 1
paint = [colors[start]] * (end+1)
while start <= end:
    if colors[start] != present_color and colors[end] != present_color:
        cnt += 1
        present_color = colors[start]
    elif colors[start] == present_color:
        start += 1
    else:
        end -= 1
print(cnt)


# 함수화
N = int(input())
colors = input()
start = 0
present_color = colors[start]
def return_end():
    for i in range(N-1, 0, -1):
        if colors[i] == present_color:
            return i
    return 0
end = return_end()
cnt = 2 if end < N-1 else 1
while start <= end:
    if colors[start] != present_color and colors[end] != present_color:
        cnt += 1
        present_color = colors[start]
    elif colors[start] == present_color:
        start += 1
    else:
        end -= 1
print(cnt)


# 전체 함수화
def calc_cnt():
    def return_end():
        for i in range(N - 1, 0, -1):
            if colors[i] == present_color:
                return i
        return 0

    def paint_problem():
        nonlocal start, end, present_color
        cnt = 2 if end < N - 1 else 1
        while start <= end:
            if colors[start] != present_color != colors[end]:
                cnt += 1
                present_color = colors[start]
            elif colors[start] == present_color:
                start += 1
            else:
                end -= 1
        return cnt

    N = int(input())
    colors = input()
    start = 0
    present_color = colors[start]
    end = return_end()
    return paint_problem()


print(calc_cnt())


# elif문 변경
def calc_cnt():
    def return_end():
        for i in range(N-1, 0, -1):
            if colors[i] == present_color:
                return i
        return 0

    def paint_problem():
        nonlocal start, end, present_color
        cnt = 2 if end < N-1 else 1
        while start <= end:
            if colors[start] != present_color != colors[end]:
                cnt += 1
                present_color = colors[start]
            else:
                if colors[start] == present_color:
                    start += 1
                else:
                    end -= 1
        return cnt

    N = int(input())
    colors = input()
    start = 0
    present_color = colors[start]
    end = return_end()
    return paint_problem()
print(calc_cnt())


# if - else문 변경
def calc_cnt():
    def return_end():
        for i in range(N-1, 0, -1):
            if colors[i] == present_color:
                return i
        return 0

    def paint_problem():
        nonlocal start, end, present_color
        cnt = 2 if end < N-1 else 1
        while start <= end:
            if colors[start] != present_color != colors[end]:
                cnt += 1
                present_color = colors[start]
            else:
                if colors[start] == present_color:
                    start += 1
                if colors[end] == present_color:
                    end -= 1
        return cnt

    N = int(input())
    colors = input()
    start = 0
    present_color = colors[start]
    end = return_end()
    return paint_problem()
print(calc_cnt())
