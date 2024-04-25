# 240425
def solution(sequence, k):
    answer = []
    total = start = 0
    n = length = len(sequence)
    for i in range(n):
        total += sequence[i]
        while total > k:
            total -= sequence[start]
            start += 1
        if total == k:
            new_length = i - start
            if new_length < length:
                answer = [start, i]
                length = new_length

    return answer