#230423
# 그리디
N, M = map(int, input().split())
min_package = min_each = 1000
for _ in range(M):
    package, each = map(int, input().split())
    if package < min_package:
        min_package = package
    if each < min_each:
        min_each = each
quot, remain = divmod(N, 6)
all_package = min_package * (quot+1 if remain else quot)
all_each = min_each * N
package_n_each = min_package * quot + min_each * remain
print(min(all_package, all_each, package_n_each))


# 함수화
def find_min_val():
    N, M = map(int, input().split())
    min_package = min_each = 1000
    for _ in range(M):
        package, each = map(int, input().split())
        if package < min_package:
            min_package = package
        if each < min_each:
            min_each = each
    quot, remain = divmod(N, 6)
    all_package = min_package * (quot+1 if remain else quot)
    all_each = min_each * N
    package_n_each = min_package * quot + min_each * remain
    return min(all_package, all_ea

               
# 리스트에 담은 후, 가장 작은 값 찾기
def find_min_val():
    N, M = map(int, input().split())
    package_list, each_list = [], []
    for _ in range(M):
        package, each = map(int, input().split())
        package_list.append(package)
        each_list.append(each)
    min_package = min(package_list)
    min_each = min(each_list)
    quot, remain = divmod(N, 6)
    all_package = min_package * (quot+1 if remain else quot)
    all_each = min_each * N
    package_n_each = min_package * quot + min_each * remain
    return min(all_package, all_each, package_n_each)
print(find_min_val())
               
               
# heap
def find_min_val():
    from heapq import heappush, heappop
    N, M = map(int, input().split())
    package_list, each_list = [], []
    for _ in range(M):
        package, each = map(int, input().split())
        heappush(package_list, package)
        heappush(each_list, each)
    min_package = heappop(package_list)
    min_each = heappop(each_list)
    quot, remain = divmod(N, 6)
    all_package = min_package * (quot+1 if remain else quot)
    all_each = min_each * N
    package_n_each = min_package * quot + min_each * remain
    return min(all_package, all_each, package_n_each)
print(find_min_val())
