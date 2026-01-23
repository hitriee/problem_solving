# 260123
# 32412 KB / 36 ms
def main():
    from sys import stdin

    new_input = stdin.readline

    N = int(new_input())
    str_arr = [new_input().rstrip() for _ in range(N)]
    left, right = 0, N-1
    new_str = ''
    while left <= right:
        left_str, right_str = str_arr[left], str_arr[right]
        if left_str < right_str:
            new_str += left_str
            left += 1
        elif left_str > right_str:
            new_str += right_str
            right -= 1
        else:
            start, end = left+1, right-1
            while start <= end:
                start_str, end_str = str_arr[start], str_arr[end]
                if start_str < end_str:
                    new_str += left_str
                    left += 1
                    break
                elif start_str > end_str:
                    new_str += right_str
                    right -= 1
                    break
                start += 1
                end -= 1
            else:
                left += 1
                new_str += left_str


    answer = ''
    for i in range(len(new_str)//80+1):
        answer += new_str[i*80:i*80+80] + '\n'

    return answer.rstrip()

print(main())





# 32412 KB / 32 ms
def main():
    from sys import stdin

    new_input = stdin.readline

    N = int(new_input())
    str_arr = [new_input().rstrip() for _ in range(N)]
    left, right = 0, N - 1
    arr = []
    while left <= right:
        left_str, right_str = str_arr[left], str_arr[right]
        if left_str < right_str:
            arr.append(left_str)
            left += 1
        elif left_str > right_str:
            arr.append(right_str)
            right -= 1
        else:
            start, end = left + 1, right - 1
            while start <= end:
                start_str, end_str = str_arr[start], str_arr[end]
                if start_str < end_str:
                    arr.append(left_str)
                    left += 1
                    break
                elif start_str > end_str:
                    arr.append(right_str)
                    right -= 1
                    break
                start += 1
                end -= 1
            else:
                left += 1
                arr.append(left_str)

    answer = ''
    for i in range(len(arr) // 80 + 1):
        answer += ''.join(arr[i * 80:i * 80 + 80]) + '\n'

    return answer.rstrip()


print(main())






# 32412 KB / 32 ms
def main():
    from sys import stdin

    new_input = stdin.readline

    N = int(new_input())
    str_arr = [new_input().rstrip() for _ in range(N)]
    left, right = 0, N - 1
    arr = []
    while left <= right:
        start, end = left, right
        left_str, right_str = str_arr[left], str_arr[right]
        while start <= end:
            start_str, end_str = str_arr[start], str_arr[end]
            if start_str < end_str:
                arr.append(left_str)
                left += 1
                break
            elif start_str > end_str:
                arr.append(right_str)
                right -= 1
                break
            start += 1
            end -= 1
        else:
            left += 1
            arr.append(left_str)


    answer = ''
    for i in range(len(arr) // 80 + 1):
        answer += ''.join(arr[i * 80:i * 80 + 80]) + '\n'

    return answer.rstrip()


print(main())