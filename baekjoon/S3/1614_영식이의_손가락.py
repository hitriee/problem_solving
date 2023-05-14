#230514
hurt_finger = int(input())
limit = int(input())

if hurt_finger == 1:
    print(8*limit)
elif hurt_finger == 5:
    print(8*limit + 4)
elif limit%2:
    print(4*limit + 5 - hurt_finger)
else:
    print(4*limit + hurt_finger - 1)
