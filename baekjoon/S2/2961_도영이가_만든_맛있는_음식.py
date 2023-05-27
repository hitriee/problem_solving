#230527
N = int(input())
ingredients = [list(map(int, input().split())) for _ in range(N)]
min_total = 1e9
def find_min(total_sour, total_bitter, start, total):
    global min_total
    if total < min_total:
        min_total = total
    for j in range(start, N):
        sour, bitter = ingredients[j]
        new_sour, new_bitter = total_sour * sour, total_bitter + bitter
        find_min(new_sour, new_bitter, j+1, abs(new_sour - new_bitter))

for i in range(N):
    sour, bitter = ingredients[i]
    find_min(sour, bitter, i+1, abs(sour - bitter))
print(min_total)


#
def return_dif():
    N = int(input())
    ingredients = [list(map(int, input().split())) for _ in range(N)]
    min_total = 1e9

    def find_min(total_sour, total_bitter, start, total):
        nonlocal min_total
        if total < min_total:
            min_total = total
        for j in range(start, N):
            sour, bitter = ingredients[j]
            new_sour, new_bitter = total_sour * sour, total_bitter + bitter
            find_min(new_sour, new_bitter, j+1, abs(new_sour - new_bitter))

    for i in range(N):
        sour, bitter = ingredients[i]
        find_min(sour, bitter, i+1, abs(sour - bitter))

    return min_total

print(return_dif())