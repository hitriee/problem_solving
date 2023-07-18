#230718
N = input()
length = len(N)
total = 0
ten = 1
for i in range(1, len(N)):
    total += 9*i*ten
    ten *= 10
total += (int(N) - ten + 1)*length
print(total)