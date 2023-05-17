#230517
num_mk = input()
cnt_m = 0
min_num = max_num = ''
for num in num_mk:
    if num == 'M':
        cnt_m += 1
    else:
        if cnt_m > 0:
            min_num += '1' + '0' * (cnt_m-1) + '5'
            max_num += '5' + '0' * cnt_m
        else:
            min_num += '5'
            max_num += '5'
        cnt_m = 0
if cnt_m > 0:
    min_num += '1' + '0' * (cnt_m - 1)
    max_num += '1' * cnt_m
print(max_num, min_num, sep='\n')


#
def to_decimal():
    num_mk = input()
    cnt_m = 0
    min_num = max_num = ''
    for num in num_mk:
        if num == 'M':
            cnt_m += 1
        else:
            if cnt_m > 0:
                min_num += '1' + '0' * (cnt_m - 1) + '5'
                max_num += '5' + '0' * cnt_m
            else:
                min_num += '5'
                max_num += '5'
            cnt_m = 0
    if cnt_m > 0:
        min_num += '1' + '0' * (cnt_m - 1)
        max_num += '1' * cnt_m
    print(max_num, min_num, sep='\n')

to_decimal()


