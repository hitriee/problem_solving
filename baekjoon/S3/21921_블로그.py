#230504
# 슬라이딩 윈도
N, X = map(int, input().split())
visitor_cnt = list(map(int, input().split()))
max_visitor, visitor = 0, sum(visitor_cnt[:X-1])
cnt = 1
for i in range(N-X+1):
    visitor += visitor_cnt[i+X-1]
    if visitor > max_visitor:
        max_visitor = visitor
        cnt = 1
    elif visitor == max_visitor:
        cnt += 1
    visitor -= visitor_cnt[i]

if max_visitor:
    print(max_visitor)
    print(cnt)
else:
    print('SAD')


#
def return_answer():
    max_visitor, visitor = 0, sum(visitor_cnt[:X-1])
    cnt = 1
    for i in range(N-X+1):
        visitor += visitor_cnt[i+X-1]
        if visitor > max_visitor:
            max_visitor = visitor
            cnt = 1
        elif visitor == max_visitor:
            cnt += 1
        visitor -= visitor_cnt[i]

    if max_visitor:
        return f'{max_visitor}\n{cnt}'
    return 'SAD'

N, X = map(int, input().split())
visitor_cnt = list(map(int, input().split()))
print(return_answer())
