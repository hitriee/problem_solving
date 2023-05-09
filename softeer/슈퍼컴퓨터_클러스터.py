#230509
# 이분탐색
from sys import stdin

def to_int(): return map(int, stdin.readline().rstrip().split())
def square(num): return num * num
def int_sqrt(num):
    start, end = 1, num
    while start <= end:
        mid = (start + end) // 2
        square_num = square(mid)
        if square_num > num:
            end = mid - 1
        elif square_num < num:
            start = mid + 1
        else:
            return mid
    return end

N, B = to_int()
computers = list(to_int())
computers.sort()
cnt_number = {}
for computer in computers:
    if cnt_number.get(computer):
        cnt_number[computer] += 1
    else:
        cnt_number[computer] = 1
root = int_sqrt(B)
start, end = computers[0] + 1, computers[-1] + root
answer = 0
while start <= end:
    mid = (start + end)//2
    total = 0
    for number in cnt_number:
        if number < mid:
            total += square(number - mid) * cnt_number[number]
    if total <= B:
        start = mid + 1
        if answer < mid:
            answer = mid
    else:
        end = mid - 1
print(end)


#
def calc_square():
    # 입력 받은 값을 숫자로 변환
    def to_int(): return map(int, stdin.readline().rstrip().split())
    # 숫자를 제곱
    def square(num): return num * num
    # 숫자의 제곱근보다 작거나 같은 정수 중 가장 큰 수
    def int_sqrt(num):
        start, end = 1, num
        while start <= end:
            mid = (start + end) // 2
            square_num = square(mid)
            if square_num > num:
                end = mid - 1
            elif square_num < num:
                start = mid + 1
            else:
                return mid
        return end
    # dictionary 채우기
    def fill_dict():
        for computer in computers:
            if cnt_number.get(computer):
                cnt_number[computer] += 1
            else:
                cnt_number[computer] = 1
    # 이분탐색으로 결괏값 찾기
    def find_number():
        root = int_sqrt(B)
        start, end = computers[0] + 1, computers[-1] + root
        answer = 0
        while start <= end:
            mid = (start + end)//2
            total = 0
            for number in cnt_number:
                if number < mid:
                    total += square(number - mid) * cnt_number[number]
            if total <= B:
                start = mid + 1
                if answer < mid:
                    answer = mid
            else:
                end = mid - 1
        return end

    from sys import stdin
    N, B = to_int()
    computers = list(to_int())
    computers.sort()
    cnt_number = {}
    fill_dict()
    return find_number()

print(calc_square())