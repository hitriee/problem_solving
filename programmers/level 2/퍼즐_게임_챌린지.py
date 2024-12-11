# 241211
def solution(diffs, times, limit):
    # 난이도 배열, 소요 시간 배열, 제한 시간
    N = len(diffs)

    # 이분탐색
    start, end = 1, max(diffs)
    while start <= end:
        mid = (start + end) // 2
        total = (diffs[0] - mid) * times[0] if diffs[0] > mid else 0
        total += times[0]
        for i in range(1, N):
            diff = diffs[i]
            if diff > mid:
                total += (diff - mid) * (times[i-1] + times[i])
            total += times[i]

        if total > limit:
            start = mid + 1
        else:
            end = mid - 1

    return start

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.03ms, 10.3MB)
테스트 5 〉	통과 (0.03ms, 10.3MB)
테스트 6 〉	통과 (0.03ms, 10.2MB)
테스트 7 〉	통과 (0.04ms, 10.1MB)
테스트 8 〉	통과 (6.48ms, 10.3MB)
테스트 9 〉	통과 (4.18ms, 10.1MB)
테스트 10 〉	통과 (4.04ms, 10.4MB)
테스트 11 〉	통과 (4.73ms, 10.4MB)
테스트 12 〉	통과 (2.86ms, 10.2MB)
테스트 13 〉	통과 (3.44ms, 10.2MB)
테스트 14 〉	통과 (4.05ms, 10.2MB)
테스트 15 〉	통과 (1320.96ms, 34.9MB)
테스트 16 〉	통과 (972.41ms, 34.7MB)
테스트 17 〉	통과 (767.13ms, 34.8MB)
테스트 18 〉	통과 (807.53ms, 34.6MB)
테스트 19 〉	통과 (1312.77ms, 34MB)
테스트 20 〉	통과 (835.66ms, 34.8MB)
테스트 21 〉	통과 (1538.08ms, 34.9MB)
'''


#
def solution(diffs, times, limit):
    # 난이도 배열, 소요 시간 배열, 제한 시간
    N = len(diffs)

    # 이분탐색
    start, end = 1, max(diffs)
    while start <= end:
        mid = (start + end) // 2
        total = (diffs[0] - mid) * times[0] if diffs[0] > mid else 0
        total += times[0]
        for i in range(1, N):
            if total > limit:
                start = mid + 1
                break
            diff = diffs[i]
            if diff > mid:
                total += (diff - mid) * (times[i - 1] + times[i])
            total += times[i]
        else:
            if total > limit:
                start = mid + 1
            else:
                end = mid - 1

    return start

'''
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.03ms, 10.3MB)
테스트 5 〉	통과 (0.03ms, 10.3MB)
테스트 6 〉	통과 (0.05ms, 10.2MB)
테스트 7 〉	통과 (0.03ms, 10.2MB)
테스트 8 〉	통과 (3.17ms, 10.3MB)
테스트 9 〉	통과 (6.69ms, 10.3MB)
테스트 10 〉	통과 (2.02ms, 10.4MB)
테스트 11 〉	통과 (4.05ms, 10.4MB)
테스트 12 〉	통과 (4.01ms, 10.3MB)
테스트 13 〉	통과 (3.83ms, 10.1MB)
테스트 14 〉	통과 (4.33ms, 10.1MB)
테스트 15 〉	통과 (1036.45ms, 35.1MB)
테스트 16 〉	통과 (1027.20ms, 34.9MB)
테스트 17 〉	통과 (684.04ms, 34.9MB)
테스트 18 〉	통과 (847.53ms, 34.6MB)
테스트 19 〉	통과 (1422.79ms, 34MB)
테스트 20 〉	통과 (335.52ms, 34.9MB)
테스트 21 〉	통과 (1532.41ms, 35MB)
'''