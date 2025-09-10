# 250910
# 32412 KB / 32 ms
def main():
    original = input().split(':')
    new = []
    N = len(original)

    if N == 8:
        for element in original:
            new.append(element.rjust(4, '0'))
    else:
        i = 0
        while i < N:
            element = original[i]
            if element == '':
                if i < N-1 and original[i+1] == '':
                    num = 10-N
                    i += 1
                else:
                    num = 9-N
                new.extend(['0'*4]*num)
            else:
                new.append(element.rjust(4, '0'))
            i += 1

    return ':'.join(new)

print(main())