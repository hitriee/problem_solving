#230709
N, L = map(int, input().split())
positions = list(map(int, input().split()))
positions.sort()
end = positions[0] + L
cnt = 1
for i in range(1, N):
    if positions[i] >= end:
        cnt += 1
        end = positions[i] + L

print(cnt)


#
def find_cnt():
    N, L = map(int, input().split())
    positions = list(map(int, input().split()))
    positions.sort()
    end = positions[0] + L
    cnt = 1
    for i in range(1, N):
        if positions[i] >= end:
            cnt += 1
            end = positions[i] + L

    return cnt

print(find_cnt())
