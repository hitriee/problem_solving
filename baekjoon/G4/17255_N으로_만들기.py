# 241025
# 37948 KB / 76 ms
def main():
    N = input()
    num_set, limit = set(N), len(N)
    check, new_check = {i: 1 for i in num_set}, {}

    for _ in range(limit-1):
        for num in check:
            for i in num_set:
                for new_num in {num+i, i+num}:
                    new_check[new_num] = new_check.get(new_num, 0) + check[num]
        check = dict(new_check)
        new_check.clear()

    return check[N]

print(main())



# 31120 KB / 32 ms
def main():
    N = input()
    limit = len(N)
    if limit == 1:
        return 1
    
    num_set = set(N)
    check, new_check = {i: 1 for i in num_set}, {N[i:i+2] : 0 for i in range(limit-1)}
    for length in range(2, limit+1):
        for num in check:
            for i in num_set:
                for new_num in {num+i, i+num}:
                    if new_check.get(new_num, -1) != -1:
                        new_check[new_num] += check[num]
        
        check = dict(new_check)
        new_check = {N[i:i+length+1]: 0 for i in range(limit-length)}

    return check[N]

print(main())



# 31120 KB / 32 ms
def main():
    N = input()
    limit = len(N)
    if limit == 1:
        return 1

    num_set = set(N)
    check, new_check = {i: 1 for i in num_set}, {N[i:i+2] : 0 for i in range(limit-1)}
    for length in range(2, limit+1):
        for new_num in new_check:
            for num in {new_num[:-1], new_num[1:]}:
                new_check[new_num] += check[num]

        check = dict(new_check)
        new_check = {N[i:i+length+1]: 0 for i in range(limit-length)}

    return check[N]

print(main())



# 31120 KB / 32 ms
def main():
    N = input()
    limit = len(N)
    if limit == 1:
        return 1

    check, new_check = {i: 1 for i in N}, {N[i:i+2] : 0 for i in range(limit-1)}
    for length in range(2, limit+1):
        for new_num in new_check:
            for num in {new_num[:-1], new_num[1:]}:
                new_check[new_num] += check[num]

        check = dict(new_check)
        new_check = {N[i:i+length+1]: 0 for i in range(limit-length)}

    return check[N]

print(main())
