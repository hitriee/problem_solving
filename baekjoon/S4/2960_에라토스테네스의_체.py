#230403
# set + 2중 반복문
N, K = map(int, input().split())
number_set = set(range(2, N+1))
cnt = 0
for num in range(2, N+1):
    if num in number_set:
        number_set.remove(num)
        cnt += 1
        if cnt == K:
            print(num)
            break
        multiple = num
        while cnt < K:
            multiple += num
            if multiple in number_set:
                cnt += 1
                number_set.remove(multiple)
            if multiple >= N:
                break
        else:
            print(multiple)
            break


# 함수형
def find_num():
    cnt = 0
    for num in range(2, N+1):
        if num in number_set:
            number_set.remove(num)
            cnt += 1
            if cnt == K:
                return num
            multiple = num
            while cnt < K:
                multiple += num
                if multiple in number_set:
                    cnt += 1
                    number_set.remove(multiple)
                if multiple >= N:
                    break
            else:
                return multiple
N, K = map(int, input().split())
number_set = set(range(2, N+1))
print(find_num())


# if문 삭제
def find_num():
    cnt = 0
    for num in range(2, N+1):
        if num in number_set:
            number_set.remove(num)
            cnt += 1
            multiple = num
            while cnt < K:
                multiple += num
                if multiple in number_set:
                    cnt += 1
                    number_set.remove(multiple)
                if multiple >= N:
                    break
            else:
                return multiple
N, K = map(int, input().split())
number_set = set(range(2, N+1))
print(find_num())


#
def find_num():
    N, K = map(int, input().split())
    cnt = 0
    number_set = set(range(2, N+1))
    for num in range(2, N+1):
        if num in number_set:
            number_set.remove(num)
            cnt += 1
            multiple = num
            while cnt < K:
                multiple += num
                if multiple in number_set:
                    cnt += 1
                    number_set.remove(multiple)
                if multiple >= N:
                    break
            else:
                return multiple
print(find_num())


# visited
#
def find_num():
    N, K = map(int, input().split())
    cnt = 0
    visited = [False] * (N+1)
    for num in range(2, N+1):
        if not visited[num]:
            visited[num] = True
            cnt += 1
            multiple = num
            while cnt < K:
                multiple += num
                if multiple > N:
                    break
                if not visited[multiple]:
                    visited[multiple] = True
                    cnt += 1
            else:
                return multiple
print(find_num())