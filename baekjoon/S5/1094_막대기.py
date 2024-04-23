# 240423
# 31120 KB / 52 ms
X = int(input())
def cnt_one(num):
    if num <= 1:
        return num
    return num%2 + cnt_one(num//2)

print(cnt_one(X))