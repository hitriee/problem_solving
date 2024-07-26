# 240726
# 56024 KB / 268 ms
def calc_min_cost():
    from sys import stdin
    
    def int_input(func=int):
        return map(func, stdin.readline().split())
    
    def minus_one(x):
        return int(x) - 1
    
    def fill_check():
        city = order[0]
        for i in range(1, M):
            num = order[i]
            small, large = sorted([city, num])
            check[small] += 1
            check[large] -= 1
            city = num

        for i in range(1, N - 1):
            check[i] += check[i - 1]
            
    def conf_cost():
        min_cost = 0
        for i in range(N - 1):
            a, b, c = cost_table[i]
            min_cost += min(check[i] * a, check[i] * b + c)
        
        return min_cost
    
    
    N, M = int_input()
    order = tuple(int_input(minus_one))
    check = [0] * N
    cost_table = [tuple(int_input()) for _ in range(N-1)]
    
    fill_check()
    return conf_cost()
    
print(calc_min_cost())




# 42080 KB / 208 ms
def calc_min_cost():
    from sys import stdin

    def int_input(func=int):
        return map(func, stdin.readline().split())

    def minus_one(x):
        return int(x) - 1

    def fill_check():
        city = order[0]
        for i in range(1, M):
            num = order[i]
            small, large = sorted([city, num])
            check[small] += 1
            check[large] -= 1
            city = num

        for i in range(1, N - 1):
            check[i] += check[i - 1]

    def conf_cost():
        min_cost = 0
        for i in range(N - 1):
            a, b, c = int_input()
            min_cost += min(check[i] * a, check[i] * b + c)

        return min_cost


    N, M = int_input()
    order = tuple(int_input(minus_one))
    check = [0] * N
    
    fill_check()
    return conf_cost()

print(calc_min_cost())



# 41948 KB / 232 ms
def calc_min_cost():
    from sys import stdin

    def int_input(func=int):
        return map(func, stdin.readline().split())

    def minus_one(x):
        return int(x) - 1

    def fill_check():
        city = order[0]
        for i in range(1, M):
            num = order[i]
            small, large = sorted([city, num])
            check[small] += 1
            check[large] -= 1
            city = num

        for i in range(1, N - 1):
            check[i] += check[i - 1]

    def conf_cost():
        min_cost = 0
        for freq in check:
            a, b, c = int_input()
            min_cost += min(freq * a, freq * b + c)

        return min_cost


    N, M = int_input()
    order = tuple(int_input(minus_one))
    check = [0] * N

    fill_check()
    check.pop()
    return conf_cost()

print(calc_min_cost())
