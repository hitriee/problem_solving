# 241213
def calc_time(time_str):
    hour, minute = map(int, time_str.split(':'))
    return hour * 60 + minute


def two_len_str(num):
    if num < 10:
        return f'0{num}'
    return f'{num}'


def solution(n, t, m, timetable):
    # 운행 횟수, 운행 간격, 탈 수 있는 최대 크루, 크루가 대기열에 도착하는 시간
    timetable.sort()
    bus_time, i = 9 * 60, 0
    people = len(timetable)
    answer = calc_time(timetable[0]) - 1

    for _ in range(n - 1):
        limit = min(i + m, people)
        for j in range(i, limit):
            time = calc_time(timetable[j])
            if time > bus_time:
                i = j
                break
        else:
            i = limit

        bus_time += t

    limit = min(i + m, people)
    for j in range(i, limit):
        time = calc_time(timetable[j])
        if time > bus_time:
            answer = bus_time
            break
    else:
        if limit == i + m:
            answer = calc_time(timetable[limit - 1]) - 1
        else:
            answer = bus_time

    answer_h, answer_m = map(two_len_str, divmod(answer, 60))

    return f'{answer_h}:{answer_m}'

'''
테스트 1 〉	통과 (0.03ms, 10.4MB)
테스트 2 〉	통과 (0.03ms, 10.4MB)
테스트 3 〉	통과 (0.03ms, 10.4MB)
테스트 4 〉	통과 (0.04ms, 10.3MB)
테스트 5 〉	통과 (0.05ms, 10.2MB)
테스트 6 〉	통과 (0.03ms, 10.4MB)
테스트 7 〉	통과 (0.60ms, 10.3MB)
테스트 8 〉	통과 (0.03ms, 10.2MB)
테스트 9 〉	통과 (0.03ms, 10.4MB)
테스트 10 〉	통과 (0.03ms, 10.3MB)
테스트 11 〉	통과 (0.04ms, 10.4MB)
테스트 12 〉	통과 (0.44ms, 10.4MB)
테스트 13 〉	통과 (0.37ms, 10.3MB)
테스트 14 〉	통과 (0.07ms, 10.4MB)
테스트 15 〉	통과 (0.10ms, 10.3MB)
테스트 16 〉	통과 (0.27ms, 10.2MB)
테스트 17 〉	통과 (0.53ms, 10.4MB)
테스트 18 〉	통과 (0.28ms, 10.3MB)
테스트 19 〉	통과 (0.28ms, 10.2MB)
테스트 20 〉	통과 (0.23ms, 10.4MB)
테스트 21 〉	통과 (0.54ms, 10.4MB)
테스트 22 〉	통과 (0.27ms, 10.4MB)
테스트 23 〉	통과 (0.18ms, 10.3MB)
테스트 24 〉	통과 (0.55ms, 10.3MB)
'''


#
def calc_time(time_str):
    hour, minute = map(int, time_str.split(':'))
    return hour * 60 + minute


def two_len_str(num):
    if num < 10:
        return f'0{num}'
    return f'{num}'


def solution(n, t, m, timetable):
    # 운행 횟수, 운행 간격, 탈 수 있는 최대 크루, 크루가 대기열에 도착하는 시간
    timetable.sort()
    bus_time, i = 9 * 60, 0
    people = len(timetable)
    answer = calc_time(timetable[0]) - 1

    for _ in range(n):
        limit = min(i + m, people)
        for j in range(i, limit):
            time = calc_time(timetable[j])
            if time > bus_time:
                answer = bus_time
                i = j
                break
        else:
            if limit == i + m:
                answer = calc_time(timetable[limit - 1]) - 1
            else:
                answer = bus_time
            i = limit

        bus_time += t

    answer_h, answer_m = map(two_len_str, divmod(answer, 60))

    return f'{answer_h}:{answer_m}'

'''
정확성  테스트
테스트 1 〉	통과 (0.05ms, 10.2MB)
테스트 2 〉	통과 (0.03ms, 10.4MB)
테스트 3 〉	통과 (0.04ms, 10.4MB)
테스트 4 〉	통과 (0.04ms, 10.4MB)
테스트 5 〉	통과 (0.05ms, 10.3MB)
테스트 6 〉	통과 (0.04ms, 10.2MB)
테스트 7 〉	통과 (0.44ms, 10.3MB)
테스트 8 〉	통과 (0.03ms, 10.4MB)
테스트 9 〉	통과 (0.04ms, 10.4MB)
테스트 10 〉	통과 (0.03ms, 10.4MB)
테스트 11 〉	통과 (0.05ms, 10.3MB)
테스트 12 〉	통과 (0.31ms, 10.4MB)
테스트 13 〉	통과 (0.31ms, 10.4MB)
테스트 14 〉	통과 (0.06ms, 10.2MB)
테스트 15 〉	통과 (0.13ms, 10.4MB)
테스트 16 〉	통과 (0.15ms, 10.3MB)
테스트 17 〉	통과 (0.63ms, 10.4MB)
테스트 18 〉	통과 (0.18ms, 10.4MB)
테스트 19 〉	통과 (0.24ms, 10.4MB)
테스트 20 〉	통과 (0.21ms, 10.3MB)
테스트 21 〉	통과 (0.52ms, 10.4MB)
테스트 22 〉	통과 (0.29ms, 10.3MB)
테스트 23 〉	통과 (0.34ms, 10.4MB)
테스트 24 〉	통과 (0.72ms, 10.4MB)
'''