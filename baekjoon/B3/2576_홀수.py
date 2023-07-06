#230706
odd_num_list = []
for _ in range(7):
    num = int(input())
    if num%2:
        odd_num_list.append(num)

if odd_num_list:
    print(sum(odd_num_list), min(odd_num_list), sep='\n')
else:
    print(-1)
