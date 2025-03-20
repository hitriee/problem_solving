# 250320
def solution(n, stations, w):
    from math import ceil
    # 아파트 개수, 현재 기지국 설치된 아파트, 전파 도달 거리
    # cnt : 증설해야할 기지국 개수
    cnt, start = 0, 1
    full_range = 2 * w + 1
    for station in stations:
        if station - w > start:
            cnt += ceil((station - w - start) / full_range)
        start = station + w + 1

    if n >= start:
        cnt += ceil((n - start + 1) / full_range)

    return cnt