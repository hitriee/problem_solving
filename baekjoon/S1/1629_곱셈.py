# 230819
A, B, C = map(int, input().split())

def power_num(num, exponential, div_num):
    if exponential == 1:
        return num % div_num
    result = power_num(num, exponential//2, div_num)
    square = result * result
    if exponential%2:
        return (square * num) % div_num
    return square % div_num

print(power_num(A, B, C))


#
A, B, C = map(int, input().split())

def power_num(num, exponential, div_num):
    if exponential == 1:
        return num % div_num
    result = power_num(num, exponential//2, div_num)
    square = result * result
    if exponential%2:
        return (square * num) % div_num
    return square % div_num

remain = A%C
if A == 1:
    print(1)
elif remain <= 1 or B == 1:
    print(remain)
else:
    print(power_num(A, B, C))