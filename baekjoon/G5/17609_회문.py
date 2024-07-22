# 240722
# 31120 KB / 196 ms
def main():
    def is_palindrome(s, e, input_str):
        while s <= e:
            if input_str[s] != input_str[e]:
                return (s, e)
            s += 1
            e -= 1
        return (s,)

    def kind_of_str(input_str):
        result = is_palindrome(0, len(input_str)-1, input_str)
        if len(result) == 1:
            return 0

        s, e = result
        for ns, ne in (s+1, e), (s, e-1):
            result = is_palindrome(ns, ne, input_str)
            if len(result) == 1:
                return 1

        return 2

    T = int(input())
    for _ in range(T):
        print(kind_of_str(input()))

main()


# 31120 KB / 188 ms
def main():
    def is_palindrome(s, e, input_str):
        while s < e:
            if input_str[s] != input_str[e]:
                return (s, e)
            s += 1
            e -= 1
        return (s,)

    def kind_of_str(input_str):
        result = is_palindrome(0, len(input_str)-1, input_str)
        if len(result) == 1:
            return 0

        s, e = result
        for ns, ne in (s+1, e), (s, e-1):
            result = is_palindrome(ns, ne, input_str)
            if len(result) == 1:
                return 1

        return 2

    T = int(input())
    for _ in range(T):
        print(kind_of_str(input()))

main()



# 31120 KB / 192 ms
def main():

    def kind_of_str(input_str):
        s, e = 0, len(input_str)-1
        while s < e:
            if input_str[s] != input_str[e]:
                break
            s += 1
            e -= 1

        else:
            return 0


        for ns, ne in (s+1, e), (s, e-1):
            while ns < ne:
                if input_str[ns] != input_str[ne]:
                    break
                ns += 1
                ne -= 1
            else:
                return 1

        return 2

    T = int(input())
    for _ in range(T):
        print(kind_of_str(input()))

main()




# 31252 KB / 188 ms
def main():

    def kind_of_str(input_str):
        s, e = 0, len(input_str)-1
        while s < e:
            if input_str[s] != input_str[e]:
                for ns, ne in (s + 1, e), (s, e - 1):
                    while ns < ne:
                        if input_str[ns] != input_str[ne]:
                            break
                        ns += 1
                        ne -= 1
                    else:
                        return 1
                break
            s += 1
            e -= 1

        else:
            return 0

        return 2

    T = int(input())
    for _ in range(T):
        print(kind_of_str(input()))

main()