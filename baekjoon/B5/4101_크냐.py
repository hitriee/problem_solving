# 230417
# 구현
while True:
    first, second = map(int, input().split())
    if first == second == 0:
        break
    if first > second:
        print('Yes')
    else:
        print('No')
