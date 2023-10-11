#231011
N = int(input())
found = False

def find_answer(answer, level=1):
    global found
    if found:
        return
    if level == N:
        print(answer)
        found = True
        return
    for i in range(1, 4):
        new_answer = answer + str(i)
        for j in range(1, (level+1)//2+1):
            str1, str2 = new_answer[level-j+1:], new_answer[level-2*j+1:level-j+1]
            if str1 == str2:
                break
        else:
            find_answer(new_answer, level+1)

for i in range(1, 4):
    if found:
        break
    find_answer(str(i))
