# 240617
def solution(weights):
    answer = 0
    cnt = {}
    multiple = [3 / 2, 2, 4 / 3]
    for weight in weights:
        cnt[weight] = cnt.get(weight, 0) + 1

    for weight in cnt:
        val = cnt[weight]
        answer += (val * (val - 1)) // 2
        for num in multiple:
            answer += (cnt.get(weight * num, 0)) * val

    return answer