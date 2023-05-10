#230510
# 이분탐색
N = int(input())
bus_list = list(map(int, input().split()))
cnt = 0
for i in range(N-1):
    bus1 = bus_list[i]
    smaller, larger = [], []
    for j in range(i+1, N):
        bus2 = bus_list[j]
        if bus2 < bus1:
            smaller.append(j)
        else:
            larger.append(j)

    len_smaller, len_larger = len(smaller), len(larger)

    if len_smaller >= len_larger:
        for j in larger:
            start, end = 0, len_smaller - 1
            while start <= end:
                mid = (start+end)//2
                k = smaller[mid]
                if k > j:
                    end = mid - 1
                else:
                    start = mid + 1
            cnt += len_smaller - start
    else:
        for k in smaller:
            start, end = 0, len_larger - 1
            while start <= end:
                mid = (start+end)//2
                j = larger[mid]
                if k > j:
                    start = mid + 1
                else:
                    end = mid - 1
            cnt += start
print(cnt)


#
def fill_list():
    for j in range(i+1, N):
        bus2 = bus_list[j]
        if bus2 < bus1:
            smaller.append(j)
        else:
            larger.append(j)

def binary_search():
    each_cnt = 0
    len_smaller, len_larger = len(smaller), len(larger)
    if len_smaller >= len_larger:
        for j in larger:
            start, end = 0, len_smaller - 1
            while start <= end:
                mid = (start + end) // 2
                k = smaller[mid]
                if k > j:
                    end = mid - 1
                else:
                    start = mid + 1
            each_cnt += len_smaller - start
    else:
        for k in smaller:
            start, end = 0, len_larger - 1
            while start <= end:
                mid = (start + end) // 2
                j = larger[mid]
                if k > j:
                    start = mid + 1
                else:
                    end = mid - 1
            each_cnt += start
    return each_cnt

N = int(input())
bus_list = list(map(int, input().split()))
cnt = 0
for i in range(N-1):
    smaller, larger = [], []
    bus1 = bus_list[i]
    fill_list()
    cnt += binary_search()

print(cnt)


#
def fill_list():
    for j in range(i+1, N):
        bus2 = bus_list[j]
        if bus2 < bus1:
            smaller.append(j)
        else:
            larger.append(j)

def binary_search():
    each_cnt = 0
    len_smaller, len_larger = len(smaller), len(larger)
    if len_smaller >= len_larger:
        for j in larger:
            start, end = 0, len_smaller - 1
            while start <= end:
                mid = (start + end) // 2
                k = smaller[mid]
                if k > j:
                    end = mid - 1
                else:
                    start = mid + 1
            each_cnt += len_smaller - start
    else:
        for k in smaller:
            start, end = 0, len_larger - 1
            while start <= end:
                mid = (start + end) // 2
                j = larger[mid]
                if k > j:
                    start = mid + 1
                else:
                    end = mid - 1
            each_cnt += start
    return each_cnt

N = int(input())
bus_list = list(map(int, input().split()))
cnt = 0
smaller, larger = [], [] # smaller => k, larger => j (i < j < k)
for i in range(N-1):
    bus1 = bus_list[i]
    fill_list()
    cnt += binary_search()
    smaller.clear()
    larger.clear()

print(cnt)


#
def fill_list():
    for j in range(i+1, N):
        bus2 = bus_list[j]
        if bus2 < bus1:
            smaller.append(j)
        else:
            larger.append(j)

def binary_search():
    each_cnt = 0
    len_smaller, len_larger = len(smaller), len(larger)
    if len_smaller >= len_larger:
        for j in larger:
            start, end = 0, len_smaller - 1
            while start <= end:
                mid = (start + end) // 2
                k = smaller[mid]
                if k > j:
                    end = mid - 1
                else:
                    start = mid + 1
            each_cnt += len_smaller - start
    else:
        for k in smaller:
            start, end = 0, len_larger - 1
            while start <= end:
                mid = (start + end) // 2
                j = larger[mid]
                if k > j:
                    start = mid + 1
                else:
                    end = mid - 1
            each_cnt += start
    return each_cnt

N = int(input())
bus_list = list(map(int, input().split()))
cnt = 0
smaller, larger = [], [] # smaller => k, larger => j (i < j < k)
for i in range(N-2):
    bus1 = bus_list[i]
    fill_list()
    cnt += binary_search()
    smaller.clear()
    larger.clear()

print(cnt)

