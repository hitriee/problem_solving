#230815
len_w, len_s = map(int, input().split())
word = input()
string = input()
check_w, check_s = {}, {}

for alp in word:
    if check_w.get(alp):
        check_w[alp] += 1
    else:
        check_w[alp] = 1

for i in range(len_w-1):
    alp = string[i]
    if check_s.get(alp):
        check_s[alp] += 1
    else:
        check_s[alp] = 1

before, cnt = False, 0

for i in range(len_w-1, len_s):
    alp = string[i]
    if check_s.get(alp):
        check_s[alp] += 1
    else:
        check_s[alp] = 1

    if before:
        if string[i] != string[i-len_w]:
            before = False
        else:
            cnt += 1
    else:
        for alp in check_w:
            if check_w[alp] != check_s.get(alp):
                break
        else:
            before = True
            cnt += 1

    alp = string[i-len_w+1]
    check_s[alp] -= 1

print(cnt)

#
def cnt_maya_word():
    len_w, len_s = map(int, input().split())
    word = input()
    string = input()
    check_w, check_s = {}, {}

    for alp in word:
        if check_w.get(alp):
            check_w[alp] += 1
        else:
            check_w[alp] = 1

    for i in range(len_w - 1):
        alp = string[i]
        if check_s.get(alp):
            check_s[alp] += 1
        else:
            check_s[alp] = 1

    before, cnt = False, 0

    for i in range(len_w - 1, len_s):
        alp = string[i]
        if check_s.get(alp):
            check_s[alp] += 1
        else:
            check_s[alp] = 1

        if before:
            if string[i] != string[i - len_w]:
                before = False
            else:
                cnt += 1
        else:
            for alp in check_w:
                if check_w[alp] != check_s.get(alp):
                    break
            else:
                before = True
                cnt += 1

        alp = string[i - len_w + 1]
        check_s[alp] -= 1

    return cnt


print(cnt_maya_word())


#
def cnt_maya_word():
    len_w, len_s = map(int, input().split())
    word = input()
    string = input()
    check_w, check_s = {}, {}
    before, cnt = False, 0

    for alp in word:
        if check_w.get(alp):
            check_w[alp] += 1
        else:
            check_w[alp] = 1

    for i in range(len_w - 1):
        alp = string[i]
        if check_s.get(alp):
            check_s[alp] += 1
        else:
            check_s[alp] = 1


    for i in range(len_w - 1, len_s):
        alp = string[i]
        if check_s.get(alp):
            check_s[alp] += 1
        else:
            check_s[alp] = 1

        if before:
            if string[i] != string[i - len_w]:
                before = False
            else:
                cnt += 1
        else:
            for alp in check_w:
                if check_w[alp] != check_s.get(alp):
                    break
            else:
                before = True
                cnt += 1

        check_s[string[i - len_w + 1]] -= 1

    return cnt


print(cnt_maya_word())


#
def cnt_maya_word():
    len_w, len_s = map(int, input().split())
    word = input()
    string = input()
    check_w, check_s = {}, {}
    large_a, small_a = ord('A'), ord('a')
    before, cnt = False, 0
    for i in range(26):
        large_key, small_key = chr(large_a+i), chr(small_a+i)
        check_w[large_key] = check_s[large_key] = 0
        check_w[small_key] = check_s[small_key] = 0


    for alp in word:
        check_w[alp] += 1

    for i in range(len_w - 1):
        check_s[string[i]] += 1


    for i in range(len_w - 1, len_s):
        check_s[string[i]] += 1

        if before:
            if string[i] != string[i - len_w]:
                before = False
            else:
                cnt += 1
        else:
            for key in check_w:
                if check_w[key] != check_s[key]:
                    break
            else:
                before = True
                cnt += 1

        check_s[string[i - len_w + 1]] -= 1

    return cnt


print(cnt_maya_word())