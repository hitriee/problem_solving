# 250311
# 32412 KB / 592 ms
def main():
    T = int(input())
    for _ in range(T):
        n, m = map(int, input().split())
        if n == 1:
            print(m)
        else:
            start, limit = 1, m+1
            before = [1] * limit
            after = [0] * limit
            for _ in range(n-1):
                for i in range(start, limit):
                    j = 2*i
                    if j < limit:
                        after[j] = before[i]
                    else:
                        for k in range(start, limit):
                            after[k] += after[k-1]
                        break
                start *= 2
                before = after[:]
                after = [0] * limit

            print(sum(before))

main()



# 32412 KB / 584 ms
def main():
    T = int(input())
    for _ in range(T):
        n, m = map(int, input().split())
        if n == 1:
            print(m)
        else:
            start, limit = 1, m+1
            before = [1] * limit
            after = [0] * limit
            for _ in range(n-1):
                for i in range(start, limit):
                    j = 2*i
                    if j < limit:
                        after[j] = before[i]
                    else:
                        start *= 2
                        for k in range(start, limit):
                            after[k] += after[k-1]
                        break
                before = after[:]
                after = [0] * limit

            print(sum(before))

main()




# 32412 KB / 596 ms
def main():
    T = int(input())
    for _ in range(T):
        n, m = map(int, input().split())
        if n == 1:
            print(m)
        else:
            start, limit = 1, m+1
            before = [1] * limit
            after = [0] * limit
            for _ in range(n-1):
                for i in range(start, limit):
                    j = 2*i
                    if j < limit:
                        after[j] = before[i]
                    else:
                        start *= 2
                        for k in range(start, limit):
                            after[k] += after[k-1]
                        break
                before = after[:]
                after = [0] * limit

            print(sum(before[start//2:]))

main()




# 32412 KB / 596 ms
def main():
    T = int(input())
    for _ in range(T):
        n, m = map(int, input().split())
        if n == 1:
            print(m)
        else:
            start, limit = 1, m+1
            before = [1] * limit
            after = [0] * limit
            for _ in range(n-1):
                for i in range(start, limit):
                    j = 2*i
                    if j < limit:
                        after[j] = before[i]
                    else:
                        start *= 2
                        for k in range(start, limit):
                            after[k] += after[k-1]
                        break
                before = after[:]
                after = [0] * limit

            print(sum(before[start//2:]))

main()
