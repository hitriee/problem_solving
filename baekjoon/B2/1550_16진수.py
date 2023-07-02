#230702
num = input()
answer = 0
converted_num = {str(i):i for i in range(10)}
for i in range(6):
    converted_num[chr(ord('A')+i)] = i+10

multiply = 1
for i in range(len(num)-1, -1, -1):
    answer += converted_num[num[i]] * multiply
    multiply *= 16

print(answer)

#
print(int(input(), 16))


#
def return_answer():
    num = input()
    answer = 0
    converted_num = {str(i):i for i in range(10)}
    for i in range(6):
        converted_num[chr(ord('A')+i)] = i+10

    multiply = 1
    for i in range(len(num)-1, -1, -1):
        answer += converted_num[num[i]] * multiply
        multiply *= 16

    return answer

print(return_answer())