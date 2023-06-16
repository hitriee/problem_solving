#230616
N = int(input())
solution = list(map(int, input().split()))
solution.sort()
if solution[0] >= 0:
    print(*solution[:2])
elif solution[-1] <= 0:
    print(*solution[-2:])
else:
    min_abs_dif = 1e9
    for i in range(N):
        if solution[i] >= 0:
            if 2 <= i:
                answer = solution[i-2:i]
                min_abs_dif = -sum(answer)
                if i <= N-2:
                    if sum(solution[i:i+2]) < min_abs_dif:
                        answer = solution[i:i+2]
                        min_abs_dif = sum(answer)
            else:
                answer = solution[i:i + 2]
                min_abs_dif = sum(answer)
            break
    left, right = i-1, i
    left_val, right_val = solution[left], solution[right]

    while True:
        dif = left_val + right_val
        if dif < 0:
            if -dif < min_abs_dif:
                min_abs_dif = -dif
                answer = [left_val, right_val]
            right += 1
            if right == N:
                break
            right_val = solution[right]
        else:
            if dif < min_abs_dif:
                min_abs_dif = dif
                answer = [left_val, right_val]
            left -= 1
            if left < 0:
                break
            left_val = solution[left]

    print(*answer)


#
def return_two():
    N = int(input())
    solution = list(map(int, input().split()))
    solution.sort()

    if solution[0] >= 0:
        return solution[:2]

    elif solution[-1] <= 0:
        return solution[-2:]

    def find_index():
        nonlocal min_abs_dif, answer
        for i in range(N):
            if solution[i] >= 0:
                if 2 <= i:
                    answer = solution[i-2:i]
                    min_abs_dif = -sum(answer)
                    if i <= N-2:
                        if sum(solution[i:i+2]) < min_abs_dif:
                            answer = solution[i:i+2]
                            min_abs_dif = sum(answer)
                else:
                    answer = solution[i:i + 2]
                    min_abs_dif = sum(answer)

                return i

    min_abs_dif = 0
    answer = []
    right = find_index()
    left = right - 1
    left_val, right_val = solution[left], solution[right]

    while True:
        dif = left_val + right_val
        if dif < 0:
            if -dif < min_abs_dif:
                min_abs_dif = -dif
                answer = [left_val, right_val]
            right += 1
            if right == N:
                break
            right_val = solution[right]
        else:
            if dif < min_abs_dif:
                min_abs_dif = dif
                answer = [left_val, right_val]
            left -= 1
            if left < 0:
                break
            left_val = solution[left]

    return answer

print(*return_two())

