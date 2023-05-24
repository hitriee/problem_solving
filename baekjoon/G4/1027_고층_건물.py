#230524
N = int(input())
building = list(map(int, input().split()))
cnt_list = []
for i in range(N):
    ref = building[i]
    cnt = 0
    slope_limit = 1e9 # 기울기의 최솟값
    for j in range(i-1, -1, -1):
        slope = (ref - building[j])/(i-j)
        if slope_limit > slope:
            slope_limit = slope
            cnt += 1
    slope_limit = -1e9 # 기울기의 최댓값
    for j in range(i+1, N, 1):
        slope = (ref - building[j])/(i-j)
        if slope_limit < slope:
            slope_limit = slope
            cnt += 1
    cnt_list.append(cnt)
print(max(cnt_list))


#
def find_max_cnt():
    N = int(input())
    building = list(map(int, input().split()))
    cnt_list = []
    for i in range(N):
        ref = building[i]
        cnt = 0
        min_limit, max_limit = [1e9, -1e9] # 기울기의 최솟값
        for j in range(i-1, -1, -1):
            slope = (ref - building[j])/(i-j)
            if min_limit > slope:
                min_limit = slope
                cnt += 1
        for j in range(i+1, N, 1):
            slope = (ref - building[j])/(i-j)
            if max_limit < slope:
                max_limit = slope
                cnt += 1
        cnt_list.append(cnt)
    return max(cnt_list)
print(find_max_cnt())