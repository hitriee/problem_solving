# 251203
# 36232 KB / 212 ms
def main():
    from sys import stdin

    new_input = stdin.readline
    N = int(new_input())
    LIMIT = 8000*12 + 1
    arr = [0] * LIMIT

    def date_to_num(year, month):
        return (year - 2000) * 12 + (month - 1)

    for _ in range(N):
        duration = new_input().split()
        for i in range(2):
            year, month = map(int, duration[i].split('-'))
            if i == 0:
                arr[date_to_num(year, month)] += 1
            else:
                arr[date_to_num(year, month)+1] -= 1


    for i in range(1, LIMIT):
        arr[i] += arr[i-1]

    max_val, answer_i = 0, 0
    for i in range(LIMIT):
        val = arr[i]
        if val > max_val:
            max_val = val
            answer_i = i


    return f"{2000 + answer_i // 12}-{str(answer_i % 12 + 1).rjust(2, '0')}"

print(main())



# 36232 KB / 220 ms
def main():
    from sys import stdin

    new_input = stdin.readline
    N = int(new_input())
    LIMIT = 8000*12 + 1
    arr = [0] * LIMIT
    start, end = LIMIT, 0

    def date_to_num(year, month):
        return (year - 2000) * 12 + (month - 1)

    for _ in range(N):
        duration = new_input().split()
        for i in range(2):
            year, month = map(int, duration[i].split('-'))
            date_num = date_to_num(year, month)
            if i == 0:
                arr[date_num] += 1
                if date_num < start:
                    start = date_num
            else:
                date_num += 1
                arr[date_num] -= 1
                if date_num > end:
                    end = date_num


    for i in range(start+1, end):
        arr[i] += arr[i-1]

    max_val, answer_i = 0, 0
    for i in range(start, end):
        val = arr[i]
        if val > max_val:
            max_val = val
            answer_i = i

    return f"{2000 + answer_i // 12}-{str(answer_i % 12 + 1).rjust(2, '0')}"

print(main())