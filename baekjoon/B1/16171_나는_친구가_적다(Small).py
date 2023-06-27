#230627
S = input()
K = input()
length = len(K)
if length == 1:
    print(1 if K in S else 0)
else:
    def has_keyword():
        position = []
        only_alp = []
        for i in range(len(S)):
            element = S[i]
            if element.isalpha():
                only_alp.append(element)

        for i in range(len(only_alp)):
            if only_alp[i] == K[0]:
                position.append(i)

        for j in position:
            for k in range(j, j+length):
                if only_alp[k] != K[k-j]:
                    break
            else:
                return 1

        return 0

    print(has_keyword())
