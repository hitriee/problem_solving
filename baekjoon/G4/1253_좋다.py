#230719
N = int(input())
num_list = list(map(int, input().split()))
num_list.sort()
num_dict = {}
for num in num_list:
    if num_dict.get(num):
        num_dict[num] += 1
    else:
        num_dict[num] = 1

keys = list(num_dict.keys())
length = len(keys)

def find_target():
    global cnt
    for j in range(length):
        plus_num = keys[j]
        if num_dict.get(num - plus_num):
            if num == 0 and plus_num == 0:
                if num_dict[0] >= 3:
                    cnt += value
                    break
            elif num == plus_num or plus_num == 0:
                if num_dict[num] >= 2:
                    cnt += value
                    break
            elif plus_num*2 != num:
                cnt += value
                break
            elif num_dict.get(plus_num) >= 2:
                cnt += value
                break

cnt = 0
for i in range(length):
    num = keys[i]
    value = num_dict[keys[i]]
    find_target()

print(cnt)


#
def cnt_good_num():
    N = int(input())
    num_list = list(map(int, input().split()))
    num_list.sort()
    num_dict = {}
    for num in num_list:
        if num_dict.get(num):
            num_dict[num] += 1
        else:
            num_dict[num] = 1

    keys = list(num_dict.keys())
    keys.sort()
    length = len(keys)

    def find_target():
        nonlocal cnt
        for j in range(length):
            plus_num = keys[j]
            if num_dict.get(num - plus_num):
                if num == 0 and plus_num == 0:
                    if num_dict[0] >= 3:
                        cnt += value
                        break
                elif num == plus_num or plus_num == 0:
                    if num_dict[num] >= 2:
                        cnt += value
                        break
                elif plus_num*2 != num:
                    cnt += value
                    break
                elif num_dict.get(plus_num) >= 2:
                    cnt += value
                    break

    cnt = 0
    for i in range(length):
        num = keys[i]
        value = num_dict[keys[i]]
        find_target()

    return cnt

print(cnt_good_num())