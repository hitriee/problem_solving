# 231121
# 31120 KB / 48 ms
N = int(input())
for _ in range(N):
    kind, value = input().split()
    if kind == '1':
        splitted_value = list(map(int, value.split('.')))
        coverted_num = 0
        multiple = 1
        for i in range(7, -1, -1):
            coverted_num += splitted_value[i] * multiple
            multiple *= 256

        print(coverted_num)

    else:
        splitted_value = []
        value = int(value)
        div = 256
        for _ in range(8):
            splitted_value.append(str(value%div))
            value //= div

        print('.'.join(splitted_value[::-1]))