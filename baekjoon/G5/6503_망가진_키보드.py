# 260120
# 35344 KB / 1004 ms
def main():
    while True:
        m = int(input())
        if m == 0:
            break

        sentence = input()
        n = len(sentence)
        alp_dict = {}
        start = cnt = 0

        for end in range(n):
            part_of = sentence[end]
            if alp_dict.get(part_of):
                alp_dict[part_of] += 1
            elif cnt < m:
                cnt += 1
                alp_dict[part_of] = 1
            else:
                max_len = end
                break
        else:
            max_len = n

        while start < n:
            while start < n:
                part_of = sentence[start]
                start += 1
                if alp_dict[part_of] == 1:
                    del alp_dict[part_of]
                    cnt -= 1
                    break

                alp_dict[part_of] -= 1

            while end < n:
                part_of = sentence[end]
                if alp_dict.get(part_of):
                    alp_dict[part_of] += 1
                elif cnt < m:
                    cnt += 1
                    alp_dict[part_of] = 1
                else:
                    break

                end += 1

            dif = end - start
            if max_len < dif:
                max_len = dif

        print(max_len)

main()






# 35344 KB / 1036 ms
def main():
    def find_end(end_s):
        nonlocal cnt

        for end in range(end_s, n):
            part_of = sentence[end]
            if alp_dict.get(part_of):
                alp_dict[part_of] += 1
            elif cnt < m:
                cnt += 1
                alp_dict[part_of] = 1
            else:
                return end
        return n


    while True:
        m = int(input())
        if m == 0:
            break

        sentence = input()
        n = len(sentence)
        alp_dict = {}
        start = cnt = 0

        end = max_len = find_end(0)

        while start < n:
            while start < n:
                part_of = sentence[start]
                start += 1
                if alp_dict[part_of] == 1:
                    del alp_dict[part_of]
                    cnt -= 1
                    break

                alp_dict[part_of] -= 1

            end = find_end(end)

            dif = end - start
            if max_len < dif:
                max_len = dif

        print(max_len)

main()