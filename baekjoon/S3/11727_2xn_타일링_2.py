# 240320
# 31252 KB / 44 ms
n = int(input())
if n == 1:
    print(1)
elif n == 2:
    print(3)
else:
    minus_one, minus_two = 3, 1
    for i in range(2, n):
        result = (minus_one + minus_two * 2)%10007
        minus_one, minus_two = result, minus_one
    print(result)

# 31120 KB / 44 ms
n = int(input())
if n == 1:
    print(1)
elif n == 2:
    print(3)
else:
    minus_one, minus_two = 3, 1
    for i in range(2, n):
        minus_one, minus_two = (minus_one + minus_two * 2)%10007, minus_one
    print(minus_one)

# 31252 KB / 40 ms
n = int(input())

def cnt_cases(n):
    if n == 1:
        return 1

    minus_one, minus_two = 3, 1
    for i in range(2, n):
        minus_one, minus_two = (minus_one + minus_two * 2)%10007, minus_one
    return minus_one

print(cnt_cases(n))