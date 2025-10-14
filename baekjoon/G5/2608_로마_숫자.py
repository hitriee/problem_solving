# 251014
# 32544 KB / 36 ms
def main():
    rome_dict = {
        'I': 1,
        'IV': 4,
        'V': 5,
        'IX': 9,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'CD': 400,
        'D': 500,
        'CM': 900,
        'M': 1000,
    }

    num_arr = [('M', (1000,)), ('C', (100, 'D', 'M')), ('X', (10, 'L', 'C')), ('I', (1, 'V', 'X'))]


    def rome_to_num(rome):
        num = idx = 0
        limit = len(rome)
        while idx < limit:
            for alp, dif in (rome[idx:idx+2], 2), (rome[idx], 1):
                if rome_dict.get(alp):
                    num += rome_dict[alp]
                    idx += dif
                    break
        return num

    def num_to_rome(initial):
        result = ''
        for rome, info in num_arr:
            quot, remain = divmod(initial, info[0])
            initial = remain
            if quot == 0:
                continue
            elif quot < 4:
                result += rome * quot
            elif quot == 4:
                result += rome + info[1]
            elif quot < 9:
                result += info[1] + rome * (quot - 5)
            else:
                result += rome + info[2]

        return result

    target = rome_to_num(input())
    target += rome_to_num(input())

    return f'{target}\n{num_to_rome(target)}'

print(main())